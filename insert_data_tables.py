import psycopg2
import sys, getopt
import config
import pandas as pd

def connect_db():
    """ Connect to the PostgreSQL database server """
    con = None
    try:
        
        # connect to the PostgreSQL server
        print('\t Connecting to the PostgreSQL database...')
        con = psycopg2.connect(host=config.server,
                                database=config.database,
                                user=config.database,
                                password=config.password)	
        # create a cursor
        print('\t Connection successful')
        return (con)
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print ("\t Could not connect to DB. Exiting..")
        sys.exit(2)



def report_table_recs(tables):
    
    #Connect to the database
    con = connect_db()
    cur = con.cursor()

    try:
        for table in tables:
            qry = "SELECT COUNT(*) FROM %s" % table
            cur.execute(qry)
            cnt = cur.fetchall()
            cnt_rec = cnt[0][0]
            print ('\t Table {} has {} records'.format(table,cnt_rec))
            
        
        # Close communication with the PostgreSQL database server
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
                print(error)
    finally:
        if con is not None:
            con.close()

    

def read_insert_data_into_tables(tables,datafiles):
    con = connect_db()
    cur = con.cursor()
                
    for table,datafile in zip(tables,datafiles):
        f = open(datafile, 'r')
        cur.copy_from(f, table, sep=',',null="")
        con.commit()
        print('\t Committed data into table: {}'.format(table))
        
    con.close()

def get_tables_datafiles(map_file):
    df = pd.read_csv(map_file, sep=',')
    tables = df.table_name
    datafiles = df.datafile_path
    return(tables,datafiles)
                

def main(argv):

        try:
            opts, args = getopt.getopt(argv,"i:", ["datamap="]) 
	except getopt.GetoptError:
            print ('Usage: python insert_data_tables.py --datamap=<file_path>')
            sys.exit(2)

        req_options = 0
	for opt, arg in opts:
            if opt == '--datamap':
                map_file = arg
                req_options = 1

        if (req_options == 0):
            print ('Usage: python insert_data_tables.py --datamap=<file_path>')
            sys.exit(2)

        #Read the mapping file
        print('1. Reading the tables to data mapping file')
        tables, datafiles = get_tables_datafiles(map_file)
        print ('\t Read the file. Found mapping info for {} tables'.format(len(tables)))
        
        #Report the status of the tables
        print('2. Reporting the records in database tables before insertion')
        report_table_recs(tables)
        
        #Insert the data
        print('3. Inserting data into database tables') 
        read_insert_data_into_tables(tables, datafiles)

        
        #Report DB Status
        print('4. Reporting the records in database tables after insertion')
        report_table_recs(tables)

        
	
if __name__ == "__main__":
   main(sys.argv[1:])

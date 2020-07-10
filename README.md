---
title: "Setting up a database on ElephantSQL Cloud service"
author: "Data Smart"
---


## About

Set-up a database on [ElephantSQL](https://www.elephantsql.com/) using Python. This involves: 

- CREATE tables 
- INSERT data 

Why ElephantSQL?

ElephantSQL provides managed database as a service - on the cloud. It allows you to start a PostgreSQL database in minutes.

Get started with a database in minutes. 


## Getting set-up 

### Install Python 

To check if your computer already has Python installed, try the below on Terminal (for Mac) or Command Prompt (for Windows):

```
python --version
```

If you see a Python version returned (like 3.8.2), you already have Python !

Windows: Follow this you-tube video and install Python 3.x on your machine. Go ahead click on the image below:

<a href="https://www.youtube.com/watch?v=lnse_uD-MaA" target="_blank"><img src="images/install_python_windows.png" alt="Python for Windows" style="max-width:100%;"></a>


### Install the packages

Your default Python installation may not have some of the packages needed to run this code.  The list of the required packages is in the requirements.txt file in the code repo. 

To install these packages run the below command on the Terminal (for Mac) or Command Prompt (for Windows): 

```
pip install -r requirements.txt
```
### Create account and DB instance  on ElephantSQL

To access Elephant SQL services, you need to open an account. Login to Elephant SQL via your Google or Github account.  

Create a new database instance.  

Go back to the home screen and click on the database instance you just created. See the instance details. You will need these details to connect to the database instance from Python. 


### Create the config.py file

The code repository needs a configuration file that stores the details of the database instance you have created. 

This repo has a file called config-template.py. Edit the file to add the details of the your database instance from the 'Details' tab on Elephant SQL. Save the file as config.py. 

## Understand the problem 

We are going to create the database for a sales organization. 

Like any sales organization, this one has customers, products, orders, payments and employees. 

The data is stored in what is called a relational database. Each entity (like customer) is stored in a table. The relationship between the various entities (or tables) is shown below:

<br><br>

<img style="float: center;" src="images/erdiagram.png">

<br><br><br>


## Running the Code 

### CREATE tables 
To run the code, just use the below on your Terminal (Mac) or Command prompt (Win):

```
python create_drop_tables.py --sqlfile='table_creation.sql'
```
This will extract the SQL statement from the sqlfile, execute the SQL statements and, finally, output all the tables in the database. 


### DELETE tables 
You can also delete the tables by using the table_deletion.sql file. 

```
python create_drop_tables.py --sqlfile='table_deletion.sql'
```

### INSERT data in the tables 

The data to be inserted is in data/. 

The data/ folder also has a file called datafilemap.txt. This has the data file name to the database table mapping information. 

To read the data from the files one by one and write to the corresponding data table, type the below. 

```
python insert_data_tables.py --datamap='data/datafilemap.txt'

```




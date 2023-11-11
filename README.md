# fast-api

# Description

The app contains two files one is the `main.py` and the other is the `ui.py` file, 

The `ui.py` file uses tkinter and the idea of the file is that it will collect information from the user and will make and API call to insert data into the DB.

The `main.py` files is powered by Fast API which exposes a `POST` endpoint which will get the information submitted by the user and will run a query to insert data into the users' table

# Steps to Start the application
The following packages needs to be installed before starting the application

The below packages are required for the `main.py` file
```
pip install fastapi uvicorn pymysql
```

The below packages are required for `ui.py` file

```
pip install requests
```

To start the `main.py` file, run the below command. This will run in the port mentioned in the file

```
python -m uvicorn main:app --reload
```

The `ui.py` is run using the below command

```
python ui.py
```

## NOTE ##

Make sure to update the mysql username and password in the `main.py` under the config dictionary

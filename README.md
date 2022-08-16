# Project name
Avto.net

# General info
API for cars management

![](static/images/API.png)

# Routes to implement
| METHOD   | ROUTE                    | FUNCTIONALITY       |
|----------|--------------------------|---------------------|
| *GET*    | ```/api/cars```          | details of all cars |
| *POST*   | ```/api/cars```          | create a car        |
| *GET*    | ```/api/cars/{car_id}``` | details of car      |
| *PUT*    | ```/api/cars/{car_id}``` | update a car        |
| *DELETE* | ```/api/cars/{car_id}``` | delete a car        |


# Technologies
* python 3
* flask 2.1.3
* flask_restx
* flask_sqlalchemy
* MySQL

# Setup

Clone the project Repository
```
git clone https://github.com/SergiiPachkovskyi/Avto_net

```

Enter the project folder and create a virtual environment
``` 
$ cd https://github.com/SergiiPachkovskyi/Avto_net 

$ python -m venv venv 

```

Activate the virtual environment
``` 
$ source env/bin/activate #On linux Or Unix

$ source env/Scripts/activate #On Windows  
```

Install all requirements

```
$ pip install -r requirements.txt
```

Run the project in development 
``` 
python app.py

or

flask run 
```

# Status
Project is: in progress

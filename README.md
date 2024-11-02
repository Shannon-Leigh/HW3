Group Members: 

Shannon Leigh Huntley 

Qanitah Danial 

 

Assignment 

This project shows how we can connect PostgreSQL with flask and show SELECT results in a HTML table. We will be using example 4 as the basis of this project. 

 

STEP 1: 

First, we need to install a Python 3 virtual environment with: 

sudo apt-get install python3-venv 

 

Create a virtual environment: 

python3 -m venv python_venv 

 

You need to activate the virtual environment when you want to use it: 

source python_venv/bin/activate 

 

To fufil all the requirements for the python server, you need to run: 

pip3 install -r requirements.txt 

 

Because we are now inside a virtual environment. We do not need sudo. 

 

Then you can start the server with: 

python3 main.py 

 

STEP 2: 

Make SQL tables with the following command: 

 

CREATE TABLE basket_a ( 

    a INT PRIMARY KEY, 

    fruit_a VARCHAR (100) NOT NULL 

); 

CREATE TABLE basket_b ( 

    b INT PRIMARY KEY, 

    fruit_b VARCHAR (100) NOT NULL 

); 

INSERT INTO basket_a (a, fruit_a) 

VALUES 

    (1, 'Apple'), 

    (2, 'Orange'), 

    (3, 'Banana'), 

    (4, 'Cucumber'); 

INSERT INTO basket_b (b, fruit_b) 

VALUES 

    (1, 'Orange'), 

    (2, 'Apple'), 

    (3, 'Watermelon'), 

    (4, 'Pear'); 

 

STEP 3: 

When a user accesses your Flask server with 127.0.0.1:5000/api/update_basket_a, it will insert a new row (5, 'Cherry') into basket_a. On the browser, it will either show "Success!" or and error message. 

 

STEP 4: 

When a user accesses your Flask server with 127.0.0.1:5000/api/unique,it will show unique fruits in basket_a and unique fruits in basket_b in an HTML table. If there are any errors from PostgreSQL, error messages will show on the browser. 

 

Note: A user may access each of these functions in any order. 
```
# AQA

## Install Python version 3.11:
- [download](https://www.python.org/downloads/) 
     
## Clone project:
     git clone https://github.com/HelHitch/AQA.git

## Install Python packages:
###  Install requirements to run tests:<h4>
     pip install -r requirements.txt --no-cache-dir
     
## Initilize venv:
     python3 -m venv venv

## Run tests locally (from directory tests):
     pytest -m marker --browser browser name
 -m = tests matkers. Read markers description in pytest.ini  
 --browser = browser configuration. Read possible parameters in coftest parameters_init

# AQA

## Install Python version 3.11:
- [download](https://www.python.org/downloads/) 
     
## Clone project:
     git clone https://github.com/HelHitch/AQA.git

## Install Java packages, add PATH variable to java:  
- [download](https://learn.microsoft.com/en-us/java/openjdk/download)
     
## Initialize venv:
     python3 -m venv venv

## Install Python packages:
###  Install requirements to run tests:
     pip install -r requirements.txt --no-cache-dir

## Run tests locally (from directory tests):
     pytest -m [marker] --browser [browser name] --headless [parameter]
 -m = tests matkers. Read markers description in pytest.ini  
 --browser = browser configuration.  By deafult = "chrome". Read possible parameters in coftest.pe file.
 --headless = test run configuration. By default = true. Change parameters in pytest.ini file.


## Make Allure report:
    For first launch:
    - Set-ExecutionPolicy RemoteSigned -Scope CurrentUser # Optional: Needed to run a remote script the first time
    - irm get.scoop.sh | iex
    Getting report:
    - pytest --alluredir=report
    - allure serve report
    
    
    

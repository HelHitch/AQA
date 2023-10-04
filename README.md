# AQA

## Install Chrome and Firefox:
- [Chrome](https://www.google.com/intl/ru_ru/chrome/)
- [Firefox](https://www.mozilla.org/en-US/firefox/new/)
  
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
     pytest -m [marker] --browser [browser name] --headless [parameter] --alluredir=report
     
     -m = tests matkers. Read markers description in pytest.ini.
     --browser = browser configuration.  By deafult = "chrome". Read possible parameters in coftest.pe file.
     --headless = test run configuration. By default = true. Change parameters in pytest.ini file.
     --alluredir = allure report result.
### COMMAND EXAMPLE:  
pytest -> Run tests session in headless mode in chrome  
pytest --headless false -> Run tests session in chrome with browser opening  
pytest --browser firefox -> Run tests session in headless mode in firefox   
etc.  

## Make Allure report:
  1) [Download](https://github.com/allure-framework/allure2/releases) allure
  2) Add /bin folder of downloaded file into PATH
  3) Open project in IDE and execute commands (Optional: Needed to run a remote script the first time):  
    1) Set-ExecutionPolicy RemoteSigned -Scope CurrentUser   
    2) irm get.scoop.sh | iex
  4) restart IDE
  5) set allure variable by executing command:
       Set-alias allure [path to allure bat file in bin folder]\allure.bat  
  6) Get report by executing command:  
          1. pytest --alluredir=report  
          2. allure serve report  
    
    
    

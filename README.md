Precondition: 

	1. SQL Server Management Studio 19 is installed
	2. Script for TRN db is executed in SQL Server MS
	3. Python is installed

1) Create Login and User in SQL Server Management Studio
	- For help: https://www.guru99.com/sql-server-create-user.html
	- If some connection issue occurs the following link can help:
	https://stackoverflow.com/questions/34430550/a-connection-was-successfully-established-with-the-server-but-then-an-error-occ
	Restarting SQL Server service manually can be a solution.
	Use SQL Server Configuration Manager > SQL Server Services to find out what processes are running (C:\Windows\SysWOW64\SQLServerManager15.msc)
	
2) Open the db_settings.txt file and change it by specifying your DB settings.
   !!!Don't change file formatting!!!
	
3) - Install pyodbc using pip - Python package manager: pip install pyodbc 
   - Install {ODBC Driver 18 for SQL Server} for connection to DB:
	 https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows
	 
4) Install pytest: pip install pytest

5) Install Allure
    - pip install allure-pytest
	- download the latest allure package zip file from the https://github.com/allure-framework/allure2/releases
	- unzip the downloaded zip file, copy the path with bin inclusive, add it to the path environment variable
	
6) The project also contains a requirements.txt file. It saves a list of the modules and packages required by the project. 
    For installation required modules use the command: pip install -r requirements.txt	

7) Generating Allure report using pytest:
	- Automatically generate a folder to save the allure reports: allure generate
	  This will create a folder named allure-report in your project directory.
	- Run your test with pytest runner by specifying the directory path to save your allure report: pytest --alluredir=allure-report/
	  Once test execution completes, all the test results would get stored in allure-report directory.
	- You can now view the allure-report in the browser with the command: allure serve allure-report/
	
8) For running tests run terminal from project folder and use one of the following commands: 
	- pytest
	- pytest -v
	- pytest test_db.py

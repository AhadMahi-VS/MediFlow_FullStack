@echo off
TITLE MediFlow - Auto Launcher
COLOR 0A

echo ==================================================
echo      STARTING MEDIFLOW SYSTEM (Please Wait...)
echo ==================================================
echo.
echo ⚠️  IMPORTANT: MAKE SURE XAMPP MySQL IS STARTED (GREEN)
echo.
pause

echo 1. Installing Python Requirements...
pip install django django-cors-headers mysqlclient

echo.
echo 2. Setting up Database Tables...
python manage.py makemigrations
python manage.py migrate

echo.
echo 3. Creating Demo Users...
python setup_users.py

echo.
echo 4. Starting Server...
start "" "client\index.html"
python manage.py runserver

pause
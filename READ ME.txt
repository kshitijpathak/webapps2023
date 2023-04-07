STEPS TO RUN APP ON SECURE SERVER

STEP 1: Command to activate venv: Powershell commands (steps to run on secure server): venv/Scripts/activate

STEP 2: Command to run safe-server: python manage.py runserver_plus --cert-file localhost.crt --key-file localhost.key

STEP 3: Command to deactivate venv: deactivate


Certificates password: webapps
hostname: localhost

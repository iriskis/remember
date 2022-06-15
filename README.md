# Places Remember - web-application to store memories of visited places

## Stack

Python 3, Django, VK auth with social-auth-app-django 

## Steps to run

1. Fill secret keys in `config/credentials.py` 
2. Install deps: `pipenv install` & `pipenv shell`
3. Prepare local db by using migrations: `python .\src\manage.py makemigrations` & `python .\src\manage.py migrate `

# :computer: DevSearch - Connect With Developers From Around The World!

### Technologies Stack
- Django
- PostgreSQL
- HTML / CSS

### Developer Staff
- [h4cktivist](https://github.com/h4cktivist)
- Templates for frontend were taken from [divanov11/Django-2021](https://github.com/divanov11/Django-2021)

### Website Features
- Browse and search for developers
- Browse and search for projects
- Sign up and log in into account
- Edit / Delete account information
- Create / Edit / Delete your projects
- Comment other's projects
- Send messages to developers / Read your inbox messages
- Reset password to your account via email

### Preview
![1](https://user-images.githubusercontent.com/51692800/124136602-5d4dcd80-da9e-11eb-8bbe-0192a989251f.png)
![2](https://user-images.githubusercontent.com/51692800/124136514-49a26700-da9e-11eb-93b8-9a319f332b97.png)
![4](https://user-images.githubusercontent.com/51692800/124136520-4a3afd80-da9e-11eb-8013-a9503aa84937.png)
![5](https://user-images.githubusercontent.com/51692800/124136524-4ad39400-da9e-11eb-9d42-fbab06202659.png)
![7](https://user-images.githubusercontent.com/51692800/124136630-6179eb00-da9e-11eb-8ffd-4cc889043356.png)
![6](https://user-images.githubusercontent.com/51692800/124136526-4ad39400-da9e-11eb-9910-e36f4266138b.png)

### Run it yourself
```sh
git clone https://github.com/h4cktivist/devSearch.git
cd devSearch
pip install - r requirements.txt
```

Go to the `setting.py` and change this lines up to your PostgreSQL account
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'devSearch',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': ENV['DB_PASS']
    }
}
```
Then run the migrations:
```sh
python manage.py migrate
```

Also change this up to your email for reset password confirmation feature
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ENV['EMAIL']
EMAIL_HOST_PASSWORD = ENV['EMAIL_PASS']
```

Then you can run it
```sh
python manage.py runserver
```

## Today I Learned - Demo application


Download the source code by using git:

```
git clone https://github.com/amitsaha/til.git
```

## Model Setup

```
$ pip install -r requirements.txt
$ python manage.py migrate
```

## Start web application

```
$ python manage.py runserver 0.0.0.0:8000
```

Go to `127.0.0.1:8000`

### Django Resources

I used these for help:

- https://docs.djangoproject.com/en/1.11/ref/csrf/
- http://www.janosgyerik.com/django-authenticationform-gotchas/
- https://django-bootstrap3.readthedocs.io/en/latest/quickstart.html#example-template
- https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
- https://stackoverflow.com/questions/14647723/django-forms-if-not-valid-show-form-with-error-message


## Web application Resources

- [A typical HTTP session](https://developer.mozilla.org/en-US/docs/Web/HTTP/Session)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
- [HTTP Compression](https://developer.mozilla.org/en-US/docs/Web/HTTP/Compression)


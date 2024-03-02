# Django-Blog
A horrible looking but functional blog with authentication using:

- Username/Password `admin/testpass123`
- Ion

## Installation
```bash
git clone https://github.com/JasonGrace2282/django-blog.git && cd django-blog
/usr/bin/env python3 -m pip install -r requirements.txt
/usr/bin/env python3 manage.py runserver
```

Note that you will need to get your own `CLIENT_ID` and `CLIENT_SECRET` from Ion
and define them as `CLIENT_ID` and `CLIENT_SECRET` in `secret.py`.
It should redirect to `http://localhost:8000/login/token-code`

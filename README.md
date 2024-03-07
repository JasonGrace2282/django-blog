# Django-Blog
A horrible looking but functional blog with authentication using:

- Username/Password `admin/testpass123`
- Ion

## Installation
```bash
git clone https://github.com/JasonGrace2282/django-blog.git && cd django-blog
python3 -m venv .venv && source .venv/bin/activate
env python3 -m pip install -r requirements.txt
env python3 manage.py runserver
```

Note that you will need to get your own `CLIENT_ID` and `CLIENT_SECRET` from Ion. 
It should redirect to `http://localhost:8000/login/token-code`.

Then define `BLOG_ION_CLIENT_ID` and `BLOG_ION_CLIENT_SECRET` environment variables before running the program.

For example, add this to your `~/.bashrc` or `~/.zshrc` and restart your shell:
```bash
export BLOG_ION_CLIENT_ID="Your CLIENT_ID"
export BLOG_ION_CLIENT_SECRET="Your Client Secret"
```

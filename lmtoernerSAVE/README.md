 2116  mkdir lmt-dj1.11
 2117  cd lmt-dj1.11/
 2118  virtualenv .venv
 2119  source .venv/bin/activate
 2120  python -m django --version
 2121  pip install Django
 2122  python -m django --version
 2123  django-admin startproject lmtoerner
 2124  ls
 2125  ls -al
 2126  cd lmtoerner/
 2127  ls -ltr
 2128  ls -al
 2129  ls -al lmtoerner/
 2130  find ~/MyDjangoSites/ -name registration
 2131  ls -al
 2132  mkdir templates
 2133  mkdir static
 2134  cp -R ../../lmtoerner1/templates/registration ./templates/
 2135  vi lmtoerner/settings.py 
 2136  python manage.py runserver
 2137  pip install django-registration
 2138  python manage.py runserver
 2139  pip install mysql-python
 2140  python manage.py runserver


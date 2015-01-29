# collect-exceptions

---
'collect-exceptions' is a python exception collector.
It can collect django and celery exception

---
### django:
In the settings file, writing the 'collect_exceptions.contrib.django' after 'djcelery' if you have 'djcelery'.
```python
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'djcelery',
    'collect_exceptions.contrib.django',
)

COLLECT_EXCEPTIONS_CONFIG = {
    'EXCEPTION_COLLECTOR': 'your_module.your_func',
}
```
'your_module.your_func' will receive the exception trace strings if you set 'COLLECT_EXCEPTIONS_CONFIG'. 'your_func' need to define like the code below.
```python
def your_func(exception_trace_str):
    pass
```

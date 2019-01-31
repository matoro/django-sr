SECRET_KEY = "123"

INSTALLED_APPS = [
    'sr'
]

# https://niwinz.github.io/django-jinja/latest/#_quick_start
TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja"
        }
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True
    }
]

SR = {
    'test1': 'Test1',
    'test2': {
        'test3': 'Test3',
    },
    'test4': {
        'test4': 'Test4 {0} {1}',
    },
    'test5': {
        'test5': "<b>foo</b>",
    }
}

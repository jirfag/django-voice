import urllib.request, urllib.parse, urllib.error
from django import VERSION as DJANGO_VERSION
from django.conf import settings
from hashlib import md5

if DJANGO_VERSION >= (1, 5):
    # Django 1.5+ compatibility
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
    except: # Django 1.7+ compatibility
        from django.contrib.auth.models import User

else:
    from django.contrib.auth.models import User


if 'gravatar' in settings.INSTALLED_APPS:
    from gravatar.templatetags.gravatar_tags import gravatar_for_user

else:
    gravatar_url = 'http://www.gravatar.com/'

    def gravatar_for_user(user, size=80):
        size_param = urllib.parse.urlencode({'s': str(size)})
        email = md5(user.email).hexdigest()
        url = '%savatar/%s/?%s' % (gravatar_url, email, size_param)

        return url

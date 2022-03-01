from django.contrib.auth.models import User
from django.utils.text import slugify


def random_string_generator(size=10,):
    return User.objects.make_random_password(length=size)


def unique_slug_generator(instance, new_slug=None):
    slug = new_slug or slugify(instance.title)

    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()
    if not qs_exists:
        return slug

    new_slug = "{slug}-{randstr}".format(
        slug=slug,
        randstr=random_string_generator(size=4)
    )
    return unique_slug_generator(instance, new_slug=new_slug)

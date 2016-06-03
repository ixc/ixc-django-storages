from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class MediaS3BotoStorage(S3BotoStorage):
    location = getattr(settings, 'MEDIA_LOCATION', 'media')


class StaticS3BotoStorage(S3BotoStorage):
    location = getattr(settings, 'STATIC_LOCATION', 'static')

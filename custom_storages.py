from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
git add . 

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

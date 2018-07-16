# S3Boto3 Storage로 STATICFILES_STORAGE설정하신분들은
# 해제하고 ROOT_DIR/.static을 STATIC_ROOT로 사용하도록 수정
from storages.backends.s3boto3 import S3Boto3Storage

__all__ = (
    'S3DefaultStorage',
)


class S3DefaultStorage(S3Boto3Storage):
    location = 'media'

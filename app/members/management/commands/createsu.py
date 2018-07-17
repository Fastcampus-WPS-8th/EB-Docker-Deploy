import json
import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

User = get_user_model()


# admin / 특정비밀번호
#  위 값으로 로그인 시도 시 authenticate가 성공하도록 커스텀 Backend를 작성
#  members.backends모듈에 작성
#  Backend명은 SettingsBackend


class Command(BaseCommand):
    def handle(self, *args, **options):
        secrets = json.load(open(os.path.join(settings.SECRETS_DIR, 'base.json')))
        if not User.objects.filter(username=secrets['SUPERUSER_USERNAME']).exists():
            User.objects.create_superuser(
                username=secrets['SUPERUSER_USERNAME'],
                password=secrets['SUPERUSER_PASSWORD'],
                email=secrets['SUPERUSER_EMAIL'],
            )

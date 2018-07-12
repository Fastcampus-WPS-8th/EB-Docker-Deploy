# EB Docker Deploy

## Requirements

- Python (3.6)
- pipenv
- Django (2.x)

### Secrets

#### `.secrets/base.json`

```json
{
  "SECRET_KEY": "<Django secret key>"
}
```

## Running

```
# Move project's directory
pipenv install
pipenv shell
cd app
export DJANGO_SETTINGS_MODULE=config.settings.local
./manage.py runserver
```

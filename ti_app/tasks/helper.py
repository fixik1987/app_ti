from django.core.mail import send_mail


def send_mail_without_celery():
    send_mail('Mail without celery',
              'CELERY IS COOL',
              'pavel87.test@gmail.com',
              ['dolliner.pavel@gmail.com']
              )
    return None
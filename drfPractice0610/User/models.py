from django.db import models
from pygments.lexers import get_all_lexers

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

GENDER_CHOICES = (
    (0, 'Male'),
    (1, 'Female'),
    (2, 'Unknown')
)


class Users(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=64)
    username = models.IntegerField(default=0, verbose_name="나이")
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name="성별")
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100, verbose_name="언어")
    level = models.CharField(max_length=8, verbose_name='등급',
                             choices=(
                                 ('admin', 'admin'),
                                 ('user', 'user')
                             ))
    sendmail = models.BooleanField(default=True, verbose_name="메일수신동의")

    class Meta:
        ordering = ['-id']
        verbose_name = 'User'
        verbose_name_plural = 'User'

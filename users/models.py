from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='/avatars/default.jpg', upload_to='avatars')
    summary = models.TextField('Summary about user', default='New user on our platform!')
    location = models.TextField('Place of residence', default='Location is not specified.')
    about = models.TextField('About', default='Apparently, this user prefers to keep an air of mystery about them.')
    other_skills = ArrayField(models.CharField('Other skills', max_length=30), null=True)

    def __str__(self):
        return f'{self.user.username} Account'


class Skill(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField('Skill name', max_length=20)
    description = models.TextField('Skill description')

    def __str__(self):
        return f'{self.account} - {self.name} Skill'


class Link(models.Model):
    ICONS = (
        ('im im-github', 'GitHub'),
        ('im im-stackoverflow', 'StackOverflow'),
        ('im im-linkedin', 'LinkedIn'),
        ('im im-twitter', 'Twitter'),
        ('im im-globe', 'Website')
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField('Link name', max_length=30)
    link = models.URLField('URL')
    icon = models.TextField('Icon name', choices=ICONS)

    def __str__(self):
        return f'{self.name} Link'

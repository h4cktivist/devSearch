from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=120)
    description = models.TextField('Description')
    tags = ArrayField(models.CharField('Tags', max_length=30), null=True)
    link = models.URLField('Source code link')
    image = models.ImageField('Project image', upload_to='project_images')
    date = models.DateField('Date of creation', auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.title} Project'

    @property
    def feedbackCount(self):
        return f'{self.comment_set.count()} feedback(s)'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField('Text of comment')
    date = models.DateField('Date', auto_now_add=True)

    def __str__(self):
        return f'{self.author} Comment to {self.project}'


class Message(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='user_to', on_delete=models.CASCADE)
    subject = models.CharField('Message subject', max_length=200)
    text = models.TextField('Message text')
    is_read = models.BooleanField('Is read', default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.user_from} to {self.user_to}'

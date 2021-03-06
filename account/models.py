from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('Photo', default='default.jpg',
                              upload_to='profile_pics')
    description = models.TextField(blank=True, null=True, max_length=250)

    def __str__(self):
        return f'{self.user.username} profile'

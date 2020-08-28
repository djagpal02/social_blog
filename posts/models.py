from django.db import models
from django.core.urls import reverse
from django.conf import settings

# Create your models here.
from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(user, related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.textField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})


    class Meta:
        ordering = ['-created_at']
        unique_togther = ['user','message'] 
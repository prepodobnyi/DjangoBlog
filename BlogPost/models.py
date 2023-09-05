from django.db import models

from users.models import User

class Posts(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = "Post"

    def __str__(self):
        return self.title

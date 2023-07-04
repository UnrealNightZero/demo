from django.db import models

class Message(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    change = models.IntegerField(default=1, null=False)

    def __str__(self):
        return self.content
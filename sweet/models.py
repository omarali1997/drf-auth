from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
    title = models.CharField(max_length=64,help_text='snack title',default='SweetSnack')
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)





    def __str__(self):
        return self.title
    
from django.db import models


# Create your models here.


class TO_DO(models.Model):
    text = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

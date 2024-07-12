from django.db import models
from Parties.models import Party
from django.contrib.auth.models import User

# Create your models here.
class Vote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
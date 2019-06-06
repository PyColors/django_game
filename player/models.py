from django.db import models

from django.contrib.auth.models import User

# Invitation Class allows user to play a game
class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitations_sent", on_delete="")
    to_user = models.ForeignKey(User, related_name="invitations_received", on_delete="")
    message = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

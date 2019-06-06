# This class can create form from Django
from django.forms import ModelForm

# Form for Invitation
from .models import Invitation

# Invitation model InvitationForm class
# He will create a HTML form with 4 fields base on the model:
# from_user
# to_user
# message
# timestamp
class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        exclude = ('from_user', 'timestamp')
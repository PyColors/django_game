from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Move

# Extends ModeForm
class MoveForm(ModelForm):
    class Meta:
        # Base on the Move model
        model = Move
        exclude = []

    def clean(self):
        x = self.cleanned_data_get("x")
        y = self.cleanned_data_get("y")
        game = self.instance.game
        try:
            if game.board()[y][x] is not None:
                raise ValidationError("Square is not empty")
        except IndexError:
            raise ValidationError("Invalid coordinates")
        return self.cleanned_data_get

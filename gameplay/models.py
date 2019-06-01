from django.db import models
from django.contrib.auth.models import User


# Set all possibilities value for the status of the game
# with a description string for each value (drop-down)
GAME_STATUS_CHOICES = (
    ('F', 'First Player To move'),
    ('S', 'Second Player To move'),
    ('W', 'First Player Wins'),
    ('L', 'Second Player Wins'),
    ('D', 'Draw'),
)

class Game(models.Model):
    first_player = models.ForeignKey(User,
                                     related_name="games_first_player", on_delete=models.CASCADE)
    second_player = models.ForeignKey(User,
                                      related_name="games_second_player", on_delete=models.CASCADE)

    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)

    # default value is required here: by 'F'
    # GAME_STATUS_CHOICES is an option for the field
    status = models.CharField(max_length=1, default='F',
                              choices=GAME_STATUS_CHOICES)

    # Display the object to a user-friendly way with `format` rather than `Game object (3)` in the Admin
    def __str__(self):
        return "{0} vs {1}".format(
            self.first_player, self.second_player
        )


# Model will represent a table in the database
class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

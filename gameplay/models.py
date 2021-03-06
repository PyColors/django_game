from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


# Set all possibilities value for the status of the game
# with a description string for each value (drop-down)
GAME_STATUS_CHOICES = (
    ('F', 'First Player To move'),
    ('S', 'Second Player To move'),
    ('W', 'First Player Wins'),
    ('L', 'Second Player Wins'),
    ('D', 'Draw'),
)
#
# QuerySet: collection from the database and use think like:
# filter and exclude
class GameQuerySet(models.QuerySet):

    # Method to call all game of user that only return game for specific user
    def game_for_user(self, user):
        return self.filter(
            # `Q` is a function can use to construct queries with a logical OR in them.
            Q(first_player=user) | Q(second_player=user)
        )

    # Selecting game depending on the status
    def active(self):
        return self.filter(
            Q(status='F') | Q(status='S')
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

    objects = GameQuerySet.as_manager()


    def board(self):
        # Return two dimensional list of Move Object
        board = [[None for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]
        for move in self.move_set.all():
            board[move.y][move.x] = move
            return board

    # Return true if that player's move in the game
    def is_user_move(self, user):
        return (user == self.first_player and self.status == 'F') or\
               (user == self.second_player and self.status == 'S')

    # Return new player move object
    def new_move(self):
        if self.status not in 'FS':
            raise ValueError("Cannot make move on finished game")

        return Move(
            game=self,
            by_first_player=self.status == 'F'
        )

    # What is the canonical URL for a model instance
    def get_absolute_url(self):
        return reverse('gameplay_detail', args=[self.id])


    # Display the object to a user-friendly way with `format` rather than `Game object (3)` in the Admin
    def __str__(self):
        return "{0} vs {1}".format(
            self.first_player, self.second_player
        )


# Model will represent a table in the database
class Move(models.Model):
    x = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(BOARD_SIZE-1)]
    )

    y = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(BOARD_SIZE - 1)]
    )

    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField(editable=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

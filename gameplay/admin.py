# Django generates a really nice and powerful interface for a models


from django.contrib import admin

# import models
from .models import Game, Move

# Which filed to show in the admin for Game class
# That allow now to see the three fields rather than str method
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_player', 'second_player', 'status')
    # Make fields editable before edit the status by `list_editable`
    # + `,` at the end because this value is a tuple (immutable)
    # https://www.tutorialspoint.com/python/python_tuples.htm
    list_editable = ('status',)


admin.site.register(Move)

from django.contrib import admin

from games_app.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	list_display = ('name', 'developer', 'release_date', 'rating')
	search_fields = ('name', 'developer')
	list_filter = ('developer', 'release_date')

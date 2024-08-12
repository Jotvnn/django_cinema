from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Cinema,Actors,Genres

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

@admin.register(Cinema)
class AdminCinema(admin.ModelAdmin):
    list_display = ('id','genres','name','date','get_image','date_update')
    list_editable = ('name','date')

    def get_image(self,obj):
        return mark_safe(f'<img src="{obj.preview_image.url}" width="50" height="60"/>')
    get_image.allow_rags=True

@admin.register(Actors)
class AdminActors(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'age', )
    list_editable = ('name', 'surname', 'age', )

@admin.register(Genres)
class AdminGenres(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)

    class CustomUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        form = CustomUserChangeForm
        model = CustomUser
        list_display = ["email", "username", ]

    admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from user_stats.admin import DailyProgressInline

class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    inlines = [DailyProgressInline]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('username', 'email', 'is_staff',)
    #inlines = [CathegoryInline,]'''


admin.site.register(CustomUser, CustomUserAdmin)


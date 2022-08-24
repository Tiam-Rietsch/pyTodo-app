from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
#from categories.models import Category



'''#class CathegoryInline(admin.StackedInline):
    model = Category
    extra = 0'''


class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('username', 'email', 'is_staff',)
    #inlines = [CathegoryInline,]'''


admin.site.register(CustomUser, CustomUserAdmin)


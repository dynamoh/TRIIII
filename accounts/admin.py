from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Profile,User

admin.site.unregister(Group)
admin.site.register(Profile)


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email','username', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password','username')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_admin','is_active','is_employee')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','username')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email','username')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)




admin.site.site_header = 'TRIIII'

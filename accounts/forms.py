from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label=None,widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'formclass'}))
    password2 = forms.CharField(label=None,widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'formclass'}))
    email = forms.CharField(label=None,widget=forms.EmailInput(attrs={'placeholder':'Email','class':'formclass'}))
    username = forms.CharField(label=None,widget=forms.TextInput(attrs={'placeholder':'Username','class':'formclass'}))

    class Meta:
        model = User
        fields = ('email','username',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        print(qs)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        print("NO Prob")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        print(password1,password2)
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        print("NO Prob")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password','username', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

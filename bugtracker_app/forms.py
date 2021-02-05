from django import forms
# from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from bugtracker_app.models import Ticket, MyUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username', 'email')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class AddTicketForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    # status = forms.ModelChoiceField(queryset=Ticket.objects.all())


class EditForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)

class ActionsForm(forms.Form):
    chooseperson = forms.ModelChoiceField(queryset=MyUser.objects.all())


class ActionsdropdownForm(forms.Form):
    ActionList = forms.ModelChoiceField(queryset=Ticket.objects.all())
    Actions_CHOICES = [
        ('edit','Edit'),
        ('assign †icket †o you','Assign Ticket †o You'),
        ('mark ticket as invalid','Mark Ticket as Invalid')
    ]

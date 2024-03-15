from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name','password1')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.password1 = self.cleaned_data['password1']

        if commit:
            user.save()
        return user
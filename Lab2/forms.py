from django import forms
from django.contrib.auth.models import User
from .models import TeamUser, Mentor
from django.contrib.auth.forms import UserCreationForm
from datetime import date

def check_pesel(pesel):
  sum, ct = 0, [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
  for i in range(11):
    sum += (int(pesel[i]) * ct[i])
  return (str(sum)[-1] == '0')

def check_is_fullage(pesel):
    current_date = date.today()
    if pesel[0] == "0":
        year = "200" + pesel[1:2]
    else:
        year = "19" + pesel[0:2]
    print(year)
    age = int(current_date.year)- int(year)
    if age>=18:
        return True
    return False

class MentorRegisterForm(forms.ModelForm):
    pesel = forms.CharField(min_length = 11, max_length = 11)
    class Meta:
        model = Mentor
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'pesel']

    def clean_pesel(self):
        pesel_passed = self.cleaned_data.get('pesel')
        if not check_pesel(pesel_passed):
            raise forms.ValidationError("Not a valid pessel. Please try again")
        if not check_is_fullage(pesel_passed):
            raise forms.ValidationError("You have to be fullage to be mentor!")
        return pesel_passed

class TeamRegisterForm(forms.ModelForm):
    class Meta:
        model = TeamUser
        fields = ['username', 'team_name', 'school', 'email', 'guardian_consent', 'participant_1', 'participant_2', 'participant_3', 'participant_4', 'participant_5']




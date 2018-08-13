from django import forms

class StatsForm(forms.Form):
    fga = forms.IntegerField(label='Field Goal Attempts')
    fgm = forms.IntegerField(label='Field Goals Made')

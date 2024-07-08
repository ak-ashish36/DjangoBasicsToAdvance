from django import forms

class userForms(forms.Form):
    num1 = forms.IntegerField(widget=forms.TextInput(attrs={'class':"box",'placeholder':"Enter num 1"}))
    num2 = forms.IntegerField(widget=forms.TextInput(attrs={'class':"box",'placeholder':"Enter num 2"}))
    num3 = forms.IntegerField(label="value 1",widget=forms.TextInput(attrs={'class':"box"}))

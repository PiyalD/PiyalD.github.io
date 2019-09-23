from django import forms


class SalaryMonthYear(forms.Form):
    month = forms.CharField(label='Month', max_length=100)
    year = forms.CharField(label='Year', max_length=100)


class SalaryMail(forms.Form):
    mailid = forms.CharField(label='mailid', max_length=100)
    msg = forms.CharField(label='msg', max_length=100)
    month = forms.CharField(label='month', max_length=100)
    year = forms.CharField(label='year', max_length=100)

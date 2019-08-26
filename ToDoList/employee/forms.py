from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Employee, Department, Login

class SearchForm(forms.Form):

    name = forms.ModelChoiceField(
        queryset=Employee.objects.values_list('name', flat=True),
        label='名前',
        empty_label='名前を選択してください',
        required=False#必須にしたいかどうか
        )

    department = forms.ModelChoiceField(
        queryset=Department.objects,
        label='部署',
        empty_label='部署を選択してください',
        required=False
        )

class PostForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name', 'department', 'todo', 'due', 'complete', 'tododetail')

class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = ('login_id',)

"""
    class DateForm(forms.ModelForm):
        class Meta:
            model = DateModel
            fields = ('date_field',)
            widgets = {
                'date_field': AdminDateWidget(),
            }

class SettingForm(forms.ModelForm):
    complete = forms.BooleanField()

    class Meta:
        model = Employee
"""

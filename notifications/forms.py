from django import forms
from .models import Notifications
from django.contrib.auth.models import User


class RequestMoney(forms.ModelForm):

    class Meta:
        model = Notifications
        fields = "__all__"
        widgets = {'from_user': forms.HiddenInput(), 'is_seen': forms.HiddenInput()}

        def __int__(self, *args, **kwargs):
            user = kwargs.pop('user', '')
            print(User.objects.filter(username=user.username))
            super(RequestMoney, self).__init__(*args, **kwargs)
            self.fields['from_user'] = forms.ModelChoiceField(queryset=User.objects.filter(username=user.username))
            print(self.fields['from_user'])

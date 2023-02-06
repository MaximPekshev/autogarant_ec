from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

class ContactForm(forms.Form):
	
	contactName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
			'placeholder': 'Ваше Имя',
			'id': 'name',
            'name': 'name',
            'type': 'text'

		}))
	contactPhone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
			'placeholder': ' Телефон',
			'id': 'phone',
            'name': 'phone',
            'type': 'text'
		}))
	contactComment = forms.CharField(max_length=1024, required=False, widget=forms.Textarea(attrs={
			'placeholder': 'Сообщение',
			'id': 'message',
            'name': 'message',
			'rows': '8',
		}))
	captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
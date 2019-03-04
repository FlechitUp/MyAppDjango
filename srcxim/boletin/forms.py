from django import forms

from .models import Registrado

""""Esta clase permite que se muestre el formulario para add Registrado en el admin"""
class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["name", "email"]
	
	#validaciones de los campos del formulario
	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not "edu" in email:
			raise forms.ValidationError("Usar correo con extension .edu")
		return email

class RegForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	email = forms.EmailField()
	#edad = forms.IntegerField()
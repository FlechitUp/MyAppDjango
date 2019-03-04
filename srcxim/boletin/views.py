from django.shortcuts import render

from .forms import RegForm
from .models import Registrado

# Create your views here.
def inicio(request):
	form = RegForm(request.POST or None)
	#print (dir(form))
	if form.is_valid():
		form_data = form.cleaned_data
		my_email =  form_data.get("email")
		my_name = form_data.get("nombre")
		obj = Registrado.objects.create(email = my_email, nombre = my_name)
		#print( form_data.get("nombre"))
	context = {
		"my_form": form,  #my_form se utilizara en el template
	}
	return render(request, "inicio.html", context)
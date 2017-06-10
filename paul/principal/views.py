from django.shortcuts import render
from datetime import date


# Create your views here.

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def home(request):
	#return HttpResponse('Tá rolando!')
	return render(request, 'home.html', {'mestredaporratoda': 'Paulino R. e Silva'})
	
def contact(request):
	return render(request, 'contact.html')

def about(request):
	idade = calculate_age((date(1973,11,4)))

	return render(request, 'sobre.html', {'idade': idade})
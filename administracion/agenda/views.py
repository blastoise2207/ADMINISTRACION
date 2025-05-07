from django.shortcuts import render
from .models import Agenda
# Create your views here.
def listado_agenda(request):
    agenda = Agenda.objects.all()
    return render(request, 'agenda/listado_agenda.html', {'agenda': agenda})    
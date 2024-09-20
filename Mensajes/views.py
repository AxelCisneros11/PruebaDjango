from django.http import HttpResponse
from django.shortcuts import render
from .forms import MensajeForm

def index(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            # Aquí puedes guardar el mensaje en la base de datos o hacer algo con los datos
            return HttpResponse(f"Gracias por tu mensaje, {nombre}!")
    else:
        form = MensajeForm()
    
    return render(request, 'enviar_mensajes.html', {'form': form})

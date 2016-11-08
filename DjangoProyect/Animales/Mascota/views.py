from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.views.generic  import ListView
from .forms import MascotaForm
from .models import Mascota
def index(request):

	return render(request,"index.html")

def mascota_view(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("Mascota:index")
	else:
		form = MascotaForm()
	return render(request,'mascota_forms.html',{"form":form})

def mascota_list(request):
	mascota = Mascota.objects.all().order_by('id')
	contexto = {'mascotas':mascota}
	return render(request,'mascota_list.html',contexto)

def mascota_edit(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == "GET":
		form = MascotaForm(instance=mascota)
	else:
		form = MascotaForm(request.POST,instance=mascota)
		if form.is_valid():
			form.save()
			return redirect('Mascota:mascota_listar')
	return render(request,'mascota_forms.html',{'form':form})

def mascota_delete(request,id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == "POST":
		mascota.delete()
		return redirect('Mascota:mascota_listar')
	return render(request,'mascota_delete.html',{'mascota':mascota})


class MascotaListView(ListView):
    model = Mascota
    template_name = "mascota_list.html"
		
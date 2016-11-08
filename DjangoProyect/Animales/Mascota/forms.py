from django import forms
from Mascota.models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
        	'name',
        	'sex',
        	'age',
        	'date',
        	'persona',
        	'vacuna',
    	]
    	labels = {
			'name':"nombre",
        	'sex':"Sexo",
        	'age':"Edad aproximada",
        	'date':"Fecha del rescate",
        	'persona':"Adoptante",
        	'vacuna':"Vacunas",    	
    	}
    	widgets={
			'name':forms.TextInput(attrs={'class':'form-control'}),
        	'sex':forms.TextInput(attrs={'class':'form-control'}),
        	'age':forms.TextInput(attrs={'class':'form-control'}),
        	'date':forms.TextInput(attrs={'class':'form-control'}),
        	'persona':forms.Select(attrs={'class':'form-control'}),
        	'vacuna':forms.CheckboxSelectMultiple(),
    	}
    
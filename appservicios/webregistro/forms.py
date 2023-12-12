from django import forms
from .models import Personas, Clientes, Tecnicos, Supervisores, Usuarios

class PersonasForm(forms.ModelForm):
    # Define la lista de opciones para Tipousuario
    TIPOS_DE_USUARIO = [
        ('---------', '---------'),
        ('tecnico', 'Tecnico'),
        ('cliente', 'Cliente'),
        ('supervisor', 'Supervisor'),
        
    ]

    # Define el campo Tipousuario como un campo de selección
    Tipousuario = forms.ChoiceField(
        choices=TIPOS_DE_USUARIO,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Personas
        fields = ('PrimerNombre', 'SegundoNombre', 'PrimerApellido', 'SegundoApellido',
                  'Direccion', 'Telefono', 'FechaNacimiento',
                  'Email', 'NumeroCedula', 'Tipousuario')
        widgets = {
            'PrimerNombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer nombre', 'required': True}),
            'SegundoNombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo nombre'}),
            'PrimerApellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer apellido', 'required': True}),
            'SegundoApellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo apellido'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion', 'required': True}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono', 'required': True, 'type': 'numeric'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': True, 'type': 'email'}),
            'NumeroCedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero de cedula', 'required': True, 'type': 'numeric'}),
            'FechaNacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }





class ClientesForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ('PersonaID', 'EmpresaID')  

class TecnicosForm(forms.ModelForm):

    class Meta:
        model = Tecnicos
        fields = ('PersonaID',)     

class SupervisoresForm(forms.ModelForm):

    class Meta:
        model = Supervisores
        fields = ('PersonaID',)      

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ('NombreUsuario', 'Contraseña')
        widgets = {
            'NombreUsuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario', 'required': True}),
            'Contraseña': forms.TextInput(attrs={'type': 'password','class': 'form-control', 'placeholder': 'Contraseña', 'required': True}),
        }

   
    
from django.forms import *
from appSGAE.models import Carrera, Nivel, Alumno, Profesor
from datetime import datetime


class CarreraForm (ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True
        self.fields['duracion'].widget.attrs['autofocus'] = False

    class Meta:
        model = Carrera
        fields = '__all__'
        # permite widgets personalizar
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de la Carrera',
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'placeholder': 'Ingrese un breve descripción',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

# Nivel Formulario


class NivelForm (ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True
        self.fields['carrera_nivel'].widget.attrs['autofocus'] = False

    class Meta:
        model = Nivel
        fields = '__all__'
        # permite widgets personalizar
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del nivel',
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'placeholder': 'Ingrese un breve descripción',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

# Alumno Formulario


class AlumnoForm (ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['dni'].widget.attrs['autofocus'] = True
        self.fields['sexo'].widget.attrs['autofocus'] = False

    class Meta:
        model = Alumno
        fields = '__all__'
        # permite widgets personalizar
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del alumno',
                }
            ),
            'apellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese el apellido del alumno',
                }
            ),
            'fecha_nacimiento': DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'fecha_nacimiento',
                    'data-target': '#fecha_nacimiento',
                    'data-toggle': 'datetimepicker'
                }),
            'email': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Email',
                }
            ),
            'direccion': TextInput(
                attrs={
                    'placeholder': 'Ingrese una direccón',
                }
            ),
            'telefono': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nº de telefono',
                }
            ),
            'comorvilidades': CheckboxInput(
                attrs={
                    'class': 'form-control',
                    'id': 'comorvilidades',
                    'data-target': '#comorvilidades',
                    'autocomplete': 'off',
                    'autofocus': 'false',
                }
            ),
            'observaciones': Textarea(
                attrs={
                    'placeholder': 'Ingrese una breve observacón',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ProfesorForm (ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['dni'].widget.attrs['autofocus'] = True
        self.fields['sexo'].widget.attrs['autofocus'] = False

    class Meta:
        model = Profesor
        fields = '__all__'
        # permite widgets personalizar
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del profesor',
                }
            ),
            'apellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese el apellido del profesor',
                }
            ),
            'fecha_nacimiento': DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'fecha_nacimiento',
                    'data-target': '#fecha_nacimiento',
                    'data-toggle': 'datetimepicker'
                }),
            'email': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Email',
                }
            ),
            'direccion': TextInput(
                attrs={
                    'placeholder': 'Ingrese una direccón',
                }
            ),
            'telefono': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nº de telefono',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

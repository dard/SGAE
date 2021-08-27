from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import render

from appSGAE.models import Carrera, Nivel, Alumno, Profesor
from appSGAE.forms import CarreraForm, NivelForm, AlumnoForm, ProfesorForm


# class indexView(TemplateView):
#     template_name = 'appSGAE/home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['panel'] = 'Panel de administración'
#         return context

# Create your views here.

class indexView(TemplateView):
    template_name = 'appSGAE/index.html'


class CarreraListView(ListView):
    model = Carrera
    template_name = 'carreras/list.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            print('POST')
            print(request.POST)
            if action == 'searchdata':
                data = []
                for i in Carrera.objects.all():
                    print(i)
                    data.append(i.toJSON())
                    print(data)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Litado de Carreras'
        context['create_url'] = reverse_lazy('appSGAE:CarreraCreateView')
        # context['list_url'] = reverse_lazy('appSGAE:CarreraListView')
        context['entity'] = 'Carrera'
        return context


class CarreraCreateView(CreateView):

    model = Carrera
    form_class = CarreraForm
    template_name = 'carreras/create.html'
    success_url = reverse_lazy('appSGAE:CarreraListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Carrera'
        context['entity'] = 'Carrera'
        context['list_url'] = reverse_lazy('appSGAE:CarreraListView')
        context['action'] = 'add'
        return context


class CarreraUpdateView(UpdateView):

    model = Carrera
    form_class = CarreraForm
    template_name = 'carreras/create.html'
    success_url = reverse_lazy('appSGAE:CarreraListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Carrera'
        context['entity'] = 'Carrera'
        context['list_url'] = reverse_lazy('appSGAE:CarreraListView')
        context['action'] = 'edit'
        return context


class CarreraDeleteView(DeleteView):
    model = Carrera
    template_name = 'carreras/delete.html'
    success_url = reverse_lazy('appSGAE:CarreraListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

        print(request.POST)
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        print(self.success_url)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Carrera'
        context['entity'] = 'Carrera'
        context['list_url'] = self.success_url
        return context


# vista form Carrera
class CarreraFormView(FormView):
    form_class = CarreraForm
    template_name = 'carreras/create.html'
    success_url = reverse_lazy('appSGAE:CarreraListView')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulario Carrera'
        context['entity'] = 'Carrera'
        context['list_url'] = self.success_url
        return context


class NivelListView(ListView):
    model = Carrera
    template_name = 'nivel/list.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            print('POST')
            print(request.POST)
            if action == 'searchdata':
                data = []
                for i in Nivel.objects.all()[:]:
                    print(i)
                    nivel = i.toJSON()
                    nivel['carrera_nivel'] = i.carrera_nivel.nombre
                    print(nivel)
                    data.append(nivel)
                    print(data)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Litado de Niveles'
        context['create_url'] = reverse_lazy('appSGAE:NivelCreateView')
        context['list_url'] = reverse_lazy('appSGAE:NivelListView')
        context['entity'] = 'Nivel'
        return context


class NivelCreateView(CreateView):

    model = Nivel
    form_class = NivelForm
    template_name = 'nivel/create.html'
    success_url = reverse_lazy('appSGAE:NivelListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Nivel'
        context['entity'] = 'Nivel'
        context['list_url'] = reverse_lazy('appSGAE:NivelListView')
        context['action'] = 'add'
        return context


class NivelUpdateView(UpdateView):

    model = Nivel
    form_class = NivelForm
    template_name = 'nivel/create.html'
    success_url = reverse_lazy('appSGAE:NivelListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Nivel'
        context['entity'] = 'Nivel'
        context['list_url'] = reverse_lazy('appSGAE:NivelListView')
        context['action'] = 'edit'
        return context


class NivelDeleteView(DeleteView):
    model = Nivel
    template_name = 'nivel/delete.html'
    success_url = reverse_lazy('appSGAE:NivelListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

        print(request.POST)
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        print(self.success_url)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Nivel'
        context['entity'] = 'Nivel'
        context['list_url'] = self.success_url
        return context


# class form Nivel
class NivelFormView(FormView):
    form_class = NivelForm
    template_name = 'nivel/create.html'
    success_url = reverse_lazy('appSGAE:NivelListView')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulario Nivel'
        context['entity'] = 'Nivel'
        context['list_url'] = self.success_url
        return context

# ******Alumnos vistas


class AlumnoListView(ListView):
    model = Alumno
    template_name = 'alumno/list.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            print('POST')
            print(request.POST)
            if action == 'searchdata':
                data = []
                for i in Alumno.objects.all():
                    print("Sexo "+i.sexo)
                    data.append(i.toJSON())
                    print(data)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Litado de Alumnos'
        context['create_url'] = reverse_lazy('appSGAE:AlumnoCreateView')
        context['list_url'] = reverse_lazy('appSGAE:AlumnoListView')
        context['entity'] = 'Alumno'
        return context


class AlumnoCreateView(CreateView):

    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumno/create.html'
    success_url = reverse_lazy('appSGAE:AlumnoListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Alumno'
        context['entity'] = 'Alumno'
        context['list_url'] = reverse_lazy('appSGAE:AlumnoListView')
        context['action'] = 'add'
        return context


class AlumnoUpdateView(UpdateView):

    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumno/create.html'
    success_url = reverse_lazy('appSGAE:AlumnoListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Alumno'
        context['entity'] = 'Alumno'
        context['list_url'] = reverse_lazy('appSGAE:AlumnoListView')
        context['action'] = 'edit'
        return context


class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'alumno/delete.html'
    success_url = reverse_lazy('appSGAE:AlumnoListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

        print(request.POST)
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        print(self.success_url)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Alumno'
        context['entity'] = 'Alumno'
        context['list_url'] = self.success_url
        return context


# class form Nivel
class AlumnoFormView(FormView):
    form_class = AlumnoForm
    template_name = 'alumno/create.html'
    success_url = reverse_lazy('appSGAE:AlumnoListView')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulario Alumno'
        context['entity'] = 'Alumno'
        context['list_url'] = self.success_url
        return context


# ******Profesor vistas


class ProfesorListView(ListView):
    model = Profesor
    template_name = 'profesor/list.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            print('POST')
            print(request.POST)
            if action == 'searchdata':
                data = []
                for i in Profesor.objects.all():
                    print("Sexo "+i.sexo)
                    data.append(i.toJSON())
                    print(data)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Litado de Profesores'
        context['create_url'] = reverse_lazy('appSGAE:ProfesorCreateView')
        context['list_url'] = reverse_lazy('appSGAE:ProfesorListView')
        context['entity'] = 'Profesor'
        return context


class ProfesorCreateView(CreateView):

    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor/create.html'
    success_url = reverse_lazy('appSGAE:ProfesorListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Profesor'
        context['entity'] = 'Profesor'
        context['list_url'] = reverse_lazy('appSGAE:ProfesorListView')
        context['action'] = 'add'
        return context


class ProfesorUpdateView(UpdateView):

    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor/create.html'
    success_url = reverse_lazy('appSGAE:ProfesorListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Profesor'
        context['entity'] = 'Profesor'
        context['list_url'] = reverse_lazy('appSGAE:ProfesorListView')
        context['action'] = 'edit'
        return context


class ProfesorDeleteView(DeleteView):
    model = Profesor
    template_name = 'profesor/delete.html'
    success_url = reverse_lazy('appSGAE:ProfesorListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

        print(request.POST)
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        print(self.success_url)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Profesor'
        context['entity'] = 'Profesor'
        context['list_url'] = self.success_url
        return context


# class form Profesor
class ProfesorFormView(FormView):
    form_class = ProfesorForm
    template_name = 'profesor/create.html'
    success_url = reverse_lazy('appSGAE:ProfesorFormView')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulario Profesor'
        context['entity'] = 'Profesor'
        context['list_url'] = self.success_url
        return context


# Ejemplos
# def miprimervista(request):
#     return HttpResponse("Hola mi primer vista")
#
#
# def misegundavista(request):
#     data = {
#         'name': 'Dardo'
#     }
#     return JsonResponse(data)
#
#
# def milistavista(request):
#     data = {
#         'Carrera': Carrera.objects.all()
#     }
#     return render(request, 'Carreras/list.html', data)
#

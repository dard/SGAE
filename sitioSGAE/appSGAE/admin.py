from django.contrib import admin
from appSGAE.models import Examen, Carrera, Nivel, Alumno, Profesor, Materia, Aula, InscripcionCarrera, Horario, InscripcionMateria, Asistencia

# Register your models here.


class CarreraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'duracion',
                    'creado', 'actualizado')
    search_fields = ('nombre', 'duracion')
    list_filter = ('id', 'duracion', 'nombre')
    date_hierarchy = 'creado'


class NivelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'carrera_nivel', 'creado',
                    'actualizado')
    search_fields = ('nombre', 'carrera_nivel')
    list_filter = ('id', 'nombre', 'carrera_nivel',
                   'creado', 'actualizado')
    date_hierarchy = 'creado'


class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'dni', 'nombre', 'apellido', 'fecha_nacimiento',
                    'sexo', 'email', 'direccion', 'telefono', 'comorvilidades',
                    'observaciones', 'creado', 'actualizado')
    search_fields = ('id', 'dni', 'nombre', 'apellido')
    list_filter = ('id', 'dni', 'sexo', 'fecha_nacimiento')
    date_hierarchy = 'creado'


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'dni', 'fecha_nacimiento',
                    'sexo', 'email', 'direccion', 'telefono',
                    'creado', 'actualizado')
    search_fields = ('id', 'dni', 'nombre', 'apellido')
    list_filter = ('id', 'dni', 'sexo', 'fecha_nacimiento')
    date_hierarchy = 'creado'


class MateriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'nivel', 'cantidad_horas',
                    'ciclo', 'creado', 'actualizado')
    search_fields = ('id', 'nombre', 'nivel')
    list_filter = ('id', 'nombre', 'nivel', 'ciclo')
    date_hierarchy = 'creado'


class AulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'capacidad', 'virtual', 'creado', 'actualizado')
    search_fields = ('id', 'nombre', 'capacidad')
    list_filter = ('id', 'nombre', 'capacidad')
    date_hierarchy = 'creado'


class InscripcionCarreraAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'alumno', 'turno', 'vigencia_desde')
    search_fields = ('id', 'fecha', 'alumno', 'turno')
    list_filter = ('id', 'fecha', 'alumno', 'turno')
    date_hierarchy = 'creado'


class HorarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'dia',  'virtual', 'aula', 'hora_inicio',
                    'hora_fin', 'materia', 'creado', 'actualizado')
    search_fields = ('id', 'materia')
    list_filter = ('id', 'materia', 'virtual')
    date_hierarchy = 'creado'


class InscripcionMateriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'estado', 'alumno', 'materia', 'creado',
                    'actualizado')
    search_fields = ('id', 'estado', 'alumno', 'materia')
    list_filter = ('id', 'estado', 'alumno', 'materia')
    date_hierarchy = 'creado'


class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'alumno', 'presente', 'materia', 'creado',
                    'actualizado')
    search_fields = ('id', 'fecha', 'alumno', 'presente')
    list_filter = ('id', 'fecha', 'alumno', 'materia', 'presente')
    date_hierarchy = 'creado'


class ExamenAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'inscripcion_materia',
                    'tipo_examen', 'creado', 'actualizado')
    search_fields = ('id', 'inscripcion_materia')
    list_filter = ('id', 'inscripcion_materia', 'tipo_examen')
    date_hierarchy = 'creado'


admin.site.register(Carrera, CarreraAdmin)

admin.site.register(Nivel, NivelAdmin)

admin.site.register(Alumno, AlumnoAdmin)

admin.site.register(Profesor, ProfesorAdmin)

admin.site.register(Materia, MateriaAdmin)

admin.site.register(Aula, AulaAdmin)

admin.site.register(InscripcionCarrera, InscripcionCarreraAdmin)

admin.site.register(Horario, HorarioAdmin)

admin.site.register(InscripcionMateria, InscripcionMateriaAdmin)

admin.site.register(Asistencia, AsistenciaAdmin)

admin.site.register(Examen, ExamenAdmin)

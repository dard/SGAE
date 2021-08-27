from datetime import datetime
# from phonenumber import PhoneNumberField

from django.core.validators import RegexValidator

from django.db import models
from django.forms import model_to_dict

# Create your models here.


class Carrera(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre',
                              unique=True)
    descripcion = models.CharField(max_length=200, verbose_name='Descripción',
                                   unique=True)
    duracion = models.PositiveIntegerField(default=5, verbose_name='Duración')
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)

    def toJSON(self):
        item = model_to_dict(self, exclude=['creado', 'actualizado'])
        return item

    def __str__(self):
        txt = '{0} (Duración: {1} años(s))'
        return txt.format(self.nombre, self.duracion)

    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
        ordering = ['id']


class Nivel(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre',
                              unique=True, null='False')
    descripcion = models.CharField(max_length=200, verbose_name='Descripción',
                                   unique=True)
    carrera_nivel = models.ForeignKey(Carrera, on_delete=models.CASCADE,
                                      verbose_name='Carrera')
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)

    def get_nombre_nivel(self):
        txt = '{0}'
        return txt.format(self.nombre)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.carrera_nivel.nombre)

    def toJSON(self):
        item = model_to_dict(self, exclude=['creado', 'actualizado'])
        item['carrera_nivel'] = self.carrera_nivel.toJSON()
        return item

    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'
        ordering = ['id']


class Alumno(models.Model):
    # Lista sexos con la tuplas
    FEMENIMO = 'F'
    MASCULINO = 'M'
    NO_BINARIO = 'N'

    sexos = [
        (FEMENIMO, 'Femenino'),
        (MASCULINO, 'Masculino'),
        (NO_BINARIO, 'No Binario')
    ]

    dni = models.CharField(max_length=8, unique=True, verbose_name='Dni')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    fecha_nacimiento = models.DateField(default=datetime.now,
                                        verbose_name='Fecha Nac')
    sexo = models.CharField(max_length=1, choices=sexos)
    email = models.EmailField(max_length=30, blank=False, null=False)
    direccion = models.CharField(max_length=40, null=False,
                                 verbose_name='Dirección')
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,12}$")
    telefono = models.CharField(validators=[phoneNumberRegex], max_length=12)
    comorvilidades = models.BooleanField(default=False)
    observaciones = models.CharField(max_length=100, null=True, blank=True,
                                     verbose_name='Observaciones')
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)

    def nombreCompletoAlum(self):
        txt = '{0} {1}'
        return txt.format(self.nombre, self.apellido)

    def __str__(self):
        return '{} {}'.format(self.nombreCompletoAlum(), self.dni)

    def toJSON(self):
        item = model_to_dict(self, exclude=['creado', 'actualizado'])
        item['fecha_nacimiento'] = self.fecha_nacimiento.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['id']


class Profesor(models.Model):
    # Lista sexos con la tuplas
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]

    dni = models.CharField(max_length=8, unique=True, verbose_name='Dni')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    fecha_nacimiento = models.DateField(default=datetime.now,
                                        verbose_name='Fecha de nacimiento')
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    email = models.EmailField(blank=False, null=False, verbose_name='Email')
    direccion = models.CharField(max_length=40, null=True,
                                 verbose_name='Dirección')
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    telefono = models.CharField(validators=[phoneNumberRegex], max_length=12)
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)

    def nombreCompletoProf(self):
        txt = '{0} {1}'
        return txt.format(self.nombre, self.apellido)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.nombreCompletoProf(),
                                       self.dni, self.telefono, self.email,
                                       self.creado)

    def toJSON(self):
        item = model_to_dict(self, exclude=['creado', 'actualizado'])
        item['fecha_nacimiento'] = self.fecha_nacimiento.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['id']


class Materia(models.Model):
    # Lista ciclo con la tuplas
    ciclos = [
        ('0', 'Anual'),
        ('1', 'Primer cuatrimestre'),
        ('2', 'Segundo cuatrimestre')
    ]
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=200,
                                   verbose_name='Descripción',
                                   unique=True)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, null=False,
                              blank=False, verbose_name='nivel')
    anio = models.PositiveIntegerField(default=0, verbose_name='Año/Grado')
    ciclo = models.CharField(max_length=1, choices=ciclos, default='0')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE,
                                 null=False, blank=False,
                                 verbose_name='Profesor')
    cantidad_horas = models.PositiveIntegerField(default=0,
                                                 verbose_name='Horas')
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)

    def get_nombre_materia(self):
        txt = '{0}'
        return txt.format(self.nombre)

    def __str__(self):
        txt = '{} - nivel {} - Ciclo {} - Profesor {} '
        return txt.format(self.nombre, self.nivel.get_nombre_nivel(),
                          self.ciclo,
                          self.profesor.nombreCompletoProf())

    def toJSON(self):
        item = model_to_dict(self, exclude=['creado', 'actualizado'])
        item['profesor'] = self.profesor.toJSON()
        item['nivel'] = self.nivel.toJSON()
        return item

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering = ['id']


class Aula(models.Model):
    nombre = models.CharField(max_length=50, unique=True,
                              verbose_name='Nombre')

    descripcion = models.CharField(max_length=200, verbose_name='Descripción')
    capacidad = models.PositiveIntegerField(default=25,
                                            verbose_name='Capacidad')
    virtual = models.BooleanField(default=False, verbose_name='Es virtual')
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)

    def get_nombre_aula(self):
        txt = '{0}'
        return txt.format(self.nombre)

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.descripcion,
                                 self.capacidad)

    def toJSON(self):
        item = model_to_dict(self, exclude=['creado', 'actualizado'])
        return item

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['id']


class InscripcionCarrera(models.Model):
    turnos = [
        ('M', 'Mañana'),
        ('T', 'Tarde'),
        ('N', 'Noche'),
        ('D', 'Doble Turno')
    ]
    fecha = models.DateField(auto_now_add=False, unique_for_date='fecha',
                             verbose_name='Fecha')
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=False,
                               blank=False,
                               related_name='alumno_inscrip_carrera')
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, null=False,
                                blank=False)
    turno = models.CharField(max_length=1, choices=turnos, default='M')
    vigencia_desde = models.DateField(auto_now_add=True)
    # vigencia_hasta = vigencia_desde + timedelta(days=365)
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.fecha,
                                       self.alumno.nombreCompletoAlum(),
                                       self.carrera.nombre,
                                       self.turno,
                                       self.vigencia_desde)

    def toJSON(self):
        item = model_to_dict(self, exclude=['vigencia_desde',
                                            'creado', 'actualizado'])
        item['alumno'] = self.alumno.toJSON()
        item['carrera'] = self.carrera.toJSON()
        return item

    class Meta:
        verbose_name = 'Inscripcion Carrera'
        verbose_name_plural = 'Inscripciones Carreras'
        ordering = ['id']


class Horario(models.Model):
    dias = [
        ('Lun', 'Lunes'),
        ('Mar', 'Martes'),
        ('Mie', 'Miercoles'),
        ('Jue', 'Jueves'),
        ('Vie', 'Viernes')
    ]

    # fecha = models.DateField(auto_now_add=False, verbose_name='Fecha')
    dia = models.CharField(max_length=3, choices=dias)
    hora_inicio = models.TimeField(auto_now_add=False)
    hora_fin = models.TimeField(auto_now_add=False)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=False,
                                blank=False)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE,
                             null=False, blank=False)
    virtual = models.BooleanField(default=False, verbose_name='Es virtual')
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.dia, self.virtual,
                                          self.hora_inicio,
                                          self.hora_fin,
                                          self.materia.get_nombre_materia(),
                                          self.aula.get_nombre_aula(),)

    def toJSON(self):
        item = model_to_dict(self, exclude=['hora_inicio', 'hora_fin',
                                            'creado',
                                            'actualizado'])
        item['materia'] = self.materia.toJSON()
        item['aula'] = self.aula.toJSON()
        return item

    # Esto le dice a Django que, si ya existe en la BD un horario con el mismo
    # dia, inicio y fin, no lo guarde
    constraints = [
        models.UniqueConstraint(fields=['dia', 'hora_inicio', 'hora_fin'],
                                name='horario_unico')
    ]

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['dia', 'hora_inicio']


class InscripcionMateria(models.Model):
    estados = [
        ('L', 'Libre'),
        ('R', 'Regular')
    ]
    fecha = models.DateField(auto_now_add=False,
                             verbose_name='Fecha')
    estado = models.CharField(max_length=1, choices=estados, default='R')
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=False,
                               blank=False,
                               related_name='alumno_inscrip_materia')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=False,
                                blank=False,
                                related_name='materia_inscripcion')
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.fecha, self.estado,
                                    self.alumno.nombreCompletoAlum(),
                                    self.materia.nombre)

    def toJSON(self):
        item = model_to_dict(self, exclude=['creado', 'actualizado'])
        item['alumno'] = self.alumno.toJSON()
        item['materia'] = self.materia.toJSON()
        return item

    class Meta:
        verbose_name = 'Inscripcion Materia'
        verbose_name_plural = 'Inscripciones Materias'
        ordering = ['id']


class Asistencia (models.Model):
    fecha = models.DateField(auto_now_add=False, verbose_name='Fecha')
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=False,
                               blank=False,
                               related_name='Alumno_asistencia')
    presente = models.BooleanField(default=False, verbose_name='Presente')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE,
                                null=False, blank=False,
                                verbose_name='Materia',
                                related_name='Asistencia_materia')
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.fecha,
                                    self.alumno.nombreCompletoAlum(),
                                    self.presente,
                                    self.materia.get_nombre_materia())

    def toJSON(self):
        item = model_to_dict(self, exclude=['creado', 'vigencia_desde'])
        item['alumno'] = self.alumno.toJSON()
        item['materia'] = self.aula_materia.toJSON()
        return item

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        ordering = ['id']


class Examen (models.Model):
    t_examen = [
        ('P', 'Parcial'),
        ('F', 'Final')
    ]
    fecha = models.DateField(auto_now_add=False, unique_for_date='fecha',
                             verbose_name='Fecha')
    inscripcion_materia = models.ForeignKey(InscripcionMateria,
                                            on_delete=models.CASCADE,
                                            null=False, blank=False,
                                            related_name='Examen_insc_mat',
                                            verbose_name='Inscripción Materia')
    tipo_examen = models.CharField(max_length=1, choices=t_examen,
                                   default='P', verbose_name='Tipo de exámen')
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)

    def __str__(self):
        return '{} {} {}'.format(self.fecha, self.tipo_examen,
                                 self.inscripcion_materia.fecha)

    def toJSON(self):
        item = model_to_dict(self, exclude=['creado', 'actualizado'])
        item['inscripcion_materia'] = self.inscripcion_materia.toJSON()
        return item

    class Meta:
        verbose_name = 'Examen'
        verbose_name_plural = 'Examenes'
        ordering = ['id']

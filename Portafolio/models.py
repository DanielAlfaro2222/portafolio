from django.db import models


class Technology(models.Model):
    """
    Modelo que representa una tecnologia.
    """

    name = models.CharField('Nombre', max_length=45)
    icon = models.CharField('Icono', max_length=120)
    state = models.BooleanField('Estado', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'
        db_table = 'Tecnologias'
        ordering = ['id']


class Project(models.Model):
    """
    Modelo que representa un proyecto.
    """

    name = models.CharField('Nombre', max_length=45)
    description = models.CharField('Descripcion', max_length=255)
    image = models.URLField('Imagen', max_length=255)
    techologies = models.ManyToManyField(
        Technology, verbose_name='Tecnologias')
    github = models.URLField('Repositorio', max_length=255)
    live = models.URLField('Demo', max_length=255, null=True, blank=True)
    state = models.BooleanField('Estado', default=True)

    def __str__(self):
        return self.name

    def tecnologias(self):
        return self.techologies.filter(state=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        db_table = 'Proyectos'
        ordering = ['id']


class Formation(models.Model):
    """
    Modelo que representa una formacion.
    """

    name = models.CharField('Nombre', max_length=120)
    school = models.CharField('Escuela', max_length=100)
    year = models.CharField('Año', max_length=10)
    state = models.BooleanField('Estado', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Formacion'
        verbose_name_plural = 'Formaciones'
        db_table = 'Formaciones'
        ordering = ['id']

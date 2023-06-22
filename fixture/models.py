from django.db import models


class Cambios(models.Model):
    id_cambio = models.AutoField(primary_key=True)
    id_partido = models.ForeignKey('Partidos', models.DO_NOTHING, db_column='id_partido', blank=True, null=True)
    id_jugador_sale = models.ForeignKey('Jugadores', models.DO_NOTHING, db_column='id_jugador_sale', blank=True, null=True)
    id_jugador_entra = models.ForeignKey('Jugadores', models.DO_NOTHING, db_column='id_jugador_entra', related_name='cambios_id_jugador_entra_set', blank=True, null=True)
    minuto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cambios'

    def __str__(self):
        return f"Cambio {self.id_cambio}"


class Equipos(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    abreviatura = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipos'

    def __str__(self):
        return self.nombre
    
    def getAbreviatura (self):
        return self.abreviatura


class Estados(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados'

    def __str__(self):
        return self.nombre


class Fechas(models.Model):
    id_fecha = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    id_estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='id_estado', blank=True, null=True,limit_choices_to={'nombre__in': ['Por Jugar', 'Jugado']})
    id_fixture = models.ForeignKey('Fixtures', models.DO_NOTHING, db_column='id_fixture', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fechas'

    def __str__(self):
        return f"Fecha {self.id_fecha}"


class Fixtures(models.Model):
    id_fixture = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    id_estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='id_estado', blank=True, null=True,limit_choices_to={'nombre__in': ['Vigente', 'No Vigente']})
    id_liga = models.ForeignKey('Ligas', models.DO_NOTHING, db_column='id_liga', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixtures'

    def __str__(self):
        return self.nombre


class Goles(models.Model):
    id_gol = models.AutoField(primary_key=True)
    id_partido = models.ForeignKey('Partidos', models.DO_NOTHING, db_column='id_partido', blank=True, null=True)
    id_jugador = models.ForeignKey('Jugadores', models.DO_NOTHING, db_column='id_jugador', blank=True, null=True)
    minuto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goles'

    def __str__(self):
        return f"Gol {self.id_gol}"


class Jugadores(models.Model):
    id_jugador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    id_equipo = models.ForeignKey(Equipos, models.DO_NOTHING, db_column='id_equipo', blank=True, null=True)
    id_estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='id_estado', blank=True, null=True,limit_choices_to={'nombre__in': ['Activo', 'Titular', 'Suplente', 'No convocado', 'Inactivo']})
    id_posicion = models.ForeignKey('Posiciones', models.DO_NOTHING, db_column='id_posicion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jugadores'

    def __str__(self):
        return self.nombre


class Ligas(models.Model):
    id_liga = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ligas'

    def __str__(self):
        return self.nombre


class Partidos(models.Model):
    id_partido = models.AutoField(primary_key=True)
    id_fecha = models.ForeignKey(Fechas, models.DO_NOTHING, db_column='id_fecha', blank=True, null=True)
    id_equipo_local = models.ForeignKey(Equipos, models.DO_NOTHING, db_column='id_equipo_local', blank=True, null=True)
    id_equipo_visitante = models.ForeignKey(Equipos, models.DO_NOTHING, db_column='id_equipo_visitante', related_name='partidos_id_equipo_visitante_set', blank=True, null=True)
    id_estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='id_estado', blank=True, null=True,limit_choices_to={'nombre__in': ['Por jugar', '1er Tiempo', 'Entretiempo', '2do tiempo', 'Finalizado']})
    inicio_pt = models.TimeField(blank=True, null=True)
    inicio_st = models.TimeField(blank=True, null=True)
    fin_pt = models.TimeField(blank=True, null=True)
    fin_st = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partidos'

    def __str__(self):
        return f"Partido {self.id_partido}: {self.id_equipo_local.getAbreviatura()} - {self.id_equipo_visitante.getAbreviatura()}"
    
        


class Posiciones(models.Model):
    id_posicion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posiciones'

    def __str__(self):
        return self.nombre


class Tarjetas(models.Model):
    id_tarjeta = models.AutoField(primary_key=True)
    id_partido = models.ForeignKey(Partidos, models.DO_NOTHING, db_column='id_partido', blank=True, null=True)
    id_jugador = models.ForeignKey(Jugadores, models.DO_NOTHING, db_column='id_jugador', blank=True, null=True)
    id_tipo_tarjeta = models.ForeignKey('Tipotarjetas', models.DO_NOTHING, db_column='id_tipo_tarjeta', blank=True, null=True)
    minuto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarjetas'

    def __str__(self):
        return f"Tarjeta {self.id_tarjeta}"


class Tecnicos(models.Model):
    id_cuerpo_tecnico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    id_equipo = models.ForeignKey(Equipos, models.DO_NOTHING, db_column='id_equipo', blank=True, null=True)
    id_estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='id_estado', blank=True, null=True,limit_choices_to={'nombre__in': ['Activo', 'Inactivo']})

    class Meta:
        managed = False
        db_table = 'tecnicos'

    def __str__(self):
        return self.nombre


class Tipotarjetas(models.Model):
    id_tipo_tarjeta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipotarjetas'

    def __str__(self):
        return self.nombre

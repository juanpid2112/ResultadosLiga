# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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


class Equipos(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre_equipo = models.CharField(max_length=100, blank=True, null=True)
    abreviatura = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipos'


class Fixture(models.Model):
    id_fecha = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixture'


class Goles(models.Model):
    id_gol = models.AutoField(primary_key=True)
    id_partido = models.ForeignKey('Partidos', models.DO_NOTHING, db_column='id_partido', blank=True, null=True)
    id_jugador = models.ForeignKey('Jugadores', models.DO_NOTHING, db_column='id_jugador', blank=True, null=True)
    minuto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goles'


class Jugadores(models.Model):
    id_jugador = models.AutoField(primary_key=True)
    nombre_jugador = models.CharField(max_length=100, blank=True, null=True)
    numero = models.SmallIntegerField(blank=True, null=True)
    id_equipo = models.ForeignKey(Equipos, models.DO_NOTHING, db_column='id_equipo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jugadores'


class Partidos(models.Model):
    id_partido = models.AutoField(primary_key=True)
    id_fecha = models.ForeignKey(Fixture, models.DO_NOTHING, db_column='id_fecha', blank=True, null=True)
    id_equipo_local = models.ForeignKey(Equipos, models.DO_NOTHING, db_column='id_equipo_local', blank=True, null=True)
    id_equipo_visitante = models.ForeignKey(Equipos, models.DO_NOTHING, db_column='id_equipo_visitante', related_name='partidos_id_equipo_visitante_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partidos'


class Tarjetas(models.Model):
    id_tarjeta = models.AutoField(primary_key=True)
    id_partido = models.ForeignKey(Partidos, models.DO_NOTHING, db_column='id_partido', blank=True, null=True)
    id_jugador = models.ForeignKey(Jugadores, models.DO_NOTHING, db_column='id_jugador', blank=True, null=True)
    minuto = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarjetas'


class Tipotarjeta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipotarjeta'

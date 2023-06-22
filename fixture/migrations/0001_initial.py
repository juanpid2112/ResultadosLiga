# Generated by Django 4.2 on 2023-06-20 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cambios',
            fields=[
                ('id_cambio', models.AutoField(primary_key=True, serialize=False)),
                ('minuto', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cambios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('abreviatura', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'equipos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'estados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fechas',
            fields=[
                ('id_fecha', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fechas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fixtures',
            fields=[
                ('id_fixture', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'fixtures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Goles',
            fields=[
                ('id_gol', models.AutoField(primary_key=True, serialize=False)),
                ('minuto', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'goles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id_jugador', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'jugadores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ligas',
            fields=[
                ('id_liga', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'ligas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Partidos',
            fields=[
                ('id_partido', models.AutoField(primary_key=True, serialize=False)),
                ('inicio_pt', models.TimeField(blank=True, null=True)),
                ('inicio_st', models.TimeField(blank=True, null=True)),
                ('fin_pt', models.TimeField(blank=True, null=True)),
                ('fin_st', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'partidos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Posiciones',
            fields=[
                ('id_posicion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'posiciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarjetas',
            fields=[
                ('id_tarjeta', models.AutoField(primary_key=True, serialize=False)),
                ('minuto', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tarjetas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tecnicos',
            fields=[
                ('id_cuerpo_tecnico', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tecnicos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipotarjetas',
            fields=[
                ('id_tipo_tarjeta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'tipotarjetas',
                'managed': False,
            },
        ),
    ]

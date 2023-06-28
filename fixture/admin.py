from django.contrib import admin
from django import forms
# Register your models here.
from .models import *

class CambiosForm(forms.ModelForm):
    equipo_especifico = forms.ModelChoiceField(queryset=Equipos.objects.all())

    class Meta:
        model = Cambios
        fields = '__all__'

@admin.register(Cambios)
class CambiosAdmin(admin.ModelAdmin):
    form = CambiosForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'id_jugador_sale':
            # Obtener el equipo seleccionado del formulario
            equipo_especifico = request.POST.get('equipo_especifico')

            # Filtrar jugadores por equipo específico (id_equipo) y estado 'Titular'
            kwargs['queryset'] = Jugadores.objects.filter(id_equipo=equipo_especifico, id_estado__nombre='Titular')
        elif db_field.name == 'id_jugador_entra':
            # Obtener el equipo seleccionado del formulario
            equipo_especifico = request.POST.get('equipo_especifico')

            # Filtrar jugadores por equipo específico (id_equipo) y estado 'Suplente'
            kwargs['queryset'] = Jugadores.objects.filter(id_equipo=equipo_especifico, id_estado__nombre='Suplente')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        # Obtener el equipo seleccionado del formulario
        equipo_especifico = form.cleaned_data.get('equipo_especifico')

        # Obtener los jugadores seleccionados
        jugador_sale = form.cleaned_data.get('id_jugador_sale')
        jugador_entra = form.cleaned_data.get('id_jugador_entra')

        # Intercambiar los estados de los jugadores
        jugador_sale.id_estado, jugador_entra.id_estado = jugador_entra.id_estado, jugador_sale.id_estado
        jugador_sale.save()
        jugador_entra.save()

        super().save_model(request, obj, form, change)



class PartidosAdmin(admin.ModelAdmin):
    #Acomodar Fechas por id
    #Acomodar Equipo Locales por nombre
    #Acomodar Equipo Visitantes por nombre
    #Acomodar Estados id
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'id_fecha':
            kwargs['queryset'] = Fechas.objects.filter().order_by('id_fecha')
        if db_field.name == 'id_equipo_local':
            kwargs['queryset'] = Equipos.objects.filter().order_by('nombre')
        if db_field.name == 'id_equipo_visitante':
            kwargs['queryset'] = Equipos.objects.filter().order_by('nombre')
        if db_field.name == 'id_estado':
            kwargs['queryset'] = Estados.objects.filter().order_by('id_estado')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

admin.site.register(Partidos, PartidosAdmin)

class JugadoresAdmin(admin.ModelAdmin):
    #Acomodar los equipos
    #Acomodar los estados
    #Acomodar las posiciones
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'id_equipo':
            kwargs['queryset'] = Equipos.objects.filter().order_by('nombre')
        if db_field.name == 'id_posicion':
            kwargs['queryset'] = Posiciones.objects.filter().order_by('id_posicion')
        if db_field.name == 'id_estado':
            kwargs['queryset'] = Estados.objects.filter().order_by('id_estado')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)






admin.site.register(Jugadores,JugadoresAdmin)








#Esta clase ordena los partidos por 
class TecnicosAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'id_equipo':
            kwargs['queryset'] = Equipos.objects.filter().order_by('nombre')    
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Tecnicos,TecnicosAdmin)



#Esta clase es primero solo mostrar los equipos partidos que esten o en 1er T o 2do T y los ordena
#Segundo muestra los jugadores que sean titulares y los ordena
class GolAdmin(admin.ModelAdmin):
    model = Goles

    def clean(self):
        cleaned_data = super().clean()
        partido = cleaned_data.get('id_partido')
        minuto = cleaned_data.get('minuto')

        if partido and minuto:
            # Verificar si el partido está en el segundo tiempo
            if partido.id_estado.id_estado == 4:
                # Verificar si el minuto está entre 0 y 45
                cleaned_data['minuto'] += 45

        return cleaned_data

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'id_partido':
            kwargs['queryset'] = Partidos.objects.filter(id_estado__in=[2,4]).order_by('id_partido')

        if db_field.name == 'id_jugador':
            kwargs['queryset'] = Jugadores.objects.filter(id_estado=7).order_by('nombre')
            
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Goles,GolAdmin)

#Esta clase toma los partidos y los ordena por id
#Tambien ordena los jugadores por nombre
class TarjetasAdmin (admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'id_partido':
            kwargs['queryset'] = Partidos.objects.filter(id_estado__in=[2,4]).order_by('id_partido')

        if db_field.name == 'id_jugador':
            kwargs['queryset'] = Jugadores.objects.filter(id_estado=7).order_by('nombre')

admin.site.register(Tarjetas,TarjetasAdmin)

#Muestra el registro, no requiere nada adicional
admin.site.register(Equipos)
admin.site.register(Estados)
admin.site.register(Posiciones)
admin.site.register(Ligas)
admin.site.register(Fixtures)
admin.site.register(Fechas)
admin.site.register(Tipotarjetas)
admin.site.register(Localidad)
admin.site.register(Negocio)
admin.site.register(PublicidadLateral)
admin.site.register(PublicidadHorizontal)
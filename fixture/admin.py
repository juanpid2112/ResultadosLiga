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
    list_filter = ('id_estado',)

admin.site.register(Partidos, PartidosAdmin)

class JugadoresAdmin(admin.ModelAdmin):
    list_filter = ('id_equipo','id_estado')


admin.site.register(Jugadores,JugadoresAdmin)

admin.site.register(Equipos)
admin.site.register(Estados)
admin.site.register(Posiciones)
#admin.site.register(Jugadores)
admin.site.register(Tecnicos)
admin.site.register(Ligas)
admin.site.register(Fixtures)
admin.site.register(Fechas)
#admin.site.register(Partidos)
admin.site.register(Goles)
admin.site.register(Tipotarjetas)
admin.site.register(Tarjetas)
#admin.site.register(Cambios)


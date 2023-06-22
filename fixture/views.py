from django.shortcuts import render
from django.views import View
from .models import Partidos, Goles, Jugadores, Equipos

#Clase para obtener la lista de partidos actuales (Los que tiene estado: 1er Tiempo, 2do Tiempo, Entretiempo)
class PartidosActuales(View):

    #Template
    template_name = 'fixture/fixture.html'
    #Ids de los estados que quiero buscar
    estados = [2, 3, 4]

    #Metodo get, donde busco los partidos y retorno una lista con strs que dicen quien esta jugando y cuanto van
    def get(self, request):

        #Obtengo todos los partidos que esten en alguno de los estados buscados
        partidos = Partidos.objects.filter(id_estado__in=self.estados)

        #Inicio un diccionario vacio donde guardare los str que pasare a la plantilla
        str_partidos = {}

        #Recorro la lista de partidos
        for partido in partidos:

            #Obtengo todos los goles que esten asociados a dicho partido, a traves del id_partido
            goles = Goles.objects.filter(id_partido=partido.id_partido)

            #Obtengo todos los jugadores del equipo local
            jugadoresLocal = Jugadores.objects.filter(id_equipo=partido.id_equipo_local.id_equipo)

            #Obtengo todos los jugadores del equipo visitante
            jugadoresVisitante = Jugadores.objects.filter(id_equipo=partido.id_equipo_visitante.id_equipo)

            #Inicio dos listas vacias donde guardare los ids de los jugadores de cada equipo
            idJugLocales = []
            idJugVisitantes = []

            #Recorro jugador por jugador,extrayendo su id y almacenandolo en la lista correspondiente
            for jugador in jugadoresLocal:
                idJugLocales.append(jugador.id_jugador)
            for jugador in jugadoresVisitante:
                idJugVisitantes.append(jugador.id_jugador)

            #Inicio 2 contadores en 0 para los goles de cada equipo
            gLocal = 0
            gVisitante = 0

            #Si hay goles asociados al partido
            if len(goles) != 0:
                #Recorro los goles
                for gol in goles:
                    #Y verifico si corresponde a algun jugador del equipo local
                    if (gol.id_jugador.id_jugador) in idJugLocales:
                        gLocal += 1#En ese caso aumento el contador en 1
                    #Si no, verifico si corresponde a algun jugador del equipo visitante
                    if (gol.id_jugador.id_jugador) in idJugVisitantes:
                        gVisitante += 1#En ese caso aumento el contador en 1

            #Obtengo el equipo local            
            equipoLocal = Equipos.objects.get(id_equipo=partido.id_equipo_local.id_equipo)
            #Obtengo el equipo visitnate
            equipoVisitante = Equipos.objects.get(id_equipo=partido.id_equipo_visitante.id_equipo)

            #Y con todos los datos formo un string con el siguiente formato:
            # GolesLocal NombreEquipoLocal vs NombreEquipoVisitante GolesVisitante
            #Ej: 0 CAU vs ADEA 0
            #Y lo agrego al diccionario
            str_partidos[partido.__str__()] = f"{gLocal} {equipoLocal} vs {equipoVisitante} {gVisitante}"

        #Luego en el retorno, agrego el diccionario
        return render(request, self.template_name, {'str_partidos': str_partidos})


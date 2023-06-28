import time
from django.shortcuts import render
from django.views import View
from .models import Cambios, Fechas, Partidos, Goles, Jugadores, Equipos, Tarjetas

#Clase para obtener la lista de partidos actuales (Los que tiene estado: 1er Tiempo, 2do Tiempo, Entretiempo)
class PartidosActuales(View):

    #Template
    template_name = 'fixture/fixture.html'
    #Ids de los estados que quiero buscar
    estados = [1,2, 3, 4]

    def obtenerIdJ (self,j):
        #Este metodo recibe una lista de Jugadores
        aux = []
        for jugador in j:#Recorro los jugadores agregando su id a la lista
            aux.append(jugador.id_jugador)
        return aux #Retorno la listas
    def obtenerResultado (self,goles,jL,jV):
        #Este metodo recibe los objetos Gol asociado al partido, los objetos Jugador del equipo Local y visitante
        g = [0,0]#Contador de goles, [0] = L, [1] = v
        idL = self.obtenerIdJ(jL)#Obtengo los id de los jugadores locales
        idV = self.obtenerIdJ(jV)#Obtengo los id de los jugadores visitantes
        for gol in goles:#Recorro los goles
            if (gol.id_jugador.id_jugador in idL):#Y verifico si el id del jugador asociado corresponde al local o visitante, en su caso aumento el contador
                g[0] += 1
            if (gol.id_jugador.id_jugador in idV):
                g[1] += 1
        return g#Retorno la lista

    #Metodo get, donde busco los partidos y retorno una lista con strs que dicen quien esta jugando y cuanto van
    def get(self, request):

        #Obtengo la fecha que se este Jugando
        fechaVigente = Fechas.objects.get(id_estado = 15)

        #Obtengo todos los partidos que esten en alguno de los estados buscados
        partidos = Partidos.objects.filter(id_fecha = fechaVigente).order_by('id_partido')#id_estado__in=self.estados,

        #Inicio un diccionario vacio donde guardare los str que pasare a la plantilla
        str_partidos = []

        #Recorro la lista de partidos
        for partido in partidos:

            #Obtengo todos los goles que esten asociados a dicho partido, a traves del id_partido
            goles = Goles.objects.filter(id_partido=partido.id_partido)

            #Obtengo todos los jugadores del equipo local
            jugadoresLocal = Jugadores.objects.filter(id_equipo=partido.id_equipo_local.id_equipo)

            #Obtengo todos los jugadores del equipo visitante
            jugadoresVisitante = Jugadores.objects.filter(id_equipo=partido.id_equipo_visitante.id_equipo)

            #Obtengo el resultado
            resultado =  self.obtenerResultado (goles,jugadoresLocal,jugadoresVisitante)

            #Obtengo el equipo local            
            equipoLocal = Equipos.objects.get(id_equipo=partido.id_equipo_local.id_equipo)

            #Obtengo el equipo visitnate
            equipoVisitante = Equipos.objects.get(id_equipo=partido.id_equipo_visitante.id_equipo)

            #Y con todos los datos formo un string con el siguiente formato:
            # GolesLocal NombreEquipoLocal vs NombreEquipoVisitante GolesVisitante
            #Ej: 0 CAU vs ADEA 0
            #Y lo agrego al diccionario

            #str_partidos[partido.__str__()] = f"{gLocal} {equipoLocal} vs {equipoVisitante} {gVisitante}"
            
            str_partidos.append([resultado[0],equipoLocal,equipoVisitante,resultado[1],partido.id_partido])

        #Luego en el retorno, agrego el diccionario
        return render(request, self.template_name, {'str_partidos': str_partidos,'fecha':fechaVigente})

    


class PartidoEspecifico (View):
    template_name = 'fixture/partidoEspecifico.html'

    def obtenerIdJ (self,j):
        #Este metodo recibe una lista de Jugadores
        aux = []
        for jugador in j:#Recorro los jugadores agregando su id a la lista
            aux.append(jugador.id_jugador)
        return aux #Retorno la listas
    def obtenerResultado (self,goles,jL,jV):
        #Este metodo recibe los objetos Gol asociado al partido, los objetos Jugador del equipo Local y visitante
        g = [0,0]#Contador de goles, [0] = L, [1] = v
        idL = self.obtenerIdJ(jL)#Obtengo los id de los jugadores locales
        idV = self.obtenerIdJ(jV)#Obtengo los id de los jugadores visitantes
        for gol in goles:#Recorro los goles
            if (gol.id_jugador.id_jugador in idL):#Y verifico si el id del jugador asociado corresponde al local o visitante, en su caso aumento el contador
                g[0] += 1
            if (gol.id_jugador.id_jugador in idV):
                g[1] += 1
        return g#Retorno la lista
    
    def obtener_diferencia(self,partido):

        # Obtener la hora y el minuto actual
        hora_actual = time.strftime("%H")
        minuto_actual = time.strftime("%M")
        segundo_actual = time.strftime("%S")
        # Crear el formato HH:MM:SS
        hora_actual = f"{hora_actual}:{minuto_actual}:{segundo_actual}"
        if (partido.id_estado.id_estado == 2):
            hora1 = str(partido.inicio_pt)
        elif (partido.id_estado.id_estado == 4):
            hora1 = str(partido.inicio_st)

        # Extraer horas y minutos de las cadenas de tiempo
        h1, m1, _ = hora1.split(':')
        h2, m2, _ = hora_actual.split(':')

        # Convertir a valores enteros
        h1 = int(h1)
        m1 = int(m1)
        h2 = int(h2)
        m2 = int(m2)

        # Convertir las horas y minutos a minutos totales
        minutos1 = h1 * 60 + m1
        minutos2 = h2 * 60 + m2

        # Calcular la diferencia en minutos
        diferencia = abs(minutos1 - minutos2)

        # Asegurarse de que la diferencia esté en el rango de 0 a 50 minutos
        #diferencia %= 60
        #if diferencia > 50:
        #    diferencia = 60 - diferencia
    
        if (partido.id_estado.id_estado == 2):
            return str(diferencia)
        elif (partido.id_estado.id_estado == 4):
            return str(diferencia+45)
        

    def get (self,request,id):
        #Obtengo el partido
        partido = Partidos.objects.get(id_partido=id)

        #Obtengo el equipo local
        equipo_local = Equipos.objects.get(id_equipo=partido.id_equipo_local.id_equipo)
        #Obtengo el equipo visitnate
        equipo_visitante = Equipos.objects.get(id_equipo=partido.id_equipo_visitante.id_equipo)

        #Obtengo los jugadores locales, y los visitante
        jugadores_local = Jugadores.objects.filter(id_equipo=equipo_local.id_equipo,id_estado__in=[7,8])#Los mismo deben ser Titulares o Suplente
        jugadores_visitante = Jugadores.objects.filter(id_equipo=equipo_visitante.id_equipo,id_estado__in=[7,8])

        jLocales = []#Lista que contendra a los jugadores
        jVisitantes = []
        #Paso los jugadores de un diccionario a una lista para poder ordenarlos y manejarlos mas facil
        for j in jugadores_local:
            jLocales.append(j)
        
        for j in jugadores_visitante:
            jVisitantes.append(j)

        #Los ordeno en base a su estado (Titular, Suplente) y luego en base a su posicion (Arquero,Defensor,Mediocampista,Suplente)
        jLocales.sort(key=lambda obj: (obj.id_estado.id_estado,obj.id_posicion.id_posicion))
        jVisitantes.sort(key=lambda obj: (obj.id_estado,obj.id_posicion))
        
        #Obtengo los cambios
        cambios = Cambios.objects.filter(id_partido=id)
        #Obtengo las tarjetas
        tarjetas = Tarjetas.objects.filter(id_partido=id)
        #Obtengo las goles
        goles = Goles.objects.filter(id_partido=id)

        #Con los goles obtengo el resultado
        resultado = self.obtenerResultado(goles,jugadores_local,jugadores_visitante)

        #Ordeno las 3 en base a los minutos
        lista = []#Para ello los guardo a todos en una misma lista
        for c in cambios:
            lista.append (c)
        for t in tarjetas:
            lista.append (t)
        for g in goles:
            lista.append (g)
        
        #Y los ordeno en base al estado (1er Tiempo o 2do Tiempo) y luego en base al minuto
        lista.sort (key=lambda obj: (obj.id_estado.id_estado,obj.minuto))
        
        
        #Obtengo el tiempo, o en su defecto si esta entretiempo
        tiempo = ""
        if (partido.id_estado.id_estado == 2) or (partido.id_estado.id_estado == 4):#Verifico primero si el partido esta en 1er tiempo o 2do tiempo
            tiempo = (self.obtener_diferencia(partido)) + "' " + partido.id_estado.nombre#En caso de que lo este obtengo los minutos calculando la diferencia entre la hora actual y la hora de comienzo del tiempo
        elif (partido.id_estado.id_estado == 3):#Si esta en entretiempo lo guardo asi nomas
            tiempo = "Entretiempo"
        

        #Guardo todo en un diccionario:
        #local = Obj Equipo Local
        #visitante = Obj Equipo Visitante
        #jL = Lista de Objs Jugador correspondientes al equipo local
        #jV = Lista de Objs Jugador correspondientes al equipo visitante
        #resultado = Array con dos valores enteros correspondientes a los goles de los equipos, [0] = Local, [1] = Visitante
        #tiempo = Minutos o str 'Entretiempo'
        #sucesos = Lista de objetos Cambios, Goles, Tarjetas correspondientes al partido
        datos = {'local':equipo_local,'jL':jLocales,'visitante':equipo_visitante,'jV':jVisitantes,'resultado':resultado, 'tiempo':tiempo,'sucesos':lista}
        #Retorno el template partidoEspecifico y los datos anteriores
        return render (request,self.template_name,{'datos':datos})
    
    
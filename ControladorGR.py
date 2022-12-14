from GR import *
from Grafica import Grafica

class ControladorGR:
    def __init__(self):
        self.gramaticas = []
        self.linea = 0

    def sacarLinea(self):
        try:
            return self.entrada.pop(0)
        except:
            return None

    def verLinea(self):
        try:
            return self.entrada[0]
        except:
            return None

    def identificarElementos(self):
        if self.linea == 0:
            self.gramatica = GR()
            self.gramatica.nombreGR = self.sacarLinea()
        elif self.linea == 1:
            self.gramatica.noTerminales = self.sacarLinea().split(',')
            for noTerminal in self.gramatica.noTerminales:
                self.gramatica.path[noTerminal] = {}
        elif self.linea == 2:
            self.gramatica.terminales = self.sacarLinea().split(',')
        elif self.linea == 3:
            self.gramatica.noTerminalInicial = self.sacarLinea()
        elif self.linea == 4:
            self.producciones = []
            self.aceptacion = []
        if self.linea >= 5:
            produccion = self.sacarLinea().split('>')
            destinoEntrada = produccion[1].split(' ')
            produccion[1] = [s for s in destinoEntrada if s]
            produccion[0] = produccion[0].replace(' ','')
            if produccion[1][0] != '$':
                self.producciones.append(Produccion(produccion[0],produccion[1][0],produccion[1][1]))
            else:
                self.producciones.append(Produccion(produccion[0],produccion[1][0]))
                self.aceptacion.append(produccion[0])
                self.gramatica.eAceptacion = self.aceptacion

            try:
                self.gramatica.path[produccion[0]][produccion[1][0]] = produccion[1][1]
            except:
                self.gramatica.path[produccion[0]][produccion[1][0]] = 'ACEPTADO'

        self.linea += 1
        if self.verLinea() == '%' or not self.verLinea():
            self.gramatica.producciones = self.producciones
            self.gramaticas.append(self.gramatica)
            self.sacarLinea()
            self.linea = 0
        if self.verLinea():
            self.identificarElementos()

    def existeEstado(self,dic,nuevo):
        for estado in dic:
            if nuevo == estado:
                return True
        return False

    def agregarGramatica(self,nombre,noTerminales,eAceptacion,terminales,noTermIni,path):
        prod = []
        gramatica = GR()
        gramatica.nombreGR = nombre
        gramatica.noTerminales = noTerminales.split(';')
        gramatica.eAceptacion = eAceptacion
        gramatica.terminales = terminales.split(';')
        gramatica.noTerminalInicial = noTermIni
        
        for estado,valor in path.items():
            for entrada,destino in valor.items():
                prod.append(Produccion(estado,entrada,destino))

        gramatica.producciones = prod
        gramatica.path = path

        self.gramaticas.append(gramatica)

    def cadenaMinima(self,cadenas,path,estado,acept,alf,cadena,cont) -> list:
        if cont > 20:
            return
        if estado in acept:
            cadenas.append(cadena)
            return
        destinos = path[estado]
        if len(cadenas) > 30:
            return
        for entrada in alf:
            try:
                self.cadenaMinima(cadenas,path,destinos[entrada],acept,alf,cadena + entrada,cont + 1)
            except: pass
        return cadenas

    def generarReporte(self,indice):
        gramatica = self.gramaticas[indice]
        cadenas = self.cadenaMinima([],gramatica.path,gramatica.noTerminalInicial,gramatica.eAceptacion,gramatica.terminales,'',1)
        try:        
            cadenas.sort(key = len)
            cadena = cadenas[0]
        except:
            cadena = '$'
        Grafica().generarDotGR(gramatica,cadena)

    # validando cadena
    def existeTransicion(self,entrada,transiciones):
        for transicion in transiciones:
            if entrada == transicion:
                return True
        return False

    def evaluarVacio(self,estado,aceptados):
        if estado in aceptados:
            return True, []
        return False

    def evaluarCaracteres(self,path,ruta,estado,aceptados,cadena,i):
        transiciones = path[estado]
        if i < len(cadena):
            if self.existeTransicion(cadena[i],transiciones):
                ruta.append([cadena[i],transiciones[cadena[i]]])
                if i == len(cadena) - 1 and transiciones[cadena[i]] in aceptados:
                    return True, ruta
                return self.evaluarCaracteres(path,ruta,transiciones[cadena[i]],aceptados,cadena,i + 1)
        return False

    def validarCadena(self,cadena,indice):
        if len(cadena) > 0:
            return self.evaluarCaracteres(self.gramaticas[indice].path,[],self.gramaticas[indice].noTerminalInicial,self.gramaticas[indice].eAceptacion,cadena,0)
        return self.evaluarVacio(self.gramaticas[indice].noTerminalInicial,self.gramaticas[indice].eAceptacion)

    def generarRuta(self,cadena,indice):
        valido = self.validarCadena(cadena,indice)
        if valido:
            Grafica().generarRuta(self.gramaticas[indice].nombreGR,valido[1],self.gramaticas[indice].noTerminalInicial)

    def verGramaticas(self):
        for i in range(len(self.gramaticas)):
            print(f'Nombre: {self.gramaticas[i].nombreGR}')
            print(f'No terminales: {self.gramaticas[i].noTerminales}')
            print(f'Estados de Aceptacion: {self.gramaticas[i].eAceptacion}')
            print(f'Terminales: {self.gramaticas[i].terminales}')
            print(f'No terminal inicial: {self.gramaticas[i].noTerminalInicial}')
            print(self.gramaticas[i].path)
            print(f'Producciones: ')
            for j in range(len(self.gramaticas[i].producciones)):
                print(f'\t{self.gramaticas[i].producciones[j].__dict__}')
            print()

    def reconocimientoGramatica(self):
        self.entrada = self.entrada.split('\n')
        self.identificarElementos()

    def leerArchivo(self,ruta):
        #ruta = 'Gramatica.gre'
        self.entrada = open(ruta,encoding='utf-8').read()

    def obtenerTerminales(self,indice):
        return ', '.join(self.gramaticas[indice].terminales)

#ctrl = ControladorGR()
#ctrl.leerArchivo()
#ctrl.reconocimientoGramatica()
#ctrl.verGramaticas()
#gr = Grafica()
#gr.generarDotGR(ctrl.gramaticas[0])
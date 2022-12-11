import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from idlelib.tooltip import Hovertip

class App():
    ALTO = 1325
    ANCHO = 600
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Proyecto1 - LFP")
        self.root.geometry(f'{App.ALTO}x{App.ANCHO}')
        self.root.state('zoomed')
        self.root.configure(bg='#212325')

        self.root.grid_columnconfigure(1,weight=1)
        self.root.grid_rowconfigure(0,weight=1)

        self.panelIzq = tk.Frame(master=self.root,width=200)
        self.panelIzq.configure(bg='#2A2D2E')
        self.panelIzq.grid(row=0,column=0,sticky='nswe')

        self.panelDer1 = tk.Frame(master=self.root)
        self.panelDer1.configure(bg='#2A2D2E')
        self.panelDer1.grid(row=0,column=1,sticky="nswe",padx=20,pady=20)

        self.panelDer2 = tk.Frame(master=self.root)
        self.panelDer2.configure(bg='#2A2D2E')
        self.panelDer2.grid(row=0,column=1,sticky="nswe",padx=20,pady=20)

        self.panelDer3 = tk.Frame(master=self.root)
        self.panelDer3.configure(bg='#2A2D2E')
        self.panelDer3.grid(row=0,column=1,sticky="nswe",padx=20,pady=20)

        self.panelDer2.grid_remove()
        self.panelDer3.grid_remove()

        self.panelOpc()
        self.panelCargarArchivo()
        self.panelCrearAFD()
        self.panelCrearGR()
        self.root.mainloop()

    def panelOpc(self):
        self.panelIzq.grid_rowconfigure(0,minsize=10)
        self.panelIzq.grid_rowconfigure(5,weight=1)
        self.panelIzq.grid_rowconfigure(8,minsize=20)
        self.panelIzq.grid_rowconfigure(11,minsize=10)

        self.opciones = tk.Label(master=self.panelIzq,text='Opciones',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        self.opciones.grid(row=1,column=0,pady=10,padx=10)

        self.cargar = tk.Button(master=self.panelIzq,text='Cargar Archivo',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.opcion1)
        self.cargar.grid(row=2,column=0,pady=10,padx=20)

        self.crearAFD = tk.Button(master=self.panelIzq,text='Crear AFD',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.opcion2)
        self.crearAFD.grid(row=3,column=0,pady=10,padx=10)

        self.crearGR = tk.Button(master=self.panelIzq,text='Crear GR',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.opcion3)
        self.crearGR.grid(row=4,column=0,pady=10,padx=10)

        self.salir = tk.Button(master=self.panelIzq,text='Salir',font=('Roboto Medium',11),bg='#D35B58',activebackground='#D35B58',foreground='white',activeforeground='white',width=15,height=1,command=quit)
        self.salir.grid(row=9,column=0,pady=10,padx=10)

    def panelCargarArchivo(self):
        self.panelDer1.rowconfigure((0,1),weight=1)
        self.panelDer1.rowconfigure(5,weight=10)
        self.panelDer1.columnconfigure((0,1),weight=1)
        self.panelDer1.columnconfigure(5,weight=0)

        self.cargarAFD = tk.Button(master=self.panelDer1,text='Cargar AFD',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.chooseFile)
        self.cargarAFD.grid(row=0,column=0,pady=(20,0),padx=(20,10),sticky='nwe')

        self.cargarAFD = tk.Button(master=self.panelDer1,text='Cargar GR',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.chooseFile)
        self.cargarAFD.grid(row=0,column=1,pady=(20,0),padx=(10,20),sticky='nwe')

        self.ruta = tk.Entry(master=self.panelDer1,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.ruta.insert(0,'Ruta')
        self.ruta.configure(disabledbackground='#343638',disabledforeground='white',state='disabled')
        self.ruta.grid(row=1,column=0,columnspan=2,padx=20,sticky='nwe')

    def panelCrearAFD(self):
        self.panelDer2.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)
        self.panelDer2.rowconfigure(10,weight=10)
        self.panelDer2.columnconfigure((0,1,2,3),weight=1)
        self.panelDer2.columnconfigure(4,weight=0)

        title1 = tk.Label(master=self.panelDer2,text='Crear Autómata Finito Determinista',font=('Roboto Medium',20),background='#2A2D2E',foreground='white')
        title1.grid(row=0,column=0,columnspan=4,padx=20,sticky='w')

        nombre = tk.Label(master=self.panelDer2,text='Nombre: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        nombre.grid(row=1,column=0,padx=20,sticky='nw')

        self.nombreAFD = tk.Entry(master=self.panelDer2,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.nombreAFD.configure(disabledbackground='#343638',disabledforeground='white')
        self.nombreAFD.grid(row=2,column=0,columnspan=2,padx=20,sticky='nwe')

        estados = tk.Label(master=self.panelDer2,text='Estados: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        estados.grid(row=1,column=2,padx=20,sticky='nw')

        self.estadosAFD = tk.Entry(master=self.panelDer2,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.estadosAFD.configure(disabledbackground='#343638',disabledforeground='white')
        self.estadosAFD.grid(row=2,column=2,columnspan=2,padx=20,sticky='nwe')
        self.agregarNota(self.estadosAFD,'Ejemplo: A;B;C;D (Separados por punto y coma)')

        alfabeto = tk.Label(master=self.panelDer2,text='Alfabeto: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        alfabeto.grid(row=3,column=0,padx=20,sticky='nw')

        self.alfabetoAFD = tk.Entry(master=self.panelDer2,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.alfabetoAFD.configure(disabledbackground='#343638',disabledforeground='white')
        self.alfabetoAFD.grid(row=4,column=0,columnspan=2,padx=20,sticky='nwe')
        self.agregarNota(self.alfabetoAFD,'Ejemplo: 0;1;2 (Separados por punto y coma)')

        eIni = tk.Label(master=self.panelDer2,text='Estado Inicial: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        eIni.grid(row=3,column=2,padx=20,sticky='nw')

        self.eInicialAFD = tk.Entry(master=self.panelDer2,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.eInicialAFD.configure(disabledbackground='#343638',disabledforeground='white')
        self.eInicialAFD.grid(row=4,column=2,columnspan=2,padx=20,sticky='nwe')

        eAcept = tk.Label(master=self.panelDer2,text='Estados de Aceptación: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        eAcept.grid(row=5,column=0,padx=20,sticky='nw')

        self.eAceptAFD = tk.Entry(master=self.panelDer2,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.eAceptAFD.configure(disabledbackground='#343638',disabledforeground='white')
        self.eAceptAFD.grid(row=6,column=0,columnspan=2,padx=20,sticky='nwe')
        self.agregarNota(self.eAceptAFD,'Ejemplo: A;B;C (Separados por punto y coma)')

        transiciones = tk.Label(master=self.panelDer2,text='Transiciones: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        transiciones.grid(row=5,column=2,padx=20,sticky='nw')

        self.transiAFD = tk.Entry(master=self.panelDer2,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.transiAFD.configure(disabledbackground='#343638',disabledforeground='white')
        self.transiAFD.grid(row=6,column=2,columnspan=2,padx=20,sticky='nwe')
        self.agregarNota(self.transiAFD,'Ejemplo: A,0,B;A,1,C - origen,entrada,destino ; origen,entrada,destino')

        self.guardarAFD = tk.Button(master=self.panelDer2,text='Guardar AFD',font=('Roboto Medium',15),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1)
        self.guardarAFD.grid(row=7,column=0,columnspan=4,pady=(20,0),padx=20,sticky='nwe')

        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground= "#343638", background= "#fff", selectforeground='white',activebackground='#343638',activeforeground='black',foreground='white')

        self.cb = ttk.Combobox(master=self.panelDer2,values=['reporte1','reporte2'],font=('Roboto Medium',16))
        self.cb.grid(row=8,column=0,columnspan=2,padx=20,pady=(50,10),sticky='we')
        self.cb.set('Seleccione un AFD')

        self.cadena = tk.Entry(master=self.panelDer2,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.cadena.configure(disabledbackground='#343638',disabledforeground='white')
        self.cadena.grid(row=8,column=2,columnspan=2,padx=20,pady=(50,10),sticky='we')
        self.agregarNota(self.cadena,'Ingrese una cadena para validar el AFD')

        self.generarReporte = tk.Button(master=self.panelDer2,text='Generar Reporte',font=('Roboto Medium',15),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1)
        self.generarReporte.grid(row=9,column=0,columnspan=2,pady=(20,0),padx=20,sticky='nwe')

        self.validarCad = tk.Button(master=self.panelDer2,text='Validar Cadena',font=('Roboto Medium',15),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1)
        self.validarCad.grid(row=9,column=2,columnspan=2,pady=(20,0),padx=20,sticky='nwe')

    def panelCrearGR(self):
        self.panelDer3.rowconfigure((0,1,2,3,4),weight=1)
        self.panelDer3.rowconfigure(5,weight=10)
        self.panelDer3.columnconfigure((0,1,2,3,4),weight=1)
        self.panelDer3.columnconfigure(5,weight=0)

    def opcion1(self):
        self.panelDer2.grid_remove()
        self.panelDer3.grid_remove()
        self.panelDer1.grid()

    def opcion2(self):
        self.panelDer1.grid_remove()
        self.panelDer3.grid_remove()
        self.panelDer2.grid()

    def opcion3(self):
        self.panelDer1.grid_remove()
        self.panelDer2.grid_remove()
        self.panelDer3.grid()

    def chooseFile(self):
        try:
            self.ruta.configure(state=tk.NORMAL)
            formatos = (
                ("form files","*.afd"),
                ("form files","*.grm"),
            )
            archivo = askopenfilename(
                title='Abrir Archivo',
                initialdir='',
                filetypes = formatos)
            #file = open(archivo).read()
            if not archivo == '':
                self.ruta.delete(0,'end')
                self.ruta.insert(0,str(archivo))
                self.ruta.configure(state='disabled')
                extension = archivo.split('.')
                if extension[1] == 'afd':
                    print('se cargó un autómata')
                else:
                    print('se cargó una gramática')
            self.tokens = None
            self.errores = None
        except:
            pass

    def agregarNota(self,componente,texto):
        self.myTip = Hovertip(componente,f'\n     {texto}     \n')

if __name__ == '__main__':
    app = App()
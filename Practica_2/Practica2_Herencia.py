from tkinter import *#importo todo de clase tkinter para la interfaz grafica

ventana_principal=Tk()#creo mi ventana de tkinter
ventana_principal.title("Figuras geometricas")#le pongo un titulo a la ventana
ventana_principal.geometry("700x400")#le asigono un tamaño
ventana_principal.resizable(1,1)
# para determinar el fondo ventana.configure(bg="dark turquoise")
Label(ventana_principal, text="Laboratorio de Análisis Clínicos DM", font=("Times New Roman",46),fg="black",).place(x=250,y=50)#creo un labbel que servira como titulo en la ventana


#esta es una funcion basica
def cerrar():#lo que hace esta funcion es cerrar la ventana
    ventana_principal.destroy()#como esta trabajando solo con la ventana solo añado .destroy() si estuviera trabajando con varias ventanas añadiria como parametros ventana, para asi usar esta misma funcion en otras ventanas

#CLASE MADRE
class Madre():
    def __init__(self,bandera):#defino mi metodo contructor, ademas de que voy a pasar como paramero una bandera
        self.bandera=bandera#asigno el valo de la bandera que pase a self.bandera para usarla durante toda la clase
        

        #METODO PARA MOSTRAR LA VENTANAS
    def mostrar_ventanas(self):
        #para crear la ventana
        self.ventana_calculo=Toplevel(ventana_principal)#top level hace que se cree una ventana sobre otra, en este caso la ventana principal
        self.ventana_calculo.title("LAC DM")#le doy nombre a la ventana
        self.ventana_calculo.geometry("800x400")#geometria de esta

        #variables que usare para los calculas, todas en double para que entren con punto decimal
        self.glucosa=DoubleVar()
        self.urico=DoubleVar()
        self.colesterol=DoubleVar()
        self.urea=DoubleVar()
        self.tri=DoubleVar()
        self.crea=DoubleVar()
        #metodo para cerrar la ventana que se creea en esta clase
        def cerrar_ventana():
            self.ventana_calculo.destroy()


        #metodoo para crear todo lo que ocupo en los estudios S3
        def estudiosS3(self):
            Label(self.ventana_calculo, text="Laboratorio de Análisis Clínicos DM", font=("Times New Roman",46),fg="black",).place(x=250,y=50)#creo un labbel que servira como titulo de la ventana
            Label(self.ventana_calculo,text="Niveles de Glucosa", font=("Palatino Linotype", 16), fg="black").place(x=50,y=200)#label para indicar que informacion entrará, lo posiciono en un lugar especifico con respecto a los demas
            Label(self.ventana_calculo,text="Niveles de Ácido Urico", font=("Palatino Linotype", 16), fg="black").place(x=50,y=270)#label para indicar que informacion entrará, lo posiciono en un lugar especifico con respecto a los demas
            Label(self.ventana_calculo,text="Niveles de Colesterol", font=("Palatino Linotype", 16), fg="black").place(x=50,y=340)#label para indicar que informacion entrará, lo posiciono en un lugar especifico con respecto a los demas
            
            #estos entry son para que entre la informacion, esta la asigno a los variables que cree anteriormente y situo los entry al lado de la info que debe de entrar

            Entry(self.ventana_calculo,textvariable=self.glucosa,font=("Palatino Linotype", 16)).place(x=400,y=200)
            Entry(self.ventana_calculo,textvariable=self.urico,font=("Palatino Linotype", 16)).place(x=400,y=270)
            Entry(self.ventana_calculo,textvariable=self.colesterol,font=("Palatino Linotype", 16)).place(x=400,y=340)
        
        #metodo para crear todo lo que ocupare en los estudios S6
        def estudiosS6(self):
            Label(self.ventana_calculo,text="Niveles de Urea", font=("Palatino Linotype", 16), fg="black").place(x=50,y=410)#label para indicar que informacion entrará, lo posiciono en un lugar especifico con respecto a los demas
            Label(self.ventana_calculo,text="Niveles de Trigliceridos", font=("Palatino Linotype", 16), fg="black").place(x=50,y=480)#label para indicar que informacion entrará, lo posiciono en un lugar especifico con respecto a los demas
            Label(self.ventana_calculo,text="Niveles de Creatinina", font=("Palatino Linotype", 16), fg="black").place(x=50,y=550)#label para indicar que informacion entrará, lo posiciono en un lugar especifico con respecto a los demas
            
            #estos entry son para que entre la informacion, esta la asigno a los variables que cree anteriormente y situo los entry al lado de la info que debe de entrar
            Entry(self.ventana_calculo,textvariable=self.urea,font=("Palatino Linotype", 16)).place(x=400,y=410)
            Entry(self.ventana_calculo,textvariable=self.tri,font=("Palatino Linotype", 16)).place(x=400,y=480)
            Entry(self.ventana_calculo,textvariable=self.crea,font=("Palatino Linotype", 16)).place(x=400,y=550)


        #aqui dependiendo de la bandera que entre como parametro en el metodo construcotr hara lo siguiente
        if self.bandera==1:
            #si la bandera es 1 significa que los estudios seran de tipo S3, entonces mando a llamar al metodo de estudios S3 para que cree todo lo necesario
            estudiosS3(self)
            Button(self.ventana_calculo,text="Calcular",font=("Palatino Linotype", 16),fg="black",width=20,height=2,command=self.calculo1).place(x=50,y=620)#creo un boton para calcular, donde al presionarlo mandara a llamar otro metdodo que explicare mas abajo
            Button(self.ventana_calculo,text="Salir", font=("Palatino Linotype", 16), fg="black", width=20,height=2,command=cerrar_ventana).place(x=750, y=620)#boton de salir, donde mando a llamar al metodo para destouir la ventana
            
        elif self.bandera==2:
            #si la bandera es igual a 2 entonces
            #mando a llamar los dos metodos para mostrar los datos y los entrys
            estudiosS3(self)
            estudiosS6(self)
            Button(self.ventana_calculo,text="Calcular",font=("Palatino Linotype", 16),fg="black",width=20,height=2,command=self.calculo2).place(x=50,y=620)#nuevamente el boton de calcular para hacer los calculos correspondientes, abajo explicare estos metodos para calcular
            Button(self.ventana_calculo,text="Salir", font=("Palatino Linotype", 16), fg="black", width=20,height=2,command=cerrar_ventana).place(x=750, y=620)#boton de salir


    #metodos para hacer los calculos        
    def calculo1(self):
        #lo primero que hago es hacer la conversion correspondiente de estos y almacenarlas en otra variable
        #uso el .get() para obtener el valor de estas variables
        conversion_glucosa=self.glucosa.get()*18.02
        conversion_urico=self.urico.get()*0.02
        conversion_colestero=self.colesterol.get()*380.66
        #creo unos label para situar especificamente los resultados correspondientes a donde deben de ir
        Label(self.ventana_calculo,text="Son iguales a: " + str(conversion_glucosa)+"mg/dl",font=("Palatino Linotype",16),fg="black").place(x=600,y=200)
        Label(self.ventana_calculo,text="Son iguales a: " + str(conversion_urico)+"mg/dl",font=("Palatino Linotype",16),fg="black").place(x=600,y=270)
        Label(self.ventana_calculo,text="Son iguales a: " + str(conversion_colestero)+"mg/dl",font=("Palatino Linotype",16),fg="black").place(x=600,y=340)
    def calculo2(self):
        self.calculo1()#llamo al metodo de calculo 1, ya que los estudios S6 son los mismos estudios S3 mas otros 3 examenes asi que reuso mis metodos para no volver a escribir las mismas linesa de codigo
        #lo primero que hago es hacer la conversion correspondiente de estos y almacenarlas en otra variable
        #uso el .get() para obtener el valor de estas variables
        conversion_urea=self.urea.get()*6.01
        conversion_tri=self.tri.get()*87.5
        conversion_crea=self.crea.get()*0.01
        #creo unos label para situar especificamente los resultados correspondientes a donde deben de ir
        Label(self.ventana_calculo,text="Son iguales a: " + str(conversion_urea)+"mg/dl",font=("Palatino Linotype",16),fg="black").place(x=600,y=410)
        Label(self.ventana_calculo,text="Son iguales a: " + str(conversion_tri)+"mg/dl",font=("Palatino Linotype",16),fg="black").place(x=600,y=480)
        Label(self.ventana_calculo,text="Son iguales a: " + str(conversion_crea)+"mg/dl",font=("Palatino Linotype",16),fg="black").place(x=600,y=550)
  


#CREACION DE CLASES HIJAS
class hija1(Madre):
    #metodo constructor
    def __init__(self, bandera):#paso la bandera y la asigono
        self.bandera=bandera

class QS6(Madre):
    #metodo constructor
    def __init__(self,bandera):#paso la bandera y la asigono
        self.bandera=bandera


#insatancias
examen1=hija1(1)#creo las instasias correspondientes con las clases hijas ademas de pasarle su debida bandera
examen2=QS6(2)#aqui cambia la bandera debido al estudio a hacer

#situo dos botones donde se presentan los tipos de estudios a hacer, y a cada uno le asigno el command donde mandan a llamar al metodo donde mostrar la ventana para hacer los calculos
Button(ventana_principal,text="Estudio QS3",font=("Palatino Linotype",20),width=20,height=2,bg="gray",command=examen1.mostrar_ventanas).place(x=50,y=200)
Button(ventana_principal,text="Estudio QS6",font=("Palatino Linotype",20),width=20,height=2,bg="gray",command=examen2.mostrar_ventanas).place(x=50,y=350)
#boton de salir, mando a llamar a la funcion para destruir la ventana principal
Button(ventana_principal,text="Salir",font=("Palatino Linotype",20),width=20,height=2,bg="gray",command=cerrar).place(x=50,y=500)
mainloop()#el maion loop es para que este en ciclo el programa y no se cierre de inmediato al abrirlo

from tkinter import *


#********************** PARTE GRAFICA *****************************
class Graficos():
	

	def __init__(self,Ventana=None,Interior=None):
		self.Ventana = Ventana
		self.Interior = Interior

	def VentanaGrafica(self):

		self.Ventana = Tk()
		self.Ventana.title("Cajero - Ing. Diie Duarte")
		self.Ventana.resizable(0,1)
		self.Ventana.iconbitmap("icono.ico")
		
		VacioHead = Frame(self.Ventana,width="350",heigh="30")
		VacioHead.pack()

		InteriorImagen = Frame(self.Ventana,width="350",heigh="150")
		InteriorImagen.pack()

		self.Interior = Frame(self.Ventana,width="350",heigh="310")
		self.Interior.pack()
	

		VacioFoot = Frame(self.Ventana,width="350",heigh="30")
		VacioFoot.pack()

		Limage2 = Label(VacioHead,text="Caja de cambio Automático",fg="blue",font=("Verdana",22),padx=10,pady=10)
		Limage2.pack()

		self.Imagen = PhotoImage(file="welcome.gif")
		Limage = Label(InteriorImagen,image=self.Imagen).place(x=100,y=0)


#*********************** ALGORITMO ********************************
class algoritmo():

	def __init__(self,Interior,CuadroTexto=None,CuadroTexto2=None,aux2=0):
		self.CuadroTexto = CuadroTexto
		self.CuadroTexto2 = CuadroTexto2
		self.Interior = Interior
		self.aux2 = aux2


	def Etiquetas(self,Texto,fila,columna,paddingx,paddingy):
		
		TextosInput = Label(self.Interior, text=Texto)
		TextosInput.grid(row=fila, column=columna,sticky="w",padx=paddingx,pady=paddingy)

	def EtiquetasNeg(self,Texto,fila,columna,paddingx,paddingy):
		
		TextosInput = Label(self.Interior, text=Texto,fg="red")
		TextosInput.grid(row=fila, column=columna,sticky="w",padx=paddingx,pady=paddingy)

	def Botones(self,Texto,callback,fila,columna,paddingx,paddingy):
		
		boton = Button(proceso.Interior,text=Texto, command=callback)
		boton.grid(row=fila,column=columna,padx=paddingx,pady=paddingy)

	def CampoInput(self,alineacion,fila,columna,paddingx,paddingy):
		
		self.CuadroTexto = Entry(self.Interior)
		self.CuadroTexto.config(justify=alineacion)
		self.CuadroTexto.grid(row=fila, column=columna,sticky="e",padx=paddingx,pady=paddingy)

	def CampoInput2(self,alineacion,fila,columna,paddingx,paddingy):
		
		self.CuadroTexto2 = Entry(self.Interior)
		self.CuadroTexto2.config(justify=alineacion)
		self.CuadroTexto2.grid(row=fila, column=columna,sticky="e",padx=paddingx,pady=paddingy)


	def inventario(self,efectivo):
		count = 0
		suma = 0
		for x in efectivo:
			suma+=efectivo[x][0]*efectivo[x][1]
			if(count<=4):
				self.Etiquetas("{}  -->  {}".format((x),(efectivo[x][0]),),count,0,10,2)
			else:
				self.Etiquetas("{}  -->  {}".format((x),(efectivo[x][0]),),count-5,1,10,2)
			count+=1

		TextosInput = Label(self.Interior, text="Dinero disponible  -->  {:.2f}".format((suma),),fg="green",font=("Verdana",14))
		TextosInput.grid(row=count-5, column=0,sticky="w",padx=10,pady=2)

	def limpiarCampos(self):

		for i in range(0,self.aux2):
			self.Etiquetas("                                                                                         .",i+8,0,0,0)


	def resultado(self,efectivo):
		
		if(self.aux2 != 0):
			self.limpiarCampos()
		else:
			self.aux2=1
			self.limpiarCampos()

		billete = self.CuadroTexto.get()
		aPagar = self.CuadroTexto2.get()


		try:

			billete = float(billete)
			aPagar = float(aPagar)
			Total = billete - aPagar

			
			if(Total == 0):
				self.EtiquetasNeg("El cambio es $0 pesos",8,0,10,2)
			else:

				TextosInput = Label(self.Interior,text="Su cambio es de ${:.2f} pesos".format((Total),),fg="green",font=("Verdana",14))
				TextosInput.grid(row=8, column=0,sticky="w",padx=10,pady=2)	

			if(billete == 0):
				self.EtiquetasNeg("No ingreso Dinero ....",8,0,10,2)
				Total=0

			if(aPagar== 0):
				self.EtiquetasNeg("No compró nada, regresale sus ${} pesos".format((billete),),8,0,10,2)
				Total=0

			if(aPagar == 0 and billete == 0):
				self.EtiquetasNeg("Los campos están en cero pesos",8,0,10,2)
				Total = 0

			
			if(billete<aPagar):
				self.EtiquetasNeg("Sus ${} pesos no alcanza para comprar".format((billete),),8,0,10,2)
				Total = 0


		except ValueError:

			self.EtiquetasNeg("Atencion: Debe ingresar un número entero.",8,0,10,2)
			aPagar=0
			billete=0
			Total = 0

		if(efectivo["Billetes de $50"][0] == 0 or efectivo["Billetes de $20"][0] == 0):
			suma = 0
			suma +=efectivo["Billetes de $50"][0]*efectivo["Billetes de $50"][1]
			suma +=efectivo["Billetes de $20"][0]*efectivo["Billetes de $20"][1]
			suma +=efectivo["Monedas de $10"][0]*efectivo["Monedas de $10"][1]
			suma +=efectivo["Monedas de $5"][0]*efectivo["Monedas de $5"][1]
			suma +=efectivo["Monedas de $2"][0]*efectivo["Monedas de $2"][1]
			suma +=efectivo["Monedas de $1"][0]*efectivo["Monedas de $1"][1]
			suma +=efectivo["Monedas de $.50"][0]*efectivo["Monedas de $.50"][1]
			if(Total>suma):
				self.EtiquetasNeg("No hay cambio....",8,0,10,2)
				Total = 0
				aPagar = 0
				Billete = 0


		#Aumenta  el dinero c		

		if(aPagar >0 and billete >0):
				for h in efectivo:
					#Aumenta el dinero si coincide la denominacion del billete
					if(efectivo[h][1] == billete):
						efectivo[h][0]+=1
						billete = 0
					#En caso de que no sea una denominacion real, lo desconpone
					elif(billete > efectivo[h][1]):
						billete -= efectivo[h][1]
						efectivo[h][0]+=1

		
		#Comparación
		contador = 1
		aux=0
		for x in efectivo:

			efectivoConvertCant = int(efectivo[x][0])
			efectivoConvertDenom = float(efectivo[x][1])
			aux = efectivoConvertCant
			contadorLocal=0
			while(Total>=efectivoConvertDenom):
				if(efectivoConvertCant>0):
					Total-=efectivoConvertDenom
					efectivoConvertCant-=1
					efectivo[x][0]-=1
					contadorLocal+=1
					self.Etiquetas("{0} a entregar --> {1}".format((x),(contadorLocal),),contador+8,0,10,2)				
					if(Total ==0):
						break
				else:
					break
			#Elcambio de columna por cada billete entregado
			if(aux>efectivoConvertCant):
				contador+=1
				self.aux2 = contador

		self.inventario(efectivo)
					




efectivo = {
#Estructura
# 	String		Cantidad  Valor
	"Billetes de $500":[0,500],
	"Billetes de $200":[3,200],
	"Billetes de $100":[4,100],
	"Billetes de $50":[8,50],
	"Billetes de $20":[6,20],
	"Monedas de $10":[20,10],
	"Monedas de $5":[15,5],
	"Monedas de $2":[10,2],
	"Monedas de $1":[40,1],
	"Monedas de $.50":[20,0.50],
}	

start = Graficos()
start.VentanaGrafica()
proceso = algoritmo(start.Interior)
proceso.inventario(efectivo)

proceso.CampoInput("center",6,1,10,10)
proceso.CampoInput2("center",7,1,10,10)


proceso.Etiquetas("Ingrese la cantidad Recibida de Dinero",6,0,10,2)	
proceso.Etiquetas("Ingrese la cantidad a Pagar",7,0,10,2)

proceso.Botones("Pagar $",lambda:proceso.resultado(efectivo),7,2,10,10)


#*************************** FIN DE GRAFICOS ************************
start.Ventana.mainloop()

from tkinter.constants import LEFT
import requests
import tkinter
from tkinter import Label, messagebox


# Constantes
ancho = 550
largo = 250
appName = "WeatherApp"
url = "http://api.weatherapi.com/v1/current.json"
apiKey = "2c1d6cf9fa914ed49bb204115211807"


# Tipo propio
class Tiempo:
    def __init__(self, nombreCiudad, temperatura, region, uv, horario):
        self.nombreCiudad = nombreCiudad
        self.temperatura = str(temperatura)
        self.region = str(region)
        self.uv = str(uv)
        self.horario = str(horario)

    def showResults(self):
        mostarClima.configure(text=self.temperatura+"°C")
        nombreCorrectoClima.configure(
            text="Ciudad: "+self.nombreCiudad)
        regionCorrectoClima.configure(
            text="Region: "+self.region)
        UVCorrectoClima.configure(
            text="UV: "+self.uv)
        horarioCorrectoClima.configure(
            text="Horario local: "+self.horario)


def checkWeahterAPI(city):
    if(city != ''):
        params = {
            "key": apiKey,
            "q": city,
            "aqi": "no"
        }
        consulta = requests.get(url, params=params)
        # print(consulta.json())
        # print("\n-----------------------------------\n")
        if(consulta.ok):
            tiempo = Tiempo(consulta.json()["location"]["name"], consulta.json()[
                "current"]["temp_c"], consulta.json()["location"]["region"], consulta.json()["current"]["uv"], consulta.json()["location"]["localtime"])
            tiempo.showResults()
        else:
            messagebox.showerror(
                title="ERROR", message="No has introducido bien el nombre de la ciudad")
    else:
        messagebox.showerror(
            title="ERROR", message="No has introducido ninguna ciudad")


def configureWindow():
    app.geometry(newGeometry=str(ancho)+"x"+str(largo))
    app.title(appName)


def start():
    app.mainloop()


app = tkinter.Tk()
configureWindow()

# Configurando la ventana
logoApp = Label(master=app, text="Weather App", font=(
    "Arial", 20, "bold"), foreground="PURPLE")
logoApp.grid(row=0, column=1)
ciudadBusqueda = tkinter.Entry(master=app)
ciudadBusqueda.focus()
ciudadBusqueda.grid(row=1, column=0)
obtenerClimaButton = tkinter.Button(
    master=app, text="Obtener el clima", command=lambda: checkWeahterAPI(ciudadBusqueda.get()), width=20)
obtenerClimaButton.grid(row=2, column=0)
nombreCorrectoClima = Label(master=app)
nombreCorrectoClima.grid(row=1, column=2)
regionCorrectoClima = Label(master=app)
regionCorrectoClima.grid(row=2, column=2)
UVCorrectoClima = Label(master=app)
UVCorrectoClima.grid(row=3, column=2)
horarioCorrectoClima = Label(master=app)
horarioCorrectoClima.grid(row=4, column=2)
mostarClima = tkinter.Label(
    master=app, font=("Courier", 50, "normal"))
mostarClima.grid(row=5, column=2)

start()

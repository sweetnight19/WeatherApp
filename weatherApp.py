import tkinter
from tkinter import Label, messagebox
import requests

# Constantes
ancho = 550
largo = 250
appName = "WeatherApp"
url = "http://api.weatherapi.com/v1/current.json"
apiKey = ""


# Tipo propio
class Tiempo:
    def __init__(self, nombreciudad, temperatura, region, uv, horario, pais):
        self.__nombreCiudad = nombreciudad
        self.__temperatura = str(temperatura)
        self.__region = str(region)
        self.__uv = str(uv)
        self.__horario = str(horario)
        self.__pais = str(pais)

    def showresults(self):
        mostarClima.configure(text=self.__temperatura+"°C")
        nombreCorrectoClima.configure(
            text="Ciudad: "+self.__nombreCiudad)
        regionCorrectoClima.configure(
            text="Region: "+self.__region)
        UVCorrectoClima.configure(
            text="UV: "+self.__uv)
        horarioCorrectoClima.configure(
            text="Horario local: "+self.__horario)
        paisCorrectoClima.configure(text="Pais: "+self.__pais)


def checkweahterapi(city):
    if city != '':
        params = {
            "key": apiKey,
            "q": city,
            "aqi": "no"
        }
        consulta = requests.get(url, params=params)
        # print(consulta.json())
        # print("\n-----------------------------------\n")
        if consulta.ok:
            tiempo = Tiempo(consulta.json()["location"]["name"], consulta.json()["current"]["temp_c"], consulta.json()[
                            "location"]["region"], consulta.json()["current"]["uv"], consulta.json()["location"]["localtime"], consulta.json()["location"]["country"])
            tiempo.showresults()
        else:
            messagebox.showerror(
                title="ERROR", message="No has introducido bien el nombre de la ciudad")
    else:
        messagebox.showerror(
            title="ERROR", message="No has introducido ninguna ciudad")


def configurewindow():
    app.geometry(newGeometry=str(ancho)+"x"+str(largo))
    app.title(appName)


def readapikey():
    global apiKey

    file = open("apiKey.txt")
    file.readline()
    apiKey = file.readline()


def start():
    app.mainloop()


if __name__ == "__main__":
    app = tkinter.Tk()
    readapikey()
    configurewindow()

    # Configurando la ventana
    logoApp = Label(master=app, text="Weather App", font=(
        "Arial", 20, "bold"), foreground="PURPLE")
    logoApp.grid(row=0, column=1)
    ciudadBusqueda = tkinter.Entry(master=app)
    ciudadBusqueda.focus()
    ciudadBusqueda.grid(row=1, column=0)
    obtenerClimaButton = tkinter.Button(
        master=app, text="Obtener el clima", command=lambda: checkweahterapi(ciudadBusqueda.get()), width=20)
    obtenerClimaButton.grid(row=2, column=0)
    nombreCorrectoClima = Label(master=app)
    nombreCorrectoClima.grid(row=1, column=2)
    regionCorrectoClima = Label(master=app)
    regionCorrectoClima.grid(row=2, column=2)
    paisCorrectoClima = Label(master=app)
    paisCorrectoClima.grid(row=3, column=2)
    UVCorrectoClima = Label(master=app)
    UVCorrectoClima.grid(row=4, column=2)
    horarioCorrectoClima = Label(master=app)
    horarioCorrectoClima.grid(row=5, column=2)
    mostarClima = tkinter.Label(master=app, font=("Courier", 50, "normal"))
    mostarClima.grid(row=6, column=2)
    start()

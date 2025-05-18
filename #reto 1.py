#Hecho por: Ignacio elizondo y Carlos Gutiérrez
#fecha de creación: 16/5/2025 a las 07:47
#última modificación: 
#versión de python: 3.13.2

#importaciones
import tkinter as tk
from tkinter import messagebox
import requests

#funciones
def buscarPokemons():
    """
    Funcionamiento: Recibe una cantidad de pokemons por parte del usuario para buscar y guardar.
    Entradas:
    -cantidad(int)= es la cantidad de pokemons que el usuario quiere buscar
    Salidas:
    - retorna el documento misPokemons.txt donde se guardan los pokemons buscados
    """
    cantidad = cantidadEntrada.get()
    tamannoMaximo= requests.get("https://pokeapi.co/api/v2/pokemon?limit=1") #se obtiene el tamaño máximo de pokemons
    pokemonsMax = tamannoMaximo.json()['count']
    try:
        cantidad = int(cantidad)
        if cantidad <= 0:
            messagebox.showerror("Error", "La cantidad debe ser mayor que cero 0")
        elif cantidad > pokemonsMax:
            raise ValueError(f"La cantidad debe ser menor o igual a {pokemonsMax}.")
        with open("misPokemons.txt", "w") as file: #acá se crea el txt
            for i in range(1, cantidad+1):
                pokemonsTamannoMax = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
                datosPokemon = pokemonsTamannoMax.json()
                idPokedex = datosPokemon['id']
                nombre = datosPokemon['name']
                file.write(f"{idPokedex}^{nombre}\n")
                messagebox.showinfo("Éxito", f"Se han guardado {cantidad} Pokémon en 'misPokemons.txt'.")#retroalimentación de que se guardaron los pokemons en el .txt
    except ValueError as valueError: #excepción 1
        messagebox.showerror("Ocurrió un problema", str(valueError))
    except Exception as e:#excepción 2 
        messagebox.showerror("Algo salió mal, intente de nuevo de nuevo por favor.")

def limpiarEntrada():
    """
    Funcionaminento: limpia el campo de entrada para el usuario
    Entradas: 
    -presionar el botón de limpiar
    Salidas:
    -Limpia el campo de entrada para colocar un valor nuevo si el usuario desea
    """
    return cantidadEntrada.delete(0, tk.END)

ventana = tk.Tk() # se crea la ventana principal
ventana.title("Búsqueda de Pokémon")

labelCantidad = tk.Label(ventana, text="Cantidad deseada:") #se crean los campos de entrada
labelCantidad.pack()

cantidadEntrada = tk.Entry(ventana)
cantidadEntrada.pack()

botonBuscar = tk.Button(ventana, text="Buscar", command=buscarPokemons)#se crean los botones, este es buscar
botonBuscar.pack()

botonLimpiar = tk.Button(ventana, text="Limpiar", command=limpiarEntrada)#este es limpiar 
botonLimpiar.pack()

ventana.mainloop() #se ejecuta la ventana mediante un ciclo

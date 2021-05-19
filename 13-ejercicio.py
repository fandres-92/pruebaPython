playlist = {} # Diccionario vacio
playlist['canciones'] = [] # lista vacia de canciones

# Funcion principal
def app():

    # Agregar playlist
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('como desea nombrar la playlist?\r\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist

            # ya tenemos un nombre, desactivar el true
            agregar_playlist = False

            print(playlist)

app()


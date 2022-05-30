'''
Gestiona una librería virtual

Podrá buscar libros por los siguientes parámetros:

id
Autor
Título
Genero
Ademas, se podrá modificar los datos de cada uno de los libros así como eliminarlos
'''
from ast import Break, Continue


DB = [{
    "id": "cf_1",
    "title": "El hombre bicentenario",
    "author": "Isaac Asimov",
    "genre": "Ciencia ficcion"
},
{
    "id": "ne_1",
    "title": "Lobo de mar",
    "author": "Jack London",
    "genre": "Narrativa extranjera"
},
{
    "id": "np_1",
    "title": "El legado de los huesos",
    "author": "Dolores Redondo",
    "genre": "Narrativa policiaca"
},
{
    "id": "dc_1",
    "title": "El error de Descartes",
    "author": "Antonio Damasio",
    "genre": "Divulgación científica"
},
{
    "id": "dc_2",
    "title": "El ingenio de los pajaros",
    "author": "Jennifer Ackerman",
    "genre": "Divulgacion cientifica"
},
{
    "id": "ne_1",
    "title": "El corazon de las tinieblas",
    "author": "Joseph Conrad",
    "genre": "Narrativa extranjera"
},
{
    "id": "dc_5",
    "title": "Metro 2033",
    "author": "Dmitri Glujovski",
    "genre": "Divulgacion cientifica"
},
{
    "id": "dc_5",
    "title": "Sidharta",
    "author": "Hermann Hesse",
    "genre": "Narrativa extranjera"
},
{
    "id": "el_1",
    "title": "Andres Trapiello",
    "author": "Las armas y las letras",
    "genre": "Narrativa extranjera"
},
{
    "id": "aa_1",
    "title": "El poder del ahora",
    "author": "Ekhart Tolle",
    "genre": "Narrativa extranjera"
},
]

genre = ["Narrativa extranjera", "Divulgacion cientifica", "Narrativa policiaca", "Ciencia ficcion", "Autoayuda"]

#Función menú inicial
def initial_menu ():
    print (('\033[36m'+"Bienvenido a la libreria").center (50, " "))
    print (("Pulse 1"+'\033[0m'+" si quiere realizar la busqueda por"+'\033[36m'+" id**").center (30, " "))
    print (("Pulse 2"+'\033[0m'+" si quiere realizar la busqueda por"+'\033[36m'+" autor, titulo o genero").center (30, " "))
    print (("Pulse 3"+'\033[0m'+" si desea ver los"+'\033[36m'+" generos disponibles").center (50, " "))
    print (("Pulse q"+'\033[0m'+" si desea"+'\033[36m'+" salir").center (50," " ))
    print ("**"+'\033[0m'+"Si desea actualizar un libro o eliminarlo debe buscar primero por id\n")
#Función menú secundario
def secondary_menu ():
    print (('\033[36m'+"Pulse 5"+'\033[0m'+" si desea"+'\033[36m'+" modificar"+'\033[0m'+" algun campo del libro\n").center (30, " "))
    print (('\033[36m'+"Pulse 6"+'\033[0m'+" si desea"+'\033[36m'+" eliminar"+'\033[0m'+" el libro de la base de datos").center (30, " ")+'\033[0m')
#Función de búsqueda por ISBN
def search_by_id (user_id, database_bookshop):
    for book in database_bookshop:
        if book ["id"] == user_id:
            return book
#Función de búsqueda por autor, título y género
def searching_book (user, term_search, database_bookshop):
    books_list = []
    for book in database_bookshop:
        if book [term_search].lower().find (user.lower()) >= 0:
            books_list.append (book)
    return books_list
#Función pel estilo de impresión de los libros
def pretty_book (book):
    for k, v in book.items ():
        print ('\033[92m'+f"{k} : {v}"+'\033[0m')
    print ()
#Función para actualizar:
def id_modifying (book_to_update):
    print ('\033[36m'+"\nPulse 1 cuando desee modificar el campo, si no pulse enter\n"+'\033[0m')
    for k, v in book_to_update.items ():
        print (f"{k} : {v}")
        user = input ()
        if user == "1":
            user_new_value = input ('\033[36m'+f"Introduzca el nuevo {k}: \n"+'\033[0m')
            print ()
            book_to_update [k] = user_new_value
        else:
            Continue
    return book_to_update
#Función para eliminar un libro
def removing_book  (book_to_remove):
    DB.remove (book_to_remove)
    return DB
#Función de búsqueda por lista de géneros
def genre_list (genres):
    for k, v in enumerate (genres):
        print ('\033[36m'+f"{k + 1}."+'\033[0m'+f"{v}")
    user = input  ('\033[36m'+"\nPulse el numero del genero por el que desea buscar: "+'\033[0m')
    return genres [int (user)-1]


user = ""
while user != "q":
    initial_menu ()
    user = input ()
    if user == "1":
        user_id = input ('\033[36m'+"Introduzca el id: "+'\033[0m')
        book_founded = search_by_id (user_id, DB)
        if book_founded:
            print ('\033[35m'+"\nSe ha encontrado el libro:\n"+'\033[0m')
            pretty_book (book_founded)
            secondary_menu ()
            user = input ()
            if user == "5":
                modified_book = id_modifying (book_founded)
                print ('\033[35m'+"Este es el libro actualizado:\n"+'\033[0m')
                pretty_book (modified_book)
            elif user == "6":
                updated_DB = removing_book (book_founded)
                if not book_founded in updated_DB:
                    print ('\033[92m'+f"El libro con id {user_id} se ha eliminado correctamente"+'\033[0m')
                else:
                    print ('\033[91m' + f"El libro con id {user_id} no se ha eliminado correctamente. Vuelva a intentarlo!" + '\033[0m')
        else:
            print ('\033[91m' + f"\nNo se ha encontrado el libro con el id {user_id}"+'\033[0m')
        user = input ('\033[93m'+"\nContinuar\n"+'\033[0m')
    elif user == "2":
        user_search = input ('\033[36m'+"Introduce tu parametro ('author', 'title', 'genre') de busqueda: "+'\033[0m').lower()
        user_term = input ('\033[36m'+"Introduce tu termino de busqueda: "+ '\033[0m').lower()
        books_list = searching_book (user_term, user_search, DB)
        if books_list:
            print ('\033[35m'+f"\nA continuacion se muestran los libros resultado de la busqueda:\n"+'\033[0m')
            for book in books_list:
                pretty_book (book)
        else:
            print ('\033[91m'+ f"No se ha encontrado {user_term} con el parametro de busqueda {user_search} en nuestra base de datos"+'\033[0m')
        user = input('\033[93m'+"\nContinuar\n"+'\033[0m')
    elif user == "3":
        print ('\033[35m'+"\nEstos son los generos disponibles\n"+'\033[0m')
        result =  genre_list(genre)
        books_by_genre_list = searching_book (result, "genre", DB)
        if books_by_genre_list:
            print ()
            print ('\033[35m'+f"Estos son los libros disponibles del genero {result} "+'\033[0m')
            print ()
            for book in books_by_genre_list:
                pretty_book (book)
        else:
            print ()
            print ('\033[91m' + f"No hay libros del genero {result} en nuestra base de datos"+'\033[0m')
        user = input ('\033[93m'+"\nContinuar\n"+'\033[0m')
    

#1.

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)

estudiantes[0]['last_name']= 'Bryant'
print(estudiantes)

directorio_deportes['fútbol'][0]='Andrés'
print(directorio_deportes)

z[0]['y'] = 30
print(z)


#2.

def iterateDictionary(some_list):
    for todos in some_list:
        for key, value in todos.items():
            print(f"{key} - {value}", end =" ")
        print()

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

iterateDictionary(estudiantes)


#3.

def iterateDictionary2(key_name, some_list):
    for diccion in some_list:          #El bucle asigna a cada diccionario en la lista, la variable diccion. Esto permite hacer operaciones en cada diccionario. 
        if key_name in diccion:               #El "in" nos permite revisar si la clave "key_name" esta en el diccionario actual.
            print(diccion[key_name])

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

print("Valores de la clave 'first_name':")
iterateDictionary2('first_name', students)

print("Valores de la clave 'last_name':")
iterateDictionary2('last_name', students)



#4. 


def printInfo (some_dict):

    for clav in some_dict:
        print(len(some_dict[clav]), clav.upper())  #se imprime el largo de la lista y luego el nombre/key en mayusculas
        for item in some_dict[clav]:          #se imprime cada uno de los items de la lista = some_dict[clav]
            print(item)

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

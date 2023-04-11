#Colocamos un mensaje de bienvenida e instrucción
print('Hola, ingrese los datos requeridos para indicarle su IMC por favor')
#Solicitamos que el usuario introduzca su nombre
nombre = input('Nombre: ')
#Solicitamos que el usuario introduzca apellido paterno
apellPat = input('Apellido Paterno: ')
#Solicitamos que el usuario introduzca apellido materno
apellMat = input('Apellido Materno: ')
#Soliciatmos al usuario que introduzca edad en años, no especificamos clase de variable ya que para el ejercicio no es relevante
edad = input('Edad (AÑOS): ')
#Solicitamos el peso del usuario, especificamos clase "float" de la variable
peso = float (input ('Peso (KG): '))
#Solicitamos el peso del usuario, especificamos clase "float" de la variable
estatura = float (input ('Estatura (MT): '))
#Realizamos el cálculo
IMC = peso / estatura**2
#Finalmente imprimimos el resultado incluyendo la información del usuario
print((nombre) + (' ') + (apellPat) + (' ') + (apellMat) + (', ') + ('Su IMC es: ') + str(IMC))
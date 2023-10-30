import Clases as C #importacion para el archivo clases.py
import datetime  #importacion para usar fecha

#MENU PRINCIPAL
def menu():
    while True:
        print("\n-----MENU PRINCIPAL-----")
        print("1. Ingresar como alumno")
        print("2. Ingresar como profesor")
        print("3. Ver cursos")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":   #Validacion estudiante
            email_a_validar = str(input("Ingrese su mail: "))
            contrasenia_a_validar = str(input("Ingrese su contraseña: "))
            validacion = C.Estudiante.validar_credenciales(
                email_a_validar, contrasenia_a_validar
            )
            if validacion == True:
                print("\nIngreso exitoso como estudiante\n")
                while True:
                    print("-----SUB-MENU ALUMNO-----")
                    print("1. Matricularse a un curso")
                    print("2. Desmatricularse de un curso")
                    print("3. Ver curso")
                    print("4. Volver al menu principal")
                    sub_opcion = input("Seleccione una opción: ")

                    if sub_opcion == "1":
                        if len(C.cursos_disponibles) > 0:
                            print("1 Programación I")
                            print("2 Programación II")  #si ingresa el numero buscamos por el indice en cual se cargo ese curso en la lista 'C.cursos_disponibles
                            print("3 Laboratorio I")    #aclaracion (No encontramos otra forma de hacerlo  )
                            print("4 Laboratorio II")   
                            print("5 Ingles I")
                            print("6 Ingles II")
                            sub_opcion2 = int(input("Seleccione un curso: "))
                            if sub_opcion2 == 1:
                                if 'Programacion I' in C.cursos_disponibles[0]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[0])
                                elif 'Programacion I' in C.cursos_disponibles[1]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[1])
                                elif 'Programacion I' in C.cursos_disponibles[2]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[2])
                                elif 'Programacion I' in C.cursos_disponibles[3]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[3])
                                elif 'Programacion I' in C.cursos_disponibles[4]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[4])
                                elif 'Programacion I' in C.cursos_disponibles[5]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[5])
                            elif sub_opcion2 == 2:
                                if 'Programacion II' in C.cursos_disponibles[0]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[0])
                                elif 'Programacion II' in C.cursos_disponibles[1]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[1])
                                elif 'Programacion II' in C.cursos_disponibles[2]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[2])
                                elif 'Programacion II' in C.cursos_disponibles[3]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[3])
                                elif 'Programacion II' in C.cursos_disponibles[4]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[4])
                                elif 'Programacion II' in C.cursos_disponibles[5]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[5])

                            elif sub_opcion2 == 3:
                                if 'Laboratorio I' in C.cursos_disponibles[0]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[0])
                                elif 'Laboratorio I' in C.cursos_disponibles[1]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[1])
                                elif 'Laboratorio I' in C.cursos_disponibles[2]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[2])
                                elif 'Laboratorio I' in C.cursos_disponibles[3]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[3])
                                elif 'Laboratorio I' in C.cursos_disponibles[4]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[4])
                                elif 'Laboratorio I' in C.cursos_disponibles[5]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[5])

                            elif sub_opcion2 == 4:
                                if 'Laboratorio II' in C.cursos_disponibles[0]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[0])
                                elif 'Laboratorio II' in C.cursos_disponibles[1]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[1])
                                elif 'Laboratorio II' in C.cursos_disponibles[2]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[2])
                                elif 'Laboratorio II' in C.cursos_disponibles[3]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[3])
                                elif 'Laboratorio II' in C.cursos_disponibles[4]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[4])
                                elif 'Laboratorio I' in C.cursos_disponibles[5]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[5])

                            elif sub_opcion2 == 5:
                                if 'Ingles I' in C.cursos_disponibles[0]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[0])
                                elif 'Ingles I' in C.cursos_disponibles[1]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[1])
                                elif 'Ingles I' in C.cursos_disponibles[2]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[2])
                                elif 'Ingles I' in C.cursos_disponibles[3]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[3])
                                elif 'Ingles I' in C.cursos_disponibles[4]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[4])
                                elif 'Ingles I' in C.cursos_disponibles[5]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[5])

                            elif sub_opcion2 == 6:
                                if 'Ingles II' in C.cursos_disponibles[0]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[0])
                                elif 'Ingles II' in C.cursos_disponibles[1]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[1])
                                elif 'Ingles II' in C.cursos_disponibles[2]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[2])
                                elif 'Ingles II' in C.cursos_disponibles[3]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[3])
                                elif 'Ingles II' in C.cursos_disponibles[4]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[4])
                                elif 'Ingles II' in C.cursos_disponibles[5]._nombre_Curso:
                                    C.Usuario1.matricular_en_curso(C.cursos_disponibles[5])
                            else:
                                print("\nSeleccione una opcion correcta\n")
                        else:
                            print("\nTodavia no hay ningun curso dado de alta\n")
                    elif sub_opcion == "2":
                        if len(C.cursos_disponibles) > 0:
                            print("1 Programación I")
                            print("2 Programación II")
                            print("3 Laboratorio I")
                            print("4 Laboratorio II")
                            print("5 Ingles I")
                            print("6 Ingles II")
                            sub_opcion2 = int(input("Seleccione un curso: "))
                            if sub_opcion2 == 1:
                                if 'Programacion I' in C.cursos_disponibles[0]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[0])
                                elif 'Programacion I' in C.cursos_disponibles[1]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[1])
                                elif 'Programacion I' in C.cursos_disponibles[2]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[2])
                                elif 'Programacion I' in C.cursos_disponibles[3]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[3])
                                elif 'Programacion I' in C.cursos_disponibles[4]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[4])
                                elif 'Programacion I' in C.cursos_disponibles[5]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[5])
                            elif sub_opcion2 == 2:
                                if 'Programacion II' in C.cursos_disponibles[0]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[0])
                                elif 'Programacion II' in C.cursos_disponibles[1]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[1])
                                elif 'Programacion II' in C.cursos_disponibles[2]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[2])
                                elif 'Programacion II' in C.cursos_disponibles[3]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[3])
                                elif 'Programacion II' in C.cursos_disponibles[4]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[4])
                                elif 'Programacion II' in C.cursos_disponibles[5]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[5])

                            elif sub_opcion2 == 3:
                                if 'Laboratorio I' in C.cursos_disponibles[0]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[0])
                                elif 'Laboratorio I' in C.cursos_disponibles[1]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[1])
                                elif 'Laboratorio I' in C.cursos_disponibles[2]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[2])
                                elif 'Laboratorio I' in C.cursos_disponibles[3]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[3])
                                elif 'Laboratorio I' in C.cursos_disponibles[4]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[4])
                                elif 'Laboratorio I' in C.cursos_disponibles[5]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[5])

                            elif sub_opcion2 == 4:
                                if 'Laboratorio II' in C.cursos_disponibles[0]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[0])
                                elif 'Laboratorio II' in C.cursos_disponibles[1]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[1])
                                elif 'Laboratorio II' in C.cursos_disponibles[2]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[2])
                                elif 'Laboratorio II' in C.cursos_disponibles[3]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[3])
                                elif 'Laboratorio II' in C.cursos_disponibles[4]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[4])
                                elif 'Laboratorio I' in C.cursos_disponibles[5]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[5])

                            elif sub_opcion2 == 5:
                                if 'Ingles I' in C.cursos_disponibles[0]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[0])
                                elif 'Ingles I' in C.cursos_disponibles[1]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[1])
                                elif 'Ingles I' in C.cursos_disponibles[2]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[2])
                                elif 'Ingles I' in C.cursos_disponibles[3]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[3])
                                elif 'Ingles I' in C.cursos_disponibles[4]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[4])
                                elif 'Ingles I' in C.cursos_disponibles[5]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[5])

                            elif sub_opcion2 == 6:
                                if 'Ingles II' in C.cursos_disponibles[0]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[0])
                                elif 'Ingles II' in C.cursos_disponibles[1]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[1])
                                elif 'Ingles II' in C.cursos_disponibles[2]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[2])
                                elif 'Ingles II' in C.cursos_disponibles[3]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[3])
                                elif 'Ingles II' in C.cursos_disponibles[4]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[4])
                                elif 'Ingles II' in C.cursos_disponibles[5]._nombre_Curso:
                                    C.Usuario1.desmatricular_curso(C.cursos_disponibles[5])
                            else:
                                print("\nSeleccione una opcion correcta\n")
                        else:
                            print("\nTodavia no hay ningun curso dado de alta\n")
                    elif sub_opcion == "3":
                        if len(C.cursos_disponibles) > 0:
                            cont = 0
                            for i in C.Usuario1.mis_cursos:
                                cont = cont + 1
                                print(f"{cont} {i}")
                                sub_opcion3 = int(input("Ingrese el numero de la materia para ver los archivos"))
                                if sub_opcion3 == cont:
                                    if len(C.listaarchivos) > 0:
                                        sorted_archivos = sorted(C.listaarchivos, key=lambda archivo: archivo._fecha)
                                        for archivo in sorted_archivos:
                                            print(archivo)
                                    else:
                                        print("No hay autos registrados.")
                        else:
                            print("\nNo hay cursos dados de alta\n")
                    elif sub_opcion == "4":
                        break
                    else:
                        print("\nSeleccione una opcion correcta\n")
            else:
                print("\nEmail no registrado, debe de darse de alta en el alumnado\n")
        elif opcion == "2":
                email_a_validar = str(input("Ingrese su mail: "))              #Validacion del profesor
                contrasenia_a_validar = str(input("ingrese su contraseña: "))
                validacion = C.Profesor.validar_credenciales(
                email_a_validar, contrasenia_a_validar
                )
                if validacion == True:
                    print("\nIngreso exitoso como Profesor\n")
                    while True:
                        print("-----SUB-MENU PROFESOR-----")
                        print("1. Dictar curso")
                        print("2. Ver cursos")
                        print("3. Volver al menú principal")
                        sub_opcion = input("Seleccione una opción: ")

                        if sub_opcion == "1":
                            nombre_curso = input(
                                "Ingrese el nombre del curso a dictar(Ingrese la primer letra en mayuscula): "
                            )
                            if (
                                nombre_curso == "Ingles I"
                                or nombre_curso == "Ingles II"
                                or nombre_curso == "Laboratorio I"
                                or nombre_curso == "Laboratorio II"
                                or nombre_curso == "Programacion I"
                                or nombre_curso == "Programacion II"
                            ):
                                nuevo_curso = C.Curso(nombre_curso)
                                #Carga de archivos
                                archivo1 = nuevo_curso.nuevo_Archivo(f"Unidad1{nombre_curso}", datetime.date(2018, 4, 10), "pdf")
                                archivo2 = nuevo_curso.nuevo_Archivo(f"Unidad2{nombre_curso}", datetime.date(2015, 4, 10), "pdf")
                                C.cursos_disponibles.append(nuevo_curso)
                                C.Usuario2.dictar_curso(nuevo_curso)
                                
                                print(f"Curso dado de alta: {nuevo_curso._nombre_Curso}")
                                print(
                                    f"Codigo:{nuevo_curso._prox_Cod}\nContraseña de matriculación:{nuevo_curso._contrasenia_matriculacion}\n"
                                )
                            else:
                                print(
                                    "Esta materia no se dicta en esta carrera, Fijese las materias en el apartado ver cursos para ver las disponibles. Gracias..."
                                )
                        elif sub_opcion == "2":
                            #ver cursos (Ingresar el numero de la materia para ver archivos)
                            cont = 0
                            for i in C.Usuario2.mis_cursos:
                                cont = cont + 1
                                print(f"{cont} {i}")
                                sub_opcion4 = int(input("ingrese un numero para ver la cantidad de archivos... "))
                                if sub_opcion4 == cont:
                                    print(f"Cantidad de archivos: {len(C.listaarchivos)}\n")  #imprime la cantidad de archivos
                                else:
                                    print("no hay archivos subidos\n")
                        elif sub_opcion == "3":
                            break
                        else:
                            print("\nSeleccione una opcion correcta\n")
                else:
                    print("\nEmail no registrado, debe de darse de alta ingresando el comando admin \n")
                    adim = str(input("\nIngrese el comando: "))   #si pasa la validacion x el false e ingresa como admin se carga como otro profe
                    if adim == "admin":
                        nombre_profe2 = str(input("\nIngrese su nombre: "))
                        apellido_profe2 = str(input("\nIngrese su apellido: "))
                        titulo_profe2 = str(input("\nIngrese su titulo universitario: "))
                        año_egreso_profe2 = str(input("\nIngrese su año de egreso: "))
                        usuario3 = C.Profesor(
                            nombre_profe2 , apellido_profe2 , email_a_validar , contrasenia_a_validar ,  titulo_profe2 ,año_egreso_profe2
                        )
                        print(f"se ha cargado el admin {usuario3}")
        elif opcion == "3":
            lista_ordenada = sorted(C.cursos_de_la_carrera, key=lambda x: x["Materia"])
            for diccionario in lista_ordenada:
                print(diccionario)

        elif opcion == "4":
            print("hasta luego")
            break
menu()

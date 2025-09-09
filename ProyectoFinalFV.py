#Proyecto Final primer cuatrimestre de Técnico en Analisis de Datos.
#Estudiante: Jose Rojas y Julian Rivera.
#Nombre de la aplicación: IronApp.
#Descripción: Aplicación para llevar un registro de los clientes en un gimnasio
#En donde el usuario puede ver toda la información registrada por el entrenador
#por ejemplo: Rutina, Progreso, Registro de entrenamientos, Una base de datos de los ejercicos que se pueden hacer en el gimnasio.

from colorama import init, Fore, Style
init(autoreset=True)
from datetime import datetime


usuarios={#Diccionario que almacena todos los datos de los usuarios
        "jose":{
            "nombre":"jose",
            "contrasenna":"jo",
            "rutina":{
                "dia1":{
                    "Pectoral":["Press horizontal","Press inclinado","Apertura horizontal","Apertura inclinada"],
                    "Biceps":["Curl Scott","Curl polea","Curl mancuerna"]},
                "dia2":{
                    "Espalda":["Pulldown abiero","Pulldown cerrado","Remo cerrado","Remo mancuerna"],
                    "Triceps":["Ext. codo","Push down","Patada mancuerna"]},
                "dia3":{
                    "Hombros":["Elevación frontal","Elevación lateral","Retractores"],
                    "Piernas":["Ext. rodillas","Press pierna","Desplantes","Peso muerto","Sentadillas","Ext. cadera"]}
                    },
            "estado":{
                "entrada": None,
                "salida":None
                    },
            "calendario":{
                "2025-08-10": "dia1",
                "2025-08-11": "dia2",
                },
            "citas_agendadas":[],
            "progreso":{"mes_pasado":{
                "peso": 93.9,
                "porcentaje de grasa":22.3,
                "grasa viseral": 6,
                "musculo total":69.4},
                    "mes_presente":{
                "peso": 90,
                "porcentaje de grasa":20,
                "grasa viseral": 5,
                "musculo total":72}
                        }
        }}
citas = {#Diccionario con subdiccionarios con todas las citas disponibles y agendadas en ele sitema
    1:{"07:00":True,"08:00":True,"09:00":True,"10:00":False,"11:00":True,
        "13:00":False,"14:00":False,"15:00":False,"16:00":False,"17:00":False,},
    2:{"07:00":True,"08:00":True,"09:00":True,"10:00":True,"11:00":True,
        "13:00":True,"14:00":True,"15:00":True,"16:00":True,"17:00":True,},
    3:{"07:00":True,"08:00":True,"09:00":True,"10:00":True,"11:00":True,
        "13:00":True,"14:00":True,"15:00":True,"16:00":True,"17:00":True,},
    4:{"07:00":True,"08:00":True,"09:00":True,"10:00":True,"11:00":True,
        "13:00":True,"14:00":True,"15:00":True,"16:00":True,"17:00":True,},
    5:{"07:00":True,"08:00":False,"09:00":True,"10:00":False,"11:00":True,
        "13:00":False,"14:00":False,"15:00":False,"16:00":False,"17:00":False,},
    6:{"07:00":False,"08:00":False,"09:00":False,"10:00":False,"11:00":True,
        "13:00":False,"14:00":False,"15:00":False,"16:00":False,"17:00":False,},
    7:{"07:00":False,"08:00":False,"09:00":False,"10:00":False,"11:00":False,
        "13:00":False,"14:00":False,"15:00":False,"16:00":False,"17:00":False,}}
dias_semana = {#Diccionario para cambiar los números por los dias por estética
                            1: "Lunes",
                            2: "Martes",
                            3: "Miércoles",
                            4: "Jueves",
                            5: "Viernes",
                            6: "Sábado",
                            7: "Domingo"
                        }

#Menú principal
while True:
    #menú inicial. Muestra 3 opciones: iniciar sesión, registrarse o salir del sistema.
    print(Fore.BLUE+f"Bienvenido a IronApp\n")
    print("╔══════════Menú Principal══════════╗")
    print("║1️⃣ 🔑 Iniciar sesión               ║")
    print("║2️⃣ 📋 Registrarse                  ║")
    print("║3️⃣ ❌ Salir                        ║")
    print("╚══════════════════════════════════╝")
    opcion=input("Elige una opción: ")
    #Se valida si el usuario existe y la contraseña coincide. Si es correcto, se accede al menú interno.
    if opcion=="1":
        usuario_ingresado=input("🧍 Introduce eu nombre de usuario: ").strip().lower()
        contrasena_ingresada=input("🔒 Introduce tu contraseña: ")
        if usuario_ingresado in usuarios and contrasena_ingresada == usuarios[usuario_ingresado]["contrasenna"]:
            #Muestra las acciones que puede realizar el usuario registrado
            print(f"✅ Inicio de sesión exitoso.")
            while  True:
                print (f"¡Bienvenido(a), {usuario_ingresado}!\n")
                print(Fore.BLUE+f"""╔══════════Menú Principal══════════╗
║ 1️⃣  🏋️   Ver rutina                ║
║ 2️⃣  📅  Calendario                ║
║ 3️⃣  ⏲️   Marcar entrada            ║
║ 4️⃣  ⏲️   Marcar salida             ║
║ 5️⃣  🗓️   Agendar cita              ║
║ 6️⃣  🗓️   ver cita                  ║                      
║ 7️⃣  🗓️   Cancelar cita             ║
║ 8️⃣  👀  Ejercicios disponibles    ║
║ 9️⃣  🏆  Ver progreso personal     ║
║ 🔟 ❌  cerrar sesión             ║ 
╚══════════════════════════════════╝""")
                
                try:
                    opc= int(input("Seleccione una opción: "))
                    match opc:
                        #Se valida si la rutina está vacía. Si no lo está, se imprime ordenadamente.
                        case 1:
                            rutina_usuario = usuarios[usuario_ingresado]["rutina"]
                            rutina_vacia = all(
                            all(len(ejercicios) == 0 for ejercicios in dia.values())
                            for dia in rutina_usuario.values()
                            )

                            if rutina_vacia:
                                print("\n⚠️  No tienes rutina asignada. Por favor contacta a tu entrenador.")
                                print("Revisa la sección de ejercicios disponibles.\n")
                            else:
                                print("🏋️ Tu rutina asignada:\n")
                                for dia_nombre, grupos in rutina_usuario.items():
                                    print(f"📅 {dia_nombre.upper()}")
                                    for musculo, ejercicios in grupos.items():
                                        if ejercicios:
                                            print(f"🔹 {musculo}: {', '.join(ejercicios)}")
                                        else:
                                            print(f"🔹 {musculo}: Sin ejercicios asignados")
                                    print("-" * 40)
                            print("")
                        #Se valida si el calendario está vacío. Si no lo está, se imprime ordenadamente.
                        case 2:
                            calendario_usuario = usuarios[usuario_ingresado].get("calendario", {})
                            if calendario_usuario:
                                print("\n📅 Calendario de rutinas registradas:")
                                for fecha, dia in sorted(calendario_usuario.items()):
                                    print(f"- {fecha}: {dia}")
                                print("")
                            else:
                                print("\n⚠️  No tienes registros en el calendario.\n")
                        #Marcar entrada para llevar un registro del entrenamiento
                        case 3:
                            if usuarios[usuario_ingresado]["estado"]["entrada"] is None:
                                rutina_usuario = usuarios[usuario_ingresado]["rutina"]

                                #Verifica que el usuario tengo una rutina ya registrada
                                rutina_vacia = all(
                                all(len(ejercicios) == 0 for ejercicios in dia.values())
                                for dia in rutina_usuario.values()
                                )
                                #Se valida si la rutian está vacia.
                                if rutina_vacia:
                                    print("⚠️ Tu rutina está vacía. Por favor contacta a tu entrenador para crear una")
                                    print("    y revisa nuestra sección de ejercicios disponibles para ejercitarte hoy.\n")
                                else:
                                    #Imprime los dias de rutina.
                                    dias_disponibles = list(rutina_usuario.keys())
                                    print("📆 Días de rutina:")
                                    for i, dia in enumerate(dias_disponibles, 1):
                                        print(f"{i}. {dia}")

                                    try:
                                        #El usuario selecciona el día que va a trabajar hoy.
                                        seleccion = int(input("Seleccione el día de la rutina que vas a trabajar hoy: "))
                                        if 1 <= seleccion <= len(dias_disponibles):
                                            dia_trabajado = dias_disponibles[seleccion - 1]

                                            #Se registra la hora de entrada.
                                            fecha_actual = datetime.now().strftime("%Y-%m-%d")
                                            hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                            usuarios[usuario_ingresado]["estado"]["entrada"] = hora_actual

                                            #Se guarda el día trabajado en el calendario.
                                            usuarios[usuario_ingresado]["calendario"][fecha_actual] = dia_trabajado

                                            print(f"✅ Entrada registrada para {usuarios[usuario_ingresado]['nombre']} a las {hora_actual}.")
                                            print(f"📌 Hoy estás trabajando: {dia_trabajado}\n")

                                            print("\n🏋️ Ejercicios del día:")
                                            for musculo, ejercicios in rutina_usuario[dia_trabajado].items():
                                                print(f"🔹 {musculo}: {', '.join(ejercicios) if ejercicios else 'Sin ejercicios asignados'}")
                                                print("")
                                        else:
                                            print("❌ Opción fuera de rango.\n")
                                    except ValueError:
                                        print("❌ Debes ingresar un número válido.\n")
                            else:
                                print(f"❌ Ya registraste tu entrada hoy a las {usuarios[usuario_ingresado]['estado']['entrada']}.\n")
                            #Solo permite marcar salida si ya marcó entrada y si aún no ha registrado su salida.
                        case 4:
                            if usuarios[usuario_ingresado]["estado"]["entrada"] is None:
                                print("No has marcado entrada")
                                print("registra entrada primero porfavor\n")
                            else:
                                if usuarios[usuario_ingresado]["estado"]["salida"] is None:
                                    usuarios[usuario_ingresado]["estado"]["salida"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    print(f"✅ Salida registrada para {usuarios[usuario_ingresado]['nombre']} a las {usuarios[usuario_ingresado]['estado']['salida']}.\n")
                                else:
                                    print(f"❌ {usuarios[usuario_ingresado]['nombre']} ya ha registrado su salida a las {usuarios[usuario_ingresado]['estado']['salida']}.\n")
                            #Agendar cita para pesaje   
                        case 5:
                            def agendar_cita(dia):
                                #Verifica que haya dia y horas validas para registrar una cita
                                if dia not in citas:
                                    print("Día inválido. Debe ser un número entre 1 y 7.\n")
                                    return
                                print(f"\nHorarios disponibles para {dias_semana[dia]}:")
                                disponibles = [hora for hora, estado in citas[dia].items() if estado]
                                if not disponibles:
                                    print(Fore.RED+"No hay horarios disponibles para este día.\n")
                                    print("")
                                    return
                                for i, hora in enumerate(disponibles, start=1):
                                    print(Fore.GREEN+f"{i}. {hora}")
                                try:
                                    #solicita y guarda la cita en el diccionario del ususario
                                    opcion = int(input("\nSeleccione el número del horario que desea agendar: "))
                                    if 1 <= opcion <= len(disponibles):
                                        hora_seleccionada = disponibles[opcion - 1]
                                        citas[dia][hora_seleccionada] = False  
                                        print(f"\n✅ Cita agendada para el {dias_semana[dia]} a las {hora_seleccionada}.\n")
                                        cita={
                                        "día": dias_semana[dia],
                                        "hora":hora_seleccionada
                                    }
                                        usuarios[usuario_ingresado]["citas_agendadas"].append(cita)
                                    else:
                                        print("Número de opción fuera de rango.\n")
                                    
                                except ValueError:
                                    print("Debe ingresar un número válido.\n")
                            try:
                                #llama a la función agendar_cita
                                print(" ")    
                                print("Ingrese el día que quiere agendar la cita: ")
                                print("1. Lunes")
                                print("2. Martes")
                                print("3. Miércoles")
                                print("4. Jueves")
                                print("5. Viernes")
                                print("6. Sábado")
                                print("7. Domingo")
                                dia_usuario = int(input("Ingrese un número de día: "))
                                agendar_cita(dia_usuario)
                            except ValueError:
                                print("Debe ingresar un número.\n")
                            #Muestra las citas agendadas ordenadamente
                        case 6:
                            if usuarios[usuario_ingresado]["citas_agendadas"]:
                                print("\n📋 Citas agendadas:")
                                for c in usuarios[usuario_ingresado]["citas_agendadas"]:
                                    print(f"- {c['día']} a las {c['hora']}")
                            else:
                                print("no tiene citas agendadas \n")
                            print("")
                            #muestra las citas
                        case 7:
                            print("Estas son las citas agendadas para esta semana.\n")
                            if usuarios[usuario_ingresado]["citas_agendadas"]:
                                print("\n📋 Citas agendadas:")
                                for i, cita in enumerate(usuarios[usuario_ingresado]["citas_agendadas"], 1):
                                    print(f"{i}. {cita['día']} a las {cita['hora']}")
                                print("")
                                #valida la cita y cambia la entrada en la libreria de citas
                                try:
                                    opcion_cancelar = int(input("Seleccione el número de la cita que desea cancelar: "))
                                    if 1 <= opcion_cancelar <= len(usuarios[usuario_ingresado]["citas_agendadas"]):
                                        cita_cancelada = usuarios[usuario_ingresado]["citas_agendadas"].pop(opcion_cancelar - 1)

                    
                                        dia_num = None
                                        for i, v in dias_semana.items():
                                            if v == cita_cancelada['día']:
                                                dia_num = i
                                                break

                                        if dia_num is not None:
                                            citas[dia_num][cita_cancelada['hora']] = True
                                            print(f"✅ Cita cancelada: {cita_cancelada['día']} a las {cita_cancelada['hora']}\n")
                                        else:
                                            print("❌ Error: no se pudo encontrar el día en el calendario.\n")
                                    else:
                                        print("❌ Opción fuera de rango.\n")
                                except ValueError:
                                    print("❌ Debe ingresar un número válido.\n")
                            else:
                                print("❌ No tienes citas agendadas para cancelar.\n")
                            #Mestra todos los ejercicios que se pueden hacer.
                        case 8:
                            grupos = {
                                "1": ("Pectoral", ["Press horizontal", "Press vertical", "Press declinado", "Apertura horizontal","Apertura inclinada","Apertura declinada","Poleas","Pull over"]),
                                "2": ("Espalda", ["Pulldown Abierto", "Pulldo cerrado", "Remo cerrado", "Remo mancuerna","Pullover","Cross over","Remo con barra","Dominadas"]),
                                "3": ("Bíceps", ["Curl Scott", "Curl polea", "Curl mancuerna","Curl martillo","Curl barra"]),
                                "4": ("Tríceps", ["Extensión codo", "Pushdown", "Press francés","Fondos","Push down inclinado","Patada mancuerna"]),
                                "5": ("Hombros", ["Press militar", "Elevaciones laterales", "Elevaciones frontales", "retraciones","Press Arnold",""]),
                                "6": ("Piernas", ["Est. rodilla", "Flex. rodilla", "Press pierna", "Sentadillas","Desplantes","Ext. cadera","Flex. cadera","Peso muerto","Elevaciones de talones"]),
                                "7": ("Core", ["Bola sentado", "Recto abdomen", "Oblicuos","AB coaster","90 grados","Paseo de granjero","El mesero","Tabla"])
                            }
                            #Ordena la biblioteca 
                            print(Fore.CYAN + "\nSeleccione el grupo muscular que desea trabajar:")
                            for clave, (nombre, _) in grupos.items():
                                print(f"{clave}. {nombre}")
                            #Se solicita el grupo muscular y se llama.
                            seleccion = input("Ingrese el número del grupo muscular: ").strip()
                            if seleccion in grupos:
                                nombre, ejercicios = grupos[seleccion]
                                print(Fore.GREEN + f"\nEjercicios para {nombre}:")
                                for i, ejercicio in enumerate(ejercicios, 1):
                                    print(f"{i}. {ejercicio}\n")
                            else:
                                print(Fore.RED + "❌ Selección no válida.\n")
                            #Se llama y valida la sección de la biblioteca llamada "porgreso"
                        case 9:
                            progreso_usuario = usuarios[usuario_ingresado]["progreso"]
                            #Se valida que "Progreso" tenga registros aparte de solo 0.
                            sin_progreso = all(
                            all(valor == 0 for valor in datos.values())
                            for datos in progreso_usuario.values()
                                )
                            #Se imprime el progreso del mes pasado y presente.
                            if sin_progreso:
                                print("⚠️ No tienes progreso registrado aún.")
                                print("Tu entrenador pronto registrará tu progreso.\n")
                            else:
                                print("📊 Progreso físico:")
                                for periodo, datos in usuarios[usuario_ingresado]["progreso"].items():
                                    print(f"\n{periodo.upper()}:")
                                    for k, v in datos.items():
                                        print(f"  {k.capitalize()}: {v}")
                                        print("")
                            #Se sale del sistema cerrando el bucle.
                        case 10:
                            print("Cerrando sesión... ¡¡Hasta pronto 🚀 🚀 !!\n")
                            break
                except ValueError:
                    print("❌ Selección no válida. Intentelo de nuevo\n")
        else:
            print("❌ Contraseña o Usuario incorrecto. Intentelo de nuevo.\n")
        #Registra nuevo usuario.
    elif opcion=="2":
        nuevo_usuario=input("🧍 Ingrese el nombre de ususario: ").strip().lower()
        #Valida que el usuario se diferente a uno ya registrado.
        if nuevo_usuario in usuarios:
            print("⚠️ ⚠️ El usuario ya existe, intenta con otro nombre ⚠️ ⚠️\n")
        else:
            nueva_contrasenna = input("🔑 Elige un contraseña: ")
            #Guarda el nuevo usuario con todas las sub bibliotecas necesarias para el registro.
            usuarios[nuevo_usuario] = {
    "nombre": nuevo_usuario,
    "contrasenna": nueva_contrasenna,
    "rutina": {
        "dia1": {
            "Pectoral": [],
            "Biceps": []
        },
        "dia2": {
            "Espalda": [],
            "Triceps": []
        },
        "dia3": {
            "Hombros": [],
            "Piernas": []
        }
    },
    "estado": {
        "entrada": None,
        "salida": None
    },
    "calendario": {},
    "citas_agendadas": [],
    "progreso": {
        "mes_pasado": {
            "peso": 0,
            "porcentaje de grasa": 0,
            "grasa viseral": 0,
            "musculo total": 0
        },
        "mes_presente": {
            "peso": 0,
            "porcentaje de grasa": 0,
            "grasa viseral": 0,
            "musculo total": 0
        }
    }
}
            print("✅ Registro exitoso.")
            print(f"¡Bienvenido(a),{nuevo_usuario}!\n")
    elif opcion=="3":
        #Sale del sistema cerrando el bucle.
        print("Saliendo del sistema... ¡¡Hasta pronto 🚀 🚀 !!\n")
        break
    #Valida que la entrada no sea 1, 2, o 3.
    if opcion not in ["1", "2", "3"]:
        print("❌ Opción inválida. Intenta nuevamente.\n")
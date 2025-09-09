#Jose Rojas Rodriguez
#Fecha: 08/01/25
#Hora inicio:11:31
#Hora fin: 12:40
#Desarrollá un programa en Python que permita registrar el consumo mensual de agua de una 
#vivienda, calcular el promedio de consumo anual y evaluar si este se encuentra dentro de un 
#rango adecuado según criterios ambientales establecidos.
from colorama import init, Fore, Style
init(autoreset=True)

while True:#Ciclo para que el programa reinicie si hay un error fatal
    print(Fore.GREEN+f"--------------------------------------------------------------------------")#Bienvenida
    print(Fore.BLUE+f"Bienvenido al Registro y Evaluación de consumo de Agua Potable del AyA.   ")#Bienvenida
    print("                                                                                  ")#Bienvenida
    print(Fore.LIGHTBLUE_EX+f"""Para calcular y evaluar debe ingresar el consumo de mensual de agua   
    de los ultimos 12 meses registrados en sus recido de agua.""")#Bienvenida
    print(Fore.GREEN+f"--------------------------------------------------------------------------")#Bienvenida
    
    try:# excepción por si el sistema tiene un error crítico
        consumo_meses=[]#Lista donde se guarde los datos ingresados por el ususario final
        for i in range(1,13):#bucle for para que se repita por los doce meses 
            while True:#bucle que repita si hay un error ya sea un número negativo o letras
                try:#excepción que verifica que la entrada se un número
                    mes=float(input(f"Ingrese el consumo de agua para el mes {i} (en m³) 📋:"))#pide el monto de los meses
                    print("")
                    if mes>=0:#condicional para verificar que el número se amoyor a 0
                        consumo_meses.append(mes)#Agrega el valor a la lista llamada consumo_meses
                        break #rompe el while para que siga al sigiente mes
                    else:
                        print("Error!! por favor ingrese solo números mayor a 0")#imprime en la pantalla por si se digita un numero negativo
                except ValueError:#excepción por si se genera un error de valor
                    print("")
                    print(Fore.LIGHTRED_EX+f"Error al igresar los datos ")
                    print("Por favor, debe ingresar solo numeros")
                    print(" ")       
        con_total= sum(consumo_meses)#suma del consumo total y lo garda en una variable 
        promedio= con_total/12#calcula y guarda el promedio en una variable
        print(Fore.MAGENTA+f"Consumo total del año: {con_total:.2f} m³")#imprime el consumo total
        print(Fore.MAGENTA+f"Promedio mensual: {promedio:.2f} m³")#imprime el promedio de los doce meses
        print("")
        if promedio<15 and promedio>0:#condcional para verifica cual es la clasificación del consumo bajo menor a 15
            print(Fore.BLUE+f"Clasificación: Consumo Bajo")#
            print(Fore.BLUE+f"Excelente trabajo")
        elif promedio>15 and promedio<30:#condcional para verifica cual es la clasificación del consumo  moderado mayor a 15 y menor a 30
            print(Fore.LIGHTYELLOW_EX+f"Clasificación: Consumo Moderado")
            print(Fore.LIGHTYELLOW_EX+f"Buen trabajo")
        else:#condcional para verifica cual es la clasificación del consumo excesivo mayor a 30
            print(Fore.LIGHTRED_EX+f"Clasificación: Consumo Excesivo")
            print(Fore.LIGHTRED_EX+"Por favor trate de usar menos agua")
            print(Fore.GREEN+"El planeta se lo agradecera 🌎🌎")
        print("")
        print("Gracias por usar el sistema de evaluación del AyA 🚀 🚀")
        break
    except Exception :# Exceción por si hay un error fatal
        print("❌❌ Error!! ❌❌")
        print("Contactese con TI")
        print(" ")
        consumo_meses.clear()  

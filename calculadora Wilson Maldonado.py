import numpy as np

def mmenu():
    print("\n ¬| Calculadora  |¬")
    print("Hecha por Wilson Maldonado")
    print("1. Suma de arrays")
    print("2. Resta de arrays")
    print("3. Multiplicación (elemento por elemento)")
    print("4. División (elemento por elemento)")
    print("5. Salir")

def operacion_basica(operacion):
    print(f"\n** {operacion} de Arrays **")
    try:
        # Ingreso de arrays
        a = np.array(eval(input("Ingresa el primer array (ej. [1, 2, 3]): ")))
        b = np.array(eval(input("Ingresa el segundo array (ej. [4, 5, 6]): ")))
        
        # Realizar operación
        if operacion == "Suma":
            resultado = a + b
        elif operacion == "Resta":
            resultado = a - b
        elif operacion == "Multiplicacion":
            resultado = a * b
        elif operacion == "División":
            resultado = np.divide(a, b)  
            
        print(f"Resultado: {resultado}")
    except Exception as e:
        print(f"Error: {e}. Verifica los datos ingresados.")

# Bucle principal
while True:
    menu()
    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        operacion_basica("Suma")
    elif opcion == "2":
        operacion_basica("Resta")
    elif opcion == "3":
        operacion_basica("Multiplicacion")
    elif opcion == "4":
        operacion_basica("División")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")
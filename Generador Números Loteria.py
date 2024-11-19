import random
import keyboard

print("""
------------------------------------
Generador de Números Para la Lotería
------------------------------------
""")

def generar_numeros():
    a = random.randint(1, 49)
    b = random.randint(1, 49)
    c = random.randint(1, 49)
    d = random.randint(1, 49)
    e = random.randint(1, 49)
    f = random.randint(1, 49)
    return f"{a} {b} {c} {d} {e} {f}"

def main():
    print("Presione ENTER para generar números de la lotería.")
    keyboard.wait("enter")
    print(f"Tu número es: {generar_numeros()}")

    print("Presione ESC para salir.")
    while True:
        if keyboard.is_pressed("esc"):
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()

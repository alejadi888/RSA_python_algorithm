def gcd(a, b):           #algoritmo de Euclides
    while b != 0:
        a, b = b, a % b
    return a

def euclides_extendido(a, b):   #algoritmo de Euclides Extendido (calcula los coeficientes de Bézout)
    if a == 0:                  # a*x + b*y = gcd(a, b)
        return b, 0, 1
    gcd_val, x1, y1 = euclides_extendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def inverso_modular(e, phi):    # calcula d tal que (d * e) % phi == 1 usando Euclides Extendido
    gcd_val, x, _ = euclides_extendido(e, phi)
    if gcd_val != 1:
        raise ValueError("El inverso modular no existe (e y phi no son coprimos).")
    return x % phi

def exponenciacion_modular(base, exponente, modulo):  #algoritmo de Cuadrados y Multiplicaciones 
    resultado = 1
    base = base % modulo
    while exponente > 0:
        if exponente % 2 == 1:
            resultado = (resultado * base) % modulo
        exponente = exponente // 2
        base = (base * base) % modulo
    return resultado

def es_primo(n):       #prueba si son primos
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print("--- RSA CRYPTOGRAPHY ---")

#primos p y q (iniciales)

p = int(input("\nIngrese el número primo p: "))
while not es_primo(p):
    p = int(input("No es primo. Ingrese p nuevamente: "))

q = int(input("Ingrese el número primo q (diferente de p): "))
while not es_primo(q) or q == p:
    q = int(input("No es primo o es igual a p. Ingrese q nuevamente: "))

#claves de cifrado
n = p * q
phi = (p - 1) * (q - 1)   #cantidad de números que son coprimos con n

print(f"\n1. Módulo n = p * q = {n}")
print(f"2. Euler Phi φ(n) = (p-1)*(q-1) = {phi}")

# Exponente público e
e = 65537
if e >= phi or gcd(e, phi) != 1:
    e = 3
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 2

# Exponente privado d
d = inverso_modular(e, phi)

print(f"3. Exponente público e = {e}")
print(f"4. Exponente privado d (mediante Euclides Extendido) = {d}")
print(f"\nClave Pública: (e={e}, n={n})")
print(f"Clave Privada: (d={d}, n={n})")

c_numero = None
c_texto = None

while True:
    print("\n-------------------------------------------")
    print("1. Cifrar / Descifrar Número (Demostración directa)")
    print("2. Cifrar / Descifrar Texto (Convertido carácter a carácter)")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        m = int(input(f"\nIngrese un número m a cifrar (0 <= m < {n}): "))
        while m < 0 or m >= n:
            m = int(input(f"Error. m debe ser menor que n ({n}): "))

        # Cifrado
        c = exponenciacion_modular(m, e, n)
        # Descifrado
        m_desc = exponenciacion_modular(c, d, n)

        print(f"-> Cifrado (c = m^e mod n): {c}")
        print(f"-> Descifrado (m = c^d mod n): {m_desc}")

    elif opcion == "2":
        texto = input("\nIngrese el texto a cifrar: ")
        
        # convertir cada carácter a su código ASCII y verificar que sea menor que n
        max_ascii = max(ord(char) for char in texto) if texto else 0
        if max_ascii >= n:
            print(f"\n[ERROR MATEMÁTICO] El código ASCII del carácter más grande es {max_ascii}.")
            print(f"Para cifrar este texto se requiere que n > {max_ascii}, pero n es {n}.")
            print("Por favor, utilice primos p y q más grandes.")
            continue
        
        # Lista antes del cifrado 
        lista_m = [ord(char) for char in texto]
        print(f"\nMensaje numérico plano m = {lista_m}")

        # Cifrado
        c_texto = [exponenciacion_modular(ord(char), e, n) for char in texto]
        print(f"\n-> Texto Cifrado: {c_texto}")

        # Descifrado
        texto_descifrado = "".join([chr(exponenciacion_modular(c_i, d, n)) for c_i in c_texto])
        print(f"-> Texto Descifrado: '{texto_descifrado}'")

    elif opcion == "3":
        print("Finalizando programa...")
        break
    else:
        print("Opción no válida.")
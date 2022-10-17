# Objetivo: 
# 
# Definir el cuerpo de la función "clasificar_edad" 
# que se encuentra a continuación
# para que reciba como argumento la edad
# Y con base en esa edad 
# nos regrese una cadena de texto
# con la clasificación correcta de la persona,
# siguiendo las siguientes pautas:
# 
# De 0 años es un Feto
# Entre 1 y 3 años es un Bebe
# Entre 4 y 12 años es un Niño
# Entre 13 y 17 años es un Adolescente
# Entre 18 y 49 años es un Adulto
# Entre 50 y 120 años es un Anciano
# Mayor a 120 años es una Monumento
#
# Nota: Asegurarte de revisar que:
# - La edad sea un entero (Esperamos retro: "La edad debe ser un entero.").
# - No se permita ingresar edades negatgivas (Esperamos retro: "La edad debe ser mayor a 0.")

def clasificar_edad(edad) -> str:
    # TODO: Definir el cuerpo de la función
    # Hint: Para regresar un valor
    # se necesita usar la palabra "return"
    # Ejemplo:
    # return 'Hola mundo'
    # Regresa una cadena de texto
    # Con el valor 'Hola mundo'
    pass

def validar_funcion():
    test_cases = [
        (0, 'Feto'),
        (1, 'Bebe'),
        (4, 'Niño'),
        (13, 'Adolescente'),
        (17, 'Adolescente'),
        (18, 'Adulto'),
        (60, 'Anciano'),
        (70, 'Anciano'),
        (200, 'Monumento'),
        ('hola', 'La edad debe ser un entero.'),
        (-1, 'La edad debe ser mayor a 0.'),
    ]
    
    for test_case in test_cases:
        (age, expected) = test_case
        result = clasificar_edad(age)
        assert result == expected, \
            f"Oops, para la edad {age} esperabamos el resultado {expected}, pero obtuvimos: {result}. Intentemos de nuevo :D"

if __name__ == '__main__':
    validar_funcion()
    print('Todo es correcto, ¡buen trabajo! :D')
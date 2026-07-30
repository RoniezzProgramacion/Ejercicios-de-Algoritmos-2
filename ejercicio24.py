
# =========================================
# 24. Condicionales anidados
# =========================================

# Descripción:
# Un condicional anidado consiste en colocar un if
# dentro de otro if para evaluar varias condiciones.

edad = 20
tiene_documento = True

if edad >= 18:
    if tiene_documento:
        print("Puede ingresar.")
    else:
        print("Debe presentar el documento.")
else:
    print("No cumple la edad requerida.")
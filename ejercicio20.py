# =========================================
# 20. filter()
# =========================================

# Descripción:
# La función filter() selecciona únicamente los
# elementos que cumplen una condición determinada.

def es_mayor(numero):
    return numero > 10

numeros = [5, 12, 18, 7, 20]

print(list(filter(es_mayor, numeros)))
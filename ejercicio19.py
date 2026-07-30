# =========================================
# 19. map()
# =========================================

# Descripción:
# La función map() aplica una función a todos los
# elementos de un iterable y devuelve los resultados.

def triplicar(numero):
    return numero * 3

valores = [1, 2, 3, 4]

print(list(map(triplicar, valores)))
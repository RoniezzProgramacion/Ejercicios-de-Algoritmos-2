# =========================================
# 17. enumerate()
# =========================================

# Descripción:
# La función enumerate() permite recorrer un iterable
# mostrando tanto la posición de cada elemento como
# su valor. Es muy útil para trabajar con listas.

frutas = ["Manzana", "Pera", "Uva"]

for indice, fruta in enumerate(frutas):
    print(indice, fruta)

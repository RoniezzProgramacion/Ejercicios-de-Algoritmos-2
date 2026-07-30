# =========================================
# 18. zip()
# =========================================

# Descripción:
# La función zip() une elementos de dos o más listas
# formando pares. Es útil cuando se desea recorrer
# varias colecciones al mismo tiempo.

nombres = ["Ana", "Luis", "Pedro"]
edades = [18, 20, 22]

print(list(zip(nombres, edades)))
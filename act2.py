# Pedimos los datos

print("¿Cuanto tiene que pagar? ...")
pago = float(input(""))

# Preguntamos en cuantas cuotas quiere pagar

print("¿En cuantas cuotas quiere pagar? ...")
cuotas = int(input(""))

# Calculamos las cuotas

if (cuotas >=6):
    total = pago + pago * 0.05
"""
Calcula el IMC (peso / (est ** 2))

Entradas:
El peso en kg
La estatura en metros

Salidas:
- Si peso menor a 18.5 => Bajo Peso
- Si peso mayor o igual a 18.5 y menor a 25 => "Normal"
- Si peso mayor o igual a 25 y menor a 30 => Sobrepeso
- Si peso mayor o igual a 30 => Obesidad

Ejemplo de ejecución:
>>> 1
>>> 2

IMC: 18.7 => Obesidad
"""
p=int(input("Peso en Kg:"))
a=float(input("Altura en m:"))
      
imc=(p/(a**2))
if imc<=18.5:
    print(f"Bajo peso, {imc}")
elif 18.5<=imc<=25:
    print(f"Normal, {imc}")
elif 25<=imc<=30:
    print(f"Sobrepeso, {imc}")
elif imc>=30:
    print(f"Obesidad, {imc}")

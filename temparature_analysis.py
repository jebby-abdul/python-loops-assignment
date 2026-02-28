temps_celsius = [ 22, 25, 28, 24, 26 ]
fahrenheit_temps = []
for temp in temps_celsius:
    fahrenheit = (temp * 9/5) + 32
    fahrenheit_temps.append(fahrenheit)
average = sum(fahrenheit_temps) / len(fahrenheit_temps)
print("Fahrenheit temparature:", fahrenheit_temps)
print("Average temparature in Fahrenheit:", average)

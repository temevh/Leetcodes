def convertTemperature(celsius):
    ans = []
    kelvin = celsius + 273.15
    ans.append(kelvin)
    fahr = celsius * 1.8 + 32
    ans.append(fahr)
    return ans


print(convertTemperature(36.50))

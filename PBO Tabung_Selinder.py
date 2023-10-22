print("aplikasi menghitung luas dan volume tabung selinder")
print("===================================================")

# atur nilai variabel
r = 2
T = 5
phi = 3.12

# rumus luas selimut tabung selinder
luas_selimut = ((2 * phi) * r * T)
#rumus luas permukaan tabung selinder
luas_permukaan = ((2 * phi * r * T) + (2 * phi * r ** 2))

#rumus volume tabung selinder: luas alas * tinggi
volume = (phi * r ** 2) * T

# hasil perhitungan luas dan volume
print("hasil luas dan volume tabung selinder: ")
print("=======================================")

print(f"maka hasil luas selimut tabung selinder: {luas_selimut}")
print(f"maka hasil luas permukaan tabung selinder: {luas_permukaan}")
print(f"maka hasil volumer tabung selinder: {volume}")
print("aplikasi menghitung luas dan volume kerucut")
print("===========================================")

# atur nilai variabel
phi = 3.14
r = 2
s = 4
T = 2

# rumus luas dan volume kerucut

# rumus luas selimut kerucut
luas_selimut = (phi * r * s)
# rumus luas permukaan
luas_permukaan = (phi * r * s) + (phi * r ** 2)

# rumus volume kerucut
volume = (1/3) * phi * r ** 2 * T

# hasil luas dan volume kerucut
print("hasil luas dan volume kerucut")
print("=============================")

# hasil luas kerucut
print(f"maka hasil luas selimut kerucut: {luas_selimut}")
print(f"maka hasil luas permukaan kerucut: {luas_permukaan}")
print(f"maka hasil volume kerucut: {volume}")
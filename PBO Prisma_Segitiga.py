# aplikasi menghitung luas dan volume prisma segitiga
print("Aplikasi menghitung luas dan volume prisma segitiga")
print("===================================================")

# Atur nilai variabel
s1 = int(input("masukkan nilai sisi 1: "))
s2 = int(input("masukkan nilai sisi 2: "))
s3 = int(input("masukkan nilai sisi 3: "))
T = int(input("masukkan nilai tinggi prisma: "))
a = int(input("masukkan nilai alas: "))
t = int(input("masukkan nilai tinggi: "))
at = int(input("masukkan nilai luas segitiga: "))

# rumus luas limas segitiga

# rumus: ls = keliling segitiga * tinggi prisma
ls = (s1 + s2 + s3) * T
# rumus: lp = keliling segitiga * T prisma + 2 luas segitiga
lp = (s1 + s2 + s3) * T + at

# rumus volume limas segitiga
volume = ((1/2) * a * t * T)

print("===================================================")
print("hasil output: ")

# output
print(f"maka hasil luas adalah: {ls}")
print(f"maka hasil luas adalah: {lp}")
print(f"maka hasil volume adalah: {volume}")
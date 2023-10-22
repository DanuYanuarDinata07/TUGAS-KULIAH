print("Aplikasi menghitung luas dan volume limas Segitiga")
print("====================================================")

# atur nilai variabel
ls1 = int(input("masukkan nilai luas sisi 1: "))
ls2 = int(input("masukkan nilai luas sisi 2: "))
ls3 = int(input("masukkan nilai luas sisi 3: "))
ls4 = int(input("masukkan nilai luas sisi 4: "))

a = int(input("masukkan nilai alas: "))
t = int(input("masukkan nilai luas alas: "))
T = int(input("masukkan nilai tinggi: "))

# rumus luas dan volume limas segitiga
luas = (ls1 + ls2 + ls3 + ls4)
volume = ((1/6) * a * t * T)

print("=======================================================")

# output
print(f"maka hail luas adalah: {luas}")
print(f"maka hasil volume adalah: {volume}")
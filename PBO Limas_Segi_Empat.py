print("Aplikasi menghitung luas dan volume limas segiempat")
print("====================================================")

# atur nilai variabel
ls1 = int(input("masukkan nilai luas sisi 1: "))
ls2 = int(input("masukkan nilai luas sisi 2: "))
ls3 = int(input("masukkan nilai luas sisi 3: "))
ls4 = int(input("masukkan nilai luas sisi 4: "))
ls5 = int(input("masukkan nilai luas sisi 5: "))

luas_alas = int(input("masukkan nilai luas_alas: "))
tinggi = int(input("masukkan nilai tinggi: "))

# rumus luas dan volume limas segi empat
luas = (ls1 + ls2 + ls3 + ls4 + ls5)
volume = ((luas_alas * tinggi)/3)

print("=======================================================")

# output
print(f"maka hail luas adalah: {luas}")
print(f"maka hasil volume adalah: {volume}")
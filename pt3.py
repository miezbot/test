berat_badan_mg = float(input("Masukkan berat badan (mg): "))
tinggi_badan_km = float(input("Masukkan tinggi badan (km): "))

# kg ke mg
berat_badan_kg = berat_badan_mg / 1000000

# km ke m
tinggi_badan_m = tinggi_badan_km * 1000

bmi = berat_badan_kg / (tinggi_badan_m ** 2)


if bmi < 18.5:
    print("Kategori BMI: Kurang")
    print("Hitungan Total :", bmi) 
elif bmi < 24.9:
    print("Kategori BMI: Normal") 
    print("Hitungan Total :", bmi) 
elif bmi < 29.9:
    print("Kategori BMI: Berlebihan") 
    print("Hitungan Total :", bmi) 
else:
    print("Kategori BMI: Obesitas") 
    print("Hitungan Total :", bmi) 


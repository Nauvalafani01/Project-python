# membuat kalkulator sederhana dengan python 
# serta logika dasar aritmatika 

# masukkan input angka 

# Banner calculator
print("""
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
""")
# list calculator
print("""
                =====Selamat datang di kalkulator sederhana=====

      +==================================================================+
      |   1. Penjumlahan (+)              4. Pembagian (/)               |   
      |                                                                  |
      |   2. Pengurangan (-)              5. Perpangkatan (**)           | 
      |                                                                  |     
      |   3. Perkalian (*)                6. Modulus (%)                 |    
      +==================================================================+
""")

print("             =============Operator :============")
while True: # pengulangan kalkulator jika benar (true)
    operator = input("Masukkan operator (1,2.,6) : ") # masukkan operator
    angka1 = float(input("Masukkan Angka1 : ")) # masukkan angka 1
    angka2 = float(input("Masukkan Angka2 : ")) # masukkan angka 2

# kondisi dan keputusan
    if operator == "1": 
        result = angka1 + angka2
        print(round(result, 3))
    elif operator == "2":
        result = angka1 - angka2
        print(round(result, 3))
    elif operator == "3":
        result = angka1 * angka2
        print(round(result, 3))
    elif operator == "4":
        result = angka1 / angka2
        print(round(result, 3))
    elif operator == "5":
        result = angka1 ** angka2
        print(round(result, 3))
    elif operator == "6":
        result = angka1 % angka2
        print(round(result, 3))
    else:
        print(f"Maaf,{operator} tidak ada dalam operator")
        
# ulangi program | lanjut atau berhenti       
    print("Ingin mengulangi kalkulator?")
    
    berhentiN = input("Apakah ingin di lanjutkan (y/n): ")  
    if berhentiN == "n":
        break

print("Terima kasih telah menggunakan kalkulator sederhana ini!")
    


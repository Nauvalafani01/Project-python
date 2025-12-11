## List Software Favorit
List1 = ["Adobe Photoshop", "Adobe Premiere Pro", "Davinci Resolve", "Blender", "Cinema 4D","Keluar"] #ini list

## Daftar Software
def Daftar_Software():
    print("=== Daftar SoftWare ===")
    for i, item in enumerate(List1, start=1):
        print(f"{i}. {item}")

## Input Software And Condition:
def main():
    while True:
        Daftar_Software()
        try:
            pilihan = int(input("Pilih Software Favorit: "))
            if pilihan == 6:
                print("Keluar dari program....")
                break
            elif 1 <= pilihan <= len(List1):
                print(f"✔️ Silakan memilih: {List1[pilihan - 1]}")
            else:
                print("❌ Pilihan Tidak Ada.")
        except ValueError:
            print("Masukkan angka :")

main()


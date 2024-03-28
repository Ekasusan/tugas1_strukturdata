#python 3.7.1

def buat_biodata():
    print("===== Program Pembuat Biodata =====")
    nama = input("Masukkan nama Anda: Eka Susanti si20230012")
    semester = input ("masukkan semester anda: semester II")
    umur = input("Masukkan umur Anda: 19")
    alamat = input("Masukkan alamat Anda: Dompu")
    jenis_kelamin = input("Masukkan jenis kelamin Anda: perempuan")
    hobi = input("Masukkan hobi Anda: banyak")

    print("\n===== Biodata Anda =====")
    print("Nama:", nama)
    print("semester:", semester)
    print("Umur:", umur)
    print("Alamat:", alamat)
    print("Jenis Kelamin:", jenis_kelamin)
    print("Hobi:", hobi)

if __name__ == "__main__":
    buat_biodata()
    
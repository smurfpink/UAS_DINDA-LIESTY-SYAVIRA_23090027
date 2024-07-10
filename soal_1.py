students = []

while True:
    print("Masukan NIM:")
    nim = input()

    print("Masukan Nama:")
    nama = input()

    student = {"NIM": nim, "Nama": nama}
    students.append(student)

    print("Ingin tambah lagi? (ya/tidak)")
    response = input().lower()

    if response == "tidak":
        break

print("Data Mahasiswa:")
for student in students:
    print(f"NIM: {student['NIM']}, Nama: {student['Nama']}")

print("Program selesai.")
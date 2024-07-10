students = [
    {"Nama": "Mahasiswa 1", "Algoritma dan Struktur Data 2": 90, "Matematika Numerik": 80},
    {"Nama": "Mahasiswa 2", "Algoritma dan Struktur Data 2": 50, "Matematika Numerik": 60},
    {"Nama": "Mahasiswa 3", "Algoritma dan Struktur Data 2": 65, "Matematika Numerik": 70}
]

rata_algoritma = sum(student["Algoritma dan Struktur Data 2"] for student in students) / len(students)
rata_matematika = sum(student["Matematika Numerik"] for student in students) / len(students)

print("Rata-rata nilai untuk setiap mata kuliah:")
print("Algoritma dan Struktur Data 2:", rata_algoritma)
print("Matematika Numerik:", rata_matematika)

for student in students:
    rata_student = (student["Algoritma dan Struktur Data 2"] + student["Matematika Numerik"]) / 2
    print("\nRata-rata nilai untuk", student["Nama"], ":", rata_student)
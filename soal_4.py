class Buah:
    def __init__(self, nama, warna, rasa):
        self.__nama = nama
        self.__warna = warna
        self.__rasa = rasa

    def setNama(self, nama):
        self.__nama = nama

    def setWarna(self, warna):
        self.__warna = warna

    def setRasa(self, rasa):
        self.__rasa = rasa

    def Information(self):
        return f"Nama: {self.__nama}, Warna: {self.__warna}, Rasa: {self.__rasa}"

class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin, umur):
        super().__init__(nama, warna, rasa)
        self.__vitamin = vitamin
        self.__umur = umur

    def setVitamin(self, vitamin):
        self.__vitamin = vitamin

    def setUmur(self, umur):
        self.__umur = umur

    def Information(self):
        return super().Information() + f", Vitamin: {self.__vitamin}, Umur: {self.__umur}"

mangga_matang = Mangga("Mangga","Kuning","Manis","C","Matang")
mangga_muda = Mangga("Mangga","Hijau","Asam","A","Muda")

print(mangga_matang.Information())

print(mangga_muda.Information())

mangga_matang.setNama("Mangga")
print(mangga_matang.Information())

mangga_muda.setUmur("Sedang")
print(mangga_muda.Information())
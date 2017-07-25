class Teman:
    JUMLAH = 0

    def __init__(self, nama, sex):
        self.nama = nama
        self.sex = sex
        self.alamat = ''
        Teman.JUMLAH = Teman.JUMLAH + 1

    def __str__(self):
        return ('Nama = %s, sex=%s, alamat=%s' % (self.nama, self.sex, self.alamat))

    def berbicara(self):
        print('Hai kamu, nama saya adalah %s. Namu kamu siapa?' % self.nama)


daftar_teman = []
daftar_teman.append(Teman('Prabowo', 'Laki-laki'))
daftar_teman.append(Teman('Joko', 'Laki-laki'))
daftar_teman.append(Teman('Mega', 'Laki-laki'))
gareng = Teman('Gareng', 'Tidak tahu')
gareng.alamat = 'Nirwana Gang Kudus Nomor 666'
gareng.berbicara()
daftar_teman.append(gareng)

print('Jumlah teman dengan fungsi len %d' % len(daftar_teman))
print('Jumlah teman dari variable class JUMLAH %d' % Teman.JUMLAH)
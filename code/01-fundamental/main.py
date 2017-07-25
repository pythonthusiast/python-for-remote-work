message = 'Hello world!'
nama = 'Anda Kaudia'
usia = 5
lingkar_perut = 2

print(message)
print(nama)
print(usia)
print(lingkar_perut)

if usia <= 17:
    print('Belum boleh nonton film 18 tahun ke atas yaks!')
    print('Muda cuy!')
else:
    print('Mayan tua...')

if lingkar_perut < 30:
    print('Sudah bagus!')
elif lingkar_perut < 40:
    print('Susah pakai seat belt ya?')
else:
    print('Bahaya!')

for i in range(2, 3):
    print(message)

while (usia > 0):
    print('Usia saat ini %s' % usia)
    print('Masih hidup!')
    usia = usia - 1

daftar_nama=['saya', 'aku', 'I', 'myself']
print(daftar_nama)
daftar_nama.append('kulo')
daftar_nama.append('abdi')
print(daftar_nama)

for dn in daftar_nama:
    print('Nama lain Anda adalah %s, padahal nama aslimu itu %s lho!' % (dn, nama))

manusia = {}
manusia['nama'] = 'Prabowo'
manusia['sex'] = 'Laki-Laki'
manusia['status'] = 'Menikah'
print(manusia)
manusia['nama'] = 'Prabowo Widagyo'
print(manusia)
manusia['alamat'] = 'Jakarta'
print(manusia)

import json
print(json.dumps(manusia))
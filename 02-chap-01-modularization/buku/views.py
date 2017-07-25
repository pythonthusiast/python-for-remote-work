from models import daftar_buku

def run_view():
    print('Daftar Buku')
    print('---')

    for db in daftar_buku:
        print(db)
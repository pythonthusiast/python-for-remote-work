from models import daftar_teman

def run_view():
    print('Daftar Teman')
    print('---')

    for dn in daftar_teman:
        print(dn)
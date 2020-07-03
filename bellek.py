import os
import glob
import sys


from hashlib import md5
from glob import glob as ls
def getirklasor():
    klasorler=list()

    dizinler=ls("*")
    dizinler.remove("backup")
    for klasor in dizinler:
        if(os.path.isdir(klasor)):
            klasorler.append(klasor)
    return klasorler


def kaydet(version_ismi):

    dosyalar = ls("*.txt")
    klasor = getirklasor()
    for kdosyalar in klasor:

        x = ls(f"{kdosyalar}/*.txt")
        for j in x:
            içtext = j.split('\\')[-1]
            dosyalar.append(j)


    print(dosyalar)
    versiyon_dosyası = open(f'backup/versiyonlar/{version_ismi}', 'w')

    for dosya_ismi in dosyalar:
        içerik = open(dosya_ismi).read()

        md5_hash = md5(içerik.encode('utf-8')).hexdigest()

        open(f'backup/içerikler/{md5_hash}', 'w').write(içerik)

        versiyon_dosyası.write(
            md5_hash + ',' + dosya_ismi + '\n'
        )


def gerial(version_ismi):
    versiyon_içeriği = open(f'backup/versiyonlar/{version_ismi}')

    for satır in versiyon_içeriği:
        _hash, dosya_ismi = satır.strip().split(',')

        içerik = open(f'backup/içerikler/{_hash}').read()

        open(dosya_ismi, 'w').write(içerik)


def durum():
    eskihasler=list()

    dosyalar=ls('*.txt')
    klasor = getirklasor()
    for kdosyalar in klasor:

        x = ls(f"{kdosyalar}/*.txt")
        for j in x:
            içtext = j.split('\\')[-1]
            dosyalar.append(j)

    icerikler=ls('backup/içerikler/*')
    for icerikk in icerikler:
        eskihasler2= icerikk.split('\\')[-1]
        eskihasler.append(eskihasler2)

    for dosya in dosyalar:
        icerik=open(dosya).read()
        md5_hash = md5(icerik.encode('utf-8')).hexdigest()
        parse_md5 = md5_hash.split('\\')[-1]

        if(parse_md5 in eskihasler):
            print(f"{dosya} değişim olmamıştır")
        else:
            print(f"{dosya} değişiklik yapılmıştır ...")



if sys.argv[1] == 'başlat':
    os.mkdir('backup')
    os.mkdir('backup/içerikler')
    os.mkdir('backup/versiyonlar')


elif sys.argv[1] == 'kaydet':
    if len(sys.argv) != 3:
        print('kaydet komutu versiyon ismi gerektirir.')
    else:
        kaydet(version_ismi=sys.argv[2])

elif sys.argv[1] == 'geçmiş':
    versiyon_isimleri = ls("backup/versiyonlar/*")
    for versiyon_isimi in versiyon_isimleri:
        print(versiyon_isimi.split('\\')[-1])

elif sys.argv[1] == 'gerial':
    if len(sys.argv) != 3:
        print('gerial komutu versiyon ismi gerektirir.')
    else:
        gerial(version_ismi=sys.argv[2])

elif sys.argv[1] == 'durum':
    durumlar = ls("backup/versiyonlar/*")
    son_dosya = max(durumlar, key=os.path.getctime)
    print(son_dosya.split('\\')[-1])
    durum()
elif sys.argv[1]=='kontrol':
    getirklasor()

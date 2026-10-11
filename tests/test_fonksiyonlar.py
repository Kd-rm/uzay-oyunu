from uzay_oyunu.oyun import envanter_metni , hedef_menusu , galaksi_kur
from uzay_oyunu.kayit import gorev_kaydi
import pytest 

def test_envanter_metni_dolu():
    sonuc = envanter_metni(True,False,True)
    assert sonuc == "Sende: bol kredi, yetenekli bir pilot"

def test_envanter_metni_bos():
    sonuc = envanter_metni(False,False,False)
    assert sonuc ==""

def test_hedef_menusu():
    hedefler = ["centauri","sirius"]
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(hedefler) == beklenen

def test_gorev_kaydi():
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Ayşe"}
    sonuc = gorev_kaydi("Kara deliğe atla", *adimlar, oncelik="yüksek", **ekler)

    beklenen = (
        "[YÜKSEK] Kara deliğe atla\n"
        "  1. Kredi kazan\n"
        "  2. Pilot bul\n"
        "  3. Hiperdrive al\n"
        "  sorumlu: Ayşe"
    )
    assert sonuc == beklenen

def test_galaksi_kur():
    veri = {
        "gezegenler": ["dünya", "mars"],
        "baglantilar": {"dünya": ["mars"], "mars": []},
        "baslangic": "dünya",
        "yakit": 100,
    }
    g = galaksi_kur(**veri)
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100

def test_galaksi_kur_varsayilan_yakit():
    g = galaksi_kur(["mars"], {"mars": []}, "mars")
    assert g["yakit"] == 50

def test_galaksi_kur_hatali_baslangic():
    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {"mars": []}, "dünya")


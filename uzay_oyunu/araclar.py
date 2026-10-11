import time


def hamle_sayaci():
    """Her cagirildiginda degeri 1 artan bir sayac fonksiyonu dondurur (Closure)."""
    sayac = 0

    def artir():
        nonlocal sayac
        sayac += 1
        return sayac

    return artir


def en_bagli_gezegenler(galaksi):
    """
    Gezegenleri baglanti sayisina gore coktan aza (azalan),
    esitlik durumunda ise alfabetik sirayla dondurur.
    """
    baglantilar = (
        galaksi["baglantilar"]
        if isinstance(galaksi, dict) and "baglantilar" in galaksi
        else galaksi
    )

    return sorted(
        baglantilar.keys(),
        key=lambda gezegen: (-len(baglantilar[gezegen]), gezegen),
    )


def sure_olc(fonksiyon):
    """
    Verilen fonksiyonu *args ve **kwargs ile cagiran,
    calisma suresini ekrana basan sarmalayici fonksiyon.
    """
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        gecen_sure = bitis - baslangic
        print(f"{fonksiyon.__name__} çalışma süresi: {gecen_sure:.6f} saniye")
        return sonuc

    return sarmalayici


if __name__ == "__main__":
    # Föydeki deneme adımı
    ornek_galaksi = {
        "dünya": ["ay", "mars"],
        "sirius": ["orion", "vega", "centauri"],
        "kara_delik": [],
    }

    # Fonksiyon sure_olc ile sarmalaniyor
    en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)
    sirali = en_bagli_gezegenler(ornek_galaksi)
    print("Sıralı liste:", sirali)
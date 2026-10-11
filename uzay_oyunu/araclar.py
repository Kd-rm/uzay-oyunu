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
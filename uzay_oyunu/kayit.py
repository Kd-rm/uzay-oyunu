def gorev_kaydi(
    baslik: str,
    *adimlar: str,
    oncelik: str = "normal",
    **ekler: object,
) -> str:
    """Gorev detaylarini, adimlarini ve ek bilgileri bicimlendirilmis metin olarak dondurur."""
    satirlar = [f"[{oncelik.upper()}] {baslik}"]

    # Adimlari 1'den baslayarak numaralandir ve ekle
    sira = 1
    for adim in adimlar:
        satirlar.append(f"  {sira}. {adim}")
        sira = sira + 1

    # Ek bilgileri (anahtar: deger) seklinde ekle
    for anahtar, deger in ekler.items():
        satirlar.append(f"  {anahtar}: {deger}")

    return "\n".join(satirlar)


if __name__ == "__main__":
    # 1. Çağrı Biçimi: Doğrudan argümanlar vererek
    print("=== 1. Çağrı Biçimi ===")
    print(
        gorev_kaydi(
            "Kara deliğe atla",
            "Kredi kazan",
            "Pilot bul",
            "Hiperdrive al",
            oncelik="yüksek",
            sorumlu="Ayşe",
        )
    )

    print()

    # 2. Çağrı Biçimi: Listeyi (*) ve Sözlüğü (**) açarak
    print("=== 2. Çağrı Biçimi (* ve ** ile) ===")
    adim_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}

    print(
        gorev_kaydi(
            "Kara deliğe atla",
            *adim_listesi,
            oncelik="yüksek",
            **ek_bilgiler,
        )
    )
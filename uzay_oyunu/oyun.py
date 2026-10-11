import json


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Mevcut esyalarin durumuna gore envanter metnini dondurur."""
    esyalar = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motor")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""
    return "Sende: " + ", ".join(esyalar)


def hedef_menusu(hedefler: list[str]) -> str:
    """Mevcut hedefleri numaralandirilmis bir menu metni olarak dondurur."""
    satirlar = ["Nereye gitmek istersin?"]
    sira = 1
    for hedef in hedefler:
        satirlar.append(f"[{sira}] {hedef}")
        sira = sira + 1
    return "\n".join(satirlar)


def galaksi_kur(
    gezegenler: list[str], baglantilar: dict, baslangic: str, **kwargs
) -> dict:
    """Galaksi haritasini kurar ve baslangic durumunu sozluk olarak dondurur."""
    if baslangic not in gezegenler:
        raise ValueError(f"Gecersiz baslangic gezegeni: {baslangic}")

    yakit = kwargs.get("yakit", 50)

    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit,
    }


def travel(
    galaksi: dict, planet: str, credits: bool, engines: bool, copilot: bool
) -> None:
    """Oyuncunun envanterini ve secilen gezegenden gidilebilecek hedefleri ekrana basar."""
    envanter = envanter_metni(credits, engines, copilot)
    if envanter:
        print(envanter)

    # Hedefleri harita sozlügünden cekiyoruz
    hedefler = galaksi["baglantilar"][planet]
    print(hedef_menusu(hedefler))


if __name__ == "__main__":
    with open("uzay_oyunu/galaksi.json", "r", encoding="utf-8") as f:
        veri = json.load(f)

    galaksi = galaksi_kur(**veri)

    travel(galaksi, galaksi["konum"], True, False, True)
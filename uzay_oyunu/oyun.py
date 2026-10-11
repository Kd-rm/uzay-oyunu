def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Mevcut esyalarin durumuna gore envanter metnini dondurur."""
    esyalar = []
    if credits :
        esyalar.append("bol kredi")
    if engines :
        esyalar.append("güçlü motor")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar :
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

def travel(hedefler: list[str], credits: bool, engines: bool, copilot: bool) -> None:
    """Oyuncunun envanterini ve gidebilecegi hedefleri ekrana basar."""
    envanter = envanter_metni(credits, engines, copilot)
    if envanter:
        print(envanter)
    print(hedef_menusu(hedefler))

if __name__ == "__main__":
    travel(["centauri", "sirius"], True, False, True)
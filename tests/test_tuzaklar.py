def yakit_ekle(miktar,depo=None):
    if depo is None :
        depo = []
    depo.append(miktar)
    return depo

def test_yakit_ekle():
    ilk_cagri = yakit_ekle(10)
    ikinci_cagri = yakit_ekle(20)

    assert ikinci_cagri == [20]
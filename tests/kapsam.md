# Değişken Kapsamı (Scope) ve Tuzaklar

## Örnek 1: Fonksiyon İçinden Global Değişkeni Okuma

```python
x = 10

def goster():
    print(x)

goster()
```

- **Tahmin:** 10
- **Gerçek Sonuç:** 10
- **Nedeni:** Fonksiyon kendi içinde x adında bir yerel değişken bulamadığı için bir üst kapsama (global alana) bakar ve oradaki 10 değerini okur.

---

## Örnek 2: Fonksiyon İçinde Yerel Değişken Tanımlama

```python
x = 10

def degistir():
    x = 20
    print(x)

degistir()
print(x)
```

- **Tahmin:** 20 ve 10
- **Gerçek Sonuç:** 20 ve 10
- **Nedeni:** Fonksiyon içinde x = 20 ataması yapıldığında fonksiyona özel yeni bir yerel (local) değişken oluşturulur. Dışarıdaki global x değişkeni bundan etkilenmez ve 10 olarak kalır.

---

## Örnek 3: Değiştirmeye Çalışırken Hata Alma (UnboundLocalError)

```python
x = 10

def artir():
    x = x + 1
    print(x)

artir()
```

- **Tahmin:** UnboundLocalError
- **Gerçek Sonuç:** UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
- **Nedeni:** Python bir fonksiyon içinde bir değişkene atama yapıldığını (x = ...) görürse, o değişkeni fonksiyon çalışmadan önce tamamen yerel (local) olarak işaretler. x = x + 1 satırında eşitliğin sağ tarafındaki x okunmaya çalışıldığında, Python globaldeki 10'a bakmaz; yerel x'i arar. Yerel x henüz bir başlangıç değerine sahip olmadığı için UnboundLocalError hatası verir.
# CALROV-27-EGITIMLERI
# Ödev: Terminal Tabanlı Gerçek Zamanlı Klavye Kontrol Sistemi

## 1. Ödevin Amacı

Bu ödevin amacı, klavyeden alınan girdilerle gerçek zamanlı olarak kontrol edilebilen ve birden fazla farklı işlevi yerine getirebilen bir uygulama geliştirmektir.

Geliştirilecek program terminal üzerinden çalışmalı, kullanıcıdan gelen klavye girdilerini algılamalı ve ilgili işlemi gecikmeden gerçekleştirmelidir.

Bu projede temel hedef yalnızca klavyeden veri almak değil, **sürekli çalışan, etkileşimli ve birden fazla görevi yönetebilen bir sistem** oluşturmaktır.

## 2. Temel Gereksinimler

Geliştirilecek uygulama aşağıdaki gereksinimlerin tamamını karşılamalıdır.

### 2.1. Gerçek Zamanlı Klavye Kontrolü

- Program, klavyeden gelen girdileri gerçek zamanlı olarak algılamalıdır.
- Kullanıcının bir işlem gerçekleştirmek için her defasında komut yazıp Enter tuşuna basması gerekmemelidir.
- Kullanıcı, programı istediği zaman güvenli bir şekilde durdurabilmelidir.
- Kullanılacak tuşlar ve bunların işlevleri açıkça belirtilmelidir.

### 2.2. Birden Fazla İşlev

Program, klavye aracılığıyla kontrol edilebilen en az **4 farklı işlev** içermelidir.

Örnek işlevler:

- **Hareket kontrolü:** Bir karakteri veya nesneyi yukarı, aşağı, sağa ve sola hareket ettirmek. Burada hareket ettirmeyi göstere bilmek için alınan girdiye göre logging ile "yukarı", "aşağı" gibi ifadeleri terminale yazdırmanız yeterlidir.
- **Mod değiştirme:** Programın çalışma modunu değiştirmek. Aynı şekilde logging ile yazdırılması yeterlidir.
- **Durum kontrolü:** Programın aktif modunu görüntülemek.
- **Eylem gerçekleştirme:** Belirli bir tuşa basıldığında bir işlemi başlatmak, durdurmak veya tetiklemek.

### 2.3. Terminal Üzerinden Kontrol

- Program terminalden başlatılmalı ve kullanılabilmelidir.
- Kontrol işlemleri terminal üzerinden gerçekleştirilebilmelidir.
- Programın durumu, yapılan işlemler ve gerekli bilgilendirmeler terminalde gösterilmelidir.
- Kullanıcı, uygulamanın hangi durumda olduğunu anlayabilmelidir.

### 2.4. Sürekli Çalışma ve Kontrol Döngüsü

Program, kullanıcı bir işlem gerçekleştirene kadar çalışmaya devam etmelidir.

- Klavye girdileri sürekli kontrol edilmelidir.
- Kullanıcı girdisi olmadığında program gereksiz işlemler yapmamalıdır.
- Bir işlev çalışırken diğer kontroller mümkün olduğunca kullanılabilir durumda kalmalıdır.
- Program sonlandırıldığında gerekli kaynaklar düzgün şekilde serbest bırakılmalıdır.

## 3. Teknik Gereksinimler

- Program bir terminal veya komut satırı üzerinden çalışmalıdır.
- İşlevler mümkün olduğunca birbirinden ayrılmalıdır.
- Hatalı veya beklenmeyen girdiler programın aniden kapanmasına neden olmamalıdır.

## 4. Kullanıcı Arayüzü ve Kontrol Şeması

Program başladığında terminalde aşağıdaki bilgilere benzer bir kontrol rehberi gösterilmelidir:

| Tuş   | Örnek görev                         |
| ----- | ----------------------------------- |
| W     | Yukarı hareket                      |
| A     | Sola hareket                        |
| S     | Aşağı hareket                       |
| D     | Sağa hareket                        |
| C     | Stabilize Moduna Geçiş              |
| H     | Depth Hold isimli Moda Geçiş        |
| I     | Sistem durumunu görüntüleme         |
| Q     | Programdan çıkış                    |

## 5. Değerlendirme Kriterleri

| Kriter                                 |    Puan |
| -------------------------------------- | ------: |
| Gerçek zamanlı klavye kontrolü         |      25 |
| En az 4 farklı işlevin doğru çalışması |      25 |
| Terminal üzerinden kullanım            |      15 |
| Kod düzeni ve modülerlik               |      25 |
| Hata yönetimi ve güvenli sonlandırma   |      10 |
| **Toplam**                             | **100** |

## 6. Başarı Ölçütü

Başarılı bir uygulama:

1. Terminal üzerinden başlatılmalı ve çalışmalıdır.
2. Gerçek zamanlı klavye girdilerini algılamalıdır.
3. Birbirinden farklı birden fazla işlev sunmalıdır.
4. Kullanıcıya sistemin mevcut modu hakkında bilgi vermelidir.

## SON NOTLAR

1. Kodlarınızı bitirdikten sonra bu branche pull request atın ve kod dosyanızın ismini kendi adınız yapın. Örneğin : ahmet_nihat.py
2. Hafta sonu ödev süresince takıldığınız herhangi bir yeri çekinmeden sorabilirsiniz.
3. Son teslim: 11 Ekim Pazar 23.59
4. Mümkün mertebe kodlarınızda AI kullanmamaya özen gösterin.
5. Hepinize kolay gelsin.

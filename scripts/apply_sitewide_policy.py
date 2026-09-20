# -*- coding: utf-8 -*-
"""Site-wide AdSense inventory: unique guides, duplicate redirects, category rebuild."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from apply_publisher_policy import (  # noqa: E402
    ARTICLE_AD,
    ROOT,
    rewrite_article,
    strip_editorial_depth,
)

DUPLICATES = {
    "akilli-ev-urunlerinde-uyumluluk-sorunu-azaliyor": "akilli-ev-cihazlari-daha-uyumlu-hale-geliyor",
    "belgesel-turunde-haftanin-dikkat-ceken-onerileri": "belgesel-onerileri-teknoloji-ve-doga-meraklilarini-hedefliyor",
    "bulut-depolama-servislerinde-yeni-kapasite-paketleri": "bulut-depolama-servisleri-kapasite-paketlerini-guncelliyor",
    "bulut-tabanli-ofis-araclari-daha-akilli-hale-geliyor": "bulut-tabanli-calisma-araclari-ekiplerin-is-akisini-degistiriyor",
    "dijital-servislerde-abonelik-fiyatlari-yeniden-gundemde": "dijital-servislerde-yeni-abonelik-paketleri-gundemde",
    "ev-internetinde-yeni-hiz-paketleri-gundemde": "ev-internetinde-hiz-ve-gecikme-degerleri-daha-fazla-onem-kazaniyor",
    "giyilebilir-teknolojiler-saglik-takibini-gelistiriyor": "giyilebilir-teknolojiler-saglik-takibinde-daha-iddiali",
    "kablosuz-kulakliklarda-yapay-zeka-destekli-ses-modu": "kablosuz-kulakliklarda-gurultu-engelleme-ozellikleri-gelisiyor",
    "kucuk-isletmeler-otomasyon-araclarini-benimsiyor": "kucuk-isletmeler-yapay-zeka-ile-otomasyon-firsatlarini-arastiriyor",
    "mobil-uygulama-gelistirmede-yeni-performans-donemi": "mobil-uygulama-gelistirmede-performans-odakli-yeni-yaklasimlar",
    "sosyal-medya-uygulamalarinda-yeni-guvenlik-ozellikleri": "sosyal-medya-uygulamalarinda-guvenlik-ozellikleri-artiyor",
    "video-uretme-modellerinde-kalite-yarisi-hizlandi": "video-uretme-yapay-zekalari-icerik-ureticilerin-radarinda",
    "yerli-girisimlerden-yapay-zeka-destekli-yeni-cozumler": "yerli-girisimler-yapay-zeka-destekli-cozumler-gelistiriyor",
    "bilim-kurgu-filmi-icin-ilk-fragman-yayinlandi": "bilim-kurgu-filmi-ilk-fragmaniyla-dikkat-cekti",
    "yeni-film-ve-dizi-haberleri-tek-sayfada-toplandi": "yeni-film-ve-dizi-takvimi-izleyiciler-icin-hareketli-geciyor",
    "ai-destekli-arama-motorlari-daha-dogal-cevap-veriyor": "yapay-zeka-destekli-arama-motorlari-klasik-aramayi-zorluyor",
    "api-servislerinde-hiz-ve-guvenilirlik-yarisi": "api-kullaniminda-hiz-ve-guvenilirlik-neden-onemli",
    "elektrikli-otomobil-pazarinda-fiyat-rekabeti-hizlandi": "elektrikli-araclarda-sarj-altyapisi-rekabeti-hizlandi",
    "ekran-teknolojilerinde-parlaklik-ve-enerji-yarisi": "ekran-teknolojilerinde-parlaklik-ve-enerji-verimliligi-yarisi",
    "gorsel-uretme-araclari-tasarim-surecini-hizlandiriyor": "gorsel-uretme-araclari-tasarim-surecini-degistiriyor",
    "kult-serinin-devam-filmi-icin-hazirlik-basladi": "kult-serinin-devam-filmi-icin-hazirliklar-basladi",
    "yayin-platformlari-yaz-takvimini-guncelledi": "yayin-platformlari-yaz-kataloglarini-guncelliyor",
    "teknoloji-dunyasinda-bugun-one-cikan-her-seyi-anlattik": "teknoloji-gundeminde-bugun-one-cikan-basliklar",
    "verimlilik-uygulamalari-ekip-calismasini-kolaylastiriyor": "verimlilik-uygulamalari-gunluk-planlamayi-kolaylastiriyor",
    "ai-araclari-is-dunyasinda-yeni-donemi-baslatti": "yapay-zeka-araclari-is-dunyasinda-yeni-verimlilik-donemi-baslatti",
    "teknoloji-alisverisinde-dikkat-edilmesi-gerekenler": "teknoloji-alisverisinde-garanti-ve-servis-destegi-neden-onemli",
    "akilli-telefonlarda-batarya-odakli-yeni-donem": "yeni-nesil-telefon-bataryalari-daha-uzun-omur-hedefliyor",
    "ogrenciler-icin-yapay-zeka-destekli-calisma-araclari": "egitimde-yapay-zeka-destekli-calisma-araclari-yayginlasiyor",
    "siber-guvenlik-ekipleri-icin-kritik-yama-uyarisi": "siber-guvenlik-yamalarini-geciktirmek-buyuk-risk-olusturuyor",
    "acik-kaynak-kutuphanelerde-haftanin-one-cikanlari": "acik-kaynak-projeler-teknoloji-dunyasinda-etkisini-artiriyor",
    "bilgisayar-donaniminda-performans-yarisi-buyuyor": "donanim-pazarinda-fiyat-ve-performans-dengesi-degisiyor",
    "haftanin-en-cok-izlenen-yapimlari-belli-oldu": "yeni-film-ve-dizi-takvimi-izleyiciler-icin-hareketli-geciyor",
    "yeni-nesil-teknoloji-haberlerini-tek-ekranda-yakala": "haftanin-kisa-teknoloji-ozeti-yayinda",
    "netflix-haftalik-top-10-listesinde-i-will-find-you-zirveye-cikti": "netflix-haftalik-top-10-listesinde-i-will-find-you-zirveye-yerlesti",
    "netflix-bu-hafta-color-book-ve-the-american-experiment-gibi-yapimlari-one-cikardi": "netflix-haftanin-izlenecek-yapimlarini-yeni-listeyle-paylasti",
    "yeni-nesil-yapay-zeka-araclari-is-dunyasinda-nasil-fark-olusturuyor": "yapay-zeka-araclari-is-dunyasinda-yeni-verimlilik-donemi-baslatti",
}


def g(title, description, dek, lede, context, h2, how, who, checks, close):
    bullets = "".join(f"<li>{c}</li>" for c in checks)
    return {
        "title": title,
        "description": description,
        "dek": dek,
        "body": f"""
<p>{lede}</p>
<p>{context}</p>
<h2>{h2}</h2>
<p>{how}</p>
{ARTICLE_AD}
<h2>Kim için, ne zaman?</h2>
<p>{who}</p>
<ul>{bullets}</ul>
<p>{close}</p>
""",
    }


GUIDES = {
    "akilli-ev-cihazlari-daha-uyumlu-hale-geliyor": g(
        "Akıllı evde uyumluluk: Matter, köprü ve gerçek maliyet",
        "Akıllı ev alırken marka vaadi değil Matter, köprü ve uygulama sayısı karar verir.",
        "Yeni standartlar işe yarar; ancak evdeki eski priz ve ampul köprü ister.",
        "Akıllı ev haberleri ‘her şey birbirine bağlandı’ diye yazılır. Mutfakta durum daha dardır: bir markanın ampulü, diğerinin hoparlörüne bazen yalnızca bir köprü ve ikinci bir uygulama ile konuşur. AcarTechs bu yazıda duyuru kopyalamaz. Hangi evin gerçekten Matter’a geçmesi gerektiğini ayırır.",
        "Matter ve Thread, üreticilerin kendi duvarını aşındırmak için çıktı. Yine de kutu üzerindeki logo, mevcut yönlendiricinizin Thread kenarlık yönlendiricisi olduğu anlamına gelmez. Evdeki 2.4 GHz doluluğu, misafir ağı ve VLAN, ‘uyumlu’ yazan bir prizin sessizce düşmesine yeter.",
        "Almadan önce üç soru",
        "Bir: cihaz yerel olarak mı çalışıyor, yoksa bulut kesilince lamba mı kalıyor? İki: evde kaç uygulama istiyorsunuz? Üç: enerji ölçümü, sahne ve ses asistanı aynı anda mı şart? Üçüne de ‘hepsi olsun’ derseniz bütçe ve arıza yüzeyi büyür. AcarTechs, ilk yıl için aydınlatma ve prizi tek ekosistemde tutmayı, kilit ve kamerayı ayrı güvenlik katmanı saymayı önerir.",
        "Kiralık evde vida delmeyen priz ve ampul daha rasyoneldir. Müstakil evde kablo çekilebiliyorsa, kablosuz kalabalığı azaltmak uzun vadede daha az baş ağrısı üretir. Yaşlı ebeveyn için ‘tek fiziksel düğme’ hâlâ en iyi arayüzdür; uygulama tek yol olmamalıdır.",
        ["Matter yazısı varsa hangi asistanın resmi listesinde durduğuna bakın", "Köprü ayrı satılıyorsa kutu fiyatına ekleyin", "Misafir Wi-Fi’de IoT cihazı bırakmayın"],
        "Uyumluluk, vitrin cümlesi değil; evdeki mevcut ağa, köprüye ve ‘internet gidince ne olur’ testine bağlıdır.",
    ),
    "belgesel-onerileri-teknoloji-ve-doga-meraklilarini-hedefliyor": g(
        "Teknoloji ve doğa belgeseli nasıl seçilir?",
        "Belgesel listesi ezberi yerine süre, anlatıcı ve abonelik katmanına göre seçim rehberi.",
        "Haftalık ‘öneri’ başlığı, sizin 50 dakikanızı doldurmaz; süzgeç doldurur.",
        "Yayın platformları her hafta doğa ve teknoloji belgeseli yığar. Listenin tamamını izlemek bir iştir. AcarTechs, belgeseli dizi gibi ‘kaçırma’ diye okumaz. Süre, anlatıcı üslubu ve bölüm bağımsızlığı asıl süzgeçtir.",
        "Teknoloji belgesellerinde ürün yerleştirme ve şirket erişimi sık görülür. Doğa belgesellerinde ise görüntü kalitesi yüksek, bağlam zayıf kalabilir. İkisinde de ‘izledim, ne öğrendim?’ cümlesi kurulamıyorsa geceyi doldurmuş olursunuz, birikim bırakmazsınız.",
        "Üç süzgeç",
        "Süre: 40–55 dakika, hafta içi için idealdir. Mini dizi 3×45, hafta sonuna bırakılır. Anlatıcı: spekülatif ‘yakında her şey değişecek’ dili varsa teknoloji belgeselini yarıda kesmek serbesttir. Bölüm bağımsızlığı: 1. bölüm yetmiyorsa 8 bölümlük taahhüt yazmayın.",
        "Öğrenci ve meraklı izleyici için tek bir iyi bilim anlatısı, beş yarım kalmış ‘öneri’ listesinden değerlidir. Çocuk profilinde doğa belgeseli, korku ve av sahneleri için yaş etiketine bakılmadan açılmamalıdır.",
        ["Abonelik katmanında gerçekten var mı kontrol edin", "İlk 10 dakikada tez yoksa bırakın", "Aynı konunun iki belgeselini üst üste izlemeyin"],
        "Belgesel önerisi, keşif aracıdır. Tamamını izleme yükümlülüğü değildir.",
    ),
    "bulut-depolama-servisleri-kapasite-paketlerini-guncelliyor": g(
        "Bulut depolama paketi seçimi: fotoğraf, yedek, paylaşım",
        "Google, iCloud ve benzeri paketleri AcarTechs kapasite duyurusu değil kullanım senaryosu olarak okur.",
        "GB sayısı, aile fotoğrafı ile iş yedeğini aynı kutuya koymaz.",
        "Bulut depolama haberleri ‘daha fazla GB, aynı fiyata’ diye akar. Evde asıl kırılım üçtür: telefon rulosu, bilgisayar yedeği ve başkasıyla klasör paylaşımı. Bu üçü aynı pakette ucuz görünebilir; çıkış kapısı (export) kapalıysa ucuzluk değildir.",
        "Fotoğraf rulosu her yıl 30–80 GB şişebilir. 200 GB’lık aile planı, dört telefon ve bir dizüstü yedeği için daralır. 2 TB’a sıçramak, ‘biraz daha yer’ değil ikinci bir fatura kararıdır. AcarTechs, ilk iş olarak hangi cihazın otomatik yükleme açık olduğunu saymanızı ister.",
        "Hangi paket kime?",
        "Tek telefon, Wi-Fi’de yükleme: ücretsiz katman + yerel kablo yedeği çoğu kişiyi taşır. Aile ve iki bilgisayar: 200 GB–2 TB arası, paylaşım izni net olan servis. Hassas iş dosyası: istemci tarafı şifreleme veya ayrı bir kasa; ‘her şey aynı bulutta’ konforu, hesap ele geçince tek noktadan kayıptır.",
        "Paket yükseltmeden önce çöp: ekran görüntüsü, tekrar indirilen kurulum ve WhatsApp medyası. 20 GB temizlik, bir yıl boyunca üst katmanı erteleyebilir. Çıkış testi yapın: 5 GB’ı başka diske indirmek bir akşamı aşıyorsa, o servise kilitlenmişsinizdir.",
        ["Otomatik yükleme hangi klasörde açık?", "Aile paylaşımında kim silebiliyor?", "İki faktör ve yedek kod kâğıtta mı?"],
        "Kapasite kampanyası, depolama alışkanlığını değiştirmiyorsa yalnızca faturayı büyütür.",
    ),
    "bulut-tabanli-calisma-araclari-ekiplerin-is-akisini-degistiriyor": g(
        "Ekip için bulut ofis: ne zaman geçilir, ne zaman yerelde kalınır?",
        "Docs, tablolar ve sohbeti tek buluta taşımanın gerçek maliyeti sürüm, izin ve çevrimdışı çalışmadır.",
        "‘Herkes aynı dosyada’ cümlesi, izin dağınıklığını gizler.",
        "Bulut ofis araçları, e-posta ekiyle dönen Word dosyasını bitirdi. Yerine sürüm karmaşası, misafir bağlantısı ve ‘kim sildi’ sorusu geldi. AcarTechs, geçişi ideoloji diye yazmaz. Ekip 3 kişiyse ve dosyalar müşteri verisi taşımıyorsa geçiş ucuzdur. 15 kişi ve sözleşmeler varsa izin şeması yazılmadan taşınmaz.",
        "Asıl kazanç, aynı anda yazmak değil; tek gerçeğin nerede durduğunu bilmektir. Üç klasörde üç ‘son_versiyon.xlsx’ varsa bulut sucu değildir, isimlendirme sucudur.",
        "Geçiş kontrol listesi",
        "Önce bir proje, bir sürücü, bir sohbet kanalı. İkinci hafta: harici paylaşımı varsayılan kapatın. Üçüncü: çevrimdışı paket gerçekten açılıyor mu, uçak modunda deneyin. Satış sunumu havalimanında açılamıyorsa araç sizin işinize göre değildir.",
        "Muhasebe ve hukuk ekipleri, müşteri dosyasını kişisel hesapta tutmamalıdır. Kurumsal kirada yönetim, cihaz kaybında uzaktan silme ve kayıt defteri yoksa ‘ucuz bulut’ gizlilik faturası keser.",
        ["Kişisel Gmail ile iş dosyası paylaşmayın", "Misafir linkine son tarih koyun", "Silinen dosya çöp kutusunda kaç gün duruyor bakın"],
        "Bulut ofis, disiplini olan ekibe hız; disiplinsiz ekibe daha hızlı dağınıklık verir.",
    ),
    "dijital-servislerde-yeni-abonelik-paketleri-gundemde": g(
        "Dijital abonelik budama rehberi: hangisi durur, hangisi iner?",
        "Yayın, depolama ve yazılım faturalarını AcarTechs katalog duyurusu değil kullanım saatiyle budar.",
        "Yeni paket, kullanılmayan eski paketi otomatik iptal etmez.",
        "Her ay bir servis ‘aile planı’ veya ‘daha ucuz yıllık’ çıkarır. Fatura uygulamasında 7–12 satır birikir. AcarTechs’in kuralı sadedir: son 30 günde açılmayan abonelik, reklam değil masraftır.",
        "Yayın servislerinde içerik dalgası aylık gelir. İki platformu aynı anda tutmak, ancak haftalık 8 saatten fazla izleyen ev için rasyoneldir. Yazılım aboneliğinde yıllık ödeme, iptali utandırır; deneme bitmeden takvim hatırlatması koyun.",
        "Budama sırası",
        "Bir: tekrarlayan ödemeleri banka ekstresinden işaretleyin. İki: her satıra ‘bu ay kaç saat?’ yazın. Üç: 2 saatten az olanı duraklatın veya indirin. Dört: aile planında kimin hesabı şişiriyor bakın; tek kişi 4K ve ek üye tutuyorsa plan yanlış kişidedir.",
        "Öğrenci ve yeni mezun için yıllık taahhüt, üç ay sonra iş değişince ceza üretebilir. Aylık tutup yoğun ayda açmak, ‘kaçırma’ dilinden ucuzdur.",
        ["Aynı içeriği iki serviste tutmayın", "Deneme bitişini takvime yazın", "Paylaşılan şifre, fatura sahibi değişince kırılır"],
        "Yeni paket haberi, sizin listenize bir satır eklemek zorunda değildir. Çoğu zaman bir satır silmek daha kârlıdır.",
    ),
    "ev-internetinde-hiz-ve-gecikme-degerleri-daha-fazla-onem-kazaniyor": g(
        "Ev interneti: Mbps değil, gecikme ve akşam saati",
        "Hız paketi reklamını AcarTechs akşam saati, kablo ve Wi-Fi katmanıyla okur.",
        "1000 Mbps yazısı, 12 ms gecikmeli oyunu garanti etmez.",
        "Operatörler paketleri indirme hızıyla satar. Evde şikâyet ise akşam 21.00’de takılan görüntülü arama ve Wi-Fi odasıdır. AcarTechs, paket yükseltmeden önce üç katmanı ayırır: binaya gelen hat, modem, odadaki kablosuz.",
        "Gecikme (ping) oyun ve arama için hızdan önce gelir. 40 ms üstü, rekabetçi oyunda cezadır. 4K yayın 25 Mbps civarı yer; 8 cihaz birden açılınca sorun hız değil, hava ve kanal kalabalığıdır.",
        "Yükseltmeden önce",
        "Kabloyla modeme bağlanıp hız testini akşam tekrarlayın. Kablo iyiyse, Wi-Fi kötüdür: kanal, 5 GHz ve konum. Kablo da kötüyse paket değil hat veya modem konuşulur. Mesh, duvarı sihirle delmez; düğüm sayısı ve Ethernet geri dönüşü işe yarar.",
        "Evde çalışan biri için yükleme hızı (upload) indirmeden kritik olabilir. 5 Mbps yükleme, 1080p yayın ve yedek için daralır. Oyun + 4K + iki telefon aynı anda ise ‘oyun için ayrı 5 GHz’ basit ve ucuz bir ayrımdır.",
        ["Akşam testi yapmadan paket değiştirmeyin", "Modem şifresini operatör varsayılanında bırakmayın", "Misafir ağı IoT ve işi ayırır"],
        "Hız paketi, evin akşam gerçeğini ölçmeden alınan bir tahmindir.",
    ),
    "giyilebilir-teknolojiler-saglik-takibinde-daha-iddiali": g(
        "Akıllı saat sağlık vaadi: ne ölçülür, ne teşhis değildir?",
        "Nabız, uyku ve oksijen sayılarını AcarTechs tıbbi cihaz gibi değil, eğilim aracı olarak okur.",
        "Yeni sensör, doktor yerine geçmez; tutarsız kullanım ise sayıyı çöpe çevirir.",
        "Saat üreticileri her yıl yeni sağlık kartı açar: uyku evreleri, stres, kan oksijeni. Bunlar eğilim gösterir. Teşhis koymaz. AcarTechs, kutudaki tıbbi dil ile gerçek kullanım arasına çizgi çeker.",
        "Nabız, sıkı kayış ve terle değişir. Uyku skoru, gece 3’te bakılan telefona göre savrulur. Oksijen ölçümü, soğuk parmakta ve hareket halinde gürültülüdür. Tek bir ‘kötü gece’ paniği, cihazı yanlış okumaktır.",
        "Ne için alınır?",
        "Adım ve tempolu yürüyüş hatırlatması çoğu insanda işe yarar. Kalp ritmi uyarıları, aile öyküsü olan ve hekimin ‘takip et’ dediği kişiye ek göz olabilir; kendi başına tanı değildir. Sporcu için GPS ve tempo, sağlık kartından değerlidir.",
        "Pil: her gece şarj edilen saat, uyku takibini yarım bırakır. 5–7 gün giden, daha az özellikli model, düzenli kullanımda ‘daha iddialı’ modelden fazla iş üretir. Verinin telefonda hangi ülkeye gittiği, sağlık vaadinden ayrı bir gizlilik kararıdır.",
        ["Kayışı parmak sığacak kadar sıkın", "Tek sapmayı değil 14 günlük eğilimi okuyun", "Kırmızı uyarıda uygulama değil hekim"],
        "Saat, aynadır. Teşhis koyan cam değildir.",
    ),
    "kablosuz-kulakliklarda-gurultu-engelleme-ozellikleri-gelisiyor": g(
        "ANC kulaklık: ofis, uçak, sokak için ayrı seçim",
        "Gürültü engelleme yazısını AcarTechs bass reklamı değil, sızdırma, konfor ve şeffaf mod üzerinden okur.",
        "ANC, her gürültüyü silmez; motor ve klima ile konuşma farklıdır.",
        "Kulaklık kutuları ‘akıllı gürültü engelleme’ yazar. Ofisteki konuşma, uçak motoru ve sokak rüzgârı aynı algoritma değildir. AcarTechs, ANC’yi tek özellik diye satmaz. Kullanım yeri, kulak ucu bedeni ve şeffaf mod kalitesi karar verir.",
        "Uçak ve metroda sürekli düşük frekans vardır; iyi ANC burada parlar. Açık ofiste insan sesi kalır. Koşuda rüzgâr, mikrofonları şaşırtır. ‘AI ses modu’ bazen kendi nefesinizi büyütür.",
        "Alırken",
        "Üç saatlik konfor, sürücü milimetresinden önce gelir. Kulak içi, yastık bedeniyle ANC’nin yarısını halleder; yanlış beden, pahalı ANC’yi boşa çıkarır. Şeffaf mod, kasa gişesinde ve bisiklette güvenliktir. Kaçak ses, kütüphanede komşu düşmanıdır.",
        "Tek telefon kullanıcısı için uygulama şartı, ikinci bir hesap demektir. Çift cihaz (iş laptop + telefon) için hızlı geçiş yoksa ‘pro’ etiket boşa çıkar. Pil kılıfı olmadan 4 saat, uçak için yetmeyebilir.",
        ["Silikon uç bedenini deneyin", "ANC’yi sokakta varsayılan açmayın", "Şeffaf modu gişeden önce test edin"],
        "Gürültü engelleme, doğru yerde konfor; yanlış yerde izolasyon ve tehlike üretir.",
    ),
    "kucuk-isletmeler-yapay-zeka-ile-otomasyon-firsatlarini-arastiriyor": g(
        "Küçük işletmede yapay zekâ: hangi iş otomatikleşir?",
        "KOBİ için yapay zekâ, ‘ajan’ reklamı değil; fatura, randevu ve sık sorulan soru otomasyonudur.",
        "İlk bot, muhasebeyi değil, tekrarlayan mesajı hedeflemelidir.",
        "Küçük işletmeye satılan yapay zekâ, çoğu zaman büyük şirket slaytının küçültülmüşüdür. 4 kişilik bir dükkânın sorunu ‘çok ajanlı orkestrasyon’ değildir. WhatsApp’ta 40 kez sorulan fiyat, randevu saati ve fatura kalemi tekrarıdır.",
        "AcarTechs, ilk 30 günü tek işe bağlar: en çok tekrarlanan müşteri sorusunu bir yanıt taslağına çevirmek. İkinci 30 gün: randevu veya sipariş formunu insansız almaktır. Muhasebe ve hukuki metin, insan onayı olmadan modele bırakılmaz.",
        "Maliyet tuzağı",
        "Aylık ‘sınırsız asistan’ paketleri, kullanılmayan koltuk gibi durur. Personel zaten Excel biliyorsa, hazır tablo + e-posta kuralı, ilk yapay zekâ faturasından ucuzdur. Müşteri verisini kişisel ChatGPT hesabına yapıştırmak, KVKK ve müşteri güveni riskidir.",
        "Restoran, klinik randevusu ve e-ticaret kargo sorusu iyi adaylardır. Uyarlama üretim, fiyat teklifi ve şikâyet yönetimi kötü adaylardır; bağlam ve tonda hata pahalıdır.",
        ["Müşteri verisini kişisel hesaba yapıştırmayın", "İlk ay tek süreç seçin", "Yanıtı yayınlamadan insan okusun"],
        "Otomasyon, işi yok etmek değil; aynı cümleyi 40 kez yazmayı yok etmektir.",
    ),
    "mobil-uygulama-gelistirmede-performans-odakli-yeni-yaklasimlar": g(
        "Mobil uygulamada performans: ilk açılış, ısınma, ağ",
        "Geliştirici duyurusu değil; kullanıcının 3 saniyesini ve pilini yiyen yerleri ayıklama rehberi.",
        "Yeni framework, soğuk açılışı tek başına düzeltmez.",
        "Mobil uygulama haberleri ‘yeni nesil performans’ diye akar. Kullanıcı ise açılışta beyaz ekran, kaydırırken takılma ve 10 dakikada ısınan telefon görür. AcarTechs, performansı pazarlama sürümü değil üç ölçüte bağlar: soğuk açılış, kare süresi, ağ suyu.",
        "Soğuk açılışta SDKların hepsini ayağa kaldırmak, ilk kareyi geciktirir. Görsel boyutu ve animasyon, orta segment cihazda kare düşürür. Analitik ve reklam SDK’sı, ağ ve pil faturasının görünmeyen kısmıdır.",
        "Geliştirici için sıra",
        "Önce gerçek cihaz, sonra emülatör. Orta segment bir Android, vitrin iPhone’undan daha dürüsttür. İkinci: ilk ekrana lazım olmayan işi erteleyin. Üçüncü: görseli WebP/AVIF ve doğru boyutta yayın. Dördüncü: ‘her olay’ analitiği yerine karar veren olayları ölçün.",
        "Ürün yöneticisi için ‘animasyon ekle’ talebi, 3 GB RAM’li telefonda kare cezasıdır. Performans bütçesi, özellik listesi kadar net yazılmalıdır.",
        ["Soğuk açılışı 3 saniyenin altında tutun", "SDK’yı ilk kareden sonra yükleyin", "Isınan cihazı ‘kullanıcı şarjı bitmiş’ diye kapatmayın"],
        "Performans, yeni araç duyurusu değil; kullanıcının elinde kalan sıcaklıktır.",
    ),
    "sosyal-medya-uygulamalarinda-guvenlik-ozellikleri-artiyor": g(
        "Sosyal medya güvenliği: varsayılanı kapatmak bir özelliktir",
        "Yeni kilit, izleyici listesi ve 2FA’yı AcarTechs duyuru değil, hesap ele geçirme öncesi kontrol listesi olarak yazar.",
        "Uygulama ‘güvenlik güncellendi’ der; varsayılan hâlâ herkese açıktır.",
        "Sosyal ağlar her çeyrek yeni kilit, gizli beğeni ve uyarı çıkarır. Çoğu kapalı kutu olarak gelir. AcarTechs, özelliği övmek yerine hesabı ele geçiren senaryoyu merkeze alır: tekrar kullanılan şifre, SMS 2FA, eski oturum ve herkese açık konum.",
        "Çocuk ve genç hesaplarında ‘bana mesaj atabilenler’ varsayılanı, arkadaş-arkadaşı bile fazla geniş olabilir. Yetişkinde iş mailiyle açılan hesap, kişisel fotoğrafla karışınca işveren araması üretir.",
        "Bu hafta yapılacaklar",
        "Şifre yöneticisi, uygulama 2FA (SMS değil), oturum listesinden tanıdık olmayan cihazı atmak. Konum ve yüz tanıma etiketini kapatmak. Eski e-posta kurtarma adresini güncellemek. ‘Bağlı uygulamalar’ listesindeki 2019 tarihli oyunu silmek.",
        "Yeni ‘güvenli klasör’ özelliği, yedek kod kâğıtta yoksa sizi kilitleyebilir. Kilit açmadan önce kurtarma yolunu yazın. Hesabı silmeden önce veri indirme (export) 48 saat sürebilir; öfke anında silmek arşivi yakar.",
        ["SMS yerine uygulama 2FA", "Herkese açık konum kapat", "Bağlı uygulamaları yılda bir budayın"],
        "Güvenlik özelliği, açılmayan anahtardır. Varsayılanı değiştirmeyen duyuru, süslemedir.",
    ),
    "video-uretme-yapay-zekalari-icerik-ureticilerin-radarinda": g(
        "Yapay zekâ video: ne zaman işe yarar, ne zaman izleyiciyi kaybeder?",
        "Kısa video üreticileri için AcarTechs, model vitrini değil; ses, süre ve telif süzgeci yazar.",
        "5 saniyelik vitrin karesi, 40 saniyelik yayın ritmini kanıtlamaz.",
        "Görsel üreticiler videoya kaydı. Kesitler parlak, el ve yazı hâlâ bozuktur. AcarTechs, bu araçları ‘film stüdyosu’ diye yazmaz. Kısa döngü, arka plan B-roll ve fikir taslağı için işe yarar. Ana anlatı ve yüz sürekliliği hâlâ pahalı emektir.",
        "Telif: modelin eğitim verisi, müziğiniz ve marka yüzünüz ayrı risklerdir. Müşteri filminde izinsiz yüz ve logo, ‘hızlı içerik’ faturasını hukuka çevirir.",
        "Üretici için pratik sınır",
        "İlk 3 saniyede okunmayan yazı, Reels/TikTok’ta ölür. Yapay zekâ videosunda yazı ve parmak sayısı sık bozulur; metni sonradan kaplayın. Ses, görüntüden daha ucuz ve daha inandırıcıdır: kendi sesiniz + sade B-roll, tam sentetik karakterden az risklidir.",
        "Ajanslar ‘sınırsız video’ satarken revizyon hakkını saklar. Prompt’u 40 kez döndürmek, çekim gününden uzun sürebilir. Araç, senaryosu net 15 saniyede parlar; belirsiz 3 dakikada dağılır.",
        ["Yüz ve logo izni olmadan müşteri filmi yapmayın", "Yazıyı modele bırakmayın", "5 saniyelik vitrini 40 saniyeye uzatmadan yayınlamayın"],
        "Yapay zekâ video, taslak ve dolgu aracıdır. Yönetmen koltuğu henüz kiralık değildir.",
    ),
    "yerli-girisimler-yapay-zeka-destekli-cozumler-gelistiriyor": g(
        "Yerli yapay zekâ girişimi: müşteri hangi soruyu sormalı?",
        "‘Yapay zekâlı’ etiketini AcarTechs demo değil; veri yeri, insan onayı ve çıkış kapısı olarak okur.",
        "Yerli olmak, verinin Türkiye’de kaldığı anlamına gelmez.",
        "Girişim haberleri ‘yerli ve millî model’ diye akar. Alıcı tarafında üç soru yeterlidir: veri nerede duruyor, model hata yapınca kim imzalıyor, sözleşmeyi iptal edince veri geri geliyor mu? AcarTechs, duyurudaki isim listesini tekrar etmez.",
        "Kamu ve sağlık komşuluğundaki işlerde dil desteği ve sunucu konumu pazarlama değil şartnamedir. Perakendede ise ‘chatbot’ çoğu zaman SSS sayfasının pahalı halidir.",
        "Alıcı kontrolü",
        "Demo, sizin gerçek fatura PDF’inizle çalışsın; stüdyo verisiyle değil. İnsan onayı olmayan otomatik e-posta, müşteri kaybettirir. Fiyat, token değil koltuk ve destek saatiyle konuşulsun. Çıkış: CSV/JSON dump 7 günde gelmiyorsa kilitlenirsiniz.",
        "Kurucu için: ilk müşteri referansı, slayttaki ‘büyük model’ cümlesinden değerlidir. Modelin kimin API’si olduğu şeffaf değilse, yerli katman yalnızca arayüz olabilir.",
        ["Veri bölgesini sözleşmeye yazın", "Hata sorumlusu insan olsun", "İptalde veri iadesi madde olsun"],
        "Yerli girişim, sorunu yerelde çözerse değerlidir. Etiket, çözüm değildir.",
    ),
    "bilim-kurgu-filmi-ilk-fragmaniyla-dikkat-cekti": g(
        "Fragman nasıl okunur: bilim kurgu vaadi ve montaj hilesi",
        "İlk fragmanı AcarTechs spoiler ezberi değil; ton, bütçe ipucu ve tarih süzgeci olarak okur.",
        "90 saniyelik kesit, 130 dakikalık ritmi kanıtlamaz.",
        "Bilim kurgu fragmanları efektle konuşur. Seyirci, ‘görüntü geldi’ diye takvime yazar. AcarTechs, fragmanı üç katmanda okur: ton (korku, macera, politika), yüz (yıldız mı fikir mi satılıyor) ve tarih (yıl mı mevsim mi).",
        "Erken fragman, henüz kurgusu bitmemiş sahneler taşıyabilir. Renk ve ses son hali değildir. ‘İlk bakış’ ile ‘nihai fragman’ aynı ürün değildir.",
        "Seyirci için",
        "Fragmanı iki kez izleyin: birinde ses kapalı, birinde açık. Ses kapalı kompozisyon, açıkken müzik hilesini ele verir. Çıkış tarihi pencereyse bilet parasını ön satışa bağlamayın. Benzer filmle kıyas ‘aynı yönetmen’ cümlesine sıkışmasın; çekim ölçeği değişmiş olabilir.",
        "Çocuk profilinde bilim kurgu, korku eşiği için yaş etiketine bakılmadan açılmamalıdır. Fragman yaş sınırı, filmin sınırı olmayabilir.",
        ["Tarih pencereyse takvime ‘belirsiz’ yazın", "Efekt karesini hikâye sanmayın", "İkinci fragmanı bekleyin"],
        "Fragman, davettir. Sözleşme değildir.",
    ),
    "yeni-film-ve-dizi-takvimi-izleyiciler-icin-hareketli-geciyor": g(
        "Yayın takvimini sadeleştirme: bu ay ne izlenir?",
        "Netflix, Prime ve yerli platform listelerini AcarTechs yığın değil, 2 başlık kuralıyla okur.",
        "Aynı hafta 12 prömiyer, sizin 6 saatinizi 12’ye bölmez.",
        "Yaz ve sonbahar takvimleri kalabalıktır. AcarTechs, ‘her şeyi tek sayfada topladık’ listesini yeniden dizmez. Evdeki gerçek süreye 2 film veya 1 dizi sığar. Üçüncü başlık istek listesidir.",
        "Platformlar aynı yapımı farklı haftalarda öne çıkarır. Top 10, zevkiniz değil, o ülkenin tıklamasıdır. Belgesel ve komedi, aynı akşam birbirini öldürür; türü ayırın.",
        "Ay planı",
        "Pazartesi: bu ay bitecek tek dizi seçin. Cuma: tek film. Çocuklu evde yaş etiketi ve bölüm süresi, ‘kritik beğeni’den önce gelir. Aboneliği yalnızca o ayın iki başlığı için açıp bitince kapatmak, yıl boyu tutmaktan ucuz olabilir.",
        "Spoiler başlıklı sosyal medya karesi, takvim zevkini çalar. Listeyi resmi uygulama sayfasından, kareyi değil başlığı okuyarak tutun.",
        ["Ayda 2 başlık", "Top 10’u zevk sanmayın", "Yaş etiketini fragmandan okuyun"],
        "Takvim haberi, sizin akşamınızı doldurmak zorunda değildir. Elemek, izlemektir.",
    ),
    "yapay-zeka-destekli-arama-motorlari-klasik-aramayi-zorluyor": g(
        "Yapay zekâ arama: ne zaman kaynak, ne zaman özet?",
        "AI arama kutusunu AcarTechs sihir değil; kaynak linki, tarih ve uydurma riski olarak okur.",
        "Akıcı cevap, doğrulanmış cevap değildir.",
        "Arama motorları artık link listesi yerine paragraf üretir. Hızlıdır. Kaynağı küçük yazar. AcarTechs, bu kutuyu ansiklopedi diye kullanmaz. Tarif, kod iskeleti ve ‘şu terim ne’ için işe yarar. Hukuk, sağlık ve güncel fiyat için asıl sayfaya gidilir.",
        "Model, emin duruşla eski tarihi birleştirebilir. ‘2024’te kalktı’ dediği özellik 2026’da geri gelmiş olabilir. Tarih ve resmi belge yoksa özet, taslaktır.",
        "Nasıl kullanılır?",
        "Cevabın altındaki linklere tıklayın. İki kaynak çelişiyorsa üçüncüyü açın. Alıntı istenen işte (ödev, haber, müşteri notu) yapay zekâ cümlesini olduğu gibi yapıştırmayın. Gizlilik: şirket içi metni tüketici arama kutusuna yapıştırmayın.",
        "Klasik arama, nadir hata kodu ve uzun PDF için hâlâ daha iyidir. Yapay zekâ arama, konuya girişte dakikayı kısaltır; dipnotu silmez.",
        ["Tarihi resmi sayfadan doğrulayın", "Sağlık/hukuk özetini karar sanmayın", "Şirket metnini kutusuna yapıştırmayın"],
        "Yeni arama, daha az tıklama vaat eder. Sorumluluk hâlâ tıklayanındır.",
    ),
    "api-kullaniminda-hiz-ve-guvenilirlik-neden-onemli": g(
        "API seçimi: gecikme, kota ve hata bütçesi",
        "Geliştirici için AcarTechs, ‘hızlı API’ reklamını p95 gecikme, kota ve kesinti günlüğüyle okur.",
        "Demo milisaniyesi, fatura günündeki p95 değildir.",
        "API haberleri yeni uç nokta ve ‘daha hızlı bölge’ ile gelir. Üretimde sizi yoran, mutlu yol değil; 429, 5xx ve 1.8 saniyelik kuyruktur. AcarTechs, entegrasyon kararını üç sayıya bağlar: p95 gecikme, aylık kota, hata bütçesi.",
        "Tek bölge, sizin kullanıcılarınızın uzağındaysa ilk bayt (TTFB) şişer. Yeniden deneme (retry) körse, kesintide kendi kendinizi DDoS’larsınız. Gizli anahtar mobil uygulamada ise kota başkasının olur.",
        "Sözleşmeden önce",
        "Statü sayfası ve geçmiş 90 gün kesinti. SLA cümlesi değil, kredi nasıl işliyor. Webhook imzası ve idempotency anahtarı var mı? Yoksa çift tahsilat sizde kalır. Fiyat, ‘bin istek’ değil, sizin gerçek tepe saatinizle çarpılmalıdır.",
        "Küçük ekip için yönetilen kuyruk, kendi retry yazmaktan ucuzdur. Büyük ekip için çok sağlayıcı, tek sağlayıcı indiriminden daha az uykusuzluk verebilir.",
        ["Anahtarı istemciye gömmeyin", "p95 ölçün, ortalamayı değil", "Retry’e jitter koyun"],
        "API, slayttaki milisaniye değil; fatura günündeki hata yüzdesidir.",
    ),
    "elektrikli-araclarda-sarj-altyapisi-rekabeti-hizlandi": g(
        "Elektrikli araç şarjı: ev, iş, yol üçgeni",
        "İstasyon duyurusunu AcarTechs etiket fiyatı değil; ev prizi, iş yeri ve yol koridoru olarak okur.",
        "Yoldaki 350 kW pano, sizin binanızdaki 11 kW kadar günlük değildir.",
        "Şarj haberleri istasyon sayısıyla konuşur. Sürücü günü ise evde gece, işte 8 saat ve ayda iki kez yol koridorudur. AcarTechs, ‘altyapı yarışı’nı bu üçgene böler.",
        "Apartmanda priz yoksa, hızlı istasyon kahraman değil zorunluluktur. İş yeri 11–22 kW veriyorsa, ev yatırımı ertelenebilir. Yol: koridor yoğunluğu, ödeme uygulaması ve arızalı soket oranı, kW sayısından önemlidir.",
        "Alıcı için",
        "Batarya boyutu, evde 7 kW ile geceyi doldurur mu? Soğuk hava ve otoyol, katalog menzilini %20–30 kesebilir. İkinci el elektrikli, şarj geçmişi ve batarya raporu olmadan ‘ucuz kilometre’ değildir.",
        "Şehir içi ikinci araç için küçük batarya + ev prizi, büyük batarya + istasyon kuyruğundan sakin bir hayattır. Taksi ve uzun yol, tersi.",
        ["Apartman yönetimine priz sormadan sipariş vermeyin", "Yol uygulamasını indirmeden ilk otoyola çıkmayın", "Soğukta menzil vaadine %20 koyun"],
        "Şarj altyapısı, panodaki kW değil; sizin gecenizin prizidir.",
    ),
    "ekran-teknolojilerinde-parlaklik-ve-enerji-verimliligi-yarisi": g(
        "Ekran parlaklığı: nit, HDR ve elektrik faturası",
        "TV ve monitör nit savaşını AcarTechs vitrin değil; oda ışığı, HDR ve watt olarak okur.",
        "2000 nit, perdeli odada göz yorar; güneşli salonda işe yarar.",
        "Üreticiler her yıl daha parlak panel açıklar. Mağaza ışığı, evdeki akşam lambasından farklıdır. AcarTechs, nit sayısını oda ve içerikle çarpar. HDR içerik yoksa parlaklık yarışı, logo ve menü yakıcılığıdır.",
        "OLED, karanlık sahnede siyahı; Mini-LED, gündüz salonunda parlaklığı tutar. İkisi de ‘en iyi’ değildir. Oyun monitöründe 1 ms ve Hz, HDR’dan önce gelebilir.",
        "Seçerken",
        "Oturduğunuz yerden pencereye bakış. Yansıma, nit kadar şikâyettir. Mat ekran, parlak film karesinden vazgeçirir ama ofiste okunur. Otomatik parlaklık, gece elektrik ve OLED iz bırakmayı azaltır; kapatıp 100’e kilitlemek paneli yer.",
        "TV’yi vitrin modunda almayın. Mağaza ‘canlı’ profili, evde abartılıdır. Film için film, oyun için oyun profili; tek ‘dinamik’ profil her ikisini de bozar.",
        ["Odayı akşam ziyaret edin", "HDR içerik yoksa nit’e prim vermeyin", "Vitrin modunu evde kapatın"],
        "Parlaklık, odanıza göre bir araçtır. Katalog rekoru değildir.",
    ),
    "gorsel-uretme-araclari-tasarim-surecini-degistiriyor": g(
        "Görsel üretici: taslak, kapak, yasak bölge",
        "Görsel yapay zekâyı AcarTechs ‘tasarımcı öldü’ diye değil; moodboard, kapak ve telif sınırı olarak kullanır.",
        "İyi prompt, marka kılavuzunun yerine geçmez.",
        "Görsel araçlar moodboard’u dakikaya indirdi. Müşteri sunumunda ‘yön bu’ demek kolaylaştı. Baskı dosyası, ambalaj dieline ve yüz sürekliliği hâlâ insan işidir. AcarTechs, aracı taslak katmanında tutar.",
        "Telif ve benzerlik: ünlü yüz, korunan karakter ve rakip logo, ‘ilham’ diye geçmez. Stok fotoğrafı tamamen bırakmak da şart değildir; hakki temiz bir stok, belirsiz model çıktısından az risklidir.",
        "İş akışı",
        "1) Metin brief. 2) 8–12 taslak. 3) İnsanın 2 taneyi düzeltmesi. 4) Tipografi ve gerçek ürün fotoğrafı. Modeli son kareye kadar zorlamak, 3D ve çekimden uzun sürebilir. Kapak görseli için 1:1 ve 16:9’u ayrı üretin; kırpmak yüzü yer.",
        "Ekip içinde ‘bu görseli kim onayladı?’ yoksa, gece yayını markayı yakar. Onay kutusunu araç değil editör işaretler.",
        ["Yüz ve logo izni", "Taslağı son ürün sanmayın", "Tipografiyi modele bırakmayın"],
        "Görsel üretici, moodboard motorudur. Sanat yönetmeni koltuğuna oturmaz.",
    ),
    "kult-serinin-devam-filmi-icin-hazirliklar-basladi": g(
        "Devam filmi haberi: ne zaman heyecan, ne zaman bekleyiş?",
        "‘Hazırlık başladı’ cümlesini AcarTechs çekim, kadro ve tarih netleşmeden bütçeye yazmaz.",
        "Geliştirme, çekim değildir; çekim, vizyon tarihi değildir.",
        "Kült seri haberleri, stüdyo ‘üzerinde çalışıyoruz’ deyince patlar. AcarTechs bu cümleyi üç mertebede okur: geliştirme, çekim, vizyon. Birinci mertebede bilet ve merch parası bağlanmaz.",
        "Kadro sızıntısı, anlaşma değildir. Yönetmen değişimi, tonu sıfırlar. Devam filmi, ilk filmin hayranını incitmeden yeni izleyici almak zorundadır; bu gerilim fragmandan önce senaryoda çözülür.",
        "Hayran için",
        "Resmi hesap ve sendika çekim bildirimi yoksa ‘hazırlık’ bir yıl sürebilir. Kitap uyarlamasında yazarın adı yeşil ışık değildir. Çocukluk serisinde nostalji, 2026 izleyicisinin temposuna uymayabilir; ilk 10 dakikalık sızıntıyı tüm film sanmayın.",
        "Ön satış, vizyon yılı netleşmeden açılırsa stüdyo nakit ister, siz tarih kilitlersiniz. Tarih kayarsa takvim ve otel iptali sizin riskinizdir.",
        ["Mertebe: geliştirme / çekim / vizyon", "Kadro sızıntısını anlaşma sanmayın", "Ön satışı yıl netleşmeden bağlamayın"],
        "Devam filmi haberi, anıdır. Bilet, tarihtir.",
    ),
    "yayin-platformlari-yaz-kataloglarini-guncelliyor": g(
        "Yaz katalogları: hangi abonelik bu ay açılır?",
        "Platform yaz listesini AcarTechs yığın değil; 30 günlük izleme bütçesi olarak okur.",
        "Aynı yaz, üç platformun ‘en iyi yazı’ olamaz.",
        "Yazın her servis kendi takvimini şişirir. AcarTechs, üç aboneliği birden tutmayı ancak tatilde günde 3 saat izleyen ev için makul görür. Diğerleri için ayın yıldızı hangisindeyse o açılır, ay bitince kapanır.",
        "Çocuklu evde yaz, animasyon ve aile filmidir; yetişkin dizi listesi ikinci plandadır. Spor yazı, dizi yazından ayrı faturadır.",
        "30 gün kuralı",
        "Ayın 1’i: bu ay bitecek tek dizi veya 3 film yazın. Ayın 25’i: bitmediyse uzatmayın, gelecek aya kaydırın. İndirimli yıllık, yazın üç aylık yoğunluğu için pahalı bir kilit olabilir.",
        "Offline indirme, köy ve uçak için katalogdan önemlidir. İndirme hakkı kısıtlı hesap, ‘yaz kataloğu zengin’ olsa da yolda işe yaramaz.",
        ["Ayda tek platform", "Çocuk listesini ayrı tutun", "Yıllık taahhüdü yaz indirimine bağmayın"],
        "Yaz kataloğu, sizin 30 gününüzdür. Stüdyonun vitrini değildir.",
    ),
    "teknoloji-gundeminde-bugun-one-cikan-basliklar": g(
        "Teknoloji gündemini süzme: üç başlık kuralı",
        "AcarTechs, ‘bugün öne çıkan her şey’ listesini yeniden dizmez; okura üç başlık bırakır.",
        "20 maddelik özet, hiçbiri okunmayan özetdir.",
        "Teknoloji günü, beş duyuru ve üç sızıntıyla dolar. Hepini aktarmak, kopya envanter üretir. AcarTechs’in günlük süzgeci: 1) sizin cihazınızı veya faturanızı değiştiren, 2) resmi kaynağı olan, 3) bu hafta karar isteyen.",
        "Sızıntı, stok fotoğrafı ve ‘olabilir’ fiili üçüncü kova değildir. Onlar istek listesidir.",
        "Okur rutini",
        "Sabah 8 dakika: resmi blog + bir analiz. Öğle: sızıntı yok. Akşam: yarın karar vereceğiniz tek başlık. Bu ritim, 40 sekmeli ‘gündem’den daha az kaygı üretir.",
        "Yatırımcı ve geliştirici aynı gündemi okumaz. Geliştirici API ve kota, tüketici fiyat ve tarih, yönetici risk ve uyum bakar. Aynı cümle üçüne hizmet etmez; bu yüzden AcarTechs kime yazdığını başta söyler.",
        ["Kaynağı resmi olmayanı güne yazmayın", "Sızıntıyı takvime işlemeyin", "Günde 3 başlık"],
        "Gündem, her şeyi bilmek değil; yarın neyi değiştireceğinizi bilmektir.",
    ),
    "verimlilik-uygulamalari-gunluk-planlamayi-kolaylastiriyor": g(
        "Görev uygulaması: bir tane seçin, gerisini kapatın",
        "Not, takvim ve kanban araçlarını AcarTechs özellik yarışı değil, tek sistem kuralıyla okur.",
        "Beş uygulama, hiçbiri güncellenmeyen listedir.",
        "Verimlilik uygulamaları her yıl yeni görünüm çıkarır. Sorun uygulama değil, listenin üç yerde durmasıdır. AcarTechs, ‘ekip çalışmasını kolaylaştırır’ cümlesini tek kaynak kuralına bağlar: görevler bir yerde, takvim bir yerde, dosya bir yerde.",
        "Kişisel işte basit liste yeter. 5 kişilik ekipte durum alanı (yapılacak/yapılıyor/bitti) olmadan sohbet dağılır. 30 kişide ise aracın kendisi proje olur; o ölçek bu yazının dışı.",
        "Geçiş",
        "Mevcut listeyi 30 dakika içinde yeni araca taşıyamıyorsanız araç ağırdır. Bildirimleri sessize alın; her onay maili, planı böler. Haftalık 15 dakikalık temizlik (bitenleri arşiv) yoksa kanban mezarlığıdır.",
        "Öğrenci için ders + teslim tarihi, iş için müşteri + son gün. İkisini aynı tahtada karıştırmak, akşamı işe çevirir.",
        ["Tek görev kaynağı", "Bildirimleri budayın", "Cuma 15 dakika arşiv"],
        "Verimlilik uygulaması, sizi planlamaz. Siz uygulamayı planlarsınız.",
    ),
    "yapay-zeka-araclari-is-dunyasinda-yeni-verimlilik-donemi-baslatti": g(
        "İşyerinde yapay zekâ: taslak hızı, onay yavaşlığı",
        "Kurumsal yapay zekâ vaadini AcarTechs ‘ajan’ slaytı değil; taslak, gizlilik ve insan onayı olarak okur.",
        "İlk taslak 10 dakikaya iner; hukuki onay hâlâ 10 gündür.",
        "İş dünyası haberleri her modeli ‘verimlilik devrimi’ diye yazar. Masada görülen: e-posta taslağı, toplantı özeti, kod iskeleti hızlanır. Karar, müşteri taahhüdü ve rakamın doğruluğu hızlanmaz. AcarTechs, bu ayrımı yazmayan metni kopya sayar.",
        "Gizlilik: müşteri sözleşmesini tüketici modeline yapıştırmak, NDA ihlalidir. Şirket kirası, kayıt kapatma ve bölgesel sunucu yoksa ‘herkesin ChatGPT’si’ resmi politika olamaz.",
        "İlk 30 gün",
        "İzinli araç, izinli veri, insan onayı. Pazarlama taslağı evet; fiyat teklifi ve sağlık/hukuk hayır. Ölçüm: taslak süresi düştü mü, revizyon sayısı arttı mı? İkincisi arttıysa model, stajyer gibi her cümleyi yeniden yazdırıyordur.",
        "Yönetici için eğitim, lisans kadar önemlidir. ‘Kullanın’ demek, gizli veriyi modele dökmeye davettir.",
        ["Müşteri metnini tüketici modele yapıştırmayın", "Onaysız gönderim yok", "Taslak süresini ve revizyonu birlikte ölçün"],
        "Verimlilik, dakikayı kısaltmaktır. Sorumluluğu kısaltmaz.",
    ),
    "teknoloji-alisverisinde-garanti-ve-servis-destegi-neden-onemli": g(
        "Teknoloji alışverişinde garanti: kutu fiyatından önce",
        "Kampanya fiyatını AcarTechs servis ağı, fatura ve ithalatçı üzerinden okur.",
        "İki yıl garanti yazısı, kapıdaki yetkili servis yoksa kâğıttır.",
        "İndirim dönemleri, aynı modeli 1500 TL aşağıya çeker. Arıza günü, kargo, yedek parça ve ‘ithalatçı biz değiliz’ cümlesi o 1500’ü geri ister. AcarTechs, teknoloji alışverişini vitrin değil servis haritası olarak görür.",
        "Gri ithal, yurt dışı kutu ve pazar yeri satıcısı, resmi distribütörden ucuzdur. Ekran ve batarya arızasında fark, yeni cihaz fiyatına yaklaşır.",
        "Almadan",
        "Faturada unvan, IMEI/seri, yetkili servis listesi. Elden teslim ‘açılmamış kutu’ fotoğrafı, yasal kanıt değildir. Uzatılmış garanti, ekran çizigini kapsamıyorsa ayrı satılan cam kadar işe yaramaz.",
        "Laptop ve TV’de yerinde servis, kargo riskini keser. Kulaklıkta ise değiştirme (swap) politikası, tamirden değerlidir.",
        ["Distribütör ve servis ilini yazın", "Faturayı PDF saklayın", "Gri ithali ‘aynı kutu’ sanmayın"],
        "Kampanya, kasa anıdır. Garanti, 14. aydır.",
    ),
    "yeni-nesil-telefon-bataryalari-daha-uzun-omur-hedefliyor": g(
        "Telefon bataryası: mAh, şarj hızı ve 2 yıl sonrası",
        "Batarya haberini AcarTechs mAh rekoru değil; şarj döngüsü, ısı ve gece prizi olarak okur.",
        "6000 mAh, 120W ile her gün 100’e doluyorsa iki yıl sonra şişer.",
        "Üreticiler kapasite ve watt yarıştırır. Kullanıcı günü 1.5 şarj ve ılık arka kapaktır. AcarTechs, ‘uzun ömür’ü döngü ve ısıya bağlar. Hızlı şarj, dakikayı kurtarır; kimyayı yer.",
        "80–20 kuralı (gece 100’e kilitlememek) birçok telefonda yazılımla gelir. Kapalıysa, 85’te kesen priz veya yazılım alarmı işe yarar. Kılıf içinde 120W, ısı tuzağıdır.",
        "Alırken",
        "Ekran 120 Hz ve parlak HDR, bataryayı mAh’den hızlı yer. 60 Hz seçeneği, seyahatte bir saat kazandırır. Değiştirilebilir batarya yoksa, 24 ay sonrası takas fiyatı kararın parçasıdır.",
        "Soğuk kışta yüzde 1’den atlayan kapanma, kapasite değil yazılım kalibrasyonudur. Tam boşaltıp doldurmak eski ni-cad alışkanlığıdır; bugün işe yaramaz.",
        ["Gece 100’e kilitlemeyin", "Hızlı şarjı kılıfla birlikte yakmayın", "120 Hz’i dışarıda kısın"],
        "Batarya ömrü, watt tablosu değil; sizin gece prizi alışkanlığınızdır.",
    ),
    "egitimde-yapay-zeka-destekli-calisma-araclari-yayginlasiyor": g(
        "Öğrenci için yapay zekâ: açıklama evet, ödev hayır",
        "Eğitim araçlarını AcarTechs kopyala-yapıştır değil; kavram, kaynak ve sınav dürüstlüğü olarak okur.",
        "Cevabı yapıştırmak, öğrenmeyi kısaltmaz; yakalanma riskini kısaltır.",
        "Öğrenci araçları özet, quiz ve ‘adım adım çöz’ vaat eder. AcarTechs’in çizgisi: kavramı sordur, cevabı yazdırma. Öğretmenin politikası yoksa, araç varsayılanı öğrencilerin aleyhine işler.",
        "Kaynak uydurma, ödevde dipnot faciasıdır. Model emin duruşla olmayan makale uydurur. Her iddiayı gerçek makalede aramak, eski kütüphane refleksidir ve hâlâ geçerlidir.",
        "Doğru kullanım",
        "‘Bu paragrafı 15 yaş diline çevir’, ‘şu formülü neden böyle’ , ‘quiz sorusu üret, cevabı sonra göster’. Yanlış: ‘bitmiş ödev yaz’. Dil öğreniminde konuşma pratiği işe yarar; sınav yazısını modele yazdırmak, sınavda boş kalmaktır.",
        "Veli için: hesap okul mailiyle açılsın, sohbet geçmişi silinsin, kişisel fotoğraf yüklenmesin. Öğretmen için: politika cümlesi (nerede serbest, nerede yasak) ödev kâğıdında dursun.",
        ["Kaynağı gerçek makalede arayın", "Ödevi yazdırmayın, açıklattırın", "Okul politikasını kâğıda yazın"],
        "Eğitimde yapay zekâ, öğretmenin yerine geçmez. Çalışma arkadaşının tembel halidir; siz yönetmezseniz o yönetir.",
    ),
    "siber-guvenlik-yamalarini-geciktirmek-buyuk-risk-olusturuyor": g(
        "Yama disiplini: ev ve küçük ofis için 48 saat kuralı",
        "Kritik yama haberini AcarTechs korku dili değil; Windows, telefon ve yönlendirici sırası olarak yazar.",
        "‘Sonra bakarım’ , botnet’in en sevdiği cümledir.",
        "Yama duyuruları her salı dolar. Ev kullanıcısı ‘ben hedef değilim’ der. Tarayıcı, yönlendirici ve eski eklenti, hedef seçmez; tarar. AcarTechs, ev ve 10 kişilik ofis için 48 saat kuralı önerir: kritik yama, iki gün içinde.",
        "Windows, telefon OS, tarayıcı, VPN, yönlendirici firmware. Beşli, antivirüs slaytından daha çok iş görür. Yazıcı ve kamera firmware’i unutulur; onlar da ağdadır.",
        "Sıra",
        "Önce yedek (bulut veya disk). Sonra OS. Sonra tarayıcı. Yönlendiriciyi gece, çünkü kopabilir. Ofiste, yamayı herkese aynı anda basmak yerine 1 PC ile deneyin. Ransomware notu: yedek, aynı ağa bağlı NAS’ta tek kopyaysa yedek değildir.",
        "Eski Windows 10 cihaz, uzatılmış destek bitince yama almaz. O kutu, bankacılık ve iş maili için ayrı ağda tutulmalı veya emekli edilmelidir.",
        ["48 saat kuralı", "Yönlendirici şifresini değiştirin", "Yedek çevrimdışı bir kopya"],
        "Yama, kahramanlık değildir. Ertelemek, başkasının botnet’ine kira vermektir.",
    ),
    "acik-kaynak-projeler-teknoloji-dunyasinda-etkisini-artiriyor": g(
        "Açık kaynağı işte kullanmak: lisans, bakım, çatal",
        "Haftalık ‘öne çıkan kütüphane’ listesini AcarTechs yıldız sayısı değil; lisans ve bakıcı olarak okur.",
        "GitHub yıldızı, güvenlik denetimi değildir.",
        "Açık kaynak, faturayı düşürür ve kilidi azaltır. Bakımsız paket, faturayı güvenlik olayına çevirir. AcarTechs, ‘bu haftanın kütüphaneleri’ni ezberletmez. İşe alınacak pakette lisans (MIT/Apache/GPL), son commit, issue yanıtı ve tek bakıcı riski arar.",
        "GPL’nin copyleft’i, kapalı ürünü zorlar. MIT, atıf ister. Lisansı okumadan npm install, hukukun ‘bilmiyordum’ kabul etmediği yerdir.",
        "Ekip kuralı",
        "SBOM veya kilit dosyası (lockfile) olmadan ‘en son sürüm’ çekmeyin. Kritik yolda tek bakıcılı paket, çatal veya ticari destek planı olmadan girmesin. Katkı: issue şablonu ve davranış kuralları yoksa, sizin PR’ınız da havada kalır.",
        "Öğrenci için açık kaynak, portföydür; ama sırf yıldız için anlamsız commit spam’i, bakıcıyı yorar ve sizi kötü tanıtır.",
        ["Lisansı README’den önce LICENSE dosyasından okuyun", "Tek bakıcı riskini yazın", "Lockfile’ı commit edin"],
        "Açık kaynak, bedava iş gücü değildir. Bakımı paylaşılmazsa borçtur.",
    ),
    "donanim-pazarinda-fiyat-ve-performans-dengesi-degisiyor": g(
        "Donanım alırken fiyat/performans: watt, garanti, ikinci el",
        "Ekran kartı ve işlemci haberini AcarTechs vitrin FPS değil; güç kaynağı, kasa ve 24 ay olarak okur.",
        "Vitrindeki FPS, 650W eski PSU’da gelmez.",
        "Donanım fiyatları ayda savrulur. ‘En yeni’ almak, monitörünüz 1080p iken 4K kartına para gömmektir. AcarTechs, dengeyi monitör, watt ve garantiye bağlar.",
        "İkinci el kart, madencilik ve hayalet garanti taşır. Faturasız kutu, arızada sizin olur. Yeni kartta 3 fan, dar kasada ısınır ve kısılır; vitrin FPS’i düşer.",
        "Sıra",
        "Monitör Hz ve çözünürlük → hedef FPS → işlemci darboğazı → PSU watt ve 80+ → kasa hava. Bu sıra tersine çevrilirse, pahalı kart yavaş kalır. RAM, 32 GB 2026 oyun ve tarayıcı için yeni varsayılandır; 16 GB ‘idare’ dir.",
        "Ofis PC’sinde iGPU yeter; oyun sloganlı kasa israftır. Sessizlik isteyen evde fan sayısı, RGB’den önemlidir.",
        ["Önce monitör", "PSU’yu kartla birlikte hesaplayın", "Faturasız ikinci eli iş PC’sine koymayın"],
        "Fiyat/performans, slayttaki FPS değil; masadaki watt ve 24. aydır.",
    ),
    "ios-ve-android-arasindaki-farklar-kullanici-deneyiminde-belirginlesiyor": g(
        "iOS mu Android mi? 2026’da gerçek farklar",
        "AcarTechs platform savaşını din ve logo değil; yedek, yan yükleme, onarım ve aile üzerinden ayırır.",
        "İkisi de ‘daha akıcı’ iddiasındadır; sizin kırılım yedek ve uygulama mağazasıdır.",
        "iOS, güncelleme süresi ve ikinci el fiyatında hâlâ öndedir. Android, yan yükleme, varsayılan uygulama ve ucuz giriş cihazında esnektir. AcarTechs, ‘hangisi daha iyi’ cümlesini evdeki diğer cihazlara bağlar.",
        "Evde Mac ve iPad varsa iPhone az sürtünme üretir. Windows ve ucuz tablet varsa Android. İki kişi iki sistem, fotoğraf ve mesaj köprüsünü (Google Fotoğraflar veya iCloud) bilinçli kurmadan acıtır.",
        "Karar maddeleri",
        "Onarım: parça ve yetkili servis iliniz. Yan yükleme: APK ihtiyacınız var mı? Çocuk: aile paneli (Family Link / Ekran Süresi) hangisini gerçekten kullanacaksınız? Bankacılık: bazı uygulamalar eski Android sürümünü keser.",
        "Klasör ve dosya: Android hâlâ USB ile rahattır. iOS, paylaşımı uygulama içine iter. Ham fotoğraf çeken için bu fark, din farkı kadar büyüktür.",
        ["Ekosistemdeki diğer cihazı yazın", "Onarım ve ikinci el fiyatına bakın", "Aile kilidini denemeden almayın"],
        "Platform, kimlik değil; yedek, servis ve evdeki diğer kutudur.",
    ),
    "mini-pc-modelleri-ev-ve-ofis-kullanimi-icin-yayginlasiyor": g(
        "Mini PC: ev ofisi, medya, sessizlik",
        "Mini PC haberini AcarTechs ‘küçük kasa’ değil; watt, RAM tavanı ve ekran çıkışı olarak okur.",
        "Cep boyu kasa, oyun kulesinin watt’ını ve soğutmasını taşımaz.",
        "Mini PC, kuleyi salondan kaldırır. Ofis, dijital tabela ve hafif montaj için uygundur. AAA oyun ve 4K kurgu için çoğu model nefes darlığı çeker. AcarTechs, ‘yaygınlaşıyor’ cümlesini kullanım yerine bağlar.",
        "RAM lehimliyse 16 GB tavan, 2026 tarayıcı + toplantı için daralır. NVMe tek yuva, yedek disk koymaz. İki HDMI 4K 60 verir; 120 Hz oyun monitörü DisplayPort ister.",
        "Alırken",
        "Idle watt ve fan gürültüsü, salonda film için FPS’den önemlidir. VESA montajı, masayı boşaltır. Windows lisansı ‘Home’ mu, yoksa etiket mi? Ofiste BitLocker ve TPM yazıyor mu bakın.",
        "Ev sunucusu (NAS benzeri) için düşük watt 7/24 kâr eder. Oyun için mini PC, eGPU macerasına kayar; o noktada kule daha dürüsttür.",
        ["RAM lehimli mi, yuva mı?", "Idle watt", "Çıkışlar monitörünüzü tutuyor mu?"],
        "Mini PC, doğru işte sessiz kahraman; yanlış işte ısınan kutudur.",
    ),
    "telefon-alirken-dikkat-edilmesi-gereken-en-onemli-ozellikler": g(
        "Telefon alırken: ekran, batarya, güncelleme, servis",
        "AcarTechs kamera megapikselini dördüncü sıraya koyar; güncelleme ve servis önce gelir.",
        "Vitrin karesi, 24. aydaki yazılımı göstermez.",
        "Telefon vitrini kamera ve parlaklık satar. İkinci yıl sizi yoran; yama kesilmesi, şişen batarya ve servis kuyruğudur. AcarTechs sıralaması: güvenlik güncellemesi taahhüdü, batarya ve şarj, ekran okunabilirliği, servis, sonra kamera.",
        "120 Hz güzeldir, 60 Hz seçeneği yoksa gezi günü yer. IP derecesi, lavabo ve yağmur içindir; deniz suyu değildir. 5G, kapsama yoksa pil yer.",
        "Bütçe dilimleri",
        "Giriş: güncelleme 3 yıl + sağlam batarya. Orta: 5–7 yıl yama vaadi, yeterli kamera. Üst: ikinci el değeri ve tamir parçası. Gri ithal, kamera aynı, servis farklıdır.",
        "Elden satışta iCloud/Google hesap kilidi ve IMEI kayıt. ‘Açılmamış’ kutu, kayıtlı başka TC olabilir.",
        ["Yama yılını üretici sayfasından okuyun", "Servis ilini yazın", "IMEI’yi faturaya işletin"],
        "İyi telefon, vitrinde parlayan değil; üçüncü yılında hâlâ yama alan telefondur.",
    ),
    "yeni-nesil-dizustu-bilgisayarlar-daha-hafif-ve-guclu-geliyor": g(
        "Dizüstü seçimi: watt, ekran, tamir, ağırlık",
        "İnce-hafif vaadini AcarTechs şarj aleti, klavye ve RAM tavanıyla tartar.",
        "1.1 kg gövde, 400 gram tuğla adaptörle çantada 1.5 kg’dır.",
        "Üreticiler her yıl daha ince metal ve daha yüksek TDP açıklar. İnce kasa, 28W üstünü kısa süre tutar; sonra kısılır. AcarTechs, ‘güçlü ve hafif’ cümlesini 30 dakikalık Cinebench değil, 2 saatlik toplantı + tarayıcı ısısıyla okur.",
        "RAM lehimli 16 GB, 2026’da tavan olabilir. SSD tek yuva, yedek koymaz. Ekran 16:10 ofiste, 16:9 filmde; dokunmatik, yansıma ve pil yer.",
        "Kim hangi kasa?",
        "Öğrenci: 1.4 kg altı, 13 saat iddia değil 8 saat gerçek, iyi klavye. Ofis: HDMI, USB-A ve servis. Üretim: soğutma ve 32 GB. Oyun ince kasa, gürültü ve 90 dakika pildir.",
        "Garanti yerinde mi, kargo mı? Menteşe ve klavye, ince kasada ilk kırılanlardır; tamir fiyatını sorun.",
        ["Adaptör ağırlığını tartın", "RAM lehimliyse 32 GB düşünün", "Menteşe tamir fiyatı"],
        "Hafif dizüstü, çantadaki toplam gram ve 2. saatteki fan ile ölçülür.",
    ),
    "windows-pc-kullanicilari-icin-performans-ipuclari": g(
        "Windows’ta yavaşlık: başlangıç, disk, ısınma",
        "AcarTechs ‘bilgisayarı hızlandıran 20 numara’ listesi yazmaz; üç gerçek nedeni ayıklır.",
        "Tema ve ‘oyun modu’, dolu diski ve tozlu fanı düzeltmez.",
        "Windows şikâyeti çoğu evde üç yerden gelir: açılışta 30 program, disk %90 dolu, laptop 90 derece. AcarTechs, kayıt defteri ‘temizleyicisi’ önermez. O yazılımlar, yedek almadan siler.",
        "Başlangıç uygulamalarını Görev Yöneticisi’nden ayıklayın. Depolama %20 boş olsun. Güç planı ‘dengeli’; ‘en iyi performans’ fanı ve ısısıyla kısılır. Sürücü, Windows Update + üretici sitesi; rastgele paket sitesi değil.",
        "Ne zaman donanım?",
        "HDD hâlâ sistem diskine SSD, en büyük tek sıçramadır. 8 GB RAM 2026’da yetmez. 16 GB ofis, 32 GB tarayıcı+VM. GPU, 1080p monitör yoksa acil değildir.",
        "Malware: tarayıcı ana sayfası kaçtıysa reset ve Defender taraması. ‘Temizleyici’ indirmek, ikinci zararlıdır.",
        ["Başlangıcı ayıkla", "Diskte %20 boşluk", "Kayıt temizleyici yok"],
        "Hız, sihirli ayar değil; açılış, boş disk ve nefes alan kasadır.",
    ),
    "ofis-bilgisayari-alirken-nelere-dikkat-edilmeli": g(
        "Ofis bilgisayarı: sessizlik, port, yönetim, gürültü",
        "AcarTechs ofis PC’sini oyun kasa vitrininden ayırır; TPM, garanti ve fan öne çıkar.",
        "RGB kasa, muhasebe masasında gürültü ve toz üretir.",
        "Ofis alımı, FPS slaytıyla yapılmaz. Gerekler: iki ekran çıkışı, TPM 2.0, BitLocker, 3 yıl yerinde servis, sessiz fan. AcarTechs, ‘iş istasyonu’ etiketini gerçek CPU/RAM ihtiyacına bağlar.",
        "iGPU, ofis ve 1080p video için yeter. CAD ve 4K kurgu ayrı listedir. Mini kasa, yer kazandırır; genişleme ve toz temizliği zorlaşır.",
        "Toplu alım",
        "Aynı model, aynı BIOS, aynı imaj. Karışık kasa, yardım masasını öldürür. Lisans: OEM Windows, cihazla ölür; iş değişince kutu lisansı ayrı konuşulur. Yedek parça: 20 cihazlık ofiste 1 yedek PSU ve 1 SSD, bir günlük duruşu keser.",
        "Çalışan dizüstü istiyorsa, ofis mini PC + paylaşılan monitör hibriti, herkese 4K oyun laptopu dağıtmaktan ucuzdur.",
        ["TPM ve 3 yıl yerinde servis", "İki ekran çıkışı", "Sessiz kasa, RGB değil"],
        "Ofis bilgisayarı, vitrin değil; sessiz, yönetilir ve 36. ayda hâlâ açılır.",
    ),
    "katlanabilir-telefonlarda-2026-rekabeti-hizlandi": g(
        "Katlanabilir telefon: menteşe, yazılım, tamir faturası",
        "Unpacked ve vitrin katlanırlarını AcarTechs menteşe ömrü, uygulama uyumu ve cam fiyatıyla okur.",
        "Açık ekran büyüktür; kapalı dış ekran küçük ve yazılım yarım kalabilir.",
        "2026 katlanır yarışı, ince menteşe ve daha parlak iç panel üzerine kurulur. Kullanıcı günü: cepte kalınlık, açıkken uygulama ikiye bölünme, düşmede iç cam. AcarTechs, ‘yeni dönem’ cümlesini tamir fiyatına bağlar.",
        "İç ekran koruyucusu ev tipi cam değildir. Toz, menteşede birikir. Uygulamalar hâlâ üst-alt reklam ve video için tam katlanır düzen vermeyebilir.",
        "Kime?",
        "Not ve PDF okuyan, tableti sevmeyen kişiye iç ekran işe yarar. Tek elle yazan ve tek cep isteyen kişiye klasik kayrak daha az pişmanlıktır. İkinci cihaz olarak katlanır, birincil telefon olarak katlanırdan az risklidir.",
        "Garanti menteşeyi kapsıyor mu, düşme iç cami kapsıyor mu ayrı maddelerdir. Sigorta primi, kasa farkını iki yılda yer.",
        ["İç cam tamir fiyatını sorun", "Uygulamayı açık-kapalı deneyin", "Tozlu ortamda menteşe riski"],
        "Katlanır, vitrinde gelecektir. Masada menteşe ve cam faturasıdır.",
    ),
    "android-telefonlarda-dosya-paylasimi-daha-kolay-hale-geliyor": g(
        "Android’de dosya gönderme: Nearby, USB, bulut",
        "Paylaşım haberini AcarTechs ‘AirDrop geldi’ sloganı değil; cihaz, ağ ve gizlilik olarak okur.",
        "Yakındaki cihaz, iki marka ve iki hesapta bazen birbirini görmez.",
        "Android paylaşımı yıllarca marka adlarıyla bölündü. Nearby Share / Quick Share birleşmeleri işi sadeleştirir. Yine de Wi-Fi, Bluetooth ve görünürlük ayarı kapalıysa sihir yoktur. AcarTechs, AirDrop cümlesini kopyalamaz; hangi yolun ne zaman kullanılacağını yazar.",
        "Kısa video ve PDF: yakındaki paylaşım. 4 GB ham video: kablo veya bilgisayar. Hassas sözleşme: kablosuz yayından çok USB veya şifreli kasa.",
        "Pratik",
        "Görünürlüğü ‘herkes’ yerine ‘kişilerim’ yapın. Misafir ağı, iki telefonu ayırabilir. iPhone’a gönderim hâlâ fotoğraf için en sorunsuz bulut veya kablo olabilir; zorlamak 20 dakika yer.",
        "İş telefonunda paylaşımı kapatmak, sızıntıyı keser. Ailede çocuk hesabı, ‘yakındaki herkes’ten dosya almamalıdır.",
        ["Görünürlük: kişilerim", "Büyük dosya kablo", "Hassas dosya herkese açık paylaşımda değil"],
        "Paylaşım kolaylığı, görünürlüğü ‘herkes’ yapmak zorunda değildir.",
    ),
    "airdrop-destegine-sahip-tum-android-telefonlar": g(
        "Android’de AirDrop benzeri paylaşım: hangi telefon, hangi ayar?",
        "Liste ezberi yerine Quick Share görünürlüğü, Google hesabı ve iPhone köprüsü.",
        "‘Destekli telefonlar’ tablosu, ayar kapalıysa boştur.",
        "Arama motoru, AirDrop yazınca Android listesi bekler. Gerçek, protokol adı ve üretici katmanıdır. AcarTechs, model ezberi yapmaz. Google hesabı, Bluetooth, konum izni ve ‘görünürlük’ kapalıysa hiçbir liste işe yaramaz.",
        "Eski cihaz, üretici arayüzünde özelliği farklı menüde saklar. İki Android, aynı Wi-Fi’de değilse keşif düşer.",
        "iPhone’a geçiş",
        "Fotoğraf için Google Fotoğraflar veya kablo hâlâ daha az kavga çıkarır. PDF için e-posta veya mesaj. Zorla ‘AirDrop gibi’ aramak, 15 dakikalık Bluetooth dansıdır.",
        "Toplantıda herkese görünür bırakmak, yabancı dosya davetidir. İş bitince kapatın.",
        ["Görünürlüğü toplantı bitince kapatın", "iPhone için ayrı köprü planlayın", "Konum izni keşif içindir, her zaman açık tutulmak zorunda değildir"],
        "AirDrop kelimesi arama tuzakıdır. Ayar ve hesap, model listesinden önce gelir.",
    ),
    "robot-supurge-modellerinde-haritalama-teknolojisi-gelisiyor": g(
        "Robot süpürge: harita, eşik, bakım maliyeti",
        "LIDAR ve ‘akıllı harita’ vaadini AcarTechs eşik yüksekliği, saç ve toz haznesi olarak okur.",
        "Güzel harita, 2 cm eşiği çıkamayan tekerleği kurtarmaz.",
        "Robot süpürge vitrini 3D ev haritası gösterir. Evde halı saçak, eşik, kablo ve uzun saç vardır. AcarTechs, ‘haritalama gelişiyor’ cümlesini üç teste bağlar: eşik, saç dolaması, haftalık bakım.",
        "LIDAR, karanlıkta duvarı görür; siyah halıda düşme sensörü şaşırabilir. Akıllı oda ayırımı, kapı eşiği fiziksel olarak geçilmiyorsa işe yaramaz.",
        "Alırken",
        "Toz istasyonu gürültüsü gece komşusudur. Filtre ve fırça fiyatını 24 aya yayın. Evde çok kablo varsa, robot değil dikey süpürge daha az küfür ettirir. Balkon ve ince halı, ayrı profil ister.",
        "Gizlilik: ev haritası üretici bulutuna gidiyorsa, kamera/mikrofonsuz model tercih edilebilir. Çocuk ve evcil hayvan için fırça kapağı ve düşme sensörü şarttır.",
        ["Eşik yüksekliğini ölçün", "Fırça yedek fiyatı", "Harita buluta gidiyor mu?"],
        "Robot, harita uygulaması değil; eşiği çıkan ve saçı dolamayan makinedir.",
    ),
    "ssd-fiyatlarindaki-degisim-bilgisayar-toplamayi-etkiliyor": g(
        "SSD alırken: TBW, DRAM, yedek, fiyat dalgası",
        "GB/TL haberini AcarTechs vitrin hızı değil; dayanım, ısı ve yedekleme olarak okur.",
        "7000 MB/s yazısı, kopyalanan 200 GB’lık arşivde ısınır ve düşer.",
        "SSD fiyatı ayda iner çıkar. ‘Bu hafta al’ paniği, TBW’si düşük QLC’yi sistem diskine koydurur. AcarTechs, sistem diski ile arşiv diskini ayırır. Sistem: daha iyi dayanım ve DRAM veya HMB’si dürüst model. Arşiv: kapasite, ısınma ve yedek.",
        "PCIe 5.0, soğutmasız 70 derecede kısılır. 4.0 iyi soğutmalı, günlük kopyada farkı hissettirmez.",
        "Pratik",
        "1 TB sistem, 2 TB oyun/medya. Tek 4 TB her şeyi koyup yedeksiz yaşamak, bir denetici hatasında her şeyi kaybetmektir. 3-2-1 yedek: 3 kopya, 2 ortam, 1 dışarıda.",
        "Laptop’ta tek yuva varsa, dışarıda 2 TB ucuz SSD yedek, içerideki ‘fırsat’ 4 TB’dan değerlidir.",
        ["TBW ve garanti yılını okuyun", "Sistem ile arşivi ayırın", "Hız rekoruna soğutmasız inanmayın"],
        "SSD fırsatı, yedeksiz kapasite değildir. Dayanım ve ikinci kopyadır.",
    ),
    "yazilim-testlerinde-otomasyon-kullanimi-artiyor": g(
        "Test otomasyonu: neyi otomatikleştirin, neyi elle bırakın?",
        "AcarTechs ‘otomasyon artıyor’ cümlesini araç listesi değil; kırılgan UI ve değerli yol olarak okur.",
        "Her tıklamayı kaydetmek, bakımı testten pahalı hale getirir.",
        "Ekipler her çeyrek yeni test aracı alır. Kırılan şey, giriş butonunun CSS sınıfıdır. AcarTechs, otomasyonu giriş, ödeme ve kayıt gibi para kaybettiren yola bağlar. Görsel ince ayar ve keşif testi elle kalır.",
        "Flaky (kırılgan) test, CI’yi yalancı çobana çevirir. Ekip kırmızıyı görmezden gelmeye başlar. O noktada otomasyon, güvenlik değil gürültüdür.",
        "İlk 10 test",
        "Giriş, şifre sıfırlama, ödeme mutlu yolu, stok bitişi, yetkisiz sayfa. Bitti. Renk ve animasyon sonra. Veri: gerçek kart değil, sahne ortamı. Gizlilik: üretim kopyasını testçilere açmayın.",
        "Küçük ekipte 10 sağlam test, 400 kırılgan kayıttan değerlidir. Araç değişimi, bu 10’u taşımıyorsa geçmeyin.",
        ["Para kaybettiren yolu otomatikleştirin", "Kırılgan testi silin veya düzeltin", "Üretim verisini teste kopyalamayın"],
        "Otomasyon, daha çok test değil; güvenilen az testtir.",
    ),
    "ses-klonlama-teknolojileri-icin-guvenlik-tartismasi": g(
        "Ses klonu: rıza, dolandırıcılık, ne yapılmaz?",
        "AcarTechs ses klonunu ‘eğlenceli demo’ diye yazmaz; rıza, banka ve aile çağrısı riskini merkeze alır.",
        "30 saniyelik örnek, annenizin sesiyle borç isteyebilir.",
        "Ses modelleri, kısa kayıttan konuşma üretir. Demo eğlencelidir. Dolandırıcılık da öyle. AcarTechs, teknolojiyi yasakçı dil olmadan, ev ve iş için kırmızı çizgiyle anlatır.",
        "Banka ve ‘oğlunuz kaza yaptı’ aramaları, ses benzerliğine yaslanır. Aile kod kelimesi (sadece sizin bildiğiniz bir soru) bu dalgaya karşı eski ve işe yarar bir yöntemdir.",
        "Ne yapılmaz?",
        "Çocuğun sesini herkese açık modele yüklemeyin. Çalışan sesini reklam için rızasız klonlamayın. ‘Bu ses yapay zekâdır’ etiketi, yasal olarak her yerde yeterli olmayabilir; kayıt ve yayın politikasını okuyun.",
        "Gazeteci ve içerik üreticisi için kaynak sesin lisansı, görsel telifi kadar ciddidir. Ünlü ses taklidi, platformdan silinme ve dava riskidir.",
        ["Aile kod kelimesi", "Çocuk sesini modele yüklemeyin", "Rızasız ticari klon yok"],
        "Ses klonu, mikrofonun ucuz halidir. Rıza yoksa dolandırıcılığın da ucuz halidir.",
    ),
    "yapay-zeka-iceriklerinde-guven-ve-dogrulama-daha-onemli-hale-geldi": g(
        "Yapay zekâ metnini doğrulama: üç kaynak kuralı",
        "AcarTechs, ‘güven önemli’ sloganı değil; tarih, birincil kaynak ve alıntı kontrolü yazar.",
        "Akıcı Türkçe, doğru Türkçe değildir.",
        "Model metinleri haber, ödev ve şirket bloguna sızdı. Okur, cümle duruşuna kanıyor. AcarTechs kendi yayınında da aynı kuralı tutar: sayı, tarih ve alıntı birincil kaynakta yoksa yazılmaz.",
        "Uydurma dipnot, akademik metinde yakılır. Haberde ‘uzmanlar’ öznesi, isim yoksa sisdir. Şirket blogunda rakip adı ve pazar payı, modelin ezberidir; resmi rapor gerekir.",
        "Üç adım",
        "1) İddiayı Google/Scholar/resmi PDF’de arayın. 2) Tarih uyuyor mu. 3) İkinci bağımsız kaynak. İkisi de yoksa taslak kalır, yayın olmaz. Alıntı tırnak içinde birebir ve sayfa numaralı olmalıdır.",
        "Okur için: ‘yapay zekâ ile yazıldı’ etiketi, doğrulamayı size bırakır; etiket, doğruluk sertifikası değildir.",
        ["Birincil kaynak", "Tarih", "İkinci kaynak"],
        "Güven, modelin özgüveni değil; sizin tıklamanızdır.",
    ),
    "yapay-zeka-etiketi-uygulamalarda-daha-gorunur-olacak": g(
        "Uygulamalarda yapay zekâ etiketi: ne işe yarar?",
        "Zorunlu etiketleme AcarTechs’e göre şeffaflıktır; kalite rozeti değildir.",
        "‘AI ile üretildi’ yazısı, içeriğin doğru olduğunu söylemez.",
        "Mağazalar ve platformlar yapay zekâ etiketini görünür kılıyor. Amaç, sentetik görüntü ve sesin reklam gibi durmasını azaltmak. AcarTechs, etiketi sansür değil uyarı etiketi olarak okur.",
        "Üretici etiket yapıştırmayı unutursa, okur yine üç kaynak kuralına döner. Etiket enflasyonu (‘her şey AI’) ise uyarıyı görünmez kılar.",
        "Geliştirici için",
        "Kullanıcı içeriği modele gidiyorsa bunu ayarlarda ve ilk çalışmada söyleyin. Çocuk uygulamasında etiket yetmez; veri gitmemelidir. Reklamda sentetik yüz, yerel mevzuata göre ek yükümlülük taşıyabilir.",
        "Okur için etiket, ‘daha dikkatli bak’ işaretidir. Kapatma tuşu değildir.",
        ["Etiket kalite rozeti değil", "Çocuk verisi gitmesin", "Sentetik reklamı ayrıca işaretleyin"],
        "Görünür etiket, dürüstlüktür. Doğruluk hâlâ sizin kontrolünüzdür.",
    ),
    "populer-uygulamada-arayuz-yenilemesi-basladi": g(
        "Uygulama arayüzü yenilenince ne yapılır?",
        "AcarTechs ‘yenilenen arayüz’ haberini menü kaybı, bildirim ve hesap kilidi kontrol listesine çevirir.",
        "Düğme yer değiştirdi diye özellik gitmiş sanılır; çoğu zaman menü taşınmıştır.",
        "Popüler uygulamalar yılda birkaç kez menü taşır. Sosyal medya öfke üretir, sonra alışılır. AcarTechs, isimsiz ‘popüler uygulama’ duyurusunu kopyalamaz. Yenileme sonrası 10 dakikalık kontrol yeter.",
        "Bildirim izni yeniden sorulabilir. Varsayılan herkese açık albüm geri gelebilir. Karanlık mod ve yazı boyutu sıfırlanabilir.",
        "Kontrol",
        "Ayarlar → gizlilik, bildirim, bağlı cihazlar. Yedek kodlar duruyor mu? Widget ve kısayol koptuysa, özellik silinmiş olmayabilir. İş profili (MDM) varsa, IT duyurusunu bekleyin; erken güncelleme şirket kilit politikasını bozar.",
        "Yaşlı ebeveyn için yenileme, ‘telefon bozuldu’ çağrısıdır. Büyük yazı ve eski menü yolu varsa gösterin; yoksa güncellemeyi bir hafta erteleyin.",
        ["Gizlilik ve bildirim", "Bağlı cihazlar", "Ebeveyn için bir hafta bekletme"],
        "Arayüz yenilemesi, ürünün sıfırlanması değildir. Ayarların tekrar bakılmasıdır.",
    ),
    "gelisim-ekipleri-icin-yeni-kodlama-araclari-tanitildi": g(
        "Yeni kod aracı: ekibe alma kontrol listesi",
        "AcarTechs ‘yeni IDE/ajan’ duyurusunu demo değil; lisans, veri çıkışı ve öğrenme maliyeti olarak okur.",
        "Haftalık yeni araç, tamamlanan işi artırmaz; bağlam değiştirmeyi artırır.",
        "Geliştirici araçları her ay yeni ajan, yeni sohbet, yeni panel çıkarır. Ekip her birini denerse, kimse aynı linter’da kalmaz. AcarTechs, aracı işe almak için üç kapı koyar: veri nereye gidiyor, lisans koltuk mu token mı, mevcut CI’yi kırıyor mu?",
        "Şirket kodunu tüketici modele yapıştırmak, NDA ve telif riskidir. Yerel model, GPU ister. Bulut ajan, depo erişimi ister; en az yetki (least privilege) yoksa fazla açarsınız.",
        "Deneme",
        "Bir ekip, bir depo, iki hafta. Metrik: PR süresi, geri dönüş, güvenlik uyarısı. ‘Daha eğlenceli’ metrik değildir. Öğrenme: kıdemli, aracı stajyere bırakmadan önce kural dosyasını (cursor/copilot rules) yazar.",
        "Küçük ekipte ikinci IDE, lisans ve eklenti dağınıklığıdır. Bir araçta kalıp kuralı sıkılaştırmak, her ay göçmekten hızlıdır.",
        ["Kod tüketici modele gitmesin", "İki haftalık tek depo denemesi", "En az yetki"],
        "Yeni araç, yeni iş değildir. Ölçülmeyen deneme, oyuncaktır.",
    ),
    "sarj-teknolojileri-daha-guvenli-ve-hizli-hale-geliyor": g(
        "Telefon şarjı: watt, kablo, ısınma, sahte kafa",
        "AcarTechs ‘daha güvenli ve hızlı’ sloganını kablo kesiti, kafa sertifikası ve yastık altı yasağına bağlar.",
        "120W, yastık altında ve sahte kabloda yangın senaryosudur.",
        "Şarj haberleri watt ve ‘akıllı koruma’ ile gelir. Evde kaza, watt değil; ezik kablo, sahte kafa ve battaniye altıdır. AcarTechs, protokol adlarını ezberletmez. Kablo kesiti, kafa ısısı ve gece prizi yeter.",
        "USB-PD, doğru konuşan kafa ve kablo ister. ‘Hızlı’ yazan sahte kablo, 20W’da ısınır. GaN kafa küçük ve sıcaktır; kapalı kutuda bırakılmaz.",
        "Alışkanlık",
        "Gece yastık altında telefon yok. 80–90’da kes. Islak elle ucuz uzatma yok. Arabada güneş altında kafa + telefon, bataryayı yer. Uçak: powerbank kapasitesi ve kabin kuralı, watt’tan önce gelir.",
        "İkinci el kafa, kabloyu yakar. Resmi veya bilinen sertifikalı kafa, 200 TL farkı yangından ucuzdur.",
        ["Sahte kablo yok", "Yastık altı yok", "Gece 100’e kilitleme"],
        "Güvenli şarj, yeni kimya değil; kablo, hava ve gece prizidir.",
    ),
    "kamera-odakli-akilli-telefonlar-sosyal-medya-kullanicilarini-hedefliyor": g(
        "Sosyal medya için telefon kamerası: ışık, renk, dosya",
        "Megapiksel savaşını AcarTechs gece ışığı, renk tutarlılığı ve ön kamera olarak okur.",
        "200 MP, 1080p Reels’te görünmez; gürültü görünür.",
        "Vitrin, ana kameranın megapikselini satar. Sosyal medya günü ön kamera, 10 lüks oda ve 15 saniyelik dikey videodur. AcarTechs, ‘kamera odaklı’ telefonu bu gerçekle tartar.",
        "Renk: her uygulama kendi filtrini basar. Telefonun ‘canlı’ profili, birleşince abartılır. LOG ve Pro, Reels için fazla; düz profil + sonradan hafif renk yeter.",
        "Alırken",
        "Ön kamerayı mağazada floresan altında deneyin. Gece ana kamera, f/1.8 ve yazılım gürültü azaltma. Optik 3x, dijital 10x’ten değerlidir. Video 4K 60, ısınma ve dosya boyutu üretir; 1080p 30 çoğu yayın için yeter.",
        "Depolama 128 GB, 4K ve WhatsApp ile dolar. 256 GB sosyal medya telefonunda ‘fazla’ değil varsayılandır.",
        ["Ön kamerayı mağazada deneyin", "Optik zoom", "128 GB’ı sosyal günde az sayın"],
        "Sosyal kamera, vitrin MP’si değil; sizin odanızdaki ışık ve ön kameradır.",
    ),
    "orta-segment-telefonlarda-fiyat-performans-yarisi-buyuyor": g(
        "Orta segment telefon: nerede para, nerede ödün?",
        "AcarTechs orta segmenti ‘flagship gibi’ diye yazmaz; güncelleme, ekran ve şarj ödünü listeler.",
        "Flagship kamerasının slaytı, orta segmentin gece fotoğrafı değildir.",
        "Orta segment, 2026’da 120 Hz ve 5G’yi standart yaptı. Ödün: yama süresi, telefoto, kutu içi kafa, cam ve titreşim motoru. AcarTechs, fiyat/performansı bu ödünlerle okur.",
        "İki yıl sonra yazılım kesilirse, ilk günkü ‘uygun fiyat’ pahalıya gelir. 4 yıl yama vaadi, 10 MP telefotodan değerlidir.",
        "Ödün tablosu",
        "Kabul: plastik çerçeve, yavaş telefoto, ortalama hoparlör. Kabul etme: 2 yıl yama, 128 GB, şişen 45W sahte kablo. Ekran PWM hassasiyeti, ofiste baş ağrısı yapar; mağazada yazı kaydırın.",
        "Gri ithal orta segment, serviste flagship’ten daha çok süründürür; parça azdır.",
        ["Yama yılını oku", "128 GB’ı geç", "PWM ve servis"],
        "Orta segment kazanır; yama ve depolama satılmazsa ikinci yılda kaybeder.",
    ),
    "laptoplarda-yapay-zeka-islemcileri-daha-fazla-kullanilacak": g(
        "Yapay zekâ işlemcili dizüstü: NPU kime lazım?",
        "AcarTechs NPU ve ‘AI PC’ etiketini Watt, RAM ve gerçek özellik listesiyle okur.",
        "NPU rozeti, 16 GB RAM tavanını kaldırmaz.",
        "Dizüstüler NPU TOPS yarıştırır. Windows’un bazı efektleri (bulanık arka plan, canlı altyazı) NPU’da ucuza çalışır. Büyük model, hâlâ RAM ve bazen GPU ister. AcarTechs, ‘AI PC’yi özellik listesinden okur; rozetten değil.",
        "16 GB lehimli RAM, yerel modeli ve tarayıcıyı bir arada boğar. 32 GB, 2026 AI PC için daha dürüst tabandır. Fanlı ince kasa, NPU ısısını değil CPU ısısını bağırır.",
        "Kime?",
        "Toplantı altyazısı ve bulanık arka plan: evet, NPU işe yarar. Yerel kod modeli ve görsel üretim: RAM ve soğutma. Sadece e-posta: NPU için prim ödemeyin.",
        "Gizlilik: ‘yerel AI’ yazısı, telemetrinin kapalı olduğu anlamına gelmez. Ayarları ilk günde kapatın.",
        ["RAM 32 GB düşünün", "Özellik listesi, TOPS değil", "Yerel yazısı telemetriyi kapatmaz"],
        "AI PC, rozet değil; RAM, watt ve kapatabildiğiniz telemetridir.",
    ),
    "sirketler-musteri-hizmetlerinde-yapay-zeka-asistanlarini-deniyor": g(
        "Müşteri hizmeti botu: ne zaman insan, ne zaman taslak?",
        "AcarTechs çağrı merkezi yapay zekâsını maliyet slaytı değil; kaçış tuşu ve yanlış bilgi riski olarak okur.",
        "Bot, iade ve öfke hattında espri yapmamalıdır.",
        "Şirketler bot ile ilk hattı ucuzlatır. Müşteri, 8 tuştan sonra insan ister. AcarTechs, botu SSS ve kargo takip için uygun; iptal, fatura itirazı ve sağlık/finans kararı için uygunsuz görür.",
        "Yanlış bilgi, ‘yapay zekâ uydurdu’ diye bitmez; şirket sözü sayılabilir. İnsan kaçış tuşu (0 veya ‘temsilci’) üçüncü cümlede görünmelidir.",
        "Kurulum",
        "Bot yalnızca onaylı SSS’den konuşsun. Güncel fiyat ve stok, canlı sistemden gelsin. Kayıt: müşteriye ‘kaydediliyor’ denilsin. Çalışan, bot özetini kör onaylamasın.",
        "Küçük işletmede WhatsApp hazır cevap, pahalı bottan dürüst olabilir. Ölçek, 50 tekrarlayan sorudan sonra konuşulur.",
        ["Kaçış tuşu görünsün", "İade ve öfkeyi insana verin", "Uydurma fiyat yok"],
        "Bot, kuyruğu kısaltır. Güveni kısaltmamalıdır.",
    ),
    "robotik-sistemlerde-yapay-zeka-kullanimi-genisliyor": g(
        "İşyerinde robot + yapay zekâ: güvenlik çemberi",
        "AcarTechs depo ve üretim robotunu demo videosu değil; çit, durdurma ve bakım olarak okur.",
        "Yumuşak demo, 400 kg’lık kolun yanındaki stajyer değildir.",
        "Robotik haberleri ‘yapay zekâ ile gördü, tuttu’ diye akar. Fabrikada ISO, acil durdurma ve bakım kilidi vardır. AcarTechs, slaytı çit ve prosedüre bağlar.",
        "Görüntü modeli hata yapınca kol duruyor mu, yoksa ‘emin’ olup devam mı ediyor? İkinci davranış, kaza raporudur.",
        "Alıcı",
        "Entegratör referansı, yedek parça süresi, gece vardiyası desteği. Yapay zekâ güncellemesi, doğrulama olmadan üretime basılmaz. İnsan-robot aynı hücredeyse hız ve kuvvet sınırları kâğıtta değil ölçümde durmalıdır.",
        "KOBİ için paletleme gibi tekrar iş, karmaşık ‘her şeyi gören kol’dan önce gelir. Kahve taşıyan lobi robotu, depo gerçeği değildir.",
        ["Acil durdurma testi", "Güncelleme doğrulama", "Hücre hız/kuvvet sınırı"],
        "Robotik yapay zekâ, video değildir. Durabildiği yerde zekâdır.",
    ),
    "mobil-uygulamalarda-yapay-zeka-destekli-yeni-donem-basladi": g(
        "Telefondaki yapay zekâ: hangi özellik yerelde kalır?",
        "AcarTechs mobil AI duyurusunu fotoğraf, klavye ve gizlilik ayarına indirger.",
        "‘Cihazda çalışır’ yazısı, her fotoğrafın buluta gitmediği anlamına gelmeyebilir.",
        "Telefonlar özet, silme, çeviri ve sesli asistanı ‘yeni dönem’ diye satar. AcarTechs, özelliği üç soruya bağlar: veri cihazdan çıkıyor mu, pil ve ısınma ne kadar, sonuç düzenlenebilir mi?",
        "Fotoğraf silme, buluta gidip geliyorsa albümünüz üreticide kopyalanır. Klavye önerisi, yazdığınız şifreyi öğrenmemelidir. Çeviri, çevrimdışı paket indirilmeden ‘yerel’ sayılmaz.",
        "Ayar",
        "İlk günde analitik ve bulut AI anahtarlarını okuyun. İş telefonunda kişisel asistanı kapatın. Çocuk hesabında sohbet asistanı varsayılan kapalı olsun.",
        "Pil: gece album tarama, şarjda ısınır. İstemiyorsanız zamanlanmış görevi kapatın.",
        ["Bulut anahtarını oku", "Şifre alanında AI klavye kapalı", "Çocukta asistan kapalı"],
        "Mobil yapay zekâ, kolaylıktır. Albüm ve şifre, kolaylıktan pahalıdır.",
    ),
    "bilgisayar-bakimi-performansi-nasil-etkiler": g(
        "Bilgisayar bakımı: toz, termal macun, kablo",
        "AcarTechs bakımı ‘hızlandırıcı yazılım’ değil; hava, macun ve kablo düzeni olarak yazar.",
        "Tozlu filtre, yeni RAM’den daha çok FPS yer.",
        "Ev PC’si yılda bir toz emer. Laptop vantilatörü, yatağın üzerinde tüy doldurur. AcarTechs, bakımın performans olduğunu; kayıt temizleyicinin olmadığını tekrar eder.",
        "Masaüstü: filtre, fan, GPU soğutucu. Laptop: serviste temizleme, evde vakum tehlikelidir (rulman). Termal macun 3–5 yıl; her yıl açmak menteşeyi yer.",
        "Kablo",
        "Ön panel kablosu emişi keser. RGB uzantı, toz tutar. Laptop’ta sert zemin; yorgan üstü 90 derecedir ve işlemci kısılır. Bu, ‘Windows bozuldu’ sanılır.",
        "Yedek: bakım günü, SSD kopyası alınmış olsun. Macun sürerken kısa devre, bakımdan pahalıdır; emin değilseniz servis.",
        ["Yılda bir toz", "Yorgan üstü laptop yok", "Kayıt temizleyici yok"],
        "Bakım, yeni ekran kartından ucuz FPS’tir.",
    ),
    "animasyon-dunyasinda-yeni-proje-duyuruldu": g(
        "Animasyon projesi haberi: stüdyo, hedef yaş, platform",
        "AcarTechs ‘yeni proje’ cümlesini fragman yokken takvime yazmaz; stüdyo, yaş ve yayın yeri arar.",
        "Duyuru posteri, bölüm sayısı ve tarih değildir.",
        "Animasyon haberleri konsept görselle patlar. Çekim canlı aksiyon gibi görünmez; yıllar sürebilir. AcarTechs, poster paylaşıp ‘duyuruldu’ diye bitirmez. Stüdyo geçmişi, hedef yaş ve platform (sinema/dizi/çocuk uygulaması) yoksa haber eksiktir.",
        "Çocuk kategorisinde merch, içerikten önce konuşulur. Bu, projenin film değil ürün hattı olduğunu gösterebilir.",
        "İzleyici",
        "Yönetmen ve stüdyo önceki işi, vaatten değerlidir. Platform çocuk kilidi, evde karar verir. Türkçe dublaj tarihi, orijinal dilden ayrı kayabilir.",
        "Hayran sanatı, resmi kadro değildir. Seslendirme sızıntısı, sözleşme bitmeden spekülasyondur.",
        ["Yaş ve platform net mi?", "Stüdyo geçmişi", "Dublaj tarihini ayrı tutun"],
        "Animasyon duyurusu, afiştir. Sezon, afişten sonra gelir.",
    ),
    "haftanin-teknoloji-firsatlari-listelendi": g(
        "Teknoloji fırsatı: sahte kupon, gri kutu, iade",
        "AcarTechs ‘fırsat listesi’ni fiyat değil; satıcı, fatura ve iade penceresi olarak okur.",
        "Yüzde 70 indirim, dün şişirilmiş etiketten iner.",
        "Haftalık fırsat yazıları tıklama üretir. Sahte kupon, gri ithal ve ‘son 3 adet’ sayacı da öyle. AcarTechs, ürün ezberi yapmaz. Satıcı puanı, fatura unvanı, iade 14 gün ve yetkili servis arar.",
        "Pazar yerinde aynı model, üç satıcı, üç kutu. En ucuzu, ithalatçı ‘biz değiliz’ dediği kutudur.",
        "Kontrol",
        "Fiyat geçmişi (resmi mağaza). Kargo süresi. Açılınca iade. Kulaklık ve şarj aletinde sahte oranı yüksektir; kafa ve kabloyu ayrı düşünün. Kredi kartı taksit, satıcı değişince garanti zincirini bozmaz; faturasız elden bozar.",
        "‘Fırsat’ı gece 03.00’te almak, sabah soğukkanlı fiyat karşılaştırmasından kötüdür.",
        ["Satıcı ve fatura", "İade penceresi", "Şişirme etiket"],
        "Fırsat, düşük fiyat değil; iadesi duran düşük fiyattır.",
    ),
    "populer-dizinin-yeni-sezon-tarihi-aciklandi": g(
        "Dizi sezon tarihi: pencere, bölge, spoiler",
        "AcarTechs ‘tarih açıklandı’ haberini gün, bölge ve yaş etiketi netleşmeden bütçeye yazmaz.",
        "‘2026 sonu’ bir tarih değil, bir penceredir.",
        "Sezon tarihleri önce yıl, sonra mevsim, sonra gün olarak netleşir. AcarTechs, gün yokken takvime kilit atmaz. Bölge: ABD günü, Türkiye’de ertesi sabah veya lisans gecikmesi olabilir.",
        "Spoiler, tarih tweet’inden hızlıdır. Resmi fragman, sosyal medya karesinden önce izlenir.",
        "İzleyici planı",
        "Günlük dizi, haftalık bölümden farklı ritimdir. Tatil planını sezon finaline kilitlemek, kayan tarih yüzünden bozulur. Çocuk profilinde yeni sezon yaş etiketi değişmiş olabilir.",
        "Abonelik yalnızca o sezon için açılıyorsa, bitişe yakın açmak depolama ve spoiler açısından daha sakin olabilir.",
        ["Gün yoksa pencere yazın", "Bölge farkı", "Yaş etiketi"],
        "Sezon tarihi, gün ve bölge ile tarihtir. Yıl ile hayaldir.",
    ),
    "oyuncu-kadrosu-guclenen-yeni-dram-dizisi-tanitildi": g(
        "Yeni dram dizisi: kadro, showrunner, bölüm süresi",
        "AcarTechs ‘güçlü kadro’ cümlesini isim ezberi değil; showrunner, süre ve platform olarak okur.",
        "Üç ünlü isim, 8×60’ın ritmini garantilemez.",
        "Dram duyuruları kadro afişiyle gelir. Diziyi taşıyan, bölüm yazar odası ve süre disiplinidir. AcarTechs, afişi haber yapıp biterse kopya envanter üretir. Showrunner önceki işi, bölüm sayısı ve platform (haftalık/günlük) yoksa yazı eksiktir.",
        "Yıldız yoğunluğu, bütçeyi şişirir; çekim takvimini de. Geciken sezon, kadro ‘güçlendi’ haberiyle çelişebilir.",
        "İzleyici",
        "45 dakikalık dram, 70 dakikalık ‘sinema bölümü’nden farklı akşam ister. Platform kilidi, evdeki diğer abonelikle çarpılır. Altyazı/dublaj tarihi, orijinal yayın gününden ayrıdır.",
        "Hayran kurgusu, resmi kadro değildir. Konuk yıldız sızıntısı, sözleşmeden önce spekülasyondur.",
        ["Showrunner geçmişi", "Bölüm süresi", "Platform ritmi"],
        "Kadro afişi davettir. Dizi, yazar odasında biter.",
    ),
    "teknoloji-alisverisinde-kampanya-donemi-basladi": g(
        "Kampanya dönemi: sepet, fiyat geçmişi, stok tuzağı",
        "AcarTechs ‘kampanya başladı’ yazısını kupon değil; fiyat geçmişi ve iade olarak okur.",
        "Kırmızı etiket, dünün şişirme listesinden inmiş olabilir.",
        "Sezon indirimleri sepeti şişirir. AcarTechs, liste yayımlamaz. Fiyat geçmişi, satıcı, iade ve enerji sınıfı (beyaz eşya/TV) sorar. ‘Son 2 adet’ sayacı, yazılım olabilir.",
        "Sepete atılan ikinci ürün, kargo eşiği için eklenir; ihtiyaç değildir. Liste yapın, 24 saat bekleyin.",
        "Kart ve iade",
        "Taksit, satıcı değişince garanti zincirini bozmaz. Kapıda ödeme, sahte sitede yoktur. İade kargo kimin? Küçük aksesuarda iade kargo, indirimi yer.",
        "İş cihazını kampanyada almak, fatura unvanı ve e-arşiv ister. Bireysel kutu, şirkete gider yazılmaz.",
        ["Fiyat geçmişi", "24 saat bekle", "İade kargo kimin?"],
        "Kampanya, planlı listenin ucuz halidir. Plansız listenin pahalı halidir.",
    ),
    "yazilim-gelistiriciler-icin-yapay-zeka-destekli-araclar-yayginlasiyor": g(
        "Geliştirici yapay zekâsı: otomatik tamamlama, PR, sır",
        "AcarTechs kod asistanını sihir değil; bağlam, sır sızıntısı ve test olarak okur.",
        "Asistan, derlenen kod üretir; anlaşılan kod üretmeyebilir.",
        "Kod asistanları dosyayı okuyup fonksiyon yazar. Hız gerçektir. Güven, test ve sır (API anahtarı) sızıntısı da. AcarTechs, aracı ‘yaygınlaşıyor’ diye övmez. .env ve anahtar dosyası bağlam dışı tutulmalıdır.",
        "Lisans: üretilen kodun kökeni, copyleft riski taşıyabilir. Şirket politikası yoksa, asistan varsayılanı sizin aleyhinizedir.",
        "Kullanım",
        "Boilerplate, test iskeleti, açıklama: evet. Kriptografi, ödeme ve yetki: hayır, insan ve kütüphane. PR’da asistan diff’ini satır satır okumadan birleştirmeyin. Metrik: derleme + test, ‘daha çok satır’ değil.",
        "Kıdemli, kural dosyası yazar. Stajyer, asistanı dersten çıkış sanmamalıdır; mülakatta model yoktur.",
        [".env bağlam dışı", "Ödeme kodunu yazdırmayın", "PR’ı okumadan birleştirmeyin"],
        "Kod asistanı, hızlı stajyerdir. Gözetimsiz bırakılmaz.",
    ),
}


CAT_META = {
    "yapay-zeka": {
        "h1": "Yapay Zeka",
        "intro": "<p>AcarTechs Yapay Zeka bölümü, model duyurusunu kopyalamaz. Okura kalan karar çerçevesi vardır: veri nereye gidiyor, kim onaylıyor, bu özellik sizin işinizi gerçekten kısaltıyor mu?</p><p>Önce kalıcı rehberler, sonra tekilleştirilmiş haberler. Reklam menünün ve açılır listenin üzerine binmez.</p>",
        "guides": [
            ("/2026da-one-cikan-yapay-zeka-modelleri-hangisi-ne-ise-yariyor/", "2026 modelleri kime göre?", "GPT, Claude, Gemini karşılaştırmasını kullanım senaryosuyla okuyun."),
            ("/chatgpt-nedir-openaiin-yapay-zeka-asistani-neler-yapabiliyor/", "ChatGPT nedir, ne değildir?", "Asistanın sınırını ve doğru soruyu sade anlatım."),
            ("/yapay-zeka-destekli-arama-motorlari-klasik-aramayi-zorluyor/", "Yapay zekâ arama", "Özet kutu ne zaman kaynak, ne zaman taslak."),
            ("/yapay-zeka-iceriklerinde-guven-ve-dogrulama-daha-onemli-hale-geldi/", "Metni doğrulama", "Üç kaynak kuralı, tarih ve alıntı."),
        ],
    },
    "yazilim": {
        "h1": "Yazılım",
        "intro": "<p>Yazılım bölümü changelog ezberi için değil; geliştiricinin ve meraklı okurun ‘bunu işe alayım mı?’ sorusu içindir. Kota, gizlilik ve bakım maliyeti yazılmayan duyuru, AcarTechs’te kopya sayılır.</p><p>Rehberler önce, tekil haberler sonra. Reklamlar menüyle çakışmaz.</p>",
        "guides": [
            ("/api-kullaniminda-hiz-ve-guvenilirlik-neden-onemli/", "API: p95 ve kota", "Demo milisaniyesi değil, fatura günü."),
            ("/yazilim-testlerinde-otomasyon-kullanimi-artiyor/", "Test otomasyonu", "Neyi otomatikleştirip neyi elle bırakmalı."),
            ("/acik-kaynak-projeler-teknoloji-dunyasinda-etkisini-artiriyor/", "Açık kaynak lisansı", "Yıldız sayısı değil, bakıcı ve LICENSE."),
            ("/yazilim-gelistiriciler-icin-yapay-zeka-destekli-araclar-yayginlasiyor/", "Kod asistanı", ".env, PR ve ödeme kodu kırmızı çizgileri."),
        ],
    },
    "teknoloji": {
        "h1": "Teknoloji",
        "intro": "<p>Teknoloji bölümü, her duyuruyu ‘devrim’ diye yazmaz. Cihaz, fatura, garanti ve yama sizin hayatınızı değiştiriyorsa haberdir. Değiştirmiyorsa kaynak linki yeter.</p><p>Kalıcı rehberler üstte, tekil gelişmeler altta.</p>",
        "guides": [
            ("/teknoloji-alisverisinde-garanti-ve-servis-destegi-neden-onemli/", "Garanti ve servis", "Kampanya fiyatından önce kapıdaki servis."),
            ("/siber-guvenlik-yamalarini-geciktirmek-buyuk-risk-olusturuyor/", "Yama disiplini", "Ev ve küçük ofis için 48 saat kuralı."),
            ("/ev-internetinde-hiz-ve-gecikme-degerleri-daha-fazla-onem-kazaniyor/", "Ev interneti", "Mbps değil, akşam saati ve gecikme."),
            ("/dijital-servislerde-yeni-abonelik-paketleri-gundemde/", "Abonelik budama", "Son 30 günde açılmayan satır masraftır."),
        ],
    },
    "mobil": {
        "h1": "Mobil",
        "intro": "<p>Mobil bölümü megapiksel ve Unpacked afişini ezberletmez. Güncelleme taahhüdü, batarya alışkanlığı, servis ili ve paylaşım ayarı yazılır.</p><p>Rehberler önce gelir. Reklam, gezinme öğelerinin üzerine binmez.</p>",
        "guides": [
            ("/telefon-alirken-dikkat-edilmesi-gereken-en-onemli-ozellikler/", "Telefon alırken sıra", "Yama, batarya, servis; kamera sonra."),
            ("/ios-ve-android-arasindaki-farklar-kullanici-deneyiminde-belirginlesiyor/", "iOS mi Android mi?", "Yedek, onarım ve evdeki diğer cihaz."),
            ("/yeni-nesil-telefon-bataryalari-daha-uzun-omur-hedefliyor/", "Batarya ömrü", "Watt değil, gece prizi ve ısı."),
            ("/android-telefonlarda-dosya-paylasimi-daha-kolay-hale-geliyor/", "Dosya paylaşma", "Nearby, USB ve gizlilik."),
        ],
    },
    "bilgisayar": {
        "h1": "Bilgisayar",
        "intro": "<p>Bilgisayar bölümü vitrin FPS’i değil; watt, tamir, RAM tavanı ve ofis sessizliğidir. ‘En yeni’ almak, monitöriniz 1080p iken 4K karta para gömmek olabilir.</p><p>Alım rehberleri üstte, donanım haberleri altta.</p>",
        "guides": [
            ("/ofis-bilgisayari-alirken-nelere-dikkat-edilmeli/", "Ofis PC", "TPM, sessizlik, yerinde servis."),
            ("/yeni-nesil-dizustu-bilgisayarlar-daha-hafif-ve-guclu-geliyor/", "Dizüstü", "Adaptör gramı, RAM, menteşe."),
            ("/windows-pc-kullanicilari-icin-performans-ipuclari/", "Windows yavaşlığı", "Başlangıç, disk, ısınma."),
            ("/ssd-fiyatlarindaki-degisim-bilgisayar-toplamayi-etkiliyor/", "SSD", "TBW, ısı ve yedek."),
        ],
    },
    "sinema-dizi": {
        "h1": "Sinema-Dizi",
        "intro": "<p>Sinema-Dizi bölümü fragman ve Top 10 ezberi değildir. Tarih pencere mi gün mü, yaş etiketi ne, bu ay hangi iki başlık sığar: bunlar yazılır.</p><p>Rehberler üstte. Reklam, menü ve oynatma düğmelerinin üzerinde değildir.</p>",
        "guides": [
            ("/yeni-film-ve-dizi-takvimi-izleyiciler-icin-hareketli-geciyor/", "Takvimi sadeleştirme", "Ayda 2 başlık kuralı."),
            ("/yayin-platformlari-yaz-kataloglarini-guncelliyor/", "Yaz katalogları", "Hangi abonelik bu ay açılır."),
            ("/belgesel-onerileri-teknoloji-ve-doga-meraklilarini-hedefliyor/", "Belgesel seçimi", "Süre, anlatıcı, bölüm bağımsızlığı."),
            ("/populer-dizinin-yeni-sezon-tarihi-aciklandi/", "Sezon tarihi", "Pencere, bölge, spoiler."),
        ],
    },
    "haberler": {
        "h1": "Haberler",
        "intro": "<p>Haberler, sitedeki tekil ve özgün yazıların ortak listesidir. Aynı konunun ikinci kopyası burada tutulmaz. Kısa duyuru, yorumsuz bırakılmaz.</p><p>Gündemi süzmek için üç başlık kuralına da bakabilirsiniz.</p>",
        "guides": [
            ("/teknoloji-gundeminde-bugun-one-cikan-basliklar/", "Gündemi süzme", "Günde üç başlık, sızıntı yok."),
            ("/haftanin-kisa-teknoloji-ozeti-yayinda/", "Haftalık özet", "Cihaz ve fatura değiştirenler."),
            ("/yapay-zeka-iceriklerinde-guven-ve-dogrulama-daha-onemli-hale-geldi/", "Doğrulama", "Birincil kaynak ve tarih."),
            ("/teknoloji-alisverisinde-garanti-ve-servis-destegi-neden-onemli/", "Alışveriş", "Kampanyadan önce servis."),
        ],
    },
    "uygulamalar": {
        "h1": "Uygulamalar",
        "intro": "<p>Uygulamalar bölümü mağaza vitrini değildir. İzin, bildirim, paylaşım ve arayüz yenilemesi sonrası ne kontrol edilir, bunlar yazılır.</p><p>Rehberler önce, uygulama haberleri sonra.</p>",
        "guides": [
            ("/verimlilik-uygulamalari-gunluk-planlamayi-kolaylastiriyor/", "Görev uygulaması", "Tek sistem, cuma arşivi."),
            ("/sosyal-medya-uygulamalarinda-guvenlik-ozellikleri-artiyor/", "Sosyal güvenlik", "2FA, konum, bağlı uygulamalar."),
            ("/populer-uygulamada-arayuz-yenilemesi-basladi/", "Arayüz yenilemesi", "Gizlilik ve bildirim kontrolü."),
            ("/whatsapp-kullanici-adi-rezervasyonunu-baslatti/", "WhatsApp kullanıcı adı", "Rezervasyon ve görünürlük."),
        ],
    },
}

AD_BLOCK = """			<aside class="acartechs-adsense-shell is-horizontal placement-article" aria-label="Reklam">
			<span class="acartechs-ad-disclosure">Reklam</span>
			<div class="acartechs-adsense-unit is-horizontal">
				<ins class="adsbygoogle"
					style="display:block"
					data-ad-client="ca-pub-4367344438750629"
					data-ad-slot="6468864091"
					data-ad-format="auto"
					data-full-width-responsive="true"></ins>
			</div>
		</aside>
"""


def guide_cards(guides):
    cards = []
    for href, title, desc in guides:
        cards.append(
            f'''				<a class="acartechs-guide-card" href="{href}">
					<span>Rehber</span>
					<strong>{title}</strong>
					<p>{desc}</p>
				</a>'''
        )
    return "\n".join(cards)


def rebuild_category(slug: str) -> None:
    if slug == "oyun":
        return
    meta = CAT_META[slug]
    path = ROOT / slug / "index.html"
    html = path.read_text(encoding="utf-8")
    articles = re.findall(r"<article>.*?</article>", html, flags=re.S)
    kept = []
    seen = set()
    for art in articles:
        m = re.search(r'href="([^"]+)"', art)
        if not m:
            continue
        href = m.group(1).strip("/")
        if href in DUPLICATES or href in seen:
            continue
        seen.add(href)
        kept.append(art)
    intro = f'''			<section class="acartechs-category-intro">
				<h1>{meta["h1"]}</h1>
				{meta["intro"]}
			</section>
			<h2 class="acartechs-section-kicker">Rehberler</h2>
			<div class="acartechs-guide-grid">
{guide_cards(meta["guides"])}
			</div>
'''
    list_html = "\n".join(kept[:12])
    inner = f'''			<section class="acartechs-hot-tags" aria-label="Populer icerikler">
			<strong>Popüler İçerikler</strong>
											<a href="/?s=Google%20AI">#GoogleAI</a>
											<a href="/?s=Apple">#Apple</a>
											<a href="/?s=Samsung">#Samsung</a>
											<a href="/?s=ElektrikliOtomobil">#ElektrikliOtomobil</a>
											<a href="/?s=ChatGPT">#ChatGPT</a>
											<a href="/oyun/">#Oyun</a>
					</section>
<section class="acartechs-category-page">
{intro}
			<section class="acartechs-category-list" aria-label="{meta["h1"]} haber listesi">
{list_html}
			</section>
{AD_BLOCK}
				</section>
'''
    html = re.sub(
        r'\s*<aside class="acartechs-adsense-shell is-horizontal placement-top".*?</aside>',
        "",
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r'(</section>\s*)\s*<section class="acartechs-hot-tags".*?<section class="acartechs-footer-panel">',
        r"\1" + inner + '\n\n			<section class="acartechs-footer-panel">',
        html,
        count=1,
        flags=re.S,
    )
    path.write_text(html, encoding="utf-8")
    print("category", slug, "kept", len(kept[:12]))


def move_home_ad() -> None:
    path = ROOT / "index.html"
    html = path.read_text(encoding="utf-8")
    html2 = re.sub(
        r'\s*<aside class="acartechs-adsense-shell is-horizontal placement-top".*?</aside>',
        "",
        html,
        count=1,
        flags=re.S,
    )
    marker = '<section class="acartechs-news-layout"'
    if marker in html2 and "placement-article" not in html2.split(marker)[0][-200:]:
        html2 = html2.replace(marker, AD_BLOCK + "\n\t" + marker, 1)
    path.write_text(html2, encoding="utf-8")
    print("homepage ad moved")


def patch_redirects() -> None:
    extra = []
    for src, dest in DUPLICATES.items():
        extra.append(f"/{src}/ /{dest}/ 301")
    p = ROOT / "_redirects"
    text = p.read_text(encoding="utf-8")
    for line in extra:
        if line.split()[0] not in text:
            text += line + "\n"
    p.write_text(text, encoding="utf-8")

    def inject_js(path: Path) -> None:
        t = path.read_text(encoding="utf-8")
        for src, dest in DUPLICATES.items():
            needle = f"['/{src}/', '/{dest}/']"
            if needle not in t:
                t = t.replace(
                    "['/yeni-nesil-dizustu-bilgisayarlar-daha-hafif-geliyor/', '/yeni-nesil-dizustu-bilgisayarlar-daha-hafif-ve-guclu-geliyor/'],",
                    "['/yeni-nesil-dizustu-bilgisayarlar-daha-hafif-geliyor/', '/yeni-nesil-dizustu-bilgisayarlar-daha-hafif-ve-guclu-geliyor/'],\n"
                    f"  ['/{src}/', '/{dest}/'],",
                    1,
                )
        path.write_text(t, encoding="utf-8")

    inject_js(ROOT.parent / "src" / "worker.js")
    inject_js(ROOT.parent / "functions" / "_middleware.js")
    print("redirects patched", len(DUPLICATES))


def noindex_dupes() -> None:
    tag = "<meta name='robots' content='noindex, follow' />\n"
    n = 0
    for slug in DUPLICATES:
        p = ROOT / slug / "index.html"
        if not p.exists():
            continue
        html = p.read_text(encoding="utf-8")
        if "noindex" not in html:
            html = html.replace("<head>", "<head>\n" + tag, 1)
            p.write_text(html, encoding="utf-8")
            n += 1
    print("noindex", n)


def global_href_fix() -> None:
    n = 0
    for p in ROOT.rglob("index.html"):
        t = p.read_text(encoding="utf-8")
        orig = t
        for src, dest in DUPLICATES.items():
            t = t.replace(f"/{src}/", f"/{dest}/")
        if t != orig:
            p.write_text(t, encoding="utf-8")
            n += 1
    print("href rewrites", n)


def main() -> None:
    for slug, data in GUIDES.items():
        rewrite_article(slug, data)
    patch_redirects()
    noindex_dupes()
    global_href_fix()
    for slug in CAT_META:
        rebuild_category(slug)
    move_home_ad()


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Second unique layer for articles still under 350 words after first expansion."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from apply_publisher_policy import ROOT
from apply_sitewide_policy import DUPLICATES
from inventory_content import text_of
from thin_extras import MORE_DUPLICATES

BODY_RE = re.compile(
    r'(<div class="acartechs-single-body">)(.*?)(</div>\s*</article>)',
    re.S,
)

# slug -> (h2, p, h2, p, close)  — unique, ~220 words
BOOST = {
    "prime-video-haziran-2026-takviminde-vox-machina-ve-yeni-orijinaller-var": (
        "Vox Machina 4’ü kim şimdi açmalı?",
        "Önceki üç sezonu bitirmiş ve yetişkin animasyon temposuna alışmış izleyici için Season 4, haziranın asıl başlığıdır. 1. sezonu yarım bırakmış ev, ‘herkes konuşuyor’ diye dördüncüye atlamasın; karakter şakası ve savaş temposu birikimsiz izlenmez. Every Year After ve diğer orijinaller, Vox Machina’nın 25 dakikalık bölüm ritminden farklı oturum ister. Aynı akşam ikisini açmak, ikisini de yarıda bırakır. Prime üyeliği kargo için zaten açıksa ek fatura yoktur; yalnızca bu dizi için yıllık kilitlemek, üç haftalık hevesi 12 aya yayar. Çocuk profilinde yetişkin etiketini fragman neşesine bakarak açmayın.",
        "Yayın gecikmesi ve indirme",
        "Prömiyer saatinde 4K kuyruğu, zayıf Wi-Fi’de kare düşürür. HD profil + indirme, uçak ve köy için takvimden önemlidir. Resmi press sayfası tarih penceresi verirse takvime belirsiz yazın. Spoiler thumbnail’i açmadan bölüm başlığını okuyun. Prime Video haziranı 30 günlük bütçedir; Vox Machina zorunlu maraton değildir.",
        "Season 4, önceki sezon borcudur. Kargo üyeliği bahane değildir.",
    ),
    "netflix-haftanin-izlenecek-yapimlarini-yeni-listeyle-paylasti": (
        "Color Book ile belgeseli aynı geceye yığmayın",
        "19–25 Haziran Tudum maddesi keşif listesidir. Color Book ve The American Experiment aynı tür değildir; biri anlatı, diğeri tez ister. Avatar: The Last Airbender çocuklu evde yaş etiketine bağlıdır. Voicemails for Isabelle ayrı bir duygusal tempo taşır. Dört adı bir cuma gecesine sığdırmak, hiçbirini bitirmemektir. AcarTechs bu hafta tek başlık, yarın istek listesi der.",
        "Editör seçkisi Top 10 değildir",
        "Tudum ‘ne izlenir’ sayfası tıklama zirvesinden ayrıdır. Zirveye çıkanı izlemek zorunda değilsiniz. İndirme hakkı yoksa yol listesi işe yaramaz. Yıllık planı bu beş ada bağlamayın. Resmi sayfa, sosyal kareden önce gelir.",
        "Haftalık liste süzgeçtir. Dört başlık bir oturum değildir.",
    ),
    "netflix-haftalik-top-10-listesinde-i-will-find-you-zirveye-yerlesti": (
        "15 Haziran zirvesi üçüncü haftayı kanıtlamaz",
        "I Will Find You’nun ilk hafta tıklaması, 8 bölüm taahhüdü değildir. 1. bölüm yetmiyorsa bırakmak serbesttir. Maternal Instinct ve Voicemails for Isabelle aynı sütunda durabilir; gerilim ve belgesel aynı akşam birbirini ezer. Çocuk profilinde yaş etiketi ‘haftanın birincisi’ cümlesinden önce gelir. AcarTechs Top 10’u zevk belgesi saymaz.",
        "Abonelik tuzağı",
        "Zirve için yıllık kilitlemeyin. Ayın 25’inde hâlâ izlemiyorsanız duraklatın. Spoiler kareyi açmadan Tudum maddesine bakın. 15 Haziran listesi keşiftir, kanon değildir.",
        "İlk hafta zirvesi başyapıt cümlesi değildir.",
    ),
    "openai-partner-network-ile-yapay-zeka-projelerinde-is-ortagi-donemi-basladi": (
        "Rozet, KVKK maddesinin yerine geçmez",
        "Partner Network, danışman ve entegrasyon kapısıdır. Veri bölgesi, alt işlemci ve eğitimde kullanılıp kullanılmadığı sözleşmede yazılmalıdır. Demo stüdyo faturasıyla çalışıyorsa sizin PDF’inizde kırılır. İnsan onayı olmayan otomatik e-posta, markayı ilk haftada yakar. Token faturası koltuk + destek saatiyle konuşulmazsa ay sonu sürpriz olur.",
        "Küçük işletme 30 günü",
        "Tek süreç seçin: SSS veya randevu. Partner slaytındaki ‘ajan orkestrasyonu’ 4 kişilik dükkâna fazla gelir. İptalde CSV dump 7 günde gelmiyorsa kilitlenirsiniz. Rozet hızdır, güvenlik belgesi değildir.",
        "İş ortağı kapıdır. Teslimat sizin kabul kriterinizdir.",
    ),
    "openai-ajanlarin-is-dunyasindaki-etkisini-yeni-arastirmayla-anlatti": (
        "Araştırma slaytı sizin NDA’nızı yazmaz",
        "Yazılım ve bilgi işinde taslak hızlanır. Fiyat teklifi, sağlık ve hukuk hızlanmaz. Tüketici ajanına müşteri sözleşmesi yapıştırmak ihlaldir. Revizyon sayısı arttıysa ajan her cümleyi yeniden yazdırıyordur; o noktada araç stajyer gibi pahalıdır. Eğitim, lisans kadar önemlidir.",
        "Ölçmeden ‘herkes kullansın’ demeyin",
        "Taslak süresi ve revizyonu birlikte ölçün. Onaysız gönderim yok. Politika cümlesi yoksa araştırma, sızıntı davetidir. Ajan tekrarlayan adımı keser, sorumluluğu devretmez.",
        "Hız ipucudur. Onay yavaşlığı silinmez.",
    ),
    "google-arama-ai-mode-icin-gemini-3-5-flash-donemine-gecti": (
        "Flash, dünkü cevabı bugün değiştirebilir",
        "Model geçişi gecikmeyi kısaltır. Ödev ve müşteri notuna yapıştırılan paragraf, kaynak linki olmadan kırılır. Tarih ve sayı uydurma en sık patlar. Hukuk, sağlık ve güncel fiyat için asıl sayfaya gidin. Şirket metnini arama kutusuna yapıştırmayın.",
        "Klasik liste duruyor",
        "Nadir hata kodu ve uzun PDF hâlâ link listesinde bulunur. AI Mode giriş içindir. Reklam birimi paragrafın yanında durabilir; ‘Google söyledi’ fatura gerekçesi olmaz. Sorumluluk tıklayanındır.",
        "Hızlı kutu dipnotu silmez.",
    ),
    "google-finance-yeni-uygulama-ve-portfolyo-ozellikleriyle-guncellendi": (
        "Yeşil portföy, lisanslı tavsiye değildir",
        "Gecikmeli fiyat, sizin emriniz değildir. Bildirim FOMO ile işlem açtırabilir; sessize almak serbesttir. Paket adını resmi sayfadan doğrulayın; mağazada benzer ada sahte uygulama durur. Vergi ve broker kaydı Finance’te durmaz.",
        "İş telefonu",
        "Kişisel izleme listesi ilgi grafiğidir. İş cihazında açmayın. İki faktör ve kilit, e-posta uygulamasından önemlidir. Finance izlemedir, al-sat kapısı değildir.",
        "Grafik güzelleşmesi emir değildir.",
    ),
    "netflix-haziran-2026-takviminde-yeni-diziler-ve-filmler-one-cikiyor": (
        "Haziran yığını 30 güne sığmaz",
        "Voicemails, Sweet Magnolias, Avatar ve belgeseller aynı ayda durur. Pazartesi tek dizi, Cuma tek film. Belgesel ile romantik komedi aynı akşam birbirini öldürür. Çocuklu evde Avatar öne çıkar; yetişkin gerilim hafta sonuna kalır. Yıllık kilidi yaza bağlamayın.",
        "Takvim ve Top 10",
        "Takvim ne gelecek, Top 10 ne tıklandı. İkisi de zevkiniz değildir. Offline indirme köy ve uçak için takvimden önemlidir. Elemek izlemektir.",
        "Aylık takvim 30 günlük bütçedir.",
    ),
    "disney-plus-the-doomies-icin-resmi-fragman-ve-yayin-tarihini-paylasti": (
        "Fragmanı ses kapalı bir kez daha izleyin",
        "Müzik hilesi korku eşiğini yumuşatır. Çocuk profilinde otomatik oynatma, fragmanı film sanır. Yaş etiketini resmi sayfadan okuyun. Tarih pencereyse parti ve izin günü bağlamayın. Aynı hafta Avatar varsa Doomies istek listesine düşebilir.",
        "Spoiler kare",
        "Sosyal medya thumbnail’i resmi tarihten önce gelir. Listeyi Disney sayfasından, kareyi değil başlığı okuyarak tutun. Fragman davettir, sözleşme değildir.",
        "The Doomies süzgeci yaş, tarih ve tondur.",
    ),
    "openai-patch-the-planet-ile-acik-kaynak-guvenligine-ai-destegi-veriyor": (
        "AI issue gürültüsü bakıcıyı yakar",
        "Patch the Planet araştırma kapasitesidir. Bin kırmızı, triyaj olmadan lockfile’ınızı güvenli kılmaz. Sorumlu açıklama, tweet’ten önce gelir. Kendi 48 saatlik yama kuralınız (OS, tarayıcı, yönlendirici) bu girişimden düşmez. Tek bakıcılı paketi kritik yola AI rozetiyle almayın.",
        "Öğrenci katkısı",
        "Yeniden üretilebilir rapor, yıldız spam’inden değerlidir. LICENSE ve lockfile hâlâ sizin işinizdir. AI taslak avcısıdır, insan yaması imzadır.",
        "Açık kaynak yaması imzalıdır. Program sihir değildir.",
    ),
    "samsung-vivatech-2026da-baglantili-bakim-vizyonunu-sergiledi": (
        "Fuar videosu iç cam fiyatını göstermez",
        "Connected care, saat-telefon-ev ekranı konuşsun ister. Sağlık verisi TV önerisinden ayrı rıza ister. Sigorta veya işveren paylaşımı ‘anlamlı öneri’ cümlesinin altında gizlenebilir. Çocuk ve yaşlı profilinde varsayılan paylaşım kapalı olsun. Türkiye fiyatı ve servis ili fuar standında yazmaz.",
        "Ne somut?",
        "Satın alma, yazılım yılı ve izin listesi netleşince. VivaTech vizyondur. Demosu ürün belgesi değildir.",
        "Bağlantılı bakım izin mimarisidir.",
    ),
    "openai-model-davranislarini-yayin-oncesi-simule-eden-yeni-yontemini-anlatti": (
        "Laboratuvar, sizin sohbetinizdeki uydurmayı sıfırlamaz",
        "Deployment Simulation ajanın dışarıda tıklamasına yakın test ister. Kırmızı takım ve politika katmanı olmadan tek başına yetmez. ‘Simülasyondan geçti’ sağlık kararı gerekçesi olmaz. Kendi ajanınızda yetki aşımı, sonsuz döngü ve prompt sızıntısı senaryosu yazın.",
        "Onay tuşu",
        "Ödeme ve e-posta adımlarında durdurma yoksa simülasyon sizi kurtarmaz. Sertifika değil, test olgunluğudur.",
        "Simülasyon laboratuvar notudur. Sıfır risk vaadi değildir.",
    ),
    "github-copilot-ucretsiz-ve-ogrenci-planlarinda-otomatik-model-secimine-geciyor": (
        "Kota bitince ‘bozuldu’ sanılır",
        "Otomatik model, dün başka bugün başka cevap üretebilir. Ödevde hangi model kaydı yoksa tekrar üretilemez. Açıklama evet, bitmiş ödev hayır. İş reposunu okul mailine bağlamayın. API anahtarı sohbet geçmişine yapışmaz. Plan sayfasındaki veri eğitim kutusunu okuyun.",
        "Kapatılabiliyor mu?",
        "Otomatik seçim kapatılabiliyorsa kritik yamada sabitleyin. Ücretsiz katman hediye zekâ değil kota ve süzgeçtir.",
        "Model adı gizlenince sır ve ödev çizgisi silinmez.",
    ),
    "disney-plus-haziran-listesinde-avatar-fire-and-ash-promiyeri-one-cikiyor": (
        "Üç saatlik oturum, çocuk ara vermeden bitmez",
        "Avatar: Fire and Ash uzun ve görsel ağırdır. 4K prömiyer kotası zayıf Wi-Fi’de düşer; HD profil utanç değildir. İndirme hakkı katmana bağlıdır. Aynı ayda ikinci ‘kaçırma’ başlığı filmi yarıda bırakır. Yalnızca bu prömiyer için yıllık plan, üç aylık hevesi kilitleyebilir.",
        "Yaş ve 2 başlık",
        "Bu ay Avatar + bir kısa aile yapımı. Üçüncü istek listesi. Prömiyer vitrindir, 30 günlük bütçe karardır.",
        "Haziran Avatar süzgeci süre, yaş ve kotadır.",
    ),
    "microsoft-agent-365-ile-kurumsal-yapay-zeka-ajanlarini-yonetmek-istiyor": (
        "Gölge ajan, gölge IT’nin 2026 halidir",
        "Kaç ajan, hangi kimlik, hangi SharePoint, hangi mailbox. Kayıt yoksa POC ertesi gün sızıntıdır. EDR ve DLP’nin yerine geçmez, yanına oturur. Kullanılmayan lisans koltukları yanar. ‘Kullanın’ demek gizli klasörü prompt’a davettir.",
        "İlk 30 gün tenancy",
        "Test ortamı, müşteri verisi yok, SSO ve koşullu erişim. Onaysız gönderim yok. Agent 365 envanterdir, ajan fabrikası değildir.",
        "İzlenmeyen ajan stajyerdir. Kontrol düzlemi şarttır.",
    ),
    "samsung-galaxy-watch-icin-yapay-zeka-destekli-saglik-ozelliklerini-duyurdu": (
        "14 gün, tek gece değil",
        "Uyku skoru gece 3’te bakılan telefona göre savrulur. Kayış gevşekse nabız yalan söyler. Veri ülkesi sağlık vaadinden ayrı karardır. Her gece şarj uyku takibini yarım bırakır. Kırmızı uyarıda hekim, uygulama değil. Telefondaki Galaxy AI ile saatteki sağlık kartı aynı izin kutusunu paylaşabilir; ayrı okuyun.",
        "Kime alınır",
        "Yürüyüş hatırlatması evet. Teşhis hayır. GPS sporcuda sağlık kartından değerlidir. Saat aynadır, reçete değildir.",
        "Watch AI eğilimdir. Doktor değildir.",
    ),
    "whatsapp-kullanici-adi-rezervasyonunu-baslatti": (
        "Sahte rezervasyon sitesi harcı yakar",
        "Yalnızca resmi uygulama: Ayarlar, Hesap, Kullanıcı adı. 2014 e-posta gibi seçmeyin; iş ve aile karışır. Bir harf farkı yaşlı akrabaya borç mesajı atabilir. Anahtarı ailede önceden konuşun. Numara gizlense de fotoğraf ve durum satırı kimlik sızdırır. Kademeli açılışta ‘bende yok’ skandalı değildir.",
        "İş ve kişisel",
        "Kurumsal hat ayrı ad. Yedek ve kilit durur. Kullanıcı adı rehber listesi değildir; tam ad + anahtar süzgecidir.",
        "Rezervasyon resmi uygulamadadır. Forum paniği değildir.",
    ),
    "github-desktop-3-6-worktree-ve-copilot-entegrasyonunu-genisletti": (
        "İki worktree, iki node_modules",
        "Disk ve IDE belleği şişer. Küçük depoda deneyin, monorepo’da CLI dürüst kalır. Windows satır sonu ve LFS sürpriz üretir. Copilot commit mesajı taslaktır; ‘fix stuff’ yerine nedeni siz yazın. Rebase çatışmasında terminal utanç değildir.",
        "Sır",
        "Müşteri verisi PR taslağına yapışmaz. Desktop 3.6 paralel dal kolaylığıdır. 30 kişilik ekipte kaynak hâlâ CI’dır.",
        "GUI worktree maliyeti gizlemez.",
    ),
    "openai-ve-broadcom-yapay-zeka-icin-jalapeno-inference-cipini-tanitti": (
        "Bu gece telefonunuza inmez",
        "Jalapeno inference faturasıdır, eğitim (training) ayrıdır. HBM bellek baskısını sihirle bitirmez. Kota ve yavaş cevap, yoğun saat + silikon + model seçimidir. Üretim tarihi ve watt netleşmeden ‘daha ucuz ChatGPT’ cümlesi slayttır. Evde yeni kutu alım gerekçesi değildir.",
        "Kurum",
        "Token fiyatını SLA ve bölge ile okuyun. Özel çip yol haritasıdır. Eldeki asistanın kalitesi bu kutu gelmeden de sizin onay kuralınızdır.",
        "Jalapeno sunucu oyunudur. Cep duyurusu değildir.",
    ),
    "microsoft-windows-10-esu-suresini-kullanicilar-icin-uzatti": (
        "TPM’siz kutu ömür boyu güvende değildir",
        "ESU özellik güncellemesi değil yama kirasıdır. Bankacılık ve iş maili yamasız 10’da ayrı ağda durmalı veya emekli edilmelidir. Kaç cihaz 11’e çıkar, hangisi ESU, hangisi yazıcı yüzünden kalır yazın. 20 cihaza aynı anda basmayın; 1 PC dene. Yedek yamadan önce gelir.",
        "Resmi tarih",
        "Blog cümlesi kayabilir. Yaşam döngüsü sayfasını işaretleyin. Ek süre plan yazdırır, sonsuz 10 vaadi değildir.",
        "ESU takvimdir. ‘Hâlâ açılıyor’ güvenlik değildir.",
    ),
    "cloudflare-workflows-icin-saga-rollback-destegi-geldi": (
        "Stok düştü, ödeme çekildi, kargo 500",
        "Telafi yazılmamışsa rollback slayttır. İdempotency yoksa çift iade doğar. Tek veritabanı işlemi saga istemez; üç harici servis ve para ister. Log olmadan gece 03.00 kördür. Dış banka telafiyi reddederse insan kuyruğu şarttır.",
        "İleri ve geri fonksiyon",
        "Her adımı isimlendirin. Saga kısmi başarıyı görünür kılar. Sihirli undo değildir.",
        "Rollback, yazdığınız telafi kadardır.",
    ),
    "chatgpt-icin-yeni-saglik-zekasi-guncellemesi-duyuruldu": (
        "Hazırlık sorusu evet, doz hayır",
        "‘Tahlil maddesi ne, hekime ne sorayım?’ doğru. ‘Tanıyı koy, ilacı yaz’ yanlış. Kronik hastalık, gebelik, çocuk dozu ve acil belirti 112’dir. Paylaşılan cihazda sağlık sohbeti bırakmayın. Uydurma kaynak ve emin duruş riski sıfırlanmaz.",
        "Ürün değil süreç",
        "Daha az zararlı cevap hedefi süreçtir. Hastane bilgi sistemi değildir. Resmi kaynak ve uzmanla doğrulayın.",
        "ChatGPT hekim değildir. Triyaj da değildir.",
    ),
    "cloudflare-oauth-akisini-tum-gelistiricilere-acti": (
        "Tüm zone izni blog yazısı için gerekmez",
        "Ajan ‘hesaba gir’ diyorsa dar kapsam ve süre şarttır. offline_access bir yıl unutulmuş entegrasyonda sızıntı üretir. İptal (revoke) yoksa OAuth vitrindir. Mobilde istemci sırrı gömmek sorunu geri getirir. İç portalda SSO + OAuth, paylaşılmış admin anahtarından iyidir.",
        "Belgeye yazın",
        "Kapsam listesi ürün belgesinde dursun. Anahtarı prompt’a yapıştırmayın. OAuth izin disiplinidir, tatil değildir.",
        "Herkese açık OAuth, herkese tam yetki demek değildir.",
    ),
    "google-haziran-pixel-drop-ile-gemini-ve-yaratici-araclari-genisletti": (
        "128 GB’da üç AI video dolar",
        "Yaratıcı araç rulo ve diski yer. Çeviri toplantı gündemini sunucuya gönderebilir; kapatın. Floating bubbles bankacılıkta yanlış tıklar. Kılıf içinde Gemini ısınır. Model listesini resmi Pixel sayfasından okuyun. Yamayı özellik için ertelemeyin.",
        "Kademe",
        "Komşuda var skandalı değildir. Wi-Fi’de ve kılıfsız dene. Drop vitrindir, sizin modeliniz karardır.",
        "Pixel Drop her cihaza aynı gün inmez.",
    ),
    "android-studio-quail-1-yapay-zeka-destekli-hata-analizini-guclendirdi": (
        "Yarış durumu uydurması özgüvenlidir",
        "Null ve izin kalıplarında ajan işe yarar. Cihaz-özel sürücüde yalan söyleyebilir. Diff’te üç satır bağımlılık şişirebilir. Üretim yığınını kişisel modele yapıştırmayın. App Quality Insights stajyer hesabında açık kalmasın. CI kırmızısı model özgüveninden değerlidir.",
        "PR kuralı",
        "Ajan açıklaması taslak, kopyala-yapıştır kapanış değil. Quail 1 hızdır, kalite kapısı değildir.",
        "Çöküş açıklaması merge emri değildir.",
    ),
    "android-gelistirici-dogrulamasi-uygulama-dagitiminda-yeni-donem-baslatiyor": (
        "Hobi APK’sı ile ticari Play aynı kapı değildir",
        "Bu çeyrek yeni paket sürecekseniz kimlik sırasını şimdi başlatın. Öğrenci hesabını marka gibi kullanmak devirde kilitlenir. Paket adını squatting’e bırakmayın. Yan yükleme ve sosyal mühendislik kimlik katmanının dışında kalır; kullanıcıyı ‘artık sahte yok’ diye uyutmayın.",
        "İç test",
        "20 kişilik kapalı dağıtım panik gerekçesi değildir. Yine de ticari adı şimdi koruyun. Doğrulama dağıtım anahtarıdır, her kullanıcının acil güncellemesi değildir.",
        "Kimlik, hobi sınırını çizer. Android’i bitirmez.",
    ),
    "apple-yeni-app-store-araclariyla-gelistiricilere-daha-fazla-esneklik-sunuyor": (
        "AB ve ABD vitrini aynı esneklik değildir",
        "Bölgede araç açık mı işaretleyin. İnceleme kuyruğu ve ekran görüntüsü kuralı durur. Kampanyayı bir haftalık ölçümle açın. Yıllık deneme iptali utandırır; takvime yazın. Aile paylaşımı fiyat tablonuzu böler. Küçük ekip için A/B fiyat, büyük yayıncının medya bütçesi değildir.",
        "Reddedilen meta",
        "Yeni kutu, reddi kurtarmaz. Store aracı çarpandır, ürün yerine geçmez.",
        "Esneklik politika tatili değildir.",
    ),
    "apple-wwdc26da-siri-ai-ve-yeni-apple-intelligence-donemini-tanitti": (
        "Sahne demosu A18 eşiğinizi göstermez",
        "Dil paketi ve model listesi resmi sayfadadır. On-device ile Private Cloud Compute ayrımını okumadan gizlilik yutmayın. Şirket metnini Siri’ye okutmak NDA sınırı olabilir. WWDC günü telefon hurdaya çıkmaz. Watch ve TV ayrı inebilir. İptal tuşu sahnede görünmez; asıl ürün odur.",
        "Rekabet",
        "İşletim sistemi katmanı sohbet kutusundan büyüktür. Eldeki cihaz ve dil karardır, sahne vaadi değildir.",
        "Siri AI takvim ve model listesidir. Bugünkü hurda gerekçesi değildir.",
    ),
    "android-haziran-drop-guvenlik-ve-kisisellestirme-ozelliklerini-buyuttu": (
        "Yaşlı kullanıcıya geri arama kuralı",
        "Sahte arama uyarısı ‘bankanız arıyor’ senaryosunu bitirmez. Uygulama içinden değil, resmi numaradan geri arama konuşulur. Photos kıyafet işi hangi sunucuda, yedekleme açık mı. iPhone paylaşımında görünürlük ‘herkes’ toplantıda yabancı dosyadır. Yama Drop’tan ayrı inebilir; özelliği beklerken yamayı ertelemeyin.",
        "Kademe",
        "Pixel ve seçilmiş sürüm. Komşuda var skandalı değildir. Drop güvenlik ile vitrini ayırarak okunur.",
        "Haziran Drop her Android’e aynı gün inmez.",
    ),
    "yazilim-gelistiriciler-icin-yapay-zeka-destekli-araclar-yayginlasiyor": (
        "Üretilen kodun lisansı belirsizse yapıştırma",
        "Tamamlama herkese, PR özeti ekibe, sır modele değil. Şirket kirası yoksa kişisel Copilot iş reposuna bakmasın. Önerilen yama testsiz merge edilmez. Diff üç satırda bağımlılık şişirebilir. CI kırmızısı özgüvenden değerlidir.",
        "Öğrenci",
        "Açıklama evet, bitmiş ödev hayır. Araç hızdır. Sır sizin kapınızdadır.",
        "Geliştirici AI iskelettir. Üretim sırrı değildir.",
    ),
    "android-developers-sayfasinda-yeni-gelistirici-duyurulari-yayimlandi": (
        "Haftada bir resmi sayfa yeter",
        "Twitter sızıntısı üçüncü kovadır. Studio/SDK derlemeyi bozar, Play politikası kapıyı kapatır, güvenlik yaması cihazı ilgilendirir. Aynı gün üç duyuru varsa yalnızca kıranı alın. Önizleme kararlı kanal değildir. Öğrenci ve ticari paket aynı doğrulamayı paylaşmaz.",
        "Kullanıcıya yazmayın",
        "‘Haber sayfası yenilendi’ kopya envanterdir. Süzgeç, yığın özeti değildir.",
        "Android news takvim süzgecidir.",
    ),
    "mobil-uygulamalarda-yapay-zeka-destekli-yeni-donem-basladi": (
        "Uçak modu yalanı ele verir",
        "Durmayan özellik yerel değildir. Klavye tahmini cihazda, uzun sohbet bulutta olabilir. Fotoğraf yedekleme kutusu ayrıdır. İş telefonunda bulut AI’yi kapatın. NPU ısınması vitrin TOPS’undan önce gelir. Küçük model büyük iddia taşır.",
        "İzin",
        "Yerel yazısı verinin çıkmadığı anlamına gelmeyebilir. Ayarları satır satır okuyun.",
        "Telefondaki AI hangi katmanın yerelde kaldığıdır.",
    ),
    "robotik-sistemlerde-yapay-zeka-kullanimi-genisliyor": (
        "Gece vardiyası sessiz davranış değiştirir",
        "Model güncellemesi sürüm kaydı olmadan kaza incelemesini kör eder. Hat kamerası çalışan yüzünü kaydeder; amaç ve saklama yazılı değilse KVKK riskidir. İnsan varken kilitli alanda kol çalışmasın. Demo videosu tozlu hattın sürtünmesini gizler. Acil stop ve çember ‘akıllı’ kelimesinden önce gelir.",
        "Pilot hat",
        "Yaya yolundan ayrı. Robot + AI güvenlik çemberidir, vitrin kolu değildir.",
        "Fuar kolu çember olmadan işe yaramaz.",
    ),
    "yapay-zeka-iceriklerinde-guven-ve-dogrulama-daha-onemli-hale-geldi": (
        "‘Çalışmaya göre’ tıklanmıyorsa yok sayın",
        "Sayı, tarih ve isim en sık uydar. Görselde el ve yazı bozuktur. Ödevde olmayan makale faciasıdır. Filigran görünmeyebilir; kim onayladı süreci daha önemlidir. Şirket metnini kutuya yapıştırmayın.",
        "Üç kaynak",
        "Model, resmi sayfa, bağımsız üçüncü. İkisi yoksa taslak. Emin duruş kanıt değildir.",
        "Güven tıklamanızdır, model özgüveni değil.",
    ),
    "populer-dizinin-yeni-sezon-tarihi-aciklandi": (
        "Bu sonbahar izin günü bağlamaz",
        "Türkiye kataloğu ABD’den haftalar sonra gelebilir. İlk bölüm özel, gerisi aylar sonra olabilir. Toplu yayın bir hafta sonunu yer, haftalık 8 hafta ister. Önceki sezon bitmeden yeni sezon arşiv borcudur. Spoiler thumbnail’i resmi tarihten önce gelir.",
        "Çocuklu ev",
        "Bölüm saati kritik beğeniden önce gelir. Pencere tarih belirsiz yazılır.",
        "Sezon tarihi net yıl ve bölgedir. Tweet değildir.",
    ),
    "yapay-zeka-etiketi-uygulamalarda-daha-gorunur-olacak": (
        "Kapatılabilen etiket dekorasyondur",
        "Rozet kaynak doğruluğu kanıtlamaz. Sohbet özeti, altyazı ve yüz güzelleştirme ayrı katmanlardır. Mağaza açıklamasındaki AI rozeti verinin nerede işlendiğini yazmaz. Çocuk uygulamasında varsayılan üretim kapalı olmalıdır. Haberde etiket dipnot yerine geçmez.",
        "Hangi katman sentetik",
        "Görünürse işe yarar. Yoksa süslemedir.",
        "Etiket şeffaflıktır. Doğruluk belgesi değildir.",
    ),
    "sirketler-musteri-hizmetlerinde-yapay-zeka-asistanlarini-deniyor": (
        "Kırk dakika ‘sizi anlıyorum’ yakar",
        "Kargo ve iade penceresi bota, öfke ve ödeme itirazı insana. İnsan tuşu her turda görünsün. Devri artıyorsa bot yanlış yerdedir. Ses kaydı rıza olmadan eğitim verisi olmaz. Müşteri kaydını tüketici modele yapıştırmayın.",
        "Ölçüm",
        "İlk çözülme ve insan devri. Bot SSS keser, şikâyet yönetimi değildir.",
        "Taslak evet, tonda hata pahalıdır.",
    ),
    "teknoloji-alisverisinde-kampanya-donemi-basladi": (
        "Son 2 adet her gün yenilenir",
        "14 gün önceki etikete bakın. Sepeti 24 saat bekletin. IMEI/seri faturada yoksa iade zorlaşır. Kapıda nakit ‘yerinde teslim’ fiş fotoğrafı o anda alınır. Uzatılmış garanti ekranı kapsamıyorsa camdır. Kargo eşiği kasa farkını yer.",
        "Gri kutu",
        "Kampanya sahte fatura sever. Servis ili ve unvan yazın. İndirim kasa anıdır, iade günü karardır.",
        "Fiyat geçmişi olmayan yüzde iddiadır.",
    ),
    "orta-segment-telefonlarda-fiyat-performans-yarisi-buyuyor": (
        "200 MP gece sokağında görünmez",
        "Para yama yılı, batarya, servistir. Ödün 120 Hz her zaman açık ve IP reklamıdır. 3–5 yıl yama skandal değil ödündür. PWM ve 80W kılıfla ısınma vitrinde yok. 256 GB, 128+bulut aboneliğinden ucuz olabilir. Gri ithal farkı serviste çıkar.",
        "Mağaza ışığı",
        "Gece testini sokağa çıkarın. Orta segment üstün karesini kopyalamak zorunda değildir.",
        "Yama yılı megapikselden değerlidir.",
    ),
    "haftanin-teknoloji-firsatlari-listelendi": (
        "Forum kuponu ölmüş olabilir",
        "Resmi sayfada deneyin. Gri kutu kamera aynı garanti farklıdır. Açılmış kulaklıkta iade sıfırlanabilir. 23.59 sayacı her gün sıfırlanır. Satıcı puanı ve faturadaki seri yoksa geçin.",
        "24 saat",
        "Sepeti bekletin. Fırsat iade günüdür, kasa yüzdesi değildir.",
        "Haftalık liste süzgeçtir. Yüzde ezberi değildir.",
    ),
    "oyuncu-kadrosu-guclenen-yeni-dram-dizisi-tanitildi": (
        "Afiş dolduran yüz hikâyeyi taşımaz",
        "Showrunner değişimi tonu sıfırlar. 42 dakika ile 70 dakika aynı akşam değildir. Haftalık ve toplu yayın ayrı borçtur. Kadro sızıntısı anlaşma değildir. İlk sezon bitmeden ikinci sezon şişirir.",
        "Spoiler",
        "Oyuncu fotoğrafı değil karakter işlevi. Afiş dolduruyorsa bekleyin. Kadro haberi showrunner ve süredir.",
        "Yıldız 8 sezon taahhüdü değildir.",
    ),
    "bilgisayar-bakimi-performansi-nasil-etkiler": (
        "Kompresör anakartı ıslatır",
        "Dışarıdan fırça ve süpürge. Macunu her yıl değiştirmeyin; 3–4 yıl veya gerçek sıcaklıkta. Performans paketi sürücü bozar. RGB yazılımı 10 süreç açar. Fan tıkırtısı, şişen pil, yanık koku servistir. SSD doluysa bakım sihir değildir.",
        "Yılda iki kapak",
        "Ofis PC yeter. Oyun kulesinde filtre yıkanmadan macun konuşulmaz. Bakım nefes alan kasadır.",
        "Toz, macun, kablo. Yirmi numara listesi değil.",
    ),
    "animasyon-dunyasinda-yeni-proje-duyuruldu": (
        "Aynı stüdyo okul öncesi ve ergen korku üretir",
        "Hedef yaş, süre, platform katmanı logo kadar önemlidir. Fragman neşeli film karanlık olabilir. Sinema+streaming aynı günse büyük ekran kararı öne alınır. Merch, resmi sayfadan önce bağlanmaz. Çocukta otomatik oynatma kapatılır.",
        "Devam ve spin-off",
        "İlk filmi bitirmemiş ev için zorunlu değildir. Üç süzgeç net değilse istek listesidir.",
        "Animasyon haberi yaş ve platformdur. Logo değildir.",
    ),
    "sarj-teknolojileri-daha-guvenli-ve-hizli-hale-geliyor": (
        "Yastık altında kafa yangın senaryosudur",
        "Kablo 60W, kutu 120W yazabilir. e-marker yoksa ısınır. Sahte kafa kıvılcım ve şişen pil üretir. PD her kafa her telefon 100W demek değildir. Otel USB’si veri sızdırabilir; şarj-only kablo. Islak elle watt yarışı yok. 85’te kesen yazılım yoksa priz zamanlayıcısı ucuzdur.",
        "Resmi liste",
        "Kablo ve kafa üretici listesinde mi? Hız dakikayı kurtarır, sahte kafa kimyayı yer.",
        "Şarj watt tablosu değil kablo, ısı ve sahte kafadır.",
    ),
    "kult-serinin-devam-filmi-icin-hazirliklar-basladi": (
        "Sendika çekim bildirimi yoksa bir yıl sürebilir",
        "Geliştirme, çekim, vizyon. Birincide merch bağlanmaz. Yönetmen değişimi tonu sıfırlar. Kitap yazarının adı yeşil ışık değildir. Ön satış yıl netleşmeden otel iptali sizin riskinizdir. 10 dakikalık sızıntı 130 dakika değildir.",
        "Nostalji",
        "2026 temposuna uymayabilir. Devam filmi anıdır, bilet tarihtir.",
        "Hazırlık başladı bilet tarihi değildir.",
    ),
    "airdrop-destegine-sahip-tum-android-telefonlar": (
        "Tablo, görünürlük kapalıysa boştur",
        "Google hesabı, Bluetooth, konum ve Quick Share menüsü. Eski üretici arayüzü özelliği saklar. Aynı Wi-Fi yoksa keşif düşer. iPhone için Fotoğraflar veya kablo 15 dakikalık dansı keser. Toplantı bitince görünürlüğü kapatın. Konum izni sürekli açık olmak zorunda değildir.",
        "Arama tuzağı",
        "AirDrop kelimesi model listesi ezberi üretir. Ayar ve hesap önce gelir.",
        "Destek listesi ayar kapalıysa işe yaramaz.",
    ),
    "android-telefonlarda-dosya-paylasimi-daha-kolay-hale-geliyor": (
        "4 GB ham video Nearby işi değildir",
        "Kablo veya bilgisayar. Hassas sözleşme herkese açık kablosuzda durmaz. Misafir ağı iki telefonu ayırır. İş telefonunda paylaşımı kapatın. Çocuk ‘yakındaki herkes’ten dosya almasın. Görünürlük kişilerim.",
        "iPhone",
        "Zorlamak 20 dakika yer. Kısa PDF Nearby, büyük dosya kablo. Kolaylık herkes görünürlüğü değildir.",
        "Paylaşım yolu, slogan listesinden önce gelir.",
    ),
    "populer-uygulamada-arayuz-yenilemesi-basladi": (
        "Eski adı arama kutusuna yazın",
        "Menü kayınca özellik kaybolmuş gibi görünür. İzinler sıfırlanabilir; konum ve mikrofonu kontrol edin. Sessiz kanal hâlâ oradadır. Yedek almadan hesap silmeyin. ‘Daha sade’ üç tıklama eklemiş olabilir. Şirket profili yeni arayüzü zorunlu kılabilir.",
        "Öfke",
        "Resmi yardım, sosyal medyadan hızlıdır. Yeni arayüz kayıp değildir. Önce ara.",
        "İzinleri tekrar okuyun. Panik silmeyin.",
    ),
    "robot-supurge-modellerinde-haritalama-teknolojisi-gelisiyor": (
        "Siyah halı düşme sensörünü şaşırtır",
        "Eşik 2 cm çıkmıyorsa oda ayırımı işe yaramaz. Toz istasyonu gece komşusudur. Fırça yedek fiyatını 24 aya yayın. Çok kablo varsa dikey süpürge daha az küfür ettirir. Harita buluta gidiyorsa mikrofonsuz model düşünün. Çocuk ve hayvanda kapak ve düşme sensörü şarttır.",
        "Ölçün",
        "Eşik yüksekliği, saç, haftalık bakım. Robot harita uygulaması değil eşiği çıkan makinedir.",
        "LIDAR vaadi eşik ve saç testidir.",
    ),
    "yazilim-testlerinde-otomasyon-kullanimi-artiyor": (
        "Kırmızıya alışmak yalancı çobandır",
        "Flaky testi silin veya düzeltin. İlk 10: giriş, şifre, ödeme, stok bitişi, yetkisiz sayfa. Renk sonra. Üretim verisini teste kopyalamayın. 10 sağlam, 400 kayıttan değerlidir. Araç değişimi bu 10’u taşımıyorsa geçmeyin.",
        "Para kaybettiren yol",
        "Otomasyon az ve güvenilen testtir. Her tıklama kaydı bakım faturasıdır.",
        "Kırılgan UI otomasyonu güvenlik değil gürültüdür.",
    ),
    "acik-kaynak-projeler-teknoloji-dunyasinda-etkisini-artiriyor": (
        "LICENSE dosyasını README’den önce okuyun",
        "GPL copyleft kapalı ürünü zorlar. MIT atıf ister. npm install ‘bilmiyordum’ kabul etmez. Tek bakıcı kritik yolda çatal veya destek olmadan girmesin. Issue şablonu yoksa PR havada kalır. Yıldız spam bakıcıyı yorar.",
        "Lockfile",
        "SBOM veya kilit dosyası olmadan en son sürüm çekmeyin. Açık kaynak bakımı paylaşılmazsa borçtur.",
        "GitHub yıldızı denetim değildir.",
    ),
    "ssd-fiyatlarindaki-degisim-bilgisayar-toplamayi-etkiliyor": (
        "QLC paniği sistem diskini yer",
        "TBW ve DRAM/HMB sistemde, kapasite arşivde. PCIe 5.0 soğutmasız kısılır. Tek 4 TB yedeksiz her şeyi bir deneticide kaybettirir. Laptop tek yuvada dış 2 TB yedek, içerideki fırsat 4 TB’dan değerlidir. 3-2-1.",
        "Isı",
        "7000 MB/s 200 GB kopyada düşer. Fırsat yedeksiz kapasite değildir.",
        "SSD GB/TL değil dayanım ve ikinci kopyadır.",
    ),
    "ses-klonlama-teknolojileri-icin-guvenlik-tartismasi": (
        "Banka ve ‘hemen yatır’ sesten doğrulanmaz",
        "Önceden kelime veya görüntülü arama. 30 saniyelik örnek yeter. WhatsApp şakası yaşlıya gerçek gelir. Çağrı merkezi klonu sözleşmede rıza ve saklama ister. Filigran her zaman duyulmaz. Başkasının sesi rızasız ihlaldir.",
        "Aile kuralı",
        "Para talebi sesten geçmez. Klon demo değil dolandırıcılık konusudur.",
        "Ses klonu rıza ve kırmızı çizgidir.",
    ),
    "teknoloji-alisverisinde-garanti-ve-servis-destegi-neden-onemli": (
        "14. ay, kasa anından pahalıdır",
        "1500 TL indirim, ekran arızasında kargo ve ‘ithalatçı biz değiliz’ ile biter. Faturada unvan, IMEI, servis listesi. Elden kutu fotoğrafı kanıt değildir. Laptop yerinde servis, kulaklık swap. PDF fatura. Gri ithal aynı kutu değildir.",
        "İl yazın",
        "Kapıdaki yetkili yoksa iki yıl kâğıttır. Kampanya servis haritasıyla okunur.",
        "Garanti 14. aydır. Vitrin indirimi değildir.",
    ),
    "verimlilik-uygulamalari-gunluk-planlamayi-kolaylastiriyor": (
        "Üç yerde duran liste hiç durmaz",
        "Görev bir yerde, takvim bir yerde, dosya bir yerde. 30 dakikada taşıyamıyorsanız araç ağırdır. Cuma 15 dakika arşiv yoksa kanban mezarlığıdır. Ders ve iş aynı tahtada akşamı işe çevirir. Bildirim her onayda planı böler.",
        "5 kişi",
        "Durum alanı yoksa sohbet dağılır. 30 kişide araç proje olur. Uygulama sizi planlamaz.",
        "Tek sistem kuralı özellik yarışından değerlidir.",
    ),
    "kamera-odakli-akilli-telefonlar-sosyal-medya-kullanicilarini-hedefliyor": (
        "Hikâyede 200 MP görünmez, ışık görünür",
        "Gece modu 3 saniye tutmayı ister. Log çekim uygulama filtresiyle bozulur. Ham yedek yoksa bir akşamlık profesyonelliktir. Canlı yayın ısıtır. İki telefon renkleri aynı hikâyede kırılır. 256 GB 4K rulo için 128’den değerlidir.",
        "Sokak testi",
        "Mağaza ışığı yalan söyler. Sosyal kamera megapiksel yarışı değil ışık, renk ve yedektir.",
        "Hikâye ışığı vitrin karesinden değerlidir.",
    ),
    "teknoloji-gundeminde-bugun-one-cikan-basliklar": (
        "Öğle sızıntısı yok",
        "Sabah 8 dakika resmi blog + bir analiz. Akşam yarın karar vereceğiniz tek başlık. 40 sekme kaygıdır. Geliştirici kota, tüketici fiyat, yönetici risk okur. Aynı cümle üçüne hizmet etmez. Kaynağı resmi olmayanı güne yazmayın.",
        "Üç başlık",
        "Cihaz/fatura, resmi kaynak, bu hafta karar. Gündem her şeyi bilmek değil yarını değiştirmektir.",
        "20 maddelik özet hiçbiri okunmayan özettir.",
    ),
    "windows-pc-kullanicilari-icin-performans-ipuclari": (
        "Temizleyici ikinci zararlıdır",
        "Ana sayfa kaçtıysa reset ve Defender. Başlangıç 30 program, disk %90, 90 derece. Dengeli güç planı. Sürücü üretici sitesi. HDD’ye SSD en büyük sıçrama. 8 GB 2026’da yetmez. GPU 1080p yoksa acil değildir.",
        "Kayıt defteri",
        "Temizleyici yedeksiz siler. Hız açılış, boş disk ve kasadır.",
        "Yirmi numara listesi dolu diski düzeltmez.",
    ),
    "yeni-nesil-telefon-bataryalari-daha-uzun-omur-hedefliyor": (
        "120 Hz HDR, mAh’den hızlı yer",
        "Gezi günü 60 Hz bir saat kazandırır. 120W kılıfta ısı tuzağıdır. 80–20 yazılımı yoksa 85 prizi. Soğukta yüzde 1 kapanma kalibrasyondur. Tam boşaltma ni-cad alışkanlığıdır. 24 ay takas, değiştirilemeyen bataryada karardır.",
        "Gece 100",
        "Kilitlemeyin. Ömür döngü ve ısıdır, watt tablosu değil.",
        "Batarya gece prizi alışkanlığıdır.",
    ),
    "gelisim-ekipleri-icin-yeni-kodlama-araclari-tanitildi": (
        "Monorepo demosu stüdyo reposu değildir",
        "Lisans, veri yeri, offline, lockfile, koltuk mu token mı. SSO yoksa şirket standardı olamaz. 10 sağlam testi taşıyamıyorsa geçmeyin. Öğrenci ücretsiz, iş ayrı kira. Belirsiz lisans kapalı ürüne yapışmaz.",
        "Snippet",
        "Eski kısayol bir hafta yer. Yeni araç sır, lisans ve testten sonra gelir.",
        "Vitrin hızı ekibe alma listesi değildir.",
    ),
    "laptoplarda-yapay-zeka-islemcileri-daha-fazla-kullanilacak": (
        "Görev yöneticisinde NPU yoksa TOPS vitrindir",
        "Altyazı ve bulanıklık NPU’da ucuz, 4K kurgu GPU’dadır. Linux sürücüsü geç gelir. 16 GB lehimli yerel model + tarayıcıda daralır. Toplantı için NPU evet, her işi hızlandırmaz. ‘Yapay zekâlı laptop’ kurgu kasası değildir.",
        "32 GB",
        "RAM lehimliyse şimdi düşünün. NPU kime lazım sorusudur.",
        "TOPS tablosu uygulama kullanmıyorsa boştur.",
    ),
    "telefon-alirken-dikkat-edilmesi-gereken-en-onemli-ozellikler": (
        "Açılmamış kutu başka TC’ye kayıtlı olabilir",
        "IMEI faturada, iCloud/Google kilit kapalı. Yama yılı üretici sayfasından. 5G kapsama yoksa pil yer. IP deniz suyu değildir. 120 Hz 60 seçeneği yoksa gezi yer. Gri ithal servis farklıdır.",
        "Dilimler",
        "Giriş 3 yıl yama, orta 5–7, üst tamir parçası. İyi telefon üçüncü yılında yama alandır.",
        "Megapiksel dördüncü sıradır.",
    ),
    "yapay-zeka-araclari-is-dunyasinda-yeni-verimlilik-donemi-baslatti": (
        "Hukuki onay 10 gün, taslak 10 dakika",
        "E-posta ve kod iskeleti hızlanır. Rakam ve taahhüt hızlanmaz. Tüketici modele NDA yapıştırmak ihlaldir. Şirket kira ve bölge yoksa herkesin ChatGPT’si politika olamaz. Revizyon arttıysa stajyer faturasıdır.",
        "30 gün",
        "Pazarlama evet, fiyat teklifi hayır. Eğitim lisans kadardır. Dakika kısalır, sorumluluk kısalmaz.",
        "Ajan slaytı onay yavaşlığını silmez.",
    ),
    "egitimde-yapay-zeka-destekli-calisma-araclari-yayginlasiyor": (
        "Olmayan makale dipnot faciasıdır",
        "Kavramı sordur, ödevi yazdırma. Quiz üret, cevabı sonra göster. Dil pratiği evet, sınav yazısı hayır. Okul maili, sohbet silinsin, fotoğraf yüklenmesin. Politika kâğıtta yoksa araç öğrenci aleyhine işler.",
        "Öğretmen",
        "Nerede serbest nerede yasak yazılsın. AI tembel arkadaştır, öğretmen değildir.",
        "Açıklama evet. Ödev hayır.",
    ),
    "donanim-pazarinda-fiyat-ve-performans-dengesi-degisiyor": (
        "1080p monitörde 4K kart ısınır",
        "Sıra monitör, FPS, CPU, PSU, kasa. 16 GB idare, 32 varsayılan. Faturasız ikinci el madencilik taşır. 3 fan dar kasada kısılır. Ofiste iGPU yeter. Sessiz evde fan RGB’den önemlidir.",
        "24 ay",
        "Watt ve garanti slayt FPS’inden değerlidir. En yeni almak çözünürlüğü yok saymaktır.",
        "Kart masadaki watt ile ölçülür.",
    ),
    "katlanabilir-telefonlarda-2026-rekabeti-hizlandi": (
        "İç cam ev tipi koruyucu değildir",
        "Tamir fiyatını sorun. Toz menteşede birikir. Uygulama açık-kapalı tam düzen vermeyebilir. PDF okuyan tableti sevmeyene iç ekran işe yarar. Tek cep isteyene kayrak az pişmanlıktır. İkinci cihaz olarak daha az risk. Sigorta primi iki yılda kasa farkını yer. Menteşe ve düşme ayrı maddelerdir.",
        "Unpacked",
        "Vitrin menteşe ömrü ve cam faturasıyla okunur.",
        "Katlanır gelecek vitrinidir. Masada cam faturasıdır.",
    ),
    "bilim-kurgu-filmi-ilk-fragmaniyla-dikkat-cekti": (
        "90 saniye 130 dakikayı kanıtlamaz",
        "Erken fragman bitmemiş sahne taşır. Renk son hali değildir. Tarih pencereyse ön satış bağlanmaz. Aynı yönetmen çekim ölçeğini değiştirmiş olabilir. Çocukta yaş etiketi fragmanın değil filmin. Efekt karesi hikâye değildir.",
        "İkinci fragman",
        "Beklemek ilk 90 saniyeye bütçe bağlamaktan ucuzdur. Fragman davettir.",
        "Ton, yüz, tarih. Sözleşme değil.",
    ),
    "yayin-platformlari-yaz-kataloglarini-guncelliyor": (
        "Üç platformun en iyi yazı olamaz",
        "Günde 3 saat tatil evi hariç ayın yıldızı hangisindeyse o açılır. Çocuk yazı animasyon, spor ayrı fatura. Ayın 1’i tek dizi veya 3 film, 25’i uzatma. Yıllık yazın üç ayı için pahalı kilit olabilir. Offline yoksa katalog yolda işe yaramaz.",
        "30 gün",
        "Yaz kataloğu sizin ayınızdır, stüdyo vitrini değil.",
        "Ayda tek kapı çoğu ev için yeter.",
    ),
    "gorsel-uretme-araclari-tasarim-surecini-degistiriyor": (
        "1:1 ve 16:9 ayrı üretilir",
        "Kırmak yüzü yer. Tipografi modele bırakılmaz. 8–12 taslak, insan 2’yi düzeltir, ürün fotoğrafı sona. Ünlü yüz ve rakip logo ilham değildir. Temiz stok belirsiz modelden az risklidir. Onay kutusu editördedir, araçta değil.",
        "Gece yayını",
        "Kim onayladı yoksa marka yanar. Moodboard motoru sanat yönetmeni değildir.",
        "Prompt marka kılavuzu değildir.",
    ),
    "ofis-bilgisayari-alirken-nelere-dikkat-edilmeli": (
        "20 cihazda 1 yedek PSU bir gün kurtarır",
        "Aynı model aynı BIOS aynı imaj. OEM Windows cihazla ölür. iGPU ofis yeter, CAD ayrı listedir. Mini kasa toz temizliği zorlaştırır. Dizüstü isteyen hibrit: mini PC + paylaşılan monitör, herkese oyun laptopundan ucuzdur. TPM, 3 yıl yerinde, iki ekran, sessiz fan.",
        "RGB",
        "Muhasebede toz ve gürültü. Ofis 36. ayda açılan kutudur.",
        "FPS slaytıyla ofis alınmaz.",
    ),
    "yapay-zeka-destekli-arama-motorlari-klasik-aramayi-zorluyor": (
        "2024’te kalktı dediği 2026’da dönmüş olabilir",
        "Tarih resmi sayfadan. İki kaynak çelişiyorsa üçüncü. Ödev ve müşteri notunda yapıştırma. Şirket metnini kutuya sokmayın. Tarif ve terim evet, hukuk/sağlık/fiyat hayır. PDF ve hata kodu klasik listede kalır.",
        "Dipnot",
        "Giriş dakikayı kısaltır. Karar tıklayanındır.",
        "Akıcı cevap doğrulanmış cevap değildir.",
    ),
    "api-kullaniminda-hiz-ve-guvenilirlik-neden-onemli": (
        "Retry körse kendinizi DDoS’larsınız",
        "p95, kota, 90 gün kesinti. SLA kredi nasıl işliyor. Webhook imzası ve idempotency yoksa çift tahsilat sizde. Anahtar mobildeyse kota başkasının. Fiyat tepe saatinizle çarpılsın. Küçük ekip yönetilen kuyruk, büyük ekip çok sağlayıcı.",
        "Jitter",
        "Ortalama milisaniye fatura günü değildir. API hata yüzdesidir.",
        "Demo p95 değildir.",
    ),
    "yeni-film-ve-dizi-takvimi-izleyiciler-icin-hareketli-geciyor": (
        "12 prömiyer 6 saati 12’ye bölmez",
        "Pazartesi tek dizi, Cuma tek film. Top 10 ülke tıklamasıdır. Belgesel ve komedi aynı akşam ölür. Aboneliği iki başlık için açıp bitince kapatmak yıl boyu tutmaktan ucuz olabilir. Spoiler kare zevki çalar.",
        "Yaş",
        "Çocuklu evde süre ve etiket kritik beğeniden önce. Takvim elemektir.",
        "Ayda 2 başlık. Yığın değil.",
    ),
    "ekran-teknolojilerinde-parlaklik-ve-enerji-verimliligi-yarisi": (
        "Vitrin canlı profili evde abartılıdır",
        "Film ve oyun ayrı profil. Dinamik ikisini bozar. Otomatik parlaklık OLED izini azaltır; 100’e kilitlemek paneli yer. Yansıma nit kadar şikâyettir. HDR içerik yoksa nit israftır. Oyun monitöründe Hz, HDR’dan önce gelebilir. Odayı akşam görün.",
        "Mağaza",
        "Işık ev lambası değildir. Parlaklık odaya göre araçtır.",
        "2000 nit perdeli odada göz yorar.",
    ),
    "siber-guvenlik-yamalarini-geciktirmek-buyuk-risk-olusturuyor": (
        "Yazıcı da ağdadır",
        "48 saat: OS, tarayıcı, VPN, yönlendirici, telefon. Yedek önce, yönlendirici gece. NAS aynı ağda tek kopya yedek değildir. Windows 10 yamasız kutu bankacılık için ayrı ağ veya emekli. 1 PC dene, 20’ye basma.",
        "Botnet",
        "Ertelemek kira vermektir. Yama kahramanlık değil sıra listesidir.",
        "Sonra bakarım taramadır, hedef seçmez.",
    ),
    "yeni-nesil-dizustu-bilgisayarlar-daha-hafif-ve-guclu-geliyor": (
        "Adaptör 400 gram, gövde 1.1, çanta 1.5",
        "28W ince kasada kısılır. 2 saat toplantı ısısı Cinebench değildir. RAM 16 lehimli tavan olabilir. Tek SSD yuva. Dokunmatik yansıma ve pil yer. Öğrenci 8 saat gerçek, ofis USB-A, üretim 32 GB. Menteşe tamir fiyatı.",
        "Oyun ince",
        "Gürültü ve 90 dakika pil. Hafiflik toplam gram ve 2. saatteki fanıdır.",
        "İnce kasa TDP mucizesi değildir.",
    ),
    "yerli-girisimler-yapay-zeka-destekli-cozumler-gelistiriyor": (
        "Yerli etiket sunucu ülkesini yazmaz",
        "Veri nerede, hata kim imzalıyor, iptalde dump. Kamu ve sağlıkta dil ve konum şartnamedir. Perakende chatbot SSS’nin pahalısı olabilir. Demo sizin faturanızla. Token değil koltuk. Model başkasının API’siyse arayüz yerlidir, çözüm değil.",
        "Referans",
        "İlk müşteri slayttaki büyük modelden değerlidir. Etiket çözüm değildir.",
        "Üç soru yeter. İsim listesi yetmez.",
    ),
    "mini-pc-modelleri-ev-ve-ofis-kullanimi-icin-yayginlasiyor": (
        "120 Hz monitör DisplayPort ister",
        "İki HDMI 4K 60 yetmeyebilir. RAM 16 lehimli 2026 dar. Tek NVMe yedek koymaz. Idle watt salonda FPS’den önemlidir. VESA masayı boşaltır. BitLocker/TPM ofiste. 7/24 ev sunucusu düşük watt. Oyun eGPU ise kule dürüsttür. Lisans Home mu etiket mi.",
        "Doğru iş",
        "Sessiz kahraman. Yanlış iş ısınan kutu.",
        "Cep boyu kasa AAA watt’ı taşımaz.",
    ),
    "cumhurbaskani-erdogandan-yapay-zeka-aciklamasi-dunya-keskin-bir-donusumden-geciyor": (
        "Kendi KVKK cümlenizi siyaset metninden çıkarmayın",
        "AcarTechs resmi açıklamayı aktarır, model zorunluluğu eklemez. Yatırım vurgusu yarınki fiyatı kilitlemez. Okul ve şirket, insan onayı ve veri kuralını kendi kâğıdına yazar. ‘Devlet böyle dedi’ diye müşteri verisi yapıştırılmaz.",
        "Ürün belgesi değil",
        "Çerçeve gündemdir. Uygulama kılavuzu sizin politikanızdır.",
        "Siyasi metin slayt vaadi değildir.",
    ),
    "e-spor-turnuvalarinda-final-haftasi-heyecani-basladi": (
        "Patch dün geldiyse grup formu sıfırdır",
        "BO3/BO5, kadro yedeği, 30–90 sn yayın gecikmesi. Sosyal spoiler yayından önce gelir. Çocukta chat kapalı. Bahis overlay kapatılır. VOD gece 3 maçından değerlidir. AcarTechs bahis dili yazmaz.",
        "Resmi yayın",
        "Korsan overlay aynı maç değildir. Final format ve yama ile okunur.",
        "Afiş skoru okumaz.",
    ),
    "google-i-o-2026-gelistirici-oturumlarinda-yapay-zeka-araclari-one-cikti": (
        "Keynote sprint backlog’u değildir",
        "Android, web, Cloud, Gemini aynı saatte. Yalnızca derlemeyi kıran veya kota değiştiren alınır. Demosu SLA değildir. Onay tuşu ve test olmadan ajan dönemi tehlikelidir. Resmi blog, Twitter karesinden önce. Kullanıcıya ‘I/O oldu’ yazılmaz.",
        "İstek listesi",
        "Gerisi yarın. I/O süzgeçtir, yığın değildir.",
        "Her madde bu haftanın işi değildir.",
    ),
    "cihaz-ici-yapay-zeka-ajanlari-telefon-ve-bilgisayarlarda-yeni-donemi-aciyor": (
        "Otomotiv yığını telefonla aynı değildir",
        "Qualcomm–Hugging Face hibrit kapısıdır. Uçak modunda durmayan yerel değildir. NPU kullanılmıyorsa TOPS vitrindir. Ödeme ve e-posta onay ister. Isınma ve disk yer. Gizlilik kazancı, büyük model bulutta kalır.",
        "Lisans",
        "Açık modeli cihazda çalıştırmak kota ve ısınma bütçesidir. Hibrit varsayılan bulut demek değildir.",
        "Ajan sohbet kutusunun ad değiştirilmiş hali değildir.",
    ),
    "konsol-oyunculari-icin-sistem-guncellemesi-yayinlandi": (
        "Akşam 18 maçı 17:50 yaması kilitleyebilir",
        "Depolama %20, gece indir, parti sohbeti kırıldı mı. Insider ürün vaadi değildir. Çocukta yeni paylaşımı kapatın. Bulut kayıt kapalıysa yedek alın. Emoji çekirdek yamayı geciktirmez. İkinci elde fabrika ve ağ şifresi ayrıdır.",
        "Beta",
        "Maç öncesi kanala geçmeyin. Güncelleme kontrol listesidir.",
        "Sosyal vitrin yama değildir.",
    ),
    "yeni-cikacak-aksiyon-oyunu-icin-ilk-oynanis-videosu-geldi": (
        "HUD kapalı çekim mağaza HUD’u değildir",
        "40. dakika tekrar döngüsü 90 saniyede gizlenir. 30 fps kayıt 60 vaadi değildir. Demo yoksa davettir, ölçüm değil. Performans hedefi hangi modelde yazıyor bakın. Müzik hilesi ses kapalı ele gelir. Ön sipariş ikinci video ve süre tahmininden sonra.",
        "Pencere tarih",
        "Belirsiz yazın. Oynanış kameradan gerçektir, 12 saat kanıtı değil.",
        "İlk video satın alma emri değildir.",
    ),
    "xbox-insiders-icin-gamertag-oyun-merkezi-ve-istek-listesi-guncellemeleri-geldi": (
        "Çocuk hesabı beta’ya alınmaz",
        "Halkadan çıkmak sürümü geri almayabilir. ‘Gelebilir’ takvime işlenmez. Çok oyunculu öncesi kanal değiştirmeyin. Hub resmi yoldur. Özellik ring’de yoksa skandal değildir. Test notu ürün gibi satılmaz.",
        "Aile",
        "Insider ciddiye alınır, satın alma gerekçesi değildir.",
        "Halka vitrin değildir.",
    ),
    "sosyal-medya-uygulamalarinda-guvenlik-ozellikleri-artiyor": (
        "2019 bağlı oyunu silin",
        "SMS 2FA değil uygulama. Oturum listesinden yabancı cihaz. Konum ve yüz etiketi kapat. Kurtarma e-postasını güncelle. Güvenli klasör yedek kod kâğıtta yoksa kilitler. Veri indirme 48 saat; öfke silmek arşivi yakar. İş maili kişisel fotoğrafla karışmasın. Çocukta mesaj çevresi daralsın.",
        "Varsayılan",
        "Yeni kilit kapalı kutudur. Açılmazsa süslemedir.",
        "Güvenlik özelliği varsayılanı kapatmaktır.",
    ),
    "haftanin-oyun-firsatlari-ve-ucretsiz-yapimlari-aciklandi": (
        "Kütüphaneye ekle, diski doldurma",
        "Süre bitmeden eklemek yeter. 80 GB 2 saatlik deneme pahalıdır. Üçüncü site anahtarı çalıntı hesap satar. Çocukta harcama onayı. 12 oyun kuyruğu üç ay güncelleme doğurur. Aile paylaşımında ücretsiz bir koltuğa bağlı kalabilir.",
        "Resmi mağaza",
        "Forum kodu değil. Fırsat keşiftir, disk emri değil.",
        "Ücretsiz yazısı süre ve kaynak olmadan tuzaktır.",
    ),
    "elektrikli-araclarda-sarj-altyapisi-rekabeti-hizlandi": (
        "Apartman prizi yoksa 350 kW kahraman değil zorunluluktur",
        "İş 11–22 kW ev yatırımını erteleyebilir. Koridor, ödeme uygulaması, arızalı soket kW’dan önemli. Soğuk ve otoyol menzili %20–30 keser. İkinci el batarya raporu olmadan ucuz kilometre değildir. Küçük batarya + ev prizi şehir ikinci araçta sakin hayattır. Yönetime sormadan sipariş avlu kablosudur.",
        "Uygulama",
        "İlk otoyoldan önce kurun. Şarj gecenizin prizidir.",
        "Pano kW’si günlük hayat değildir.",
    ),
    "xbox-22-26-haziran-haftasinda-cikacak-yeni-oyunlari-listeledi": (
        "Üç büyük indirme 512 GB’ı tıkar",
        "Core ile Ultimate aynı kapı değil. Dil ve bulut kayıt mağaza sayfasında. 30 dakikalık indie ile 40 saat kampanya aynı ihtiyaç değil. Cloud’da dene. Yaş ve harcama pimi liste heyecanından önce. Bir indir, iki istek listesi.",
        "FOMO",
        "Haftalık Wire keşiftir, fiş değildir.",
        "Kısa pencere seçici indirmedir.",
    ),
}


def boost_html(h2a, a, h2b, b, close) -> str:
    return (
        f'\n<section class="acartechs-boost">\n'
        f"<h2>{h2a}</h2>\n<p>{a}</p>\n"
        f"<h2>{h2b}</h2>\n<p>{b}</p>\n"
        f"<p>{close}</p>\n"
        f"</section>\n"
    )


def insert_boost(slug: str, parts: tuple[str, str, str, str, str]) -> None:
    path = ROOT / slug / "index.html"
    html = path.read_text(encoding="utf-8")
    if "acartechs-boost" in html:
        print("skip boost", slug)
        return
    extra = boost_html(*parts)
    m = BODY_RE.search(html)
    if not m:
        print("no body", slug)
        return
    inner = m.group(2)
    if 'class="acartechs-source-note"' in inner:
        inner = re.sub(r'(<p class="acartechs-source-note")', extra + r"\1", inner, count=1)
    else:
        inner = inner.rstrip() + extra
    html = html[: m.start()] + m.group(1) + inner + m.group(3) + html[m.end() :]
    path.write_text(html, encoding="utf-8")
    print("boosted", slug)


def main() -> None:
    dups = set(DUPLICATES) | set(MORE_DUPLICATES)
    n = 0
    for slug, parts in BOOST.items():
        if slug in dups:
            continue
        p = ROOT / slug / "index.html"
        if not p.exists():
            print("missing", slug)
            continue
        w = len(text_of(p.read_text(encoding="utf-8")).split())
        if w >= 350:
            continue
        insert_boost(slug, parts)
        n += 1
    print("boosted count", n)


if __name__ == "__main__":
    main()

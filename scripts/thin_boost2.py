# -*- coding: utf-8 -*-
"""Third unique pass for remaining unique articles under 300 words."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from thin_boost import BODY_RE, ROOT

B2 = {
    "google-finance-yeni-uygulama-ve-portfolyo-ozellikleriyle-guncellendi":
        "Portföy ekranındaki yeşil çizgi, sizin al-sat emriniz değildir. Gecikmeli veri, bildirim FOMO’su ve sahte mağaza ikizi bu güncellemenin asıl riskleridir. Resmi paket adını doğrulayın, iş telefonunda kişisel izleme listesi açmayın, vergi kaydını broker uygulamasında tutun. Finance izleme kutusudur; lisanslı tavsiye ve teminat hesabı başka kapıdadır.",
    "openai-model-davranislarini-yayin-oncesi-simule-eden-yeni-yontemini-anlatti":
        "Simülasyon, ajanın ödeme ve e-posta adımında durdurma tuşu yoksa sizi kurtarmaz. Kendi ürününüzde yetki aşımı, sonsuz döngü ve prompt sızıntısı senaryosu yazın. ‘Laboratuvardan geçti’ cümlesi sağlık veya hukuk kararı gerekçesi olmaz. Deployment Simulation olgunluktur, sertifika değildir.",
    "openai-ajanlarin-is-dunyasindaki-etkisini-yeni-arastirmayla-anlatti":
        "Taslak süresi düşüp revizyon artıyorsa ajan her cümleyi yeniden yazdırıyordur; o noktada araç pahalı stajyerdir. NDA metnini tüketici ajanına yapıştırmayın. Fiyat teklifi ve hukuk kötü aday, kod iskeleti iyi adaydır. Araştırma hız ipucudur, sizin onay politikanızın yerine geçmez.",
    "samsung-vivatech-2026da-baglantili-bakim-vizyonunu-sergiledi":
        "Saat nabzı, telefon asistanı ve ev ekranı konuşuyorsa amaç, saklama süresi ve iptal ayrı yazılı olmalıdır. Çocuk ve yaşlı profilinde varsayılan paylaşımı kapatın. Fuar standı Türkiye fiyatı, yazılım yılı ve servis ilini göstermez. Connected care vizyondur; sicilsiz sağlık paylaşımı ürün değildir.",
    "disney-plus-the-doomies-icin-resmi-fragman-ve-yayin-tarihini-paylasti":
        "Fragmanı ses kapalı izlemek müzik hilesini ele verir. Yaş etiketini resmi başlık sayfasından okuyun; fragman sınırı filmin sınırı olmayabilir. Tarih pencereyse parti planı bağlamayın. Aynı hafta başka prömiyer varsa Doomies istek listesine düşebilir. Çocukta otomatik oynatmayı kapatın.",
    "google-arama-ai-mode-icin-gemini-3-5-flash-donemine-gecti":
        "Flash dünkü cevabı bugün kaydırabilir. Sayı ve tarihi resmi sayfadan tutun, iki kaynak çelişiyorsa üçüncüyü açın. Şirket metnini kutuya yapıştırmayın. Klasik link listesi PDF ve hata kodunda durur. AI Mode giriş hızıdır; dipnot ve sorumluluk tıklayanın işidir.",
    "netflix-haziran-2026-takviminde-yeni-diziler-ve-filmler-one-cikiyor":
        "Voicemails, Sweet Magnolias, Avatar ve belgeseller aynı 30 güne sığmaz. Pazartesi tek dizi, Cuma tek film, üçüncü istek listesi. Belgesel ile komediyi aynı akşama yığmayın. Yıllık kilidi yalnızca haziran yıldızına bağlamayın. Takvim ne gelecek, Top 10 ne tıklandı; ikisi de zevkiniz değildir.",
    "openai-patch-the-planet-ile-acik-kaynak-guvenligine-ai-destegi-veriyor":
        "Bin kırmızı issue, triyaj olmadan bakıcıyı yakar. Sorumlu açıklama tweet’ten önce gelir. Sizin 48 saatlik OS-tarayıcı-yönlendirici kuralınız bu programdan düşmez. Lockfile ve tek bakıcı riski hâlâ sizin listenizdir. AI taslak avcısıdır, yama imzası insandadır.",
    "github-copilot-ucretsiz-ve-ogrenci-planlarinda-otomatik-model-secimine-geciyor":
        "Kota bitince model sessizce zayıflar; bunu ‘bozuldu’ sanmayın. Ödevde hangi modelin cevap verdiği kaydı yoksa tekrar üretilemez. İş reposunu okul hesabına bağlamayın. Otomatik seçim kapatılabiliyorsa kritik yamada sabitleyin. Açıklama evet, bitmiş ödev hayır.",
    "github-desktop-3-6-worktree-ve-copilot-entegrasyonunu-genisletti":
        "İki worktree iki node_modules indirir; önce küçük depoda deneyin. LFS ve satır sonu Windows’ta sürpriz üretir. Copilot commit mesajı taslaktır, nedeni siz yazın. Rebase çatışmasında CLI utanç değildir. Müşteri sırrı PR taslağına yapışmaz. Monorepo’da kaynak hâlâ CI’dır.",
    "netflix-haftalik-top-10-listesinde-i-will-find-you-zirveye-yerlesti":
        "15 Haziran zirvesi 8 bölüm borcu değildir. 1. bölüm yetmiyorsa bırakın. Gerilim ve belgeseli aynı akşama koymayın. Yaş etiketini çocuk profilinde ‘birinci’ cümlesinden önce okuyun. Zirve için yıllık kilitlemeyin. İlk hafta tıklaması üçüncü hafta kalıcılığı kanıtlamaz.",
    "microsoft-agent-365-ile-kurumsal-yapay-zeka-ajanlarini-yonetmek-istiyor":
        "Kaç ajan, hangi kimlik, hangi SharePoint ve mailbox yazılmamışsa POC sızıntıdır. EDR/DLP yerine geçmez. Test tenancy, müşteri verisi yok, onaysız gönderim yok. ‘Kullanın’ demek gizli klasörü prompt’a davettir. Gölge ajan 2026’nın gölge IT’sidir.",
    "openai-partner-network-ile-yapay-zeka-projelerinde-is-ortagi-donemi-basladi":
        "Rozet veri bölgesini, alt işlemciyi ve eğitimde kullanımı yazmaz. Demo sizin fatura PDF’inizle çalışsın. İptalde dump 7 günde gelmiyorsa kilitlenirsiniz. İlk 30 gün tek süreç: SSS veya randevu. Token sürprizi koltuk+destekle konuşulsun. Partner kapıdır, teslimat sizin kabulünüzdür.",
    "samsung-galaxy-watch-icin-yapay-zeka-destekli-saglik-ozelliklerini-duyurdu":
        "14 günlük eğilim, tek kötü geceden değerlidir. Kayış gevşekse nabız yalan söyler. Veri ülkesi ayrı gizlilik kararıdır. Her gece şarj uyku takibini yarım bırakır. Kırmızı uyarıda hekim. Telefondaki Galaxy AI ile saat kartı aynı izin kutusunu paylaşabilir; ayrı okuyun. Saat eğilimdir, teşhis değil.",
    "cloudflare-workflows-icin-saga-rollback-destegi-geldi":
        "Stok düştü ödeme çekildi kargo 500: telafi yazılmamışsa rollback slayttır. Idempotency yoksa çift iade doğar. Para hareketinde insan kuyruğu bırakın. Log olmadan gece üçü kördür. Tek veritabanı saga istemez. Rollback yazdığınız geri fonksiyon kadardır.",
    "disney-plus-haziran-listesinde-avatar-fire-and-ash-promiyeri-one-cikiyor":
        "Üç saatlik oturum çocuk ara vermeden bitmez. Prömiyer 4K kotası zayıf Wi-Fi’de düşer; HD utanç değildir. İndirme hakkı katmana bağlıdır. Yalnızca bu film için yıllık kilitlemeyin. Bu ay Avatar artı bir kısa başlık, üçüncü istek listesi. Prömiyer vitrindir, 30 gün karardır.",
    "whatsapp-kullanici-adi-rezervasyonunu-baslatti":
        "Yalnızca resmi uygulama: Ayarlar, Hesap, Kullanıcı adı. Sahte rezervasyon sitesine gitmeyin. Bir harf farkı yaşlıya borç mesajı atabilir. Anahtarı ailede konuşun. Fotoğraf ve durum satırı numara gizlense de kimlik sızdırır. İş hattı ayrı ad. Kademeli açılış skandal değildir.",
    "google-haziran-pixel-drop-ile-gemini-ve-yaratici-araclari-genisletti":
        "128 GB’da üç AI video dolar. Çeviri toplantı gündemini sunucuya gönderebilir. Floating bubbles bankacılıkta yanlış tıklar. Kılıf içinde ısınır. Model listesini resmi Pixel sayfasından okuyun. Yamayı özellik için ertelemeyin. Komşuda var skandalı değildir.",
    "openai-ve-broadcom-yapay-zeka-icin-jalapeno-inference-cipini-tanitti":
        "Jalapeno bu gece telefona inmez. Inference faturasıdır, eğitim ayrıdır. HBM baskısını sihirle bitirmez. Kota ve yavaş cevap yoğun saat artı silikon artı modeldir. Evde kutu alım gerekçesi değildir. Token fiyatını SLA ve bölge ile okuyun. Yol haritasıdır, cep duyurusu değil.",
    "android-studio-quail-1-yapay-zeka-destekli-hata-analizini-guclendirdi":
        "Yarış durumu ve cihaz sürücüsünde ajan özgüvenli uydurur. Diff’te üç satır bağımlılık şişebilir. Üretim yığınını kişisel modele yapıştırmayın. Insights stajyer hesabında açık kalmasın. CI kırmızısı özgüvenden değerlidir. Açıklama taslak, merge emri değil.",
    "chatgpt-icin-yeni-saglik-zekasi-guncellemesi-duyuruldu":
        "Tahlil maddesi ne, hekime ne sorayım doğru; tanı koy ilaç yaz yanlış. Gebelik, çocuk dozu ve acil 112’dir. Paylaşılan cihazda sohbet bırakmayın. Uydurma kaynak sıfırlanmaz. Daha yararlı cevap reçete değildir. Süreçtir, hastane sistemi değil.",
    "microsoft-windows-10-esu-suresini-kullanicilar-icin-uzatti":
        "ESU özellik güncellemesi değil yama kirasıdır. TPM’siz kutu ömür boyu güvende değildir. Bankacılık yamasız 10’da ayrı ağda veya emekli. Kaç cihaz 11, hangisi ESU yazın. 1 PC dene, 20’ye basma. Yedek yamadan önce. Yaşam döngüsü sayfasını işaretleyin.",
    "netflix-haftanin-izlenecek-yapimlarini-yeni-listeyle-paylasti":
        "Color Book ile American Experiment aynı geceye sığmaz. Avatar yaş etiketine bağlıdır. Dört adı cuma gecesine yığmak hiçbirini bitirmemektir. Editör seçkisi Top 10 değildir. İndirme yoksa yol listesi boştur. Bu hafta tek başlık, yarın istek listesi.",
    "cloudflare-oauth-akisini-tum-gelistiricilere-acti":
        "Tüm zone izni blog yazısı için gerekmez. Ajan dar kapsam ve süre ister. offline_access unutulmuş entegrasyonda sızıntı üretir. Revoke yoksa OAuth vitrindir. Mobilde sır gömmeyin. Kapsam listesini belgeye yazın. Anahtarı prompt’a yapıştırmayın.",
    "apple-yeni-app-store-araclariyla-gelistiricilere-daha-fazla-esneklik-sunuyor":
        "AB ve ABD vitrini aynı esneklik değildir. İnceleme kuyruğu durur. Kampanyayı bir hafta ölçün. Deneme bitişini takvime yazın. Aile paylaşımı fiyatı böler. Reddedilen meta yeni kutuyla kurtulmaz. Bölgede araç açık mı bakın. Çarpan, ürün yerine geçmez.",
    "android-gelistirici-dogrulamasi-uygulama-dagitiminda-yeni-donem-baslatiyor":
        "Hobi APK’sı ile ticari Play aynı kapı değildir. Bu çeyrek paket sürecekseniz kimliği şimdi başlatın. Öğrenci hesabını marka yapmayın. Paket adını kaptırmayın. Yan yükleme kimlik katmanının dışındadır. İç test panik gerekçesi değildir; ticari adı yine de koruyun.",
    "yazilim-gelistiriciler-icin-yapay-zeka-destekli-araclar-yayginlasiyor":
        "Belirsiz lisanslı üretilen kodu kapalı ürüne yapıştırmayın. Şirket kirası yoksa kişisel Copilot iş reposuna bakmasın. Testsiz merge yok. Diff bağımlılık şişirebilir. Öğrenci açıklama evet ödev hayır. CI kırmızısı model özgüveninden değerlidir. Sır sohbete gitmez.",
    "yapay-zeka-etiketi-uygulamalarda-daha-gorunur-olacak":
        "Kapatılabilen rozet dekorasyondur. Sohbet özeti, altyazı ve yüz güzelleştirme ayrı katmanlardır. Mağaza rozeti verinin işlendiği ülkeyi yazmaz. Çocuk uygulamasında varsayılan üretim kapalı olsun. Haberde etiket dipnot değildir. Hangi katman sentetik görünürse işe yarar.",
    "mobil-uygulamalarda-yapay-zeka-destekli-yeni-donem-basladi":
        "Uçak modunda durmayan özellik yerel değildir. Klavye tahmini cihazda, uzun sohbet bulutta olabilir. Fotoğraf yedek kutusu ayrıdır. İş telefonunda bulut AI’yi kapatın. NPU ısınması TOPS’tan önce gelir. Yerel yazısı verinin çıkmadığı anlamına gelmeyebilir.",
    "android-developers-sayfasinda-yeni-gelistirici-duyurulari-yayimlandi":
        "Haftada bir resmi news yeter. Studio derlemeyi bozar, Play kapıyı kapatır, yama cihazı ilgilendirir. Önizlemeyi kararlı sanmayın. Öğrenci ve ticari paket aynı doğrulamayı paylaşmaz. Twitter üçüncü kovadır. Kullanıcıya ‘sayfa yenilendi’ yazmak kopya envanterdir.",
    "android-haziran-drop-guvenlik-ve-kisisellestirme-ozelliklerini-buyuttu":
        "Sahte aramada resmi numaradan geri arayın, uygulama içinden değil. Photos kıyafet hangi sunucuda işleniyor bakın. iPhone paylaşımında görünürlük herkes toplantıda yabancı dosyadır. Yama Drop’tan ayrı inebilir. Pixel ve seçilmiş sürüm kademelidir. Komşuda var skandalı değildir.",
    "apple-wwdc26da-siri-ai-ve-yeni-apple-intelligence-donemini-tanitti":
        "Sahne demosu sizin model ve dil listeniz değildir. On-device ile Private Cloud ayrımını okuyun. Şirket metnini Siri’ye okutmak NDA sınırı olabilir. WWDC günü telefon hurdaya çıkmaz. Watch ve TV ayrı inebilir. İptal tuşu sahnede görünmez; asıl ürün odur.",
    "yapay-zeka-iceriklerinde-guven-ve-dogrulama-daha-onemli-hale-geldi":
        "Çalışmaya göre dipnotu tıklanmıyorsa yok sayın. Sayı tarih isim uydar. Görselde el bozuktur. Üç kaynak: model, resmi sayfa, bağımsız üçüncü. Şirket metnini kutuya sokmayın. Filigran görünmeyebilir; kim onayladı daha önemlidir. Emin duruş kanıt değildir.",
    "haftanin-teknoloji-firsatlari-listelendi":
        "Forum kuponu ölmüş olabilir, resmi sayfada deneyin. 23.59 sayacı her gün sıfırlanır. Gri kutu garanti farklıdır. Sepeti 24 saat bekletin. Faturada seri yoksa geçin. Açılmış kulaklıkta iade sıfırlanabilir. Fırsat iade günüdür, kasa yüzdesi değildir.",
    "sirketler-musteri-hizmetlerinde-yapay-zeka-asistanlarini-deniyor":
        "Kırk dakika sizi anlıyorum yakar. Kargo bota, öfke ve ödeme insana. İnsan tuşu her turda görünsün. Devri artıyorsa bot yanlış yerdedir. Ses kaydı rıza olmadan eğitim olmaz. Müşteri kaydını tüketici modele yapıştırmayın. Bot SSS keser, şikâyet yönetimi değildir.",
    "oyuncu-kadrosu-guclenen-yeni-dram-dizisi-tanitildi":
        "Afiş dolduran yüz hikâyeyi taşımaz. Showrunner değişimi tonu sıfırlar. 42 ile 70 dakika aynı akşam değildir. Haftalık ve toplu yayın ayrı borçtur. Kadro sızıntısı anlaşma değildir. İlk sezon bitmeden ikinci sezon şişirir. Yıldız 8 sezon taahhüdü değildir.",
    "populer-dizinin-yeni-sezon-tarihi-aciklandi":
        "Bu sonbahar izin günü bağlamaz. Türkiye kataloğu ABD’den sonra gelebilir. İlk bölüm özel gerisi aylar sonra olabilir. Toplu yayın hafta sonunu yer. Önceki sezon bitmeden yeni sezon arşiv borcudur. Spoiler kare resmi tarihten önce gelir. Pencere belirsiz yazılır.",
    "robotik-sistemlerde-yapay-zeka-kullanimi-genisliyor":
        "Gece vardiyası sessiz davranış değiştirir; sürüm kaydı yoksa kaza kördür. Hat kamerası yüz kaydeder, amaç yazılı olsun. İnsan varken kol çalışmasın. Demo tozlu hattı gizler. Acil stop ve çember akıllı kelimesinden önce gelir. Pilot hat yaya yolundan ayrıdır.",
    "teknoloji-alisverisinde-kampanya-donemi-basladi":
        "Son 2 adet her gün yenilenir. 14 gün önceki etikete bakın. IMEI faturada yoksa iade zorlaşır. Kapıda nakit fiş fotoğrafı o anda. Uzatılmış garanti ekranı kapsamıyorsa camdır. Kargo eşiği kasa farkını yer. Gri kutu kampanya sever. Fiyat geçmişi olmayan yüzde iddiadır.",
    "orta-segment-telefonlarda-fiyat-performans-yarisi-buyuyor":
        "200 MP gece sokağında görünmez. Para yama yılı batarya servistir. 120 Hz her zaman açık ödündür. PWM ve 80W kılıf ısınması vitrinde yok. 256 GB 128+buluttan ucuz olabilir. Gri ithal serviste çıkar. Gece testini sokağa çıkarın. Yama yılı megapikselden değerlidir.",
    "prime-video-haziran-2026-takviminde-vox-machina-ve-yeni-orijinaller-var":
        "Season 4 önceki üç sezonu bitirmiş izleyiciye aittir. Yarım 1. sezonla dördüncüye atlamayın. Yetişkin animasyonu çocuk profilinde açmayın. Yalnızca bu dizi için yıllık kilitlemeyin. Prömiyerde HD + indirme zayıf ağda 4K’dan iyidir. Vox Machina zorunlu maraton değildir.",
}


def main() -> None:
    n = 0
    for slug, para in B2.items():
        path = ROOT / slug / "index.html"
        if not path.exists():
            print("missing", slug)
            continue
        html = path.read_text(encoding="utf-8")
        if "acartechs-boost2" in html:
            continue
        extra = f'\n<section class="acartechs-boost2"><p>{para}</p></section>\n'
        m = BODY_RE.search(html)
        if not m:
            print("no body", slug)
            continue
        inner = m.group(2)
        if 'class="acartechs-source-note"' in inner:
            inner = inner.replace('<p class="acartechs-source-note"', extra + '<p class="acartechs-source-note"', 1)
        else:
            inner = inner.rstrip() + extra
        html = html[: m.start()] + m.group(1) + inner + m.group(3) + html[m.end() :]
        path.write_text(html, encoding="utf-8")
        n += 1
        print("b2", slug)
    print("boost2", n)


if __name__ == "__main__":
    main()

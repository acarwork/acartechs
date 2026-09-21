# -*- coding: utf-8 -*-
"""Unique 350+ word rewrites for thin news; extras for mid-length unique news."""
from __future__ import annotations

from apply_publisher_policy import ARTICLE_AD
from thin_extras import e

def n(title, description, dek, body):
    return {"title": title, "description": description, "dek": dek, "body": body}


def note(url, label):
    return f'<p class="acartechs-source-note">Resmi kaynak: <a href="{url}" target="_blank" rel="nofollow noopener">{label}</a></p>'


NEWS = {
    "android-developers-sayfasinda-yeni-gelistirici-duyurulari-yayimlandi": n(
        "Android geliştirici duyurusu nasıl takip edilir?",
        "developer.android.com/news akışını AcarTechs kopya özet değil; Studio, Play ve kimlik doğrulama süzgeci olarak okur.",
        "Haber sayfası her duyuruyu sizin sprint’inize yazmak zorunda değildir.",
        f"""
<p>Google, Android Developers haber sayfasında Studio, Play, güvenlik ve kimlik doğrulama duyurularını yayımlamayı sürdürüyor. AcarTechs bu sayfayı ‘yeni duyurular yayımlandı’ diye tekrar etmez. Asıl iş, hangi notun bu hafta sizin uygulamanızı değiştirdiğini ayırmaktır.</p>
<p>Üç kova yeter: 1) Android Studio ve SDK, derlemeyi bozar. 2) Play politikası ve geliştirici doğrulaması, mağaza kapısını kapatır. 3) Güvenlik yaması, kullanıcı cihazını ilgilendirir. Sosyal medyadaki ‘Android değişti’ karesi çoğu zaman bu üçünden birine indirgenmeden dolaşır.</p>
<h2>Sprint’e almadan önce</h2>
<p>Resmi sayfadaki tarih ve etkilenen sürüm satırını okuyun. Emülatör notunu üretim cihazı sanmayın. ‘Önizleme’ ile ‘kararlı kanal’ aynı takvim değildir. Öğrenci ve hobi hesabı ile ticari paket adı farklı doğrulama ister; duyuruyu ikisine birden yapıştırmayın.</p>
{ARTICLE_AD}
<h2>Takip ritmi</h2>
<p>Haftada bir, resmi news sayfası + Android Developers Blog yeter. RSS veya e-posta özeti, Twitter sızıntısından az gürültü üretir. Aynı gün üç duyuru varsa yalnızca derlemeyi kıran veya mağaza politikasını değiştiren maddeyi kopyalayın. Gerisi istek listesidir.</p>
<h2>Son kullanıcıya dolaylı etki</h2>
<p>Geliştirici aracı hızlanırsa uygulama daha az ısınır, daha az çöker. Bu dolaylıdır. Kullanıcıya ‘Android haber sayfası yenilendi’ diye yazmak, kopya envanterdir. AcarTechs, sayfayı süzgeç olarak tutar.</p>
<ul><li>Studio/SDK notunu sprint’e al</li><li>Play politika tarihini takvime yaz</li><li>Önizlemeyi kararlı sanma</li></ul>
<p>Android duyuru sayfası resmi kaynaktır. Yığın özeti değildir.</p>
{note("https://developer.android.com/news", "developer.android.com/news")}
""",
    ),
    "android-gelistirici-dogrulamasi-uygulama-dagitiminda-yeni-donem-baslatiyor": n(
        "Android geliştirici doğrulaması: kimlik, paket, hobi sınırı",
        "Google’ın kimlik ve paket adı kontrolünü AcarTechs korku dili değil; hobi, öğrenci ve ticari dağıtım ayrımı olarak okur.",
        "Geniş dağıtım, hobi hesabının varsayılanı değildir.",
        f"""
<p>Android Developers sayfasında güncellenen geliştirici doğrulaması, uygulama dağıtımında kimlik ve paket adı kontrolünün sıkılaşacağını gösteriyor. Google, öğrenci ve hobi geliştiriciler için sınırlı dağıtım seçenekleri sunarken geniş mağaza dağıtımı isteyenlerden kimlik ve paket kaydını tamamlamasını bekliyor. AcarTechs bunu ‘Android bitti’ diye yazmaz. Sahte uygulama ve paket adı taklidine karşı katmandır.</p>
<p>Hobi projesi, 20 kişilik kapalı test ve ticari Play yayını aynı kapı değildir. Kimlik belgesi ve paket sahipliği, ticari kapının bedelidir. Öğrenci hesabını ticari marka gibi kullanmak, ileride devir ve marka itirazında kilitlenir.</p>
<h2>Ne zaman acil?</h2>
<p>Bu çeyrek Play’e yeni paket sürecekseniz doğrulama sırasını (kimlik, D-U-N-S veya bireysel, paket adı) resmi sayfadan işaretleyin. Yalnızca iç test APK’sı dağıtan ekip için panik gerekmez; yine de paket adını başkasına kaptırmayın. Eski ‘unlisted’ alışkanlığı, yeni kuralla kapanabilir.</p>
{ARTICLE_AD}
<h2>Kullanıcı tarafı</h2>
<p>Doğrulama, mağazada sahte bankacılık uygulamasını zorlaştırabilir. Sihir değildir: yan yükleme ve sosyal mühendislik ayrı kapıdır. Kullanıcı hâlâ Play dışından APK alıyorsa kimlik katmanı onu tutmaz.</p>
<ul><li>Ticari paket için kimliği şimdi başlat</li><li>Hobi ile ticari hesabı karıştırma</li><li>Paket adını squatting’e bırakma</li></ul>
<p>Doğrulama, dağıtım kapısının anahtarıdır. Her Android kullanıcısının acil güncellemesi değildir.</p>
{note("https://developer.android.com/news", "developer.android.com/news")}
""",
    ),
    "android-haziran-drop-guvenlik-ve-kisisellestirme-ozelliklerini-buyuttu": n(
        "Android Haziran Drop: sahte arama, Photos, iPhone paylaşımı",
        "Google’ın Haziran 2026 Android Drop’unu AcarTechs özellik listesi değil; hangi telefonun ne zaman alacağı ve neyin bölgesel kaldığı olarak okur.",
        "Fake call uyarısı, kılık planı ve iPhone paylaşımı aynı günde her cihaza inmez.",
        f"""
<p>Google, Haziran Android Drop duyurusunda sahte arama (fake call) uyarıları, Google Photos üzerinden kıyafet planlama ve iPhone kullanıcılarıyla daha kolay fotoğraf paylaşımı gibi başlıklar açıkladı. AcarTechs duyuru metnini yeniden dizmez. Bu Drop, güvenlik yaması ile vitrin özelliğini aynı cümlede satar; ikisini ayırmak okurun işidir.</p>
<p>Sahte arama uyarısı, dolandırıcılık sesini sihirle bitirmez. Numara sahteciliği ve ‘bankanız arıyor’ senaryosu devam eder. Özellik, bilinen kalıpları işaretler. Ailede yaşlı kullanıcı için asıl iş, ‘aranınca geri arama, uygulama içinden değil’ kuralını konuşmaktır.</p>
<h2>Photos ve paylaşım</h2>
<p>Kıyafet planlama, kamera rulosunu stil asistanına çevirir. Gizlilik: kıyafet fotoğrafı hangi sunucuda işleniyor, yedekleme açık mı bakın. iPhone ile paylaşım, AirDrop hayali değil; Google’ın resmi paylaşım yolu ve hesap görünürlüğüdür. İki işletim sistemi arasında ‘herkes’ görünürlüğü toplantıda yabancı dosya davetidir.</p>
{ARTICLE_AD}
<h2>Cihaza inene kadar bekleyin</h2>
<p>Drop, Pixel ve seçilmiş Android sürümlerinde kademeli gelir. ‘Komşuda var bende yok’ skandalı değildir. Ayarlar > sistem güncellemesi, mağaza uygulaması ve bölge. Güvenlik yamasını özellik gelsin diye geciktirmeyin; yama Drop’tan ayrı inebilir.</p>
<ul><li>Sahte aramada geri arama kuralı konuş</li><li>Photos kıyafet işinin sunucusunu oku</li><li>Güncellemeyi kademeli bekle, yamayı erteleme</li></ul>
<p>Haziran Drop, sahte arama ve paylaşım katmanıdır. Her Android’e aynı gün inen sihir değildir.</p>
{note("https://blog.google/products-and-platforms/platforms/android/android-drop-june-2026/", "blog.google")}
""",
    ),
    "android-studio-quail-1-yapay-zeka-destekli-hata-analizini-guclendirdi": n(
        "Android Studio Quail 1: çöküş analizi, öneri, test şartı",
        "App Quality Insights içindeki yapay zekâ ajanını AcarTechs sihirli yama değil; bağlamlı açıklama ve insan onayı olarak okur.",
        "Crash açıklaması, merge emri değildir.",
        f"""
<p>Android Studio Quail 1 Haziran 2026 yama notları, App Quality Insights tarafında yapay zekâ ajan entegrasyonunu öne çıkarıyor. Geliştiriciler çöküş verisini kaynak koduyla birlikte analiz ettirip daha ayrıntılı açıklama ve düzeltme önerisi alabiliyor. AcarTechs bunu ‘artık hata yok’ diye yazmaz. Büyük kod tabanında nedeni arama süresini kısaltır; önerilen yama testsiz merge edilmez.</p>
<p>Çöküş, null, izin ve arka plan sınırı gibi tekrarlayan kalıplarda ajan iyi tahmin eder. Yarış durumu ve cihaz-özel sürücü hatasında özgüvenli uydurma yapabilir. Öneriyi diff olarak okuyun, tek satır ‘düzeltme’ bağımlılık şişirebilir.</p>
<h2>Play ve gizlilik</h2>
<p>Crash kaydı kullanıcı verisi taşır. Şirket kirası olmayan modele üretim yığını yapıştırmayın. App Quality Insights’ın hangi projeye bağlı olduğu, stajyer hesabında açık kalmamalıdır. Öğrenci projesi ile bankacılık uygulaması aynı sohbet geçmişini paylaşmaz.</p>
{ARTICLE_AD}
<h2>Ekip kuralı</h2>
<p>Ajan açıklaması PR açıklamasına taslak olur, kopyala-yapıştır kapanış olmaz. CI kırmızısı model özgüveninden değerlidir. Quail 1, hata ayıklama hızıdır. Kalite kapısı değildir.</p>
<ul><li>Önerilen yamayı testsiz merge etme</li><li>Üretim yığınını kişisel modele yapıştırma</li><li>Diff’i oku, tek satıra güvenme</li></ul>
<p>Yapay zekâ çöküş analizi bağlamlı yardımcıdır. Otomatik tamirci değildir.</p>
{note("https://developer.android.com/studio/releases", "developer.android.com/studio/releases")}
""",
    ),
    "apple-wwdc26da-siri-ai-ve-yeni-apple-intelligence-donemini-tanitti": n(
        "WWDC26 Siri AI: ekosistem, gizlilik, ne zaman elde?",
        "Apple Intelligence ve Siri AI duyurusunu AcarTechs sohbet uygulaması yarışı değil; cihaz listesi, dil ve on-device sınır olarak okur.",
        "Sahne demosu, sizin iPhone modelinizin takvimi değildir.",
        f"""
<p>Apple, WWDC26 kapsamında Siri AI ve yeni nesil Apple Intelligence deneyimlerini tanıttı. Duyurular iPhone, iPad, Mac, Apple Watch, Apple TV ve Vision Pro yazılımını kapsıyor. AcarTechs sahne cümlesini kopyalamaz. Asıl kırılım üçtür: hangi modeller, hangi diller, hangi işlem cihazda kalıyor.</p>
<p>Siri’nin daha bağlamsal asistan olması, her uygulamaya anahtar teslimi demek değildir. Geliştirici API’si ve izin kutusu yoksa ‘Siri halleder’ pazarlamadır. Gizlilik iddiası, on-device ile Private Cloud Compute ayrımını okumadan yutulmaz. Şirket içi metni Siri’ye okutmak, NDA’nızın sınırı olabilir.</p>
<h2>Alım kararı</h2>
<p>WWDC, mevcut telefonu aynı gün hurdaya çevirmez. Özellik listesi sonbahar sürümüne ve bölgeye bağlıdır. ‘Komşunun iPhone’u konuşuyor’ sizin A18/A19 eşiğiniz ve dil paketiniz olmayabilir. Watch ve Apple TV tarafı, telefon asistanından ayrı inebilir.</p>
{ARTICLE_AD}
<h2>Rekabet cümlesi</h2>
<p>Mobil yapay zekâ artık sohbet kutusu değil işletim sistemi katmanıdır. Apple gizlilik ve entegrasyon, Google Gemini ve Android Drop hız ve cihaz çeşitliliği satar. Kullanıcı için pratik: asistanın hangi uygulamaya yazabildiği ve iptal tuşu. Sahne demosu iptal tuşunu göstermez.</p>
<ul><li>Model ve dil listesini resmi sayfadan oku</li><li>On-device / bulut ayrımına bak</li><li>WWDC günü telefon hurdaya çıkmaz</li></ul>
<p>Siri AI ekosistem vaadidir. Eldeki cihaz ve dil paketi karardır.</p>
{note("https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/", "apple.com")}
""",
    ),
    "apple-yeni-app-store-araclariyla-gelistiricilere-daha-fazla-esneklik-sunuyor": n(
        "App Store büyüme araçları: fiyat, kampanya, küçük ekip",
        "Apple’ın geliştirici büyüme duyurusunu AcarTechs ‘Store serbest kaldı’ diye değil; fiyatlandırma, edinme ve abonelik kuralı olarak okur.",
        "Yeni araç, inceleme kuyruğunu ve bölge kuralını silmez.",
        f"""
<p>Apple, App Store’da geliştiricilerin büyümesine yardımcı olacak pazarlama, kullanıcı edinme ve uygulama içi satın alma esnekliği duyurdu. AcarTechs bunu bağımsız ekip için görünürlük kapısı olarak okur; politika affı olarak değil. İyi ürün hâlâ incelemeden geçer. Yeni kampanya kutusu, reddedilen meta veriyi kurtarmaz.</p>
<p>Fiyatlandırma ve abonelik denemesi, küçük ekibin gelir modelini değiştirir. Yıllık taahhüt, iptali utandırır; deneme bitişini takvime yazın. Reklam kredisi veya vitrin slotu, dönüşüm hunisi yoksa para yakar. Aile paylaşımı ve öğrenci indirimi, sizin fiyat tablonuzu böler.</p>
<h2>AB ve bölge</h2>
<p>Avrupa kuralları ile ABD vitrini aynı esneklik değildir. Duyuruyu tek dünya sanmayın. Vergi, KDV ve yerel ödeme yöntemi, ‘esneklik’ cümlesinin görünmeyen satırıdır. Bağımsız geliştirici için asıl kazanç, A/B fiyat ve özel ürün sayfası olabilir; büyük yayıncının medya bütçesi değil.</p>
{ARTICLE_AD}
<h2>Ne yapmalı?</h2>
<p>Resmi geliştirici sayfasındaki hangi aracın sizin ülkenizde açık olduğunu işaretleyin. Kampanyayı bir haftalık ölçümle açın. İnceleme notunu ve ekran görüntüsü kuralını aynı gün güncelleyin. Store aracı büyüme çarpanıdır. Ürün kalitesinin yerine geçmez.</p>
<ul><li>Bölgede araç açık mı bak</li><li>Deneme bitişini takvime yaz</li><li>İnceleme kuralını esneklik sanma</li></ul>
<p>App Store esnekliği fiyat ve edinme aracıdır. Politika tatili değildir.</p>
{note("https://www.apple.com/newsroom/2026/06/apple-expands-app-store-capabilities-to-help-developers-grow-and-reach-new-users/", "apple.com")}
""",
    ),
    "chatgpt-icin-yeni-saglik-zekasi-guncellemesi-duyuruldu": n(
        "ChatGPT sağlık zekâsı: hekim değil, triyaj değil",
        "OpenAI’nin sağlık yanıtlarını iyileştirme çalışmasını AcarTechs tanı vaadi değil; destekleyici bilgi ve kırmızı çizgi olarak okur.",
        "Daha yararlı cevap, reçete değildir.",
        f"""
<p>OpenAI, ChatGPT’de sağlıkla ilgili yanıtları daha yararlı ve dikkatli hale getirmeye odaklanan çalışmasını paylaştı. Hekim destekli değerlendirme ve model iyileştirmeleri anılıyor. AcarTechs bunu ‘ChatGPT doktor oldu’ diye yazmaz. Asistan bilgiye ulaşmayı kolaylaştırır. Tanı, doz ve acil triyaj insan işidir.</p>
<p>İyileştirme, uydurma kaynak ve emin duruş riskini sıfırlamaz. ‘Şu ilacı bırak’ cümlesi, sohbet geçmişinde kalsa da sizin sorumluluğunuzdadır. Kronik hastalık, gebelik ve çocuk dozu, modele bırakılacak konuların başında gelir. Acil belirtilerde 112, sohbet penceresi değil.</p>
<h2>Nasıl kullanılır?</h2>
<p>Hazırlık: ‘bu tahlil maddesi ne anlama gelir, hekime hangi soruyu sorayım?’ Yanlış: ‘tanımı koy, ilacı yaz’. Gizlilik: sağlık metnini iş hesabı veya paylaşılan cihazda bırakmayın. OpenAI’nin resmi metni de destekleyici bilgi çerçevesindedir; AcarTechs aynı çizgiyi kalın çizer.</p>
{ARTICLE_AD}
<h2>Ürün değil süreç</h2>
<p>Sağlık zekâsı güncellemesi, modelin daha az zararlı cevap üretmesi için bir süreçtir. Hastane bilgi sistemi değildir. Kullanıcı resmi kaynak ve uzmanla doğrular. Aksi, akıcı yanlışın hızlanmasıdır.</p>
<ul><li>Tanı ve doz yazdırma</li><li>Acilde 112</li><li>Sağlık sohbetini paylaşılan cihazda bırakma</li></ul>
<p>ChatGPT sağlıkta hazırlık sorusu üretir. Hekim yerine geçmez.</p>
{note("https://openai.com/index/improving-health-intelligence-in-chatgpt/", "openai.com")}
""",
    ),
    "cloudflare-oauth-akisini-tum-gelistiricilere-acti": n(
        "Cloudflare OAuth: kapsam, ajan, SaaS izni",
        "Self-managed OAuth’un tüm geliştiricilere açılmasını AcarTechs ‘giriş kolaylaştı’ değil; dar yetki ve iptal olarak okur.",
        "Standart izin akışı, anahtarı koda gömmeyi meşrulaştırmaz.",
        f"""
<p>Cloudflare, self-managed OAuth özelliğini tüm geliştiricilere açtığını duyurdu. Uygulamalar kullanıcılardan daha standart ve sınırlı yetkilerle izin alabilecek. AcarTechs bunu özellikle SaaS entegrasyonu, iç geliştirici platformu ve yapay zekâ ajanları için okur. Ajanın ‘hesabıma gir’ demesi, kapsam (scope) listesi olmadan tehlikelidir.</p>
<p>Kullanıcı hangi veriye, hangi süreyle izin verdiğini görmek ister. ‘offline_access’ ve geniş okuma, bir yıl unutulmuş entegrasyonda sızıntı üretir. İptal tuşu (token revoke) yoksa standart OAuth yalnızca vitrindir. Mobil uygulamada istemci sırrı gömmek, OAuth’un çözdüğü sorunu geri getirir.</p>
<h2>Ajan ve iç araç</h2>
<p>Yapay zekâ ajanı, kullanıcının Cloudflare veya SaaS hesabında işlem yapacaksa her adımda dar kapsam ve onay ekranı şarttır. ‘Tüm zone’ izni, blog yazısı güncellemek için gerekmez. İç geliştirici portalında SSO + OAuth, paylaşılmış admin anahtarından iyidir.</p>
{ARTICLE_AD}
<h2>Ne yapmalı?</h2>
<p>Resmi blog’daki akışı, sizin mevcut API anahtarı alışkanlığınızla karşılaştırın. Anahtarı ajan prompt’una yapıştırmayın. Kapsam listesini ürün belgesine yazın. OAuth, izin disiplini aracıdır. Güvenlik tatili değildir.</p>
<ul><li>Kapsamı dar tut</li><li>İptal yolunu dene</li><li>Sırrı istemciye gömme</li></ul>
<p>OAuth herkese açık olması, herkese tam yetki demek değildir.</p>
{note("https://blog.cloudflare.com/oauth-for-all/", "blog.cloudflare.com")}
""",
    ),
    "cloudflare-workflows-icin-saga-rollback-destegi-geldi": n(
        "Cloudflare Workflows saga rollback: ödeme, sipariş, telafi",
        "Saga tarzı geri almayı AcarTechs sihirli undo değil; her adımın telafi fonksiyonu olarak okur.",
        "Rollback, adımın telafisi yazılmadıysa çalışmaz.",
        f"""
<p>Cloudflare, Workflows ürününe saga tarzında rollback desteği eklediğini duyurdu. Çok adımlı işlemde bir adım başarısız olunca önceki adımlar için telafi edici işlemler çalışabilir. AcarTechs bunu ödeme, sipariş, dosya işleme ve çok servisli entegrasyon için okur. Demo mutlu yolu, üretimdeki kısmi başarı değildir.</p>
<p>Örnek: stok düştü, ödeme çekildi, kargo API 500 verdi. Telafi: stoku geri yaz, ödemeyi iade et veya iptal bayrağı koy. İkisi de yazılmamışsa ‘rollback var’ cümlesi slayttır. Idempotency anahtarı yoksa telafi çift iade üretir.</p>
<h2>Ne zaman saga?</h2>
<p>Tek veritabanı işlemi saga istemez. Üç harici servis ve para hareketi ister. Dosya yükleme + virüs tarama + yayın da adaydır. Her adımın ‘ileri’ ve ‘geri’ fonksiyonunu isimlendirin. Log olmadan rollback, gece 03.00’te kördür.</p>
{ARTICLE_AD}
<h2>Geliştirici notu</h2>
<p>Okunabilir telafi, kendi retry döngünüzden ucuzdur. Yine de sınır: dış banka API’si telafiyi reddedebilir. O noktada insan kuyruğu şarttır. Saga, kısmi başarıyı görünür kılar. Sihirli geri al tuşu değildir.</p>
<ul><li>Her adımın telafisini yaz</li><li>Idempotency koy</li><li>Para hareketinde insan kuyruğu bırak</li></ul>
<p>Rollback, yazdığınız telafi kadar vardır.</p>
{note("https://blog.cloudflare.com/rollbacks-for-workflows/", "blog.cloudflare.com")}
""",
    ),
    "disney-plus-haziran-listesinde-avatar-fire-and-ash-promiyeri-one-cikiyor": n(
        "Disney Plus haziran: Avatar prömiyeri ve 2 başlık kuralı",
        "Avatar: Fire and Ash öne çıkışını AcarTechs katalog yığını değil; süre, yaş ve abonelik ayı olarak okur.",
        "Prömiyer, listenin tamamını bu hafta izleme emri değildir.",
        f"""
<p>Disney Plus haziran listesinde Avatar: Fire and Ash prömiyeri öne çıkıyor. AcarTechs başlık listesini yeniden dizmez. Evde gerçek süre 2 film veya 1 dizi taşır. Avatar, uzun ve görsel ağır bir oturumdur; çocuklu evde yaş etiketi ve ara vermeden 3 saat, ‘aile gecesi’ planını bozar.</p>
<p>Prömiyer günü ağ ve 4K kotası şişer. Wi-Fi zayıfsa HD profili, kare düşmesinden iyidir. İndirme hakkı katmana bağlıdır; uçak yolunda prömiyer yoksa liste işe yaramaz. Aynı ayda ikinci bir ‘kaçırma’ başlığı, Avatar’ı yarıda bırakır.</p>
<h2>Abonelik matematiği</h2>
<p>Yalnızca bu prömiyer için yıllık plan açmak, üç aylık izlemesi olan ev için pahalı kilit olabilir. Ayın 1’i aç, 25’i bitmediyse uzatma. Top 10, sizin zevkiniz değil tıklamadır.</p>
{ARTICLE_AD}
<h2>Ne izlenir?</h2>
<p>Bu ay Avatar + bir kısa aile yapımı. Üçüncü başlık istek listesi. Prömiyer vitrindir. 30 günlük bütçeniz karardır.</p>
<ul><li>Yaş ve süre</li><li>İndirme hakkı</li><li>Ayda 2 başlık</li></ul>
<p>Haziran listesi süzgeçtir. Avatar zorunlu maraton değildir.</p>
{note("https://www.disneyplus.com", "Disney Plus")}
""",
    ),
    "disney-plus-the-doomies-icin-resmi-fragman-ve-yayin-tarihini-paylasti": n(
        "The Doomies: fragman, tarih, çocuk profili",
        "Disney Plus’ın resmi fragman ve yayın tarihini AcarTechs 90 saniyelik kesit değil; ton, yaş ve takvim olarak okur.",
        "Fragman neşesi, filmin korku eşiği olmayabilir.",
        f"""
<p>Disney Plus, The Doomies için resmi fragman ve yayın tarihini paylaştı. AcarTechs fragmanı iki kez izlemenizi ister: ses kapalı, ses açık. Müzik hilesi tonu yumuşatır. Çocuk profilinde otomatik oynatma, fragmanı film sanır. Yaş etiketini resmi sayfadan okuyun; fragman yaş sınırı filmin sınırı olmayabilir.</p>
<p>Yayın tarihi pencereyse takvime belirsiz yazın. Ön satış ve parti planı, tarih kayınca sizin iptalinizdir. Aynı hafta Avatar veya başka prömiyer varsa Doomies istek listesine düşebilir; ikisini aynı gece bitirme zorunluluğu yoktur.</p>
<h2>Ne takip edilir?</h2>
<p>Resmi Disney sayfası, tarih ve dil seslendirme. Sosyal medya karesi spoiler taşır. Fragman davettir. Sözleşme değildir.</p>
{ARTICLE_AD}
<h2>Aile süzgeci</h2>
<p>Korku eşiği, süre, dil. Üçü net değilse bu akşamın filmi değildir. AcarTechs duyuruyu kopyalamaz; süzgeç yazar.</p>
<ul><li>Yaş etiketini resmi sayfadan oku</li><li>Tarih pencereyse belirsiz yaz</li><li>Otomatik oynatmayı çocukta kapat</li></ul>
<p>The Doomies haberi fragman ve tarihtir. Maraton emri değildir.</p>
{note("https://www.disneyplus.com", "Disney Plus")}
""",
    ),
    "github-copilot-ucretsiz-ve-ogrenci-planlarinda-otomatik-model-secimine-geciyor": n(
        "Copilot ücretsiz/öğrenci: otomatik model, kota, sır",
        "Otomatik model seçimini AcarTechs ‘daha zeki Copilot’ değil; kota, gizlilik ve ödev çizgisi olarak okur.",
        "Model adı gizlenince hangi verinin nereye gittiği silinmez.",
        f"""
<p>GitHub, Copilot’un ücretsiz ve öğrenci planlarında otomatik model seçimine geçeceğini duyurdu. AcarTechs bunu hız ve kota yönetimi olarak okur. Arka planda model değişmesi, aynı sohbetin dün başka, bugün başka model olduğu anlamına gelebilir. Ödev ve iş kodunda ‘hangi model?’ kaydı yoksa tekrar üretilemez.</p>
<p>Öğrenci için: açıklama evet, bitmiş ödev hayır. Ücretsiz katman kota bitince sessizce zayıflar; ‘bozuldu’ sanılır. Şirket reposunu öğrenci hesabıyla açmak, okul mailinin sınırını aşar. API anahtarı sohbet geçmişine yapışmaz.</p>
<h2>Ne kontrol edilir?</h2>
<p>Plan sayfasındaki kota, model ailesi ve veri eğitim kutusu. Otomatik seçim kapatılabiliyor mu bakın. İş için şirket kirası, öğrenci için okul hesabı. İkisini karıştırmayın.</p>
{ARTICLE_AD}
<h2>Kalite</h2>
<p>Otomatik model, ortalama işi hızlandırır. Kritik yama ve lisans belirsiz kodda insan diff’i şarttır. Copilot ücretsiz planı hediye zekâ değil kota ve süzgeçtir.</p>
<ul><li>Kota bitişini izle</li><li>İş reposunu öğrenci hesabına bağlama</li><li>Ödevi yazdırma</li></ul>
<p>Otomatik model seçimi kolaylıktır. Sır ve ödev çizgisini silmez.</p>
{note("https://github.blog", "github.blog")}
""",
    ),
    "github-desktop-3-6-worktree-ve-copilot-entegrasyonunu-genisletti": n(
        "GitHub Desktop 3.6: worktree, Copilot, ne zaman CLI?",
        "Worktree ve Copilot genişlemesini AcarTechs herkese zorunlu GUI değil; paralel dal ve sır sınırı olarak okur.",
        "Worktree, diski iki repo sanarak doldurur.",
        f"""
<p>GitHub Desktop 3.6, worktree ve Copilot entegrasyonunu genişletti. Worktree, aynı depoda iki dalı yan yana açar; özellik dalı ve acil yama aynı anda durur. AcarTechs bunu CLI bilmeyen için kapı, büyük monorepo için dikkat notu olarak okur. İki worktree, node_modules’ü iki kez indirir. Disk ve IDE belleği şişer.</p>
<p>Copilot’un Desktop’a girmesi, commit mesajı ve PR taslağını hızlandırır. Üretim sırrı ve müşteri verisi taslağa yapışmamalıdır. Desktop, rebase çatışmasında CLI kadar net olmayabilir; o noktada terminal dürüsttür.</p>
<h2>Kim için?</h2>
<p>Öğrenci ve küçük ekip: Desktop + worktree yeter. 30 kişilik monorepo: Git GUI ikinci araçtır, kaynak CLI ve CI’dır. Windows satır sonu ve LFS, worktree’de sürpriz üretir; ilk gün küçük depoda deneyin.</p>
{ARTICLE_AD}
<h2>Commit mesajı</h2>
<p>Copilot mesajı taslaktır. ‘fix stuff’ yerine neyin neden değiştiğini siz yazın. Desktop 3.6 paralel dal kolaylığıdır. Disk ve sır disiplinini silmez.</p>
<ul><li>Worktree diskini say</li><li>Sırrı Copilot taslağına yapıştırma</li><li>Çatışmada CLI’ye geçmek serbest</li></ul>
<p>GUI kolaylıktır. Worktree maliyeti gizlenmez.</p>
{note("https://github.blog", "github.blog")}
""",
    ),
    "google-arama-ai-mode-icin-gemini-3-5-flash-donemine-gecti": n(
        "Google AI Mode: Gemini 3.5 Flash, kaynak, tarih",
        "Arama AI Mode model geçişini AcarTechs daha akıcı kutu değil; hız, uydurma ve tıklama sorumluluğu olarak okur.",
        "Flash, dipnotu silmez.",
        f"""
<p>Google, Arama AI Mode için Gemini 3.5 Flash dönemine geçtiğini duyurdu. Flash, gecikmeyi kısaltır. AcarTechs bunu ansiklopedi güncellemesi saymaz. Akıcı paragraf, tarih ve resmi belge yoksa taslaktır. Hukuk, sağlık ve fiyat için asıl sayfaya gidilir.</p>
<p>Model değişince dünkü cevap bugün kayabilir. Ödev ve müşteri notunda yapıştırılan AI Mode cümlesi, kaynak linki olmadan kırılır. Şirket içi metni arama kutusuna yapıştırmayın. Klasik sonuç listesi nadir hata kodu ve PDF için hâlâ iyidir.</p>
<h2>Nasıl kullanılır?</h2>
<p>Cevabın altındaki linklere tıklayın. İki kaynak çelişiyorsa üçüncüyü açın. Flash hızlı giriş içindir. Karar, tıklayanındır.</p>
{ARTICLE_AD}
<h2>Ne değişmedi?</h2>
<p>Reklam ve alışveriş birimleri, AI paragrafının yanında durabilir. ‘Google söyledi’ cümlesi fatura veya tanı gerekçesi olmaz. AI Mode hızdır. Kaynak disiplini sizin işinizdir.</p>
<ul><li>Linke tıkla</li><li>Sağlık/hukuku kutuya bırakma</li><li>Şirket metnini aramaya yapıştırma</li></ul>
<p>Gemini 3.5 Flash AI Mode’u hızlandırır. Doğrulamayı devretmez.</p>
{note("https://blog.google", "blog.google")}
""",
    ),
    "google-finance-yeni-uygulama-ve-portfolyo-ozellikleriyle-guncellendi": n(
        "Google Finance: portföy, uygulama, yatırım tavsiyesi değil",
        "Yeni uygulama ve portföy özelliklerini AcarTechs broker değil; izleme ve uyarı aracı olarak okur.",
        "Grafik güzelleşmesi, al-sat emri değildir.",
        f"""
<p>Google Finance, yeni uygulama ve portföy özellikleriyle güncellendi. İzleme listesi, haber ve temel veriyi tek yerde toplamak kolaylaşır. AcarTechs bunu yatırım tavsiyesi saymaz. Gecikmeli fiyat, sizin piyasa emriniz değildir. Uygulama bildirimi, FOMO ile işlem açtırmak için tasarlanabilir; sessize almak serbesttir.</p>
<p>Portföy senkronu hangi hesapla bağlı, vergi ve yerel broker kaydı orada durmaz. ‘Google’da portföyüm yeşil’ cümlesi, SPK lisanslı danışman değildir. Sahte uygulama adları mağazada Finance’a benzer; paket adını resmi sayfadan doğrulayın.</p>
<h2>Ne için kullanılır?</h2>
<p>Haber + izleme + basit getiri. Al-sat, teminat ve halka arz başka uygulamadır. İki faktör ve cihaz kilidi, finans uygulamasında e-postadan önemlidir.</p>
{ARTICLE_AD}
<h2>Gizlilik</h2>
<p>İzleme listeniz ilgi grafiğidir. İş telefonunda kişisel portföy açmayın. Finance güncellemesi izleme kolaylığıdır. Servet yönetimi değildir.</p>
<ul><li>Tavsiye sanma</li><li>Paket adını doğrula</li><li>Bildirimleri FOMO için açık bırakmak zorunda değilsin</li></ul>
<p>Portföy ekranı aynadır. Emir kapısı değildir.</p>
{note("https://blog.google", "blog.google")}
""",
    ),
    "google-haziran-pixel-drop-ile-gemini-ve-yaratici-araclari-genisletti": n(
        "Pixel Drop haziran: Gemini, ekran kaydı, çeviri, kademe",
        "Haziran 2026 Pixel Drop’u AcarTechs her Pixel’e aynı gün inen sihir değil; cihaz listesi, ısınma ve gizlilik olarak okur.",
        "AI video ve müzik, kılıf içinde ısınır.",
        f"""
<p>Google, Haziran Pixel Drop ile Gemini iyileştirmeleri, ekran kaydı tepkileri, AI destekli video ve müzik, floating app bubbles ve daha geniş cihaz desteğiyle gerçek zamanlı ses çevirisi duyurdu. AcarTechs listeyi ezberletmez. Hangi Pixel modeli, hangi bölge, hangi özellik kademeli gelir bakın. ‘Komşuda var’ skandalı değildir.</p>
<p>Yaratıcı araçlar rulo ve diski yer. 4K AI video, 128 GB telefonda üç denemede dolar. Çeviri, konuşmayı sunucuya gönderebilir; toplantıda gizli gündem için kapatın. Floating bubbles, yanlış tıklama ve reklam çakışması üretir; oyun ve bankacılıkta kapatın.</p>
<h2>Pil ve ısı</h2>
<p>Gemini ve yaratıcı modeller NPU/GPU’yu yer. Kılıf içinde Drop özellikleri ısınır. 60 Hz ve karanlık tema, seyahatte bir saat kazandırır. Güvenlik yamasını yaratıcı özellik gelsin diye geciktirmeyin.</p>
{ARTICLE_AD}
<h2>Ne yapılmalı?</h2>
<p>Sistem güncellemesini aç, özellik listesini resmi Pixel sayfasından modele göre oku. Disk ve ısı için yaratıcı aracı Wi-Fi’de ve kılıfsız dene. Pixel Drop vitrin listesidir. Sizin modeliniz karardır.</p>
<ul><li>Model listesini oku</li><li>Toplantıda çeviriyi kapat</li><li>Yamayı özellik için erteleme</li></ul>
<p>Haziran Pixel Drop Gemini ve yaratıcı katmandır. Her cihaza aynı anda inmez.</p>
{note("https://blog.google/products-and-platforms/devices/pixel/june-2026-pixel-drop/", "blog.google")}
""",
    ),
    "microsoft-agent-365-ile-kurumsal-yapay-zeka-ajanlarini-yonetmek-istiyor": n(
        "Microsoft Agent 365: ajan envanteri, yetki, denetim",
        "Kurumsal ajan kontrol düzlemini AcarTechs ‘ajan üret’ slaytı değil; kim hangi veriye erişiyor olarak okur.",
        "Sorun ajan üretmek değil, izinsiz ajanın çoğalmasıdır.",
        f"""
<p>Microsoft, kurumsal yapay zekânın olgunlaşması için Agent 365 kontrol düzlemini öne çıkardı. Farklı kaynaklardan gelen veya içeride yazılan ajanların tek yerden izlenmesi, yönetilmesi ve güvence altına alınması gerektiğini vurguluyor. AcarTechs bunu siber güvenlik ve veri ekiplerinin yeni envanteri olarak okur. Shadow IT, artık gölge ajanıdır.</p>
<p>Ajanın hangi SharePoint’e yazdığı, hangi mailbox’ı okuduğu, hangi ödeme API’sini çağırdığı kayıt altında değilse ‘başarılı POC’ ertesi gün sızıntıdır. İnsan onayı olmayan gönderim, müşteri mailinde markayı yakar. Lisans koltukları, kullanılmayan ajanlarda yanar.</p>
<h2>İlk 30 gün</h2>
<p>Envanter: kaç ajan, hangi kimlik, hangi sır. SSO ve koşullu erişim. Test tenancy. Üretim müşteri verisi yok. Eğitim, lisans kadar önemlidir. ‘Kullanın’ demek, gizli klasörü ajan prompt’una davettir.</p>
{ARTICLE_AD}
<h2>Güvenlik ile birlikte</h2>
<p>Agent 365, EDR ve DLP’nin yerine geçmez. Yanına oturur. Ajan yönetimi, üretimden önce kontrol düzlemidir.</p>
<ul><li>Ajan envanteri tut</li><li>Onaysız gönderim yok</li><li>Müşteri verisini POC’ye koyma</li></ul>
<p>Kurumsal ajan, izlenmeyen stajyerdir. Kontrol düzlemi olmadan çoğalmaz olmamalıdır.</p>
{note("https://blogs.microsoft.com/blog/2026/06/16/achieving-success-with-ai/", "blogs.microsoft.com")}
""",
    ),
    "microsoft-windows-10-esu-suresini-kullanicilar-icin-uzatti": n(
        "Windows 10 ESU: ek süre, yenileme, ne zaman 11?",
        "Kişisel cihaz ESU bilgisini AcarTechs ‘Windows 10 sonsuz’ değil; yama takvimi ve donanım eşiği olarak okur.",
        "Ek süre, TPM’siz kutuyu ömür boyu güvenceye almaz.",
        f"""
<p>Microsoft, Windows 10 kullanan kişisel cihazlar için Extended Security Updates programına ilişkin güncel bilgi paylaştı. Kullanıcıların Windows 11 geçişine daha kontrollü hazırlanması için ek süre anılıyor. AcarTechs bunu yenileme planı olarak okur. ESU, özellik güncellemesi değil güvenlik yaması kirasıdır. Biten destek, tarayıcı ve bankacılık için ayrı riskdir.</p>
<p>TPM 2.0, güvenli önyükleme ve işlemci listesi Windows 11 eşiğidir. Eşiği tutmayan kutu: ESU + tarayıcı yaması, veya Linux, veya emekli. Bankacılık ve iş maili, yamasız Windows 10’da ayrı ağda tutulmalıdır. ‘Hâlâ açılıyor’ güvenlik değildir.</p>
<h2>Ev ve küçük ofis</h2>
<p>Kaç cihaz 10’da, hangisi 11’e çıkar, hangisi ESU. Yazıcı ve muhasebe yazılımı 11’de kırılıyorsa önce o yazılım. Akşam 21.00’de 20 cihaza aynı anda basmayın; 1 PC dene. Yedek, yamadan önce gelir.</p>
{ARTICLE_AD}
<h2>Tarihi resmi sayfadan tut</h2>
<p>ESU bitiş cümlesi blog’da kayabilir. blogs.windows.com ve resmi yaşam döngüsü sayfası. Ek süre, donanım alışverişini bu çeyreğe sıkıştırmaz; plan yazdırır.</p>
<ul><li>Cihaz envanteri</li><li>TPM/CPU eşiği</li><li>Yamasız kutuda bankacılık yok</li></ul>
<p>ESU ek süredir. Sonsuz Windows 10 değildir.</p>
{note("https://blogs.windows.com/windowsexperience/2025/06/24/stay-secure-with-windows-11-copilot-pcs-and-windows-365-before-support-ends-for-windows-10/", "blogs.windows.com")}
""",
    ),
    "netflix-haftalik-top-10-listesinde-i-will-find-you-zirveye-yerlesti": n(
        "Netflix Top 10 (15 Haziran): I Will Find You ve süzgeç",
        "15 Haziran 2026 Tudum listesini AcarTechs zevk belgesi değil; o haftanın tıklaması olarak okur.",
        "Zirve, sizin 6 saatinizi o diziye mahkûm etmez.",
        f"""
<p>Netflix Tudum, haftalık Top 10’da I Will Find You yapımının zirveye yerleştiğini duyurdu. Maternal Instinct ve Voicemails for Isabelle da anılıyor. AcarTechs listeyi yeniden dizmez. Top 10, o ülkenin tıklamasıdır. Belgesel ve gerilim aynı akşam birbirini öldürür.</p>
<p>Zirvedeki dizi 8 bölüm taahhüdü olabilir. 1. bölüm yetmiyorsa bırakmak serbesttir. Spoiler thumbnail’i açmadan resmi Tudum sayfasına bakın. Çocuk profilinde yaş etiketi, ‘haftanın birincisi’ cümlesinden önce gelir.</p>
<h2>Ay planı</h2>
<p>Bu hafta bir başlık. İkinci istek listesi. Aboneliği yalnızca zirve için yıllık kilitlemeyin. 15 Haziran listesi keşiftir. Kanon değildir.</p>
{ARTICLE_AD}
<h2>Strateji ipucu</h2>
<p>Platform, yeni sezonun ilk hafta tıklamasını vitrinler. Kalıcılık üçüncü haftada belli olur. AcarTechs ilk hafta zirvesini ‘başyapıt’ diye yazmaz.</p>
<ul><li>Top 10’u zevk sanma</li><li>Yaş etiketini oku</li><li>1. bölüm yetmiyorsa bırak</li></ul>
<p>15 Haziran Top 10 tıklama vitrinidir. İzleme borcu değildir.</p>
{note("https://www.netflix.com/tudum/articles/top-10-june-15-2026", "Netflix Tudum")}
""",
    ),
    "netflix-haftanin-izlenecek-yapimlarini-yeni-listeyle-paylasti": n(
        "Netflix 19–25 Haziran: Color Book, süzgeç, 2 başlık",
        "Tudum’un 19–25 Haziran listesini AcarTechs yığın değil; 2 başlık kuralı olarak okur.",
        "Color Book ve Avatar aynı gece bitmez.",
        f"""
<p>Netflix Tudum, 19–25 Haziran haftasında Color Book, The American Experiment, Voicemails for Isabelle ve Avatar: The Last Airbender gibi başlıkları öne çıkardı. AcarTechs dört adı yan yana dizerek aktarmaz. Evde 6 saat vardır. Belgesel (American Experiment) ile animasyon aynı oturumda birbirini ezer.</p>
<p>Haftalık ‘ne izlenir’ sayfası keşif aracıdır. Top 10 ile karıştırmayın; editör seçkisi ve tıklama listesi ayrıdır. İndirme hakkı yolculuk için katalogdan önemlidir. Yaş etiketi çocuk profilinde fragmandan okunmaz, başlık sayfasından okunur.</p>
<h2>Bu hafta</h2>
<p>Bir film veya bir dizi bölümü. İkinci başlık istek listesi. Yıllık planı bu beş ada bağlama.</p>
{ARTICLE_AD}
<h2>Spoiler</h2>
<p>Sosyal kare, Tudum maddesinden önce gelir. Listeyi resmi sayfadan, kareyi değil başlığı okuyarak tutun.</p>
<ul><li>Ayda/haftada 2 başlık</li><li>Türü ayır</li><li>Yaş etiketini başlık sayfasından oku</li></ul>
<p>19–25 Haziran listesi süzgeçtir. Maraton fişi değildir.</p>
{note("https://www.netflix.com/tudum/articles/what-to-watch-on-netflix-june-19-2026", "Netflix Tudum")}
""",
    ),
    "netflix-haziran-2026-takviminde-yeni-diziler-ve-filmler-one-cikiyor": n(
        "Netflix haziran takvimi: Voicemails, süzgeç, abonelik ayı",
        "Haziran 2026 ekleme takvimini AcarTechs her başlığı izleme listesi değil; 30 günlük bütçe olarak okur.",
        "Aylık takvim, üç aboneliği birden tutma gerekçesi değildir.",
        f"""
<p>Netflix, Haziran 2026 boyunca Voicemails for Isabelle, Office Romance, Sweet Magnolias, Avatar: The Last Airbender ve America’s Sweethearts gibi başlıkların yanı sıra The American Experiment ve Maternal Instinct belgesellerini duyurdu. AcarTechs takvimi yeniden yayımlamaz. Pazartesi bu ay bitecek tek dizi, Cuma tek film. Üçüncü istek listesidir.</p>
<p>Belgesel ve romantik komedi aynı akşam birbirini öldürür. Çocuklu evde Avatar ve aile başlığı öne çıkar; yetişkin gerilim hafta sonuna kalır. Takvim sadakat aracıdır. Sizin 30 gününüz stüdyonun vitrini değildir.</p>
<h2>Abonelik</h2>
<p>Yalnızca haziran yıldızı için yıllık kilitlemeyin. Ayın 1’i aç, 25’i gözden geçir. Offline indirme köy ve uçak için takvimden önemlidir.</p>
{ARTICLE_AD}
<h2>Top 10 ile karıştırma</h2>
<p>Takvim ‘ne gelecek’, Top 10 ‘ne tıklandı’. İkisi de zevkiniz değildir. Elemek izlemektir.</p>
<ul><li>Ayda 2 başlık</li><li>Türü ayır</li><li>Yıllık kilidi yaza bağlama</li></ul>
<p>Haziran takvimi 30 günlük bütçedir. Yığın değildir.</p>
{note("https://www.netflix.com/tudum/articles/new-on-netflix", "Netflix Tudum")}
""",
    ),
    "openai-ajanlarin-is-dunyasindaki-etkisini-yeni-arastirmayla-anlatti": n(
        "OpenAI ajan araştırması: yazılım, bilgi işi, onay",
        "Ajanların işyerindeki etkisine dair araştırmayı AcarTechs ‘iş bitti’ değil; tekrarlayan görev ve insan onayı olarak okur.",
        "Hızlanan taslak, hızlanan hukuki onay değildir.",
        f"""
<p>OpenAI, ajan tabanlı sistemlerin iş dünyasında nasıl kullanıldığına odaklanan bir araştırma paylaştı. Yazılım geliştirme ve bilgi işlerinde tekrarlayan görevlerin hızlanabileceği belirtiliyor. AcarTechs bunu verimlilik slaytı olarak yutmaz. Ajan hedefi parçalara böler. Karar, müşteri taahhüdü ve rakamın doğruluğu insanda kalır.</p>
<p>Kod iskeleti ve doküman taslağı iyi adaydır. Fiyat teklifi ve sağlık/hukuk kötü adaydır. NDA altındaki metni tüketici ajanına yapıştırmak ihlaldir. Ölçüm: taslak süresi düştü mü, revizyon arttı mı? İkincisi arttıysa ajan her cümleyi yeniden yazdırıyordur.</p>
<h2>Ekip</h2>
<p>İzinli araç, izinli veri, insan onayı. Eğitim lisans kadar önemlidir. Araştırma, ajanın yayıldığını gösterir. Sizin politikanız yoksa yayılma sızıntıdır.</p>
{ARTICLE_AD}
<h2>Ne yapılmaz?</h2>
<p>Onaysız gönderim, üretim sırrı, ölçümsüz ‘herkes kullansın’. Ajan tekrarlayan adımı keser. Sorumluluğu devretmez.</p>
<ul><li>Müşteri metnini tüketici ajana yapıştırma</li><li>Taslak ve revizyonu birlikte ölç</li><li>Onaysız gönderim yok</li></ul>
<p>Araştırma hız ipucudur. Politika yerine geçmez.</p>
{note("https://openai.com/index/how-agents-are-transforming-work/", "openai.com")}
""",
    ),
    "openai-model-davranislarini-yayin-oncesi-simule-eden-yeni-yontemini-anlatti": n(
        "OpenAI Deployment Simulation: ajan riski, kullanıcı vaadi değil",
        "Yayın öncesi simülasyonu AcarTechs ‘artık zarar yok’ değil; laboratuvar testi olarak okur.",
        "Simülasyon, sizin sohbetinizdeki uydurmayı sıfırlamaz.",
        f"""
<p>OpenAI, modellerin yayımlanmadan önce gerçek kullanım koşullarına daha yakın test edilmesini hedefleyen Deployment Simulation yaklaşımını paylaştı. Özellikle araç kullanan ajan sistemlerinde istenmeyen davranışı önceden görmek amaçlanıyor. AcarTechs bunu güvenlik olgunluğu olarak okur. Klasik benchmark, ajanın dış dünyada tıklamasını ölçmez.</p>
<p>Simülasyon, kırmızı takım ve politika katmanlarından biridir. Hepsi birlikte işe yarar. Kullanıcı tarafında ‘bu model simülasyondan geçti’ cümlesi, sağlık veya hukuk kararı gerekçesi olmaz. Ajanın ödeme ve e-posta adımlarında onay tuşu hâlâ şarttır.</p>
<h2>Geliştirici ve kurum</h2>
<p>Kendi ajanınızı üretime almadan benzer senaryo testleri yazın. Mutlu yol yetmez. Yetki aşımı, sonsuz döngü, prompt sızıntısı. OpenAI’nin yöntemi, sizin test bütçenizi silmez.</p>
{ARTICLE_AD}
<h2>Okur için</h2>
<p>Yeni modelin daha öngörülebilir olması iyidir. Elinizdeki asistanın her cümlesi denetlenmiş değildir. Simülasyon laboratuvar notudur. Sertifika değildir.</p>
<ul><li>Simülasyonu sıfır risk sanma</li><li>Ajan onay tuşunu kapatma</li><li>Kendi kötü senaryonu yaz</li></ul>
<p>Deployment Simulation test olgunluğudur. Kullanıcıya zarar-yok vaadi değildir.</p>
{note("https://openai.com/index/deployment-simulation/", "openai.com")}
""",
    ),
    "openai-partner-network-ile-yapay-zeka-projelerinde-is-ortaki-donemi-basladi": n(
        "OpenAI Partner Network: entegrasyon, veri, çıkış kapısı",
        "İş ortağı programını AcarTechs ‘OpenAI onaylı sihir’ değil; danışman, entegrasyon ve sözleşme süzgeci olarak okur.",
        "Partner rozeti, verinin nerede durduğunu yazmaz.",
        f"""
<p>OpenAI, ChatGPT ve API tabanlı projelerde danışmanlık ve uygulama desteği için Partner Network’ü duyurdu. AcarTechs bunu teknik ekibi sınırlı işletme için hız kapısı olarak okur. Model seçmek yetmez. Veri bölgesi, iş akışı, eğitim ve ölçüm merkezidir.</p>
<p>Doğru partner, fikirden çalışan ürüne süreyi kısaltabilir. Yanlış partner, slayt ve token faturası üretir. Demo sizin fatura PDF’inizle çalışsın. İnsan onayı olmayan otomatik e-posta müşteri kaybettirir. İptalde veri iadesi 7 günde gelmiyorsa kilitlenirsiniz.</p>
<h2>Sözleşme</h2>
<p>Veri nerede, alt işlemci kim, eğitimde kullanılıyor mu. Rozet bu maddelerin yerine geçmez. Fiyat koltuk ve destek saatiyle konuşulsun, gizli token sürprizi olmasın.</p>
{ARTICLE_AD}
<h2>Küçük işletme</h2>
<p>İlk 30 gün tek süreç (SSS veya randevu). Partner Network kapısıdır. Teslimat sizin kabul kriterinizdir.</p>
<ul><li>Veri bölgesini yaz</li><li>Demo gerçek dosyanızla</li><li>İptalde dump maddesi</li></ul>
<p>İş ortağı rozeti entegrasyon hızıdır. Güvenlik belgesi değildir.</p>
{note("https://openai.com/index/introducing-openai-partner-network/", "openai.com")}
""",
    ),
    "openai-patch-the-planet-ile-acik-kaynak-guvenligine-ai-destegi-veriyor": n(
        "Patch the Planet: AI araştırma, insan yaması, lockfile",
        "Daybreak girişimini AcarTechs ‘AI her açığı kapatır’ değil; insan uzmanlı yama disiplini olarak okur.",
        "Bulunan açık, yama yayınlanmadan tweet’lenmez.",
        f"""
<p>OpenAI, Patch the Planet adlı Daybreak girişimini duyurarak açık kaynak güvenliğine AI destekli araştırma ile insan uzman kontrolünü birleştirmeyi hedefledi. AcarTechs bunu internet altyapısının kütüphane katmanı için okur. Erken bulunan açık, milyonlarca kilidi ilgilendirir. AI, issue gürültüsü de üretebilir. İnsan triyajı olmadan ‘bin kırmızı’ bakıcıyı yakar.</p>
<p>Sizin ekibiniz: lockfile, SBOM, tek bakıcı riski. AI’nın bulduğu CVE adayı, upstream’e sorumlu açıklama ile gider. Kendi fork’unuzda sessiz yama, ekosistemi bölmez ama kullanıcıyı kör bırakabilir.</p>
<h2>Ne beklemeyin?</h2>
<p>Yarın tüm npm’in güvenli olması. Program, araştırma kapasitesidir. Sizin 48 saatlik yama kuralınız ayrıdır. Windows ve yönlendirici firmware’i bu girişimden düşmez.</p>
{ARTICLE_AD}
<h2>Katkı</h2>
<p>Öğrenci için yıldız spam’i değil, yeniden üretilebilir rapor. Bakıcı için şablon ve asgari örnek. Patch the Planet hız katmanıdır. Bakım borcunu silmez.</p>
<ul><li>Lockfile commit</li><li>Sorumlu açıklama</li><li>AI issue gürültüsünü triyaj et</li></ul>
<p>Açık kaynak yaması insan imzalıdır. AI taslak avcısıdır.</p>
{note("https://openai.com/index/patch-the-planet/", "openai.com")}
""",
    ),
    "openai-ve-broadcom-yapay-zeka-icin-jalapeno-inference-cipini-tanitti": n(
        "Jalapeno inference çipi: maliyet, hız, sizin ChatGPT faturanız",
        "OpenAI–Broadcom duyurusunu AcarTechs ‘evde yeni çip’ değil; sunucu inference maliyeti olarak okur.",
        "Özel silikon, bu gece telefonunuza inmez.",
        f"""
<p>OpenAI ve Broadcom, büyük dil modellerinin inference yüküne odaklanan Jalapeno adlı özel işlemciyi tanıttı. AcarTechs bunu maliyet, gecikme ve ölçek rekabeti olarak okur. Eğitim (training) ayrı, yanıt üretme (inference) ayrı faturadır. Kullanıcının ChatGPT’de hissettiği hız ve kota, bu katmana bağlıdır.</p>
<p>Özel çip, GPU kirasını düşürmeyi hedefler. Tedarik, yazılım yığını ve enerji, slayttaki TOPS’tan geç gelir. Bellek fiyat baskısı (HBM) ayrı haberde; Jalapeno o baskıyı sihirle bitirmez. Kurum müşterisi için ‘daha ucuz token’ vaadi, SLA ve bölge ile birlikte okunur.</p>
<h2>Tüketici</h2>
<p>Yeni telefon alım gerekçesi değildir. Kota ve yavaş cevap şikâyeti, model ve yoğun saat kadar silikon da olabilir. AcarTechs çip adını vitrin yapmaz; inference faturasının evrildiğini yazar.</p>
{ARTICLE_AD}
<h2>Ne zaman somut?</h2>
<p>Üretim tarihi, watt ve yazılım kilidi resmi metinde netleşince. O zamana kadar Jalapeno yol haritasıdır. Eldeki asistanın kalitesi, bu çip kutusundan bağımsızdır.</p>
<ul><li>Training ile inference’ı karıştırma</li><li>Ev cihazı sanma</li><li>Token fiyatını SLA ile oku</li></ul>
<p>Jalapeno sunucu inference oyunudur. Cep telefonu duyurusu değildir.</p>
{note("https://openai.com/index/openai-broadcom-jalapeno-inference-chip/", "openai.com")}
""",
    ),
    "prime-video-haziran-2026-takviminde-vox-machina-ve-yeni-orijinaller-var": n(
        "Prime Video haziran: Vox Machina 4 ve 2 başlık",
        "Amazon MGM’in haziran takvimini AcarTechs yığın değil; süre, yaş ve abonelik ayı olarak okur.",
        "Season 4, önceki sezonu bitirme borcudur.",
        f"""
<p>Amazon MGM Studios, Prime Video haziran 2026 takviminde The Legend of Vox Machina Season 4, Every Year After ve başka orijinaller duyurdu. AcarTechs listeyi yeniden dizmez. Vox Machina yetişkin animasyondur; çocuk profilinde otomatik oynatma kapatılır. Season 4, 1–3’ü bitirmemiş ev için ‘kaçırma’ değildir.</p>
<p>Prime, kargo üyeliğiyle karışır. Yalnızca bu dizi için yıllık kilitlemeyin. Ayın 1’i aç, 25’i gözden geçir. Aynı ay Netflix ve Disney yıldızı varsa üç kapı birden israftır.</p>
<h2>Bu ay</h2>
<p>Vox Machina veya bir orijinal film. İkinci istek listesi. İndirme hakkı yol için takvimden önemlidir.</p>
{ARTICLE_AD}
<h2>Spoiler ve tarih</h2>
<p>Resmi press sayfası, sosyal kare değil. Pencere tarih takvime belirsiz yazılır.</p>
<ul><li>Yaş etiketini oku</li><li>Önceki sezon borcu</li><li>Ayda 2 başlık</li></ul>
<p>Haziran Prime takvimi 30 günlük bütçedir. Maraton fişi değildir.</p>
{note("https://press.amazonmgmstudios.com/us/en/whatson/june-2026", "Amazon MGM press")}
""",
    ),
    "samsung-galaxy-watch-icin-yapay-zeka-destekli-saglik-ozelliklerini-duyurdu": n(
        "Galaxy Watch AI sağlık: eğilim, teşhis değil, pil",
        "Samsung’un yapay zekâ sağlık özelliklerini AcarTechs doktor yerine geçmeyen eğilim aracı olarak okur.",
        "Proaktif rehber, kırmızı uyarıda hekim cümlesini silmez.",
        f"""
<p>Samsung, Galaxy Watch için yapay zekâ destekli sağlık özelliklerini duyurdu. Adım ve nabızdan, uyku, stres ve öneri katmanına geçiş hedefleniyor. AcarTechs kutudaki tıbbi dili gerçek kullanımdan ayırır. Saat eğilim gösterir. Teşhis koymaz. Tek kötü gece paniği, 14 günlük eğilimden değersizdir.</p>
<p>Kayış gevşekse nabız yalan söyler. Soğuk parmakta oksijen gürültülüdür. Verinin hangi ülkeye gittiği, sağlık vaadinden ayrı gizlilik kararıdır. Her gece şarj edilen saat uyku takibini yarım bırakır; 5–7 gün giden model düzenli kullanımda daha çok iş üretir.</p>
<h2>Kime?</h2>
<p>Yürüyüş hatırlatması çoğu insanda işe yarar. Aile öyküsü ve hekimin ‘takip et’ dediği kişiye ek göz olabilir. Sporcu için GPS, sağlık kartından değerlidir. Kırmızı uyarıda uygulama değil hekim.</p>
{ARTICLE_AD}
<h2>Galaxy AI ile karıştırma</h2>
<p>Telefondaki asistan ile saatteki sağlık kartı aynı izin kutusunu paylaşabilir. Ayarları ayrı okuyun. Watch özelliği eğilimdir. Reçete değildir.</p>
<ul><li>14 günlük eğilim</li><li>Kayışı doğru sık</li><li>Veri bölgesine bak</li></ul>
<p>Galaxy Watch AI sağlık aynadır. Teşhis camı değildir.</p>
{note("https://news.samsung.com/global/samsung-introduces-next-gen-galaxy-watch-features-for-ai-powered-everyday-health-companion", "news.samsung.com")}
""",
    ),
    "samsung-vivatech-2026da-baglantili-bakim-vizyonunu-sergiledi": n(
        "Samsung VivaTech: connected care, izin, cihaz ağı",
        "Bağlantılı bakım vizyonunu AcarTechs fuar demosu değil; hangi verinin hangi cihaza aktığı olarak okur.",
        "Telefon, saat ve ev cihazı aynı rıza kutusunu varsaymaz.",
        f"""
<p>Samsung, VivaTech 2026’da connected care yaklaşımını sergiledi: cihazlar, servisler ve iş ortaklarıyla sağlık ve iyi yaşam deneyimini kesintisiz hale getirme. AcarTechs fuar videosunu ürün belgesi saymaz. En kritik konu veri ve izin. Sağlık verisi, televizyon önerisinden ayrı sınıftır.</p>
<p>Saat nabzı, telefon asistanı ve ev ekranı konuşuyorsa amaç, saklama ve iptal yazılı olmalıdır. ‘Daha anlamlı öneri’ cümlesi, sigorta veya işveren ile paylaşımı gizleyebilir. Çocuk ve yaşlı profilinde varsayılan paylaşım kapalı olsun.</p>
<h2>Ne somut, ne vizyon?</h2>
<p>VivaTech vizyon durağidir. Satın alma, Türkiye fiyatı, yazılım yılı ve servis ilinden sonra gelir. Fuar standı menteşe ve cam tamir fiyatını göstermez.</p>
{ARTICLE_AD}
<h2>İzin listesi</h2>
<p>Hangi cihaz, hangi sağlık metriği, hangi ülke. Connected care kesintisiz öneridir. Kesintisiz paylaşım olmak zorunda değildir.</p>
<ul><li>Sağlık verisi rızasını ayrı oku</li><li>Çocuk profilinde varsayılan paylaşımı kapat</li><li>Fuarı fiyat listesi sanma</li></ul>
<p>Bağlantılı bakım vizyonu izin mimarisidir. Demosu ürün değildir.</p>
{note("https://news.samsung.com/global/samsung-redefines-everyday-wellness-with-connected-care-solutions-at-vivatech-2026", "news.samsung.com")}
""",
    ),
    "whatsapp-kullanici-adi-rezervasyonunu-baslatti": n(
        "WhatsApp kullanıcı adı: rezervasyon, anahtar, numara gizleme",
        "Rezervasyon sürecini AcarTechs ‘numara bitti’ değil; kimlik, anahtar ve sahte hesap süzgeci olarak okur.",
        "Kullanıcı adı herkese açık rehber değildir.",
        f"""
<p>WhatsApp, özellik yıl içinde açılmadan önce kullanıcı adı rezervasyonunu başlattı. İlk iletişimde telefon numarasının doğrudan paylaşılmasını azaltmak hedefleniyor. Adlar herkese açık dizinde listelenmeyecek; ulaşmak için tam adın bilinmesi gerekecek. İsteğe bağlı kullanıcı adı anahtarı açılırsa, yazmak isteyen ek anahtarı da bilecek. AcarTechs bunu gizlilik katmanı olarak okur. Sihirli anonimlik değildir.</p>
<p>Rezervasyon: Ayarlar &gt; Hesap &gt; Kullanıcı adı, güncel sürüm. Ülkelere kademeli açılınca uygulama içi bildirim gelecek. ‘Alınmazsa biter’ paniği, sahte rezervasyon siteleri üretir. Yalnızca resmi uygulama. Adınızı 2014 e-posta gibi seçmeyin; iş ve aile karışır.</p>
<h2>Dolandırıcılık</h2>
<p>Yakın ad taklidi (bir harf fark) yaşlı akrabaya borç mesajı atabilir. Anahtarı aile grubunda önceden konuşun. Numara gizlense de profil fotoğrafı ve durum satırı kimlik sızdırır.</p>
{ARTICLE_AD}
<h2>İş hesabı</h2>
<p>Kurumsal WhatsApp, kişisel addan ayrı dursun. Rezervasyon, numara paylaşımını azaltır. Yedek ve cihaz kilidini silmez.</p>
<ul><li>Yalnızca resmi uygulamadan ayırt</li><li>Anahtarı ailede konuş</li><li>Sahte rezervasyon sitesine gitme</li></ul>
<p>Kullanıcı adı rezervasyonu kimlik süzgecidir. Rehber listesi değildir.</p>
{note("https://blog.whatsapp.com/its-time-to-reserve-your-whatsapp-username", "blog.whatsapp.com")}
""",
    ),
}

# Partner network slug typo in dump vs actual folder
NEWS["openai-partner-network-ile-yapay-zeka-projelerinde-is-ortagi-donemi-basladi"] = NEWS.pop(
    "openai-partner-network-ile-yapay-zeka-projelerinde-is-ortaki-donemi-basladi"
)

NEWS_EXTRA = {
    "android-bench-yapay-zeka-modellerini-android-gelistirme-gorevlerinde-olcuyor": e(
        "Lider panosu sizin Compose işiniz değildir",
        "Harbor’a taşınan Android Bench, Jetpack Compose, platform API ve wearable görevlerinde modeli ölçer. AcarTechs ‘en iyi model’ sıralamasını kopyalamaz. Sizin işiniz Compose geçişi ise o satıra bakın; genel sohbet skoru yanıltır. Maliyet sütunu, başarı oranından ayrı okunur. Ücretsiz katman, panodaki şampiyonu taşımaz.",
        "Sekiz yeni model, sprint kararı değildir",
        "Claude, GLM, Kimi, MiniMax ve Qwen satırları vitrindir. Ekip, bir modeli 2 hafta gerçek PR’da denemeden panoya göre lisans değiştirmez. Gizli kodu ölçüm servisine yapıştırmayın. Bench, pazarlama iddiasına karşı referanstır. Üretim kapısı değildir.",
        "Mobil ekip için pratik",
        "İç test: aynı 10 görev, sizin kod stilinize. Pano yön gösterir. Sizin CI yeşilidir.",
        ["Görev satırına bak, genel skora değil", "Maliyet sütununu oku", "Lisansı 2 haftalık PR’siz değiştirme"],
        "Android Bench karşılaştırılabilir referanstır. Otomatik model seçimi değildir.",
        skip_ad=True,
    ),
    "android-gelistirici-araclarinda-verimlilik-odakli-uc-yeni-guncelleme-duyuruldu": e(
        "Üç güncelleme aynı sprint’e girmez",
        "Studio, komut satırı ve performans ölçümü ayrı risk taşır. CI’yı kıran CLI notunu önce alın. Editör içi yardım, stajyerin sır yapıştırmasına davet olabilir. AcarTechs üç başlığı tek ‘Android hızlandı’ cümlesine sıkıştırmaz.",
        "Son kullanıcı dolaylıdır",
        "Daha iyi test, daha az ısınan uygulama üretebilir. Kullanıcıya araç zinciri duyurusu yazmak kopya envanterdir. Resmi blog tarihini sprint notuna bağlayın. Önizleme kanalını üretim sanmayın.",
        "Orta segment cihazda ölçün",
        "Vitrin emülatörü yalan söyler. Verimlilik güncellemesi sizin darboğazınızda işe yarar.",
        ["CLI notunu CI’dan önce oku", "Önizlemeyi kararlı sanma", "Gerçek telefonda ölç"],
        "Haziran verimlilik notu üç ayrı kapıdır. Tek müjde değildir.",
        skip_ad=True,
    ),
    "cihaz-ici-yapay-zeka-ajanlari-telefon-ve-bilgisayarlarda-yeni-donemi-aciyor": e(
        "Qualcomm–Hugging Face: hibrit, gizlilik, ısınma",
        "24 Haziran 2026 iş birliği, açık modelleri telefondan veri merkezine taşımayı kolaylaştırmayı hedefler. AcarTechs ajanı sihir saymaz. Cihaz içi gizlilik ve gecikme kazandırır; ısınma ve disk yer. Bulut büyük model içindir. Uçak modunda durmayan özellik yerel değildir.",
        "Agentic AI her uygulamaya anahtar vermez",
        "Planlayan ajan, ödeme ve e-posta adımında onay ister. NPU TOPS’u, sürücü kullanmıyorsa vitrindir. Otomotiv ve giyilebilir, telefonla aynı yazılım yığını değildir; duyuruyu tek dünya sanmayın.",
        "Geliştirici için",
        "Açık modeli on-device çalıştırmak lisans, kota ve ısınma bütçesidir. Hibrit, varsayılan bulut demek değildir.",
        ["Uçak modunda dene", "Onay tuşunu kapatma", "NPU gerçekten kullanılıyor mu bak"],
        "Cihaz içi ajan hibrit iş yüküdür. Sohbet kutusunun rebrand’i değildir.",
    ),
    "cumhurbaskani-erdogandan-yapay-zeka-aciklamasi-dunya-keskin-bir-donusumden-geciyor": e(
        "Siyasi çerçeve, ürün belgesi değildir",
        "AcarTechs resmi açıklamayı aktarır, slayt vaadi eklemez. ‘Dönüşüm’ cümlesi, sizin KVKK politikanızı, okul ödev kuralınızı veya şirket ajan yasağınızı yazmaz. Okur için pratik: resmi metin, sonra kendi sektörünüzdeki somut kural (veri, etiket, insan onayı).",
        "Ne çıkarılmamalı",
        "Açıklama, belirli bir modelin Türkiye’de zorunlu olduğu anlamına gelmez. Yatırım ve eğitim vurgusu, yarınki ürün fiyatını sabitlemez. Kaynak metne bağlanır; yorum katmanı ayrı durur.",
        "Kurum ve okul",
        "Politika cümlesi yazılmadan ‘devlet böyle dedi’ diye müşteri verisi modele yapıştırılmaz.",
        ["Resmi metni oku", "Ürün vaadi ekleme", "Kendi veri kuralını ayrı yaz"],
        "Siyasi yapay zekâ çerçevesi gündemdir. Uygulama kılavuzu sizin politikanızdır.",
    ),
    "github-copilot-icin-tarayici-araclari-vs-codeda-genel-kullanima-acildi": e(
        "Tarayıcı aracı, ajanın tıklamasıdır",
        "VS Code’da genel kullanıma açılan tarayıcı araçları, Copilot’un sayfa açıp form doldurmasına yaklaşır. AcarTechs bunu üretkenlik ve risk olarak okur. Banka ve admin paneli oturumu, ajan tarayıcısına verilmez. Onay tuşu yoksa ‘genel kullanım’ tehlikelidir.",
        "Şirket kirası",
        "Kişisel Copilot, iş reposu ve iç paneli görmemelidir. Test tenancy. Kayıt, hangi URL’nin ziyaret edildiğini tutar mı bakın.",
        "Ne zaman işe yarar?",
        "Dokümantasyon gezintisi ve yerel preview. Üretim ödeme sayfası değil.",
        ["Admin oturumunu ajana verme", "Onay tuşu", "İş reposunu kişisel Copilot’a bağlama"],
        "Tarayıcı aracı tıklama gücüdür. Anahtar teslimi değildir.",
        skip_ad=True,
    ),
    "github-copilot-uygulamasi-tum-kullanicilar-icin-acildi": e(
        "Copilot uygulaması IDE değildir",
        "Tüm kullanıcılara açılması, VS Code’un yerine geçmez. Mobil ve masaüstü sohbet, repo bağlamı olmadan uydurur. AcarTechs bunu taslak ve açıklama aracı sayar. Bitmiş PR değildir. Kota ve plan sayfasını okuyun.",
        "Sır",
        "Ekran görüntüsü ve log yapıştırmak üretim sırrını taşır. Öğrenci planı iş müşterisine gitmez.",
        "Ne için açın?",
        "Hata mesajını açıklattırma, test fikri. Merge emri değil.",
        ["Repo bağlamı yoksa şüphe et", "Log yapıştırma", "Kota bitişini izle"],
        "Copilot uygulaması sohbet kapısıdır. IDE ve CI değildir.",
        skip_ad=True,
    ),
    "github-copilot-uygulamasina-guvenlik-incelemesi-ozelligi-geldi": e(
        "Güvenlik incelemesi, pentest değildir",
        "Copilot’un güvenlik taraması bilinen kalıpları işaretler. İş mantığı ve yetki aşımını kaçırır. AcarTechs yeşil rozeti onay kapısı saymaz. İnsan review ve bağımlılık taraması (lockfile) yerinde kalır.",
        "Yanlış yeşil",
        "Rozet, stajyeri ‘güvenli’ merge’e iter. Kritik yolda SAST/DAST ayrıdır. Gizli anahtarı sohbete yapıştırarak taratmak, taramadan büyük risktir.",
        "Nasıl kullanılır?",
        "PR taslağındaki düşük asılı meyve. Sertifika değil.",
        ["Rozeti pentest sanma", "Lockfile tarasın", "Sırrı sohbete yapıştırma"],
        "Copilot güvenlik incelemesi yardımcı işarettir. Onay kapısı değildir.",
        skip_ad=True,
    ),
    "github-copilot-vscode-haziran-2026-guncellemelerini-duyurdu": e(
        "Haziran VS Code Copilot: notu sprint’e bağla",
        "Aylık not, ajan, tamamlama ve sohbet kutusunu kaydırır. AcarTechs her maddeyi almak zorunda değilsiniz der. Kırılan kısayol, bir gün eski sürüme pin ile çözülür. Şirket politikası yeni ajanı kapatabilir.",
        "Öğrenci ve iş",
        "Aynı güncelleme iki planda farklı kota taşır. Changelog’u plan sayfasıyla çarpın.",
        "Ne zaman bekleyin?",
        "Cuma akşamı üretim hotfix’inde güncellemeyin. Pazartesi iç test.",
        ["Changelog’u planla çarp", "Cuma hotfix’te güncelleme", "Ajanı politika yoksa açma"],
        "Haziran Copilot notu sprint seçmecisidir. Otomatik yükseltme emri değildir.",
        skip_ad=True,
    ),
    "github-copilot-vs-code-temmuz-2026-guncellemelerini-yayimladi": e(
        "Temmuz notu hazirandan ayrı süzülür",
        "Aynı ürün, ayrı ay, ayrı kırılma. AcarTechs iki changelog’u tek ‘Copilot yenilendi’ sayfasında eritmez. Temmuz maddesini kendi PR akışınızda 3 gün deneyin. Agent ve model değişimi, dünkü talimatı bozabilir.",
        "Pin ve politika",
        "Uzantı sürümünü kilitlemek, sürpriz ajanı keser. İş tenancy’sinde otomatik update kapatılır.",
        "Ölçün",
        "Tamamlama kabul oranı düştüyse model veya ayar kaymıştır. Suç ‘ben bozuldu’ değil changelog’dur.",
        ["Temmuz notunu ayrı oku", "Uzantıyı pin’leyebil", "3 gün iç test"],
        "Temmuz Copilot güncellemesi ayrı süzgeçtir. Haziran kopyası değildir.",
        skip_ad=True,
    ),
    "google-gemini-cli-adini-antigravity-cli-olarak-degistirme-surecini-duyurdu": e(
        "İsim değişikliği, script’lerinizi kırar",
        "Gemini CLI → Antigravity CLI geçişi PATH, doküman ve CI satırını etkiler. AcarTechs bunu rebrand + yön olarak okur. Eski komut takma adı ne kadar duracak, resmi yazıdan işaretleyin. Ajan CLI, sohbet kutusundan çok dosya yazar; sır ve lockfile ayrı kova.",
        "Ne değişmez?",
        "Test, lisans ve insan review. İsim değişince politika değişmez. Şirket içi wrapper’ı bir haftada güncelleyin.",
        "Geliştirici",
        "Dokümantasyon linklerini, eğitim slaytını ve alias’ı aynı PR’da tutun. Yarım geçiş, ‘komut yok’ paniğidir.",
        ["PATH ve CI’yı güncelle", "Takma ad süresini oku", "CLI ajana sır yapıştırma"],
        "Antigravity CLI geçişi isim ve iş akışıdır. Sihirli ajan değildir.",
        skip_ad=True,
    ),
    "google-i-o-2026-gelistirici-oturumlarinda-yapay-zeka-araclari-one-cikti": e(
        "Keynote yığını, sizin SDK’nız değildir",
        "Android, web, Cloud ve Gemini aynı saatte konuşulur. AcarTechs her maddeyi sprint’e yazmaz. Bu hafta derlemeyi kıran veya kota değiştiren satır alınır. Gerisi istek listesi. Resmi developers.googleblog.com metni, Twitter karesinden önce gelir.",
        "Ajan dönemi sloganı",
        "Kod tamamlayıcıdan iş akışı ortağına geçiş, onay tuşu ve test olmadan tehlikelidir. I/O demosu üretim SLA’sı değildir.",
        "Son kullanıcı",
        "Dolaylıdır. Araç haberi kullanıcıya ‘Google I/O oldu’ diye yazılmaz; ürün düşünce yansır.",
        ["Derlemeyi kıranı al", "Demosu SLA sanma", "Kaynağı resmi blog"],
        "I/O 2026 keynote süzgeçtir. Yığın özeti değildir.",
        skip_ad=True,
    ),
    "google-litert-js-ile-tarayicida-calisan-yapay-zekayi-hizlandiriyor": e(
        "WebGPU/WebNN her telefonda yoktur",
        "LiteRT.js .tflite’i tarayıcıya taşır. AcarTechs bunu gizlilik ve gecikme kazancı, cihaz piyangosu olarak okur. Düşük RAM’li telefon, model indirmesinde şişer. Çevrimdışı vaadi, ilk indirme ve tarayıcı desteği olmadan boştur.",
        "Ne taşınır?",
        "Kamera, ses, küçük metin. 70B parametre değil. Hassas görüntü cihazdaysa iyi; model çereze sığmaz, önbellek politikası yazın.",
        "Geliştirici",
        "WASM boyutu, yedek CPU yolu, izin kutusu (kamera). LiteRT.js kapıdır. Her model web’e sığmaz.",
        ["Cihaz RAM’ini say", "WebGPU yoksa yedek yol", "Model önbelleğini yaz"],
        "Tarayıcıda yapay zekâ cihaz ve model boyutuyla sınırlıdır. Sunucusuz sihir değildir.",
        skip_ad=True,
    ),
    "netflix-haftalik-top-10-listesinde-enola-holmes-3-zirveye-cikti": e(
        "29 Haziran Top 10: Enola zirve, I Will Find You dizi",
        "Film ve dizi ayrı sütundur. AcarTechs ikisini tek ‘Netflix birincisi’ cümlesine yığmaz. Enola Holmes 3 açılış tıklamasıdır; üçüncü hafta kalıcılık ayrıdır. 6 saatinize bir başlık. Yaş etiketi çocuk profilinde.",
        "Yaz rekabeti",
        "Aynı dönemde macera, aile ve drama paylaşır. Top 10 zevkiniz değil. Spoiler kareyi açmayın.",
        "Abonelik",
        "Zirve için yıllık kilitlemeyin. Keşif listesidir.",
        ["Film/dizi sütununu karıştırma", "Ayda 2 başlık", "Yaş etiketini oku"],
        "29 Haziran Tudum tıklama vitrinidir. Kanon değildir.",
        skip_ad=True,
    ),
    "openai-chatgpt-agent-ile-gorevleri-tek-akista-topluyor": e(
        "Onay tuşu olmayan ajan, ödeme tuşudur",
        "ChatGPT agent araştırma ve çok adımlı işi birleştirir. AcarTechs durdurma, izin ve satın alma adımını merkeze alır. Web’de işlem, hesap girişi olmadan ‘tamamlandı’ sanılırsa fatura sizin olur. Masa başı araştırma iyi adaydır. Banka ve sağlık kötü adaydır.",
        "Kontrol",
        "Ara adımda durdurabiliyor musunuz? Kaynak linki var mı? Şirket metnini tüketici ajana yapıştırmayın.",
        "2026 yönü",
        "Sohbet botundan görev yardımcısına geçiş. Sorumluluk hâlâ tıklayanındır.",
        ["Ödeme adımında onay", "Sağlık/hukuku ajana bırakma", "Durdurmayı dene"],
        "ChatGPT agent görev akışıdır. Kendi başına muhasebeci değildir.",
        skip_ad=True,
    ),
    "samsung-temmuz-2026-galaxy-unpacked-icin-yeni-katlanabilir-donemini-isaret-etti": e(
        "22 Temmuz Londra: davet, spekülasyon değil",
        "A New Shape Unfolds daveti model adı ve fiyat yazmaz. AcarTechs menteşe, iç cam tamiri, dış ekran ve yazılım yılı spekülasyonunu etkinlik gününe bırakır. Mevcut katlanırını satmak için davet gerekçesi değildir.",
        "Alıcı listesi",
        "Etkinlik sonrası: fiyat, Türkiye tarihi, 7 yıl yama vaadi, iç cam fiyatı. Dördü yoksa ‘yeni dönem’ slayttır.",
        "İzleme",
        "Resmi Newsroom ve canlı yayın. Sızıntı karesi takvime işlenmez.",
        ["Fiyat ve servis ilini bekle", "İç cam tamirini sor", "Daveti sipariş sanma"],
        "Unpacked daveti form faktörü işaretidir. Teknik cetvel değildir.",
        skip_ad=True,
    ),
    "yapay-zeka-cihazlari-iddialari-hizlanirken-openai-donanim-ekibini-buyutuyor": e(
        "io Products birleşmesi telefon duyurusu değildir",
        "OpenAI’nin doğruladığı: Jony Ive’ın io ekibinin katılması ve tasarım sorumluluğu. MediaTek telefon ve Musk cihazı iddiası resmi metin değildir. AcarTechs iddiayı iddia yazar. Kesin ürün cümlesi kurmaz.",
        "Neden izlenir?",
        "Ajanlar uygulama ızgarasını zorluyor. Donanım ekibi, ekran-merkezli telefonun yanına başka bir arayüz arayışı olabilir. Takvim yoksa ön sipariş yok.",
        "Okur disiplini",
        "Resmi openai.com/sam-and-jony/. Sızıntıyı stok fotoğrafıyla karıştırmayın.",
        ["Resmi metin / iddia ayrımı", "Ön sipariş yok", "Sızıntıyı takvime yazma"],
        "Donanım ekibi büyümesi kadro haberidir. Model numarası değildir.",
        skip_ad=True,
    ),
    "yapay-zeka-sunuculari-bellek-pazarinda-fiyat-baskisini-artiriyor": e(
        "TrendForce çeyrek tahmini, mağaza etiketini bugün kilitlemez",
        "DRAM yüzde 58–63, NAND yüzde 70–75 bandı 2026/2Ç beklentisidir. AcarTechs bunu PC, telefon ve kart fiyatına dolaylı baskı olarak okur. Stokçuluk paniği, TBW’si düşük SSD’yi sistem diskine koydurur. Sistem ve arşivi ayırın.",
        "Üretici planı",
        "Telefon markası üretim adedini kısabilir. 16 GB lehimli laptop, 32 GB’a zamlanır. İkinci el RAM, sahte etiket taşır.",
        "Alıcı",
        "İhtiyaç varsa al, ‘gelecek ay daha kötü’ diye 4 TB yedeksiz disk doldurma. 3-2-1 yedek.",
        ["İhtiyacı yaz", "QLC’yi sistem diskine panikle koyma", "Fiyat tahminini sipariş emri sanma"],
        "Bellek baskısı maliyettir. Bugünkü etiket spekülasyonu değildir.",
        skip_ad=True,
    ),
    "yenilenmis-elektronik-cihazlarda-dijital-sicil-donemi-basliyor": e(
        "1 Ağustos 2026 YÜBİS: sicil, 14 gün, merkeze sor",
        "Ticaret Bakanlığı yönetmeliği telefon, PC, saat, konsolda dijital sicil ister. AcarTechs bunu ikinci el geçmiş körlüğüne karşı okur. Sicil yoksa fiyat ucuzluğu risk primidir. Mağaza cayma 14 gün; açılmış kulaklıkta istisna okuyun.",
        "Alıcı listesi",
        "YÜBİS kaydı, değişen parça, sertifika, satıcı unvanı. Elden ‘yenilenmiş’ yazısı sistem değildir. IMEI sicille eşleşmeli.",
        "Sektör",
        "Yenileme merkezi şartları sıkılaşır. Kayıt dışı vitrin, denetimde düşer. Döngüsel ekonomi, sicilsiz kutu değildir.",
        ["Sicili sor", "14 gün cayma", "IMEI eşleşsin"],
        "Dijital sicil şeffaflıktır. Ucuz kutu belgesi değildir.",
        skip_ad=True,
    ),
    "yurt-disi-telefon-kayitlarinda-e-devlet-donemi-ve-2026-harci": e(
        "Harç 54 bin TL bandı: e-Devlet, IMEI, ödeme sahibi",
        "BTK IMEI Kaydet hizmeti kimlik, yurda giriş ve cihazı bağlar. AcarTechs tutarı her yıl yeniden değerlemeyle değişir diye yazar; işlem öncesi e-Devlet, BTK ve GİB ekranını son kez okuyun. Çift SIM’de hangi IMEI. Kayıt kişiye bağlıdır; devir ayrı kuraldır.",
        "Kayıtsız cihaz",
        "Süre bitince şebeke kesilir. ‘Bir ay idare eder’ tatil uzamasında pahalıdır. Sahte IMEI kayıtçısı, harcı da kimliği de yakar. Yalnızca turkiye.gov.tr.",
        "Ödeme",
        "Harç ödeyen ile kayıt sahibi aynı olsun. Faturasız elden telefon, kayıtta yurda girişle uyuşmazsa reddedilir.",
        ["Güncel harcı GİB’den doğrula", "Doğru IMEI", "Sahte aracıya gitme"],
        "Yurt dışı kayıt e-Devlet ve güncel harçtır. Forum tutarı değildir.",
        skip_ad=True,
    ),
}

# -*- coding: utf-8 -*-
"""Rewrite /oyun/ inventory, identity pages, and duplicate game posts for AdSense policy."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "public"

ARTICLE_AD = """
<aside class="acartechs-adsense-shell is-horizontal placement-article" aria-label="Reklam">
			<span class="acartechs-ad-disclosure">Reklam</span>
			<div class="acartechs-adsense-unit is-horizontal">
				<ins class="adsbygoogle"
					style="display:block"
					data-ad-client="ca-pub-4367344438750629"
					data-ad-slot="5763121236"
					data-ad-format="auto"
					data-full-width-responsive="true"></ins>
			</div>
		</aside>
"""

ARTICLES = {
    "xbox-wire-temmuz-ayi-indie-selects-listesini-yayimladi": {
        "title": "Xbox Indie Selects temmuz seçkisi: bağımsız oyunu nasıl okumalı?",
        "description": "Xbox Wire temmuz Indie Selects listesini duyurdu. AcarTechs, seçkiyi kopyalamak yerine oyuncunun neye bakması gerektiğini anlatıyor.",
        "dek": "Resmi seçki bir keşif listesidir; satın alma kararı için tür, seans süresi ve erişim modeline bakmak gerekir.",
        "body": f"""
<p>Xbox Wire’ın temmuz Indie Selects paylaşımı, büyük stüdyo takvimlerinin yanında duran bağımsız yapımları görünür kılmak için hazırlanmış bir keşif listesidir. AcarTechs’te bu tür duyuruları oyun adlarını yan yana dizerek aktarmıyoruz. Asıl soru şudur: liste, yaz döneminde kısa bir deney mi arıyorsunuz, yoksa birkaç saatlik hikâye mi istiyorsunuz, bunu ayırmanıza yardım ediyor mu?</p>
<p>Bağımsız oyun seçkilerinin değeri, “hangi oyun çıktı” cümlesinden değil, oyuncunun riskini azaltmasından gelir. Küçük ekiplerin işlerinde demo, erken erişim, niş tür ve kısa seans sık görülür. Bu yüzden resmi listede bir başlık görünce hemen mağaza sayfasına bakmak, etiketleri ve tahmini oyun süresini kontrol etmek daha doğru bir reflekstir.</p>
<h2>Seçki neden haber değeri taşır?</h2>
<p>Platformların indie vitrinleri, mağaza algoritmasının tek başına öne çıkarmadığı işlere ikinci bir kapı açar. Oyuncu tarafında bu, “bilmediğim bir yapımı denemek” maliyetini düşürür. Yayıncı tarafında ise görünürlük, inceleme ve istek listesi trafiği demektir. Yani Indie Selects bir ödül töreni değil, keşif aracıdır.</p>
{ARTICLE_AD}
<h2>Listeye bakarken üç filtre</h2>
<p>Birinci filtre türdür. Aynı seçkide bulmaca, anlatı, aksiyon ve kısa arcade yan yana durabilir. İkinci filtre erişimdir: oyun Game Pass’te mi, ayrı satış mı, yoksa yalnızca belirli bölgelerde mi görünüyor? Üçüncü filtre zamandır. Yaz döneminde 30 dakikalık bir deney ile 12 saatlik bir hikâye aynı ihtiyaç değildir.</p>
<p>Bu üç filtreyi kullanmadan listedeki her başlığı “kaçırılmaması gereken oyun” diye okumak, duyuruyu olduğundan büyük gösterir. AcarTechs’in yaklaşımı, resmi kaynağı işaret etmek ve oyuncunun kendi kütüphanesine göre elemesini kolaylaştırmaktır.</p>
<h2>Oyuncu için pratik sonuç</h2>
<p>Temmuz seçkisi, yeni çıkan AAA takviminin boşluklarını doldurmak isteyenler için işe yarar. Özellikle kısa seans arayan, denemeye açık ve bütçesini abonelikle yöneten oyuncular için keşif maliyeti düşüktür. Tam tersine, yalnızca uzun kampanya ve rekabetçi çok oyunculu arayan biri için listenin tamamı zorunlu değildir.</p>
<p>Satın alma veya indirme kararı vermeden önce resmi Xbox sayfasındaki erişim notunu, dil desteğini ve sistem gereksinimini kontrol edin. Seçkiye girmek, oyunun her cihazda aynı performansı vereceği anlamına gelmez.</p>
<p class="acartechs-source-note">Kaynak: <a href="https://news.xbox.com/en-us/2026/07/01/indie-selects-july/" target="_blank" rel="nofollow noopener">Xbox Wire, Indie Selects July</a></p>
""",
    },
    "xbox-konsol-fiyatlarinda-agustos-itibariyla-yeni-donem-basliyor": {
        "title": "Xbox konsol fiyatı değişince ne yapılmalı?",
        "description": "Xbox, 1 Ağustos 2026 itibarıyla konsol fiyatlarını güncelliyor. AcarTechs duyuruyu bütçe, depolama ve zamanlama açısından inceliyor.",
        "dek": "512 GB ve 1 TB modellerde fiyat artışı, 2 TB modelin sonlanması: donanım kararı artık takvim işidir.",
        "body": f"""
<p>Xbox Wire, 1 Ağustos 2026’dan itibaren konsol fiyatlarında dünya genelinde yeni bir düzenlemeye gidileceğini duyurdu. 512 GB ve 1 TB modellerde artış öngörülürken 2 TB modelin satışı sonlandırılacak. Bu, yalnızca bir etiket değişikliği değil; depolama, ikinci el ve “şimdi mi sonra mı” kararını aynı anda etkileyen bir donanım haberi.</p>
<p>Konsol fiyatı yükselince oyuncunun ilk refleksı panik almak olmamalı. Asıl bakılması gereken üç kalem var: ihtiyaç duyulan dahili depolama, Game Pass ve dijital kütüphane alışkanlığı, bir de mevcut nesil oyunların sizin için yeterli olup olmadığı.</p>
<h2>2 TB model neden kritik?</h2>
<p>Güncel AAA oyunlar 80–150 GB aralığına sıkça oturuyor. 512 GB’lık bir cihazda sistem alanı düşülünce pratik boşluk hızla daralır. 2 TB modelin kalkması, yüksek depolama isteyen oyuncuyu harici SSD, genişletme kartı veya dijital kütüphaneyi seyreltme seçeneklerine iter. Bu maliyet, etiket fiyatındaki artıştan bağımsız ikinci bir bütçe kalemidir.</p>
{ARTICLE_AD}
<h2>Kim için acil, kim için beklemeli?</h2>
<p>Hâlâ eski nesilde kalan, fiziksel koleksiyonu olan ve 1 Ağustos öncesi stok gören oyuncu için zamanlama önemlidir. Zaten Series cihazı olan, oyunlarını Game Pass ve bulut üzerinden yöneten biri için fiyat değişikliği dolaylıdır: yeni konsol almak zorunda değilsiniz, ama ikinci bir cihaz veya hediye planı varsa tarih netleşmiştir.</p>
<p>Türkiye’de nihai rafta görünen fiyat, kur, vergi ve stok süresine göre resmi duyurudan sapabilir. Bu yüzden “dünya genelinde artış” cümlesini yerel mağaza etiketine birebir taşımak yanıltıcı olur. Kararı vermeden önce satıcının güncel stok ve garanti koşullarına bakın.</p>
<h2>AcarTechs notu</h2>
<p>Donanım haberlerinde en sık yapılan hata, duyuruyu yalnızca zam olarak okumaktır. Burada asıl kırılım depolama seçeneklerinin daralmasıdır. 512 GB alan kişi, oyun silme döngüsüne girmeye razı mı? 1 TB alan kişi, 2026 kütüphanesi için yeterli mi? 2 TB’ı kaçıran kişi, genişletme maliyetini göze alıyor mu? Bu üç soru, resmi metindeki cümlelerden daha işe yarar.</p>
<p class="acartechs-source-note">Kaynak: <a href="https://news.xbox.com/en-us/2026/06/25/xbox-console-price-update/" target="_blank" rel="nofollow noopener">Xbox Wire, console price update</a></p>
""",
    },
    "xbox-game-pass-temmuz-listesine-yeni-oyunlar-ekleniyor": {
        "title": "Game Pass temmuz listesi: katalogdan nasıl seçilir?",
        "description": "Xbox Game Pass temmuz 2026 dalgasını AcarTechs, kopya liste yerine oyun süresi, tür ve abonelik katmanı üzerinden okuyor.",
        "dek": "Gears of War: Reloaded, Planet Crafter ve Palworld 1.0 aynı ayda gelebilir; hepsi aynı oyuncu için zorunlu değildir.",
        "body": f"""
<p>Microsoft, Temmuz 2026 Game Pass dalgasında Gears of War: Reloaded, The Planet Crafter, Tony Hawk’s Pro Skater 1+2 ve Palworld 1.0 gibi başlıkları öne çıkardı. Liste kalabalık görünür; fakat abonelik katalogları “her oyunu oyna” diye okunmaz. Doğru okuma, kendi haftalık oyun sürenize göre üç-dört başlık seçmektir.</p>
<p>Reloaded tipi yenilenmiş markalar, seriyi tanıyan oyuncuya düşük öğrenme maliyeti sunar. Planet Crafter gibi üretim-hayatta kalma işleri ise uzun oturum ister. Tony Hawk kısa seanslı, skor odaklı bir moladır. Palworld 1.0 ise zaten kütüphanede olan bir oyunun olgunlaşma adımıdır: yeni almak değil, devam etmek meselesi.</p>
<h2>Katalog değerini şişirmemek</h2>
<p>Aynı ayda aksiyon, spor, hayatta kalma ve açık dünya görmek, Game Pass’in tür çeşitliliğini gösterir. Bu, her başlığın sizin için “kaçırılmaması gereken” olduğu anlamına gelmez. AcarTechs, resmi listeleri aktarırken oyuncuya seçim kriteri vermeyi tercih eder: seans süresi, çok oyunculu ihtiyaç ve cihaz (konsol, PC, bulut).</p>
{ARTICLE_AD}
<h2>Ayrılacak oyunlar da planın parçası</h2>
<p>Game Pass duyurularında eklenenler kadar kütüphaneden çıkacaklar da önemlidir. İndirdiğiniz ama bitirmediğiniz bir yapım ayrılıyorsa, kalan süreyi ona ayırmak yeni çıkanı denemekten daha rasyonel olabilir. Katalog haberini yalnızca ekleme listesi diye okumak, aboneliğin asıl mekaniğini kaçırır.</p>
<p>Katman farkı da unutulmamalı. Bir oyun konsolda gün 1 gelebilir, PC veya bulutta farklı tarihte görünebilir. Kararı vermeden Xbox uygulamasındaki bölgesel tarihi ve hangi Game Pass katmanını kapsadığını kontrol edin.</p>
<h2>Kim için değerli?</h2>
<p>Haftada 4–6 saat oynayan biri için Reloaded veya Tony Hawk daha gerçekçi bir plan üretir. Hafta sonunu açık dünyaya ayırabilen oyuncu Planet Crafter veya Palworld güncellemesine yönelebilir. Amaç, duyurudaki isimleri ezberlemek değil, kendi takviminize üç başlık yazmaktır.</p>
<p class="acartechs-source-note">Kaynak: <a href="https://news.xbox.com/en-us/2026/07/07/xbox-game-pass-july-2026-wave-1/" target="_blank" rel="nofollow noopener">Xbox Wire, Game Pass July 2026 Wave 1</a></p>
""",
    },
    "xbox-wire-20-24-temmuz-haftasinin-yeni-oyunlarini-duyurdu": {
        "title": "Haftalık Xbox çıkış listesi nasıl kullanılır?",
        "description": "Xbox Wire’ın 20-24 Temmuz haftalık listesini AcarTechs, ham duyuru yerine platform ve öncelik rehberi olarak okuyor.",
        "dek": "Haftalık listeler alışveriş fişi değildir; cihaz, depolama ve oynama penceresine göre elenir.",
        "body": f"""
<p>Xbox Wire’ın 20–24 Temmuz haftası için yayımladığı çıkış listesi, Series X|S, Xbox One, PC ve Game Pass tarafına dağılan başlıkları bir araya getirir. Bu formatın tuzağı, her satırı eşit önemde okumaktır. Haftalık listeler bir vitrindir; sizin kütüphaneniz değildir.</p>
<p>AcarTechs bu listeleri iki soruyla okur. Bir: oyun sizin cihazınızda gerçekten çalışıyor mu? Xbox One satırı, Series oyuncusu için her zaman müjde değildir. İki: başlık Game Pass’te mi, yoksa tam fiyatlı mı? Aynı haftada ücretsiz denenecek bir yapım ile 70 dolarlık bir çıkış yan yana durabilir.</p>
<h2>Depolama ve indirme gerçeği</h2>
<p>Haftalık listelerin görünmeyen maliyeti indirme kuyruğudur. 100 GB üstü birkaç oyunu “bu hafta çıkıyor” diye aynı anda çekmek, hem bağlantıyı hem dahili depolamayı tıkar. Pratik yöntem, listeden en fazla iki başlık seçip birini bitirmeden üçüncüyü indirmemektir.</p>
{ARTICLE_AD}
<h2>Game Pass satırı neden ayrı okunmalı?</h2>
<p>Listede Game Pass işareti olan oyun, satın alma baskısını düşürür. İşareti olmayan oyun ise bütçe kararıdır. Haftalık özetleri tek bir “yeni oyunlar geldi” başlığı altında eritmek, bu ayrımı yok eder. Bu da düşük değerli içerik üretir. Biz resmi listeyi kaynak gösterip oyuncuya eleme çerçevesi bırakıyoruz.</p>
<p>Çıkış günü kayması, bölgesel mağaza farkı ve puanlama kilidi de sık görülür. Listenin pazartesi yayımlanmış olması, cuma gecesi her başlığın hazır olacağı anlamına gelmez. Şüphede resmi mağaza sayfasındaki tarih geçerlidir.</p>
<p class="acartechs-source-note">Kaynak: <a href="https://news.xbox.com/" target="_blank" rel="nofollow noopener">Xbox Wire haftalık çıkış duyuruları</a></p>
""",
    },
    "xbox-insiders-icin-gamertag-oyun-merkezi-ve-istek-listesi-guncellemeleri-geldi": {
        "title": "Xbox Insider güncellemesi: test özelliğini ne zaman ciddiye almalı?",
        "description": "Xbox, Insider programında gamertag, Game Hubs ve istek listesi denemeleri açtı. AcarTechs, henüz herkese gelmeyen özellikleri nasıl okumak gerektiğini yazıyor.",
        "dek": "Insider duyurusu ürün vaadi değildir; halka açık sürüme geçmeden satın alma kararına temel olmaz.",
        "body": f"""
<p>Xbox Wire, Insider kullanıcıları için gamertag deneyimi, Game Hubs ve istek listesi tarafında yeni arayüz denemeleri açıldığını duyurdu. Bu cümle sıkça “Xbox menüsü yenilendi” diye büyütülür. Gerçek durum daha dardır: özellik, test halkasına giren hesaplarda ve belirli cihazlarda görünür.</p>
<p>Insider programının işi, kırık köşeleri oyuncu trafiğine çıkmadan görmektir. Gamertag ve istek listesi gibi sık kullanılan yüzeyler değişince yanlış tıklama, kaybolan filtre ve alışkanlık bozulması riski artar. Bu yüzden Microsoft’un önce dar grupta denemesi doğaldır.</p>
<h2>Oyuncu ne yapmalı?</h2>
<p>Insider değilseniz bu haberi “menüm yarın değişecek” diye okumayın. Insider iseniz yedek bir hesap veya en azından istek listenizin ekran görüntüsü faydalıdır. Test sürümünde kaybolan bir etiket, henüz resmi hata kabul edilmeyebilir.</p>
{ARTICLE_AD}
<h2>Neden yine de takip ediyoruz?</h2>
<p>Gamertag ve oyun merkezi, Xbox’ın kimlik ve keşif katmanıdır. Buradaki sadeleşme, mağazada oyunu bulmayı ve arkadaş görünürlüğünü etkiler. Yani haberin değeri, bugünkü ekran görüntüsü değil, Microsoft’un hangi sorunu çözmeye çalıştığıdır: keşif dağınıklığı ve profil karmaşası.</p>
<p>AcarTechs, test duyurularını ürün incelemesi gibi yazmaz. “Geldi” demek yerine “kimde, hangi halkada, neyi değiştirmeyi deniyor” diye bakarız. Satın alma, abonelik iptali veya konsol yenileme kararı, Insider notuna dayandırılmamalıdır.</p>
<p class="acartechs-source-note">Kaynak: <a href="https://news.xbox.com/" target="_blank" rel="nofollow noopener">Xbox Wire Insider duyuruları</a></p>
""",
    },
    "xbox-22-26-haziran-haftasinda-cikacak-yeni-oyunlari-listeledi": {
        "title": "Haziran sonu Xbox takvimi: kısa pencere, seçici indirme",
        "description": "22-26 Haziran Xbox çıkış listesini AcarTechs, resmi satırları tekrar etmek yerine oyuncu takvimi olarak yorumluyor.",
        "dek": "Haftanın bütün oyunlarını indirmek yerine cihaz ve süreye göre iki başlık seçmek daha işe yarar.",
        "body": f"""
<p>Xbox’ın 22–26 Haziran haftası için paylaştığı resmi çıkış listesi, konsol ve PC tarafına dağılan başlıkları tek sayfada toplar. Bu tür listelerin okur için faydası, “ne çıktı” ezberi değil, o beş güne sığdırılabilecek gerçekçi bir plan çıkarmaktır.</p>
<p>Hafta içi çalışan oyuncu için cuma-pazar penceresi asıl savaş alanıdır. Listenin salı ve çarşamba satırları çoğu zaman indirme kuyruğuna kalır. Bu yüzden AcarTechs, haftalık listelerde ilk iş olarak “bu hafta sonuna hangi iki oyun sığar?” sorusunu sorar.</p>
<h2>Platform satırını atlamayın</h2>
<p>Aynı oyun Xbox One, Series ve PC’de farklı gün veya farklı sürümle gelebilir. Listede adın görünmesi, sizin cihazınızda 4K ve 60 kare alacağınız anlamına gelmez. Performans modu, geriye dönük uyumluluk ve depolama notu mağaza sayfasındadır; haftalık özet tablosunda değil.</p>
{ARTICLE_AD}
<h2>Abonelik mi, tam fiyat mı?</h2>
<p>Haziran sonu listelerinde Game Pass işareti olan başlık, deneme maliyetini sıfırlar. İşareti olmayan çıkış ise bütçe kararıdır. İkisini aynı heyecanla yazmak, okuru yanıltır. Biz kaynak olarak resmi listeyi bırakır, yorumu erişim modeline kaydırırız.</p>
<p>Kısa vadede bitmeyecek açık dünya bir yapımı, aynı hafta çıkan kısa indie ile kıyaslamak da yanıltıcıdır. Takvim haberi, tür ve seans süresi yazılmadan envanter değeri üretmez.</p>
<p class="acartechs-source-note">Kaynak: <a href="https://news.xbox.com/" target="_blank" rel="nofollow noopener">Xbox Wire haftalık oyun listeleri</a></p>
""",
    },
    "xbox-games-showcase-2026-oyun-dunyasinda-yeni-duyurularla-tamamlandi": {
        "title": "Xbox Games Showcase 2026: duyurudan sonra ne takip edilmeli?",
        "description": "Xbox Games Showcase 2026’yı AcarTechs fragman ezberi olarak değil, platform, tarih ve abonelik açısından okuyor.",
        "dek": "Sahne gösterisi heyecan üretir; satın alma kararı çıkış penceresi, cihaz ve Game Pass notu netleşince verilir.",
        "body": f"""
<p>Xbox Games Showcase 2026, yeni oyunlar, donanım vurguları ve eski serilerin dönüşüyle yılın en yoğun duyuru pencerelerinden biri oldu. Bu tür yayınların ardından internet, fragman kareleriyle dolar. AcarTechs’in işi kareleri tekrar etmek değil, hangi duyurunun oyuncu kararını gerçekten değiştirdiğini ayırmaktır.</p>
<p>Showcase’te üç katman vardır. Birinci katman, tarihi netleşen oyunlardır. İkinci katman, yalnızca “geliştiriliyor” denilen işlerdir. Üçüncü katman, donanım ve abonelik vaatleridir. Birinci katman takvime yazılır. İkinci katman izlenir, bütçeye yazılmaz. Üçüncü katman ise sahip olduğunuz cihaz ve Game Pass planınızla çarpıştırılır.</p>
<h2>Fragman ile sürüm aynı şey değildir</h2>
<p>Sahne gösterisinde 30 saniyelik bir kesit, son ürünün tempo, zorluk ve teknik durumunu kanıtlamaz. Özellikle yeniden yapım ve serinin geri dönüşü haberlerinde “aynı his” vaadi, oynanış videosu ve inceleme yasağı kalkınca test edilir. Bu yüzden Showcase gecesi verilen puanlar, yayın politikamıza göre haber değildir.</p>
{ARTICLE_AD}
<h2>Oyuncu için kalıcı başlıklar</h2>
<p>Takip listesine yalnızca çıkış yılı net, platformu sizin cihazınız olan ve mümkünse deneme yolu (Game Pass, demo, erken erişim) görünen işleri yazın. Geri kalanı “duyuru envanteri”dir. Duyuru envanteri tıklama üretir ama okura hizmet etmez.</p>
<p>Donanım sızıntısı gibi duran cümleleri de resmi slayt olmadan kesinleşmiş kabul etmiyoruz. Showcase sonrası günlerde stüdyo blogları ve Xbox Wire düzeltmeleri asıl kaynaktır.</p>
<p class="acartechs-source-note">Kaynak: <a href="https://news.xbox.com/" target="_blank" rel="nofollow noopener">Xbox Wire / Xbox Games Showcase 2026</a></p>
""",
    },
    "halo-campaign-evolved-temmuzda-oyuncularla-bulusmaya-hazirlaniyor": {
        "title": "Halo Campaign Evolved: tarih, platform ve kim için mantıklı?",
        "description": "Halo Campaign Evolved’ın temmuz çıkışını AcarTechs, Xbox Wire duyurusunu kopyalamadan platform ve erken erişim açısından inceliyor.",
        "dek": "28 Temmuz küresel çıkış, 23 Temmuz Premium erken erişim; asıl kırılım PlayStation 5 ve çapraz ilerleme.",
        "body": f"""
<p>Halo Campaign Evolved için paylaşılan resmi takvim, oyunun 28 Temmuz 2026’da küresel çıkış yapacağını, Premium Edition sahiplerinin ise 23 Temmuz’da girebileceğini söylüyor. Platform listesi Xbox Series X|S, PC, bulut, Steam ve PlayStation 5’i kapsıyor. Cross-play ve cross-progression notu, serinin uzun süredir kapalı duran kapısını fiilen açıyor.</p>
<p>Bu haberin ağırlığı “Halo dönüyor” sloganı değil, markanın tek ekosistem iddiasını bırakmasıdır. Yıllardır Xbox kimliğiyle büyümüş bir kampanyanın PlayStation 5’te ve Steam’de ilerlemesini taşıyabilmesi, kimlerin oyunu deneyeceğini değiştirir.</p>
<h2>Erken erişim kime yarar?</h2>
<p>Beş günlük Premium farkı, hafta sonunu kampanyaya ayırabilecek oyuncu için anlamlıdır. Günlük 1 saatlik seansı olan biri için 23–28 Temmuz penceresi abartılmamalı. Sürüm farkını yalnızca “daha önce girmek” diye almak, içerik listesi net değilse zayıf bir gerekçedir. Satın almadan önce Premium’un ne verdiğini resmi sayfadan kontrol edin.</p>
{ARTICLE_AD}
<h2>Hangi oyuncu için öncelik?</h2>
<p>Seriyi hiç oynamamış biri için Campaign Evolved, modern kontroller ve güncel çözünürlükle giriş kapısı olabilir. Kampanyayı defalarca bitirmiş oyuncu ise görsel yenileme, performans ve çapraz ilerleme notuna bakmalıdır. Rekabetçi çok oyunculu bekleyenler, bu başlığın kampanya odaklı çerçevesini atlamamalı.</p>
<p>Teknik beklenti de sakin tutulmalı. Çok platformlu çıkışlarda ilk hafta yama döngüsü olağandır. Day-one indirmeyi “bitmiş ürün” sanmak yerine, ilk 48 saatte yama notlarını izlemek daha doğru bir alışkanlıktır.</p>
<p class="acartechs-source-note">Kaynak: <a href="https://news.xbox.com/en-us/2026/06/10/halo-campaign-evolved-hands-on-demo-2/" target="_blank" rel="nofollow noopener">Xbox Wire, Halo Campaign Evolved</a></p>
""",
    },
    "playstation-plus-haziran-katalogunda-final-fantasy-xvi-one-cikti": {
        "title": "PlayStation Plus haziran kataloğu: Extra/Premium kime yeter?",
        "description": "Final Fantasy XVI, Sonic X Shadow Generations ve Kingdom Come: Deliverance’ın Plus kataloğuna girişini AcarTechs abonelik kararı olarak yorumluyor.",
        "dek": "Büyük isim görmek yeterli değil; katman, depolama ve bitirme süresi katalog değerini belirler.",
        "body": f"""
<p>PlayStation Blog’un haziran Game Catalog paylaşımında Final Fantasy XVI, Sonic X Shadow Generations, Kingdom Come: Deliverance ve Life is Strange: Double Exposure öne çıktı. Bu isimler tek tek güçlüdür. Yine de Plus haberini “bütün katalog bende olmalı” diye okumak, aboneliğin katmanlı yapısını yok sayar.</p>
<p>Essential, Extra ve Premium aynı şey değildir. Katalog oyunu Extra/Premium’da görünür, Essential abonesi aynı başlığa erişemez. AcarTechs’in ilk uyarısı budur: başlıktaki oyun adını kendi fatura katmanınızla çarpın.</p>
<h2>Üç farklı seans, üç farklı oyuncu</h2>
<p>Final Fantasy XVI uzun, sinematik ve tek oyunculu bir yatırım ister. Sonic X Shadow Generations daha kısa, skor ve tempo odaklıdır. Kingdom Come yavaş, simülasyon ağırlıklı bir Orta Çağ temposu sunar. Life is Strange ise bölüm bölüm ilerleyen anlatıdır. Aynı ayda durmaları, aynı hafta hepsinin bitirileceği anlamına gelmez.</p>
{ARTICLE_AD}
<h2>Katalog değeri nasıl ölçülür?</h2>
<p>Abonelik, tam fiyatlı raflara göre ucuz görünür; fakat kullanılmayan 100 GB’lık indirme ucuz değildir. Pratik yöntem: bu ay gerçekten 15 saatten fazla ayırabileceğiniz bir kampanya seçin, ikinci oyunu kısa seans için tutun, üçüncüyü istek listesine bırakın. “Hepsini indir, sonra bakarım” yaklaşımı hem depolamayı hem de katalog algısını bozar.</p>
<p>Çıkış tarihi geçmiş AAA oyunların kataloga girmesi, Plus’ın yeni oyuncu çekme yoludur. Seriyi hiç oynamamış biri için FFXVI güçlü bir deneme kapısıdır. Oyunu zaten bitirmiş oyuncu için haberin değeri düşüktür; o okura Sonic veya Kingdom Come daha çok hizmet eder. Bu ayrımı yazmayan haber, kopya duyuru olarak kalır.</p>
<p class="acartechs-source-note">Kaynak: <a href="https://blog.playstation.com/2026/06/10/playstation-plus-game-catalog-for-june-final-fantasy-xvi-sonic-x-shadow-generations-kingdom-come-deliverance-and-more/" target="_blank" rel="nofollow noopener">PlayStation Blog, June Game Catalog</a></p>
""",
    },
    "nintendo-direct-switch-2-icin-yeni-oyunlari-ve-klasik-donusleri-duyurdu": {
        "title": "Nintendo Direct sonrası alışveriş listesi nasıl sadeleştirilir?",
        "description": "Nintendo Direct’in Switch 2 ve klasik dönüş duyurularını AcarTechs, fragman yığını yerine öncelik listesi olarak ele alıyor.",
        "dek": "Direct gecesi her duyuru eşit değildir; cihaz, tarih ve ilk parti destek ayrılmadan bütçe yazılmaz.",
        "body": f"""
<p>Nintendo Direct yayınları, kısa sürede onlarca fragman, tarih ve klasik seri dönüşü yığar. Bu tempo, “hepsini almak lazım” hissi üretir. AcarTechs Direct’i bir alışveriş kataloğu gibi değil, üç sütunlu bir eleme tahtası gibi okur: bu yıl çıkanlar, gelecek yıla kalanlar, yalnızca fikir aşamasındakiler.</p>
<p>Switch 2’ye bağlı duyurularda ikinci bir süzgeç daha vardır. Oyun yeni donanıma özel mi, yoksa mevcut kütüphaneyle geriye dönük mü çalışacak? Bu ayrım netleşmeden ikinci cihaz kararı vermek, duyuru heyecanını donanım bütçesine çevirir.</p>
<h2>Klasik dönüşleri ayrı okuyun</h2>
<p>Eski serilerin geri gelmesi duygusal tepki üretir. Teknik olarak ise remake, remaster ve yeniden yayın farklı ürünlerdir. Fiyat, çözünürlük, çevrimiçi özellik ve kayıt aktarımı net değilse “klasik dönüyor” cümlesi yeterli değildir.</p>
{ARTICLE_AD}
<h2>Direct sonrası 48 saat kuralı</h2>
<p>Yayın bittikten sonra stüdyo siteleri ve Nintendo’nun kendi sayfası düzeltme geçer. İlk gece yazılan “kesin tarih” bazen pencereye döner. Bu yüzden Direct gecesi sipariş vermek yerine, 48 saat bekleyip resmi ürün sayfasındaki maddeleri okumak daha az pişmanlık üretir.</p>
<p>AcarTechs, Direct haberini fragman özeti olarak bırakmaz. Okura üç soru bırakır: bu yıl oynayacak mıyım, cihazım destekliyor mu, deneme yolu var mı? Üçüne de “emin değilim” ise başlık istek listesindedir, sepetinde değil.</p>
""",
    },
    "oyun-abonelik-servislerine-yeni-yapimlar-eklendi": {
        "title": "Game Pass mi PlayStation Plus mı? 2026 abonelik rehberi",
        "description": "Xbox Game Pass ve PlayStation Plus’ı AcarTechs, katalog duyurusu kopyalamadan cihaz, bütçe ve oyun süresi üzerinden karşılaştırıyor.",
        "dek": "Abonelik seçimi marka sadakati değil; cihaz, seans süresi ve katalog katmanı meselesidir.",
        "body": f"""
<p>Oyun abonelikleri, 2026’da “aylık birkaç yeni oyun” olmaktan çıktı. Game Pass ve PlayStation Plus, deneme maliyeti, dijital kütüphane ve hatta bulut oynatma kararını aynı faturada topluyor. Bu rehber, katalog duyurularını tekrar etmez. Hangi oyuncunun hangi servise para basması gerektiğini sadeleştirir.</p>
<p>İlk kırılım cihazdır. Evinizde Series ve PC varsa Game Pass’in çok cihazlı değeri artar. Yalnızca DualSense ve bir PlayStation varsa Plus kataloğu daha doğrudur. İki konsolu da olan evde çift abonelik, ancak haftalık oyun süresi gerçekten iki ekosistemi dolduruyorsa mantıklıdır.</p>
<h2>Katman tuzakları</h2>
<p>Plus Essential ile Extra/Premium aynı şey değildir. Game Pass Core ile Ultimate da değildir. Reklamlarda gördüğünüz AAA isim çoğu zaman üst katmandadır. Fatura kaydınızı kontrol etmeden “katalogda var” demek, okuru boş indirme kuyruğuna sokar.</p>
{ARTICLE_AD}
<h2>Ne zaman iptal, ne zaman tut?</h2>
<p>Aboneliği tutma gerekçesi, “bu ay üç büyük isim geldi” olmamalı. Gerekçe, sizin 30 günde bitirebileceğiniz işlerin toplamının aylık ücreti aşmasıdır. Bitiremeyeceğiniz beş oyunu indirmek, değer üretmez. Tersine, her ay 20 saat oynayan biri için tek bir uzun kampanya bile faturayı amorti edebilir.</p>
<p>İkinci el fiziksel koleksiyonu olan oyuncu, aboneliği keşif katmanı olarak kullanabilir. Dijital-only oyuncu için abonelik, mağaza indiriminden önce gelen varsayılan yoldur. Bulut oynamayı düşünenler ise internet yükünü ve giriş gecikmesini kendi evlerinde test etmeden Ultimate/Premium’a “çözüm” dememelidir.</p>
<h2>AcarTechs önerisi</h2>
<p>Tek konsol, haftada 5 saatten az: üst katmanı sürekli açık tutmayın, yoğun ayda açıp bitirin. Haftada 8 saat ve üzeri, iki cihaz: tek bir üst katman seçin, ikincisini yalnızca özel bir çıkış ayında açın. Çocuk profili ve aile paylaşımı varsa, resmi aile paylaşım kurallarını mağaza metninden okuyun; forum tarifine güvenmeyin.</p>
""",
    },
    "bagimsiz-oyunlar-yaratici-fikirleriyle-one-cikiyor": {
        "title": "Bağımsız oyun seçme rehberi: kısa seans, niş tür, düşük pişmanlık",
        "description": "AcarTechs’in bağımsız oyun rehberi: demo, süre, tür ve fiyat üzerinden düşük pişmanlıklı keşif.",
        "dek": "Indie vitrinleri ilham verir; iyi seçim, süreyi ve demoyu okumaktan geçer.",
        "body": f"""
<p>Bağımsız oyunlar, büyük stüdyoların risk almadığı türleri ve anlatıları denemek için hâlâ en verimli alandır. Sorun, vitrinin kalabalık olmasıdır. Her hafta “dikkat çeken indie” başlığı yayımlamak, keşfi kolaylaştırmaz; gürültüyü artırır. Bu rehber, AcarTechs’in kendi eleme yöntemini açıklar.</p>
<p>İlk bakılan şey oyun süresidir. 2 saatlik bir deney ile 40 saatlik bir simülasyon aynı bütçe kalemi değildir. İkincisi demo veya oynanış videosunun tempo dürüstlüğüdür. Müzik ve renk güzel olsa da 20 dakikalık bir kesit, geç oyun tekrarına dair bir şey söylemeyebilir.</p>
<h2>Niş türde ne sorulur?</h2>
<p>Bulmaca, anlatı, korku ve kısa arcade, indie’nin en sık parladığı yerlerdir. Bunlarda pişmanlık genellikle düşüktür. Erken erişimli hayatta kalma ve canlı hizmet taklidi yapan küçük ekip işlerinde ise risk yükselir. “Erken erişimde al, destekle” cümlesi ancak yama ritmi görünen stüdyolar için anlamlıdır.</p>
{ARTICLE_AD}
<h2>Fiyat ve istek listesi</h2>
<p>Bağımsız oyunda 15 dolar, 70 dolarlık AAA’dan daha pahalı hissedilebilir; çünkü vaat daha dardır. İstek listesi indirimini beklemek, özellikle demo beğendiğiniz işlerde rasyoneldir. Beğenmediğiniz demoyu “ileride açılır” diye almak, düşük değerli kütüphane üretir.</p>
<p>Platform seçkileri (Indie Selects, mağaza vitrinleri, Plus/Game Pass indie rafları) keşif için iyidir. Satın alma gerekçesi olarak zayıftır. Seçkiye girmek kalite sertifikası değildir; görünürlük biletidir.</p>
<h2>Mini oyunlarla ilişki</h2>
<p>AcarTechs Arcade’deki tarayıcı oyunları, bağımsız üretim fikrini küçük ölçekte gösterir: kuralı net, seansı kısa, pişmanlığı düşük. Uzun indie kampanyasına girmeden önce kendi zevkinizin kısa seans mı hikâye mi istediğini anlamanın pratik yolu budur.</p>
""",
    },
    "oyuncu-ekipmanlarinda-fiyat-performans-secimleri": {
        "title": "Oyuncu ekipmanında fiyat/performans: mouse, kulaklık, klavye",
        "description": "Oyuncu mouse, kulaklık ve klavye alırken AcarTechs’in 2026 fiyat/performans rehberi. RGB’den önce bakılacak maddeler.",
        "dek": "İyi ekipman, vitrin ışığı değil; tutuş, rahatlık ve değiştirilebilir parça meselesidir.",
        "body": f"""
<p>Oyuncu ekipmanı pazarında aynı fiyata duran ürünler, vitrinde birbirine benzer. Masada ayrışırlar. AcarTechs bu rehberde mouse, kulaklık ve klavyeyi “pro” etiketine bakmadan; tutuş, rahatlık, yedek parça ve gürültü üzerinden okur.</p>
<p>Mouse’ta ilk soru tutuştur. Avuç içi, pençe ve parmak ucu aynı kabuğu sevmez. Gramaj tek başına karar vermez; 50 gramlık hafif mouse, büyük elde kayabilir. Sensör pazarlama sayısı, 400–1600 DPI aralığında düzgün iz süren bir üründen daha az işe yarar.</p>
<h2>Kulaklıkta konfor, mikrofon ve kaçak ses</h2>
<p>Üç saatlik bir oturumda kafa bandı baskısı, sürücü çapından önce gelir. Mikrofon, yalnızca yayıncı için değil, parti sohbeti için de önemlidir. Kaçak ses (sound leak) evde başkası varken kulak üstü modellerde sık şikâyettir. “7.1 sanal” yazısı, iyi bir stereo sahne ve rahat yastıktan daha zayıf bir gerekçedir.</p>
{ARTICLE_AD}
<h2>Klavye: switch hikâyesi ve servis</h2>
<p>Mekanik klavyede switch tipi yazı ve gece kullanımı belirler. Tıklamalı switch, paylaşılmış odada komşu düşmanı olabilir. Sökülebilir switch ve tuş başlığı, iki yıl sonra ürünü çöpe atmamak demektir. RGB katmanı, bu servis kolaylığından sonra gelir.</p>
<p>Bütçe dilimi olarak 2026’da “her şeyi bir kitte al” paketleri çekici durur. Parça parça almak, zayıf halkayı (genelde kulaklık yastığı veya mouse kaydırıcıları) sonra yükseltmeye izin verir. AcarTechs, ilk alımda mouse ve kulaklığa öncelik vermeyi, klavyeyi masadaki mevcut düzen yeterliyse ertelemeyi önerir.</p>
<p>Garanti, yerinde servis ve yedek ayak/yastık bulunabilirliği, vitrin puanından daha kalıcı bir fiyat/performans göstergesidir.</p>
""",
    },
    "mobil-oyunlarda-grafik-kalitesi-hizla-artiyor": {
        "title": "Mobil oyunda grafik ve pil: ayarları nasıl dengelemeli?",
        "description": "Mobil oyunlarda yükselen grafik vaadini AcarTechs, pil, ısınma ve net animasyon açısından pratik rehbere çeviriyor.",
        "dek": "Daha parlak vitrin karesi, daha iyi oynanış demek değildir; ısınma ve kare süresi asıl ölçü.",
        "body": f"""
<p>Mobil oyun vitrinleri 2026’da konsol fragmanına yaklaşan kareler gösteriyor. Cihaz cebinizdeyken aynı kare, ısınma, pil ve dokunmatik kontrol ile çarpışır. Bu rehber, “grafikler çok gelişti” cümlesini tekrar etmez. Telefonda gerçekten nereye bakmanız gerektiğini söyler.</p>
<p>İlk ölçü kare süresidir. 60 fps yazısı, 20 saniyede bir yaşanan takılmayı gizleyebilir. İkinci ölçü çözünürlük ölçeğidir. Birçok oyun varsayılanı “yüksek”e çekerek vitrin şovunu telefonun ısısına yıkar. Üçüncü ölçü parlaklıktır: HDR benzeri filtreler dışarıda hoş, içeride pil düşmanıdır.</p>
<h2>Hangi ayar düşürülür?</h2>
<p>Gölge ve kalabalık ortam ayrıntısı, pil ve ısınmada en pahalı kalemlerdir. Karakter netliği ve arayüz okunabilirliği ise oynanışı taşır. AcarTechs’in pratik tarifi: gölgeyi orta/düşük, doku netliğini orta-yüksek, kare hedefini sabit tutun. Değişken kare, parmak zamanlamasını bozar.</p>
{ARTICLE_AD}
<h2>Kontrol ve seans</h2>
<p>Grafik yükseldikçe ekranda bilgi kalabalığı artar. Mobilde bu, başparmağın tuşu kapatması demektir. İyi mobil port, tuş ölçeği ve kör nokta ayarı sunar. Sunmuyorsa, vitrin karesi ne kadar güzel olursa olsun uzun seans cezası vardır.</p>
<p>İndirme boyutu da grafik yarışının gizli faturasıdır. 8–12 GB güncellemeler, şehir içi veri ve depolama gerçeğiyle çarpışır. Wi-Fi dışında “otomatik yüksek kalite paketi”ni açık bırakmayın.</p>
<p>Sonuç: mobil oyunda kalite, fragman kesiti değil, 25 dakikalık otobüs seansında telefonun elinizde kalmasıdır.</p>
""",
    },
    "oyuncu-bilgisayarlarinda-ekran-karti-secimi-yeniden-gundemde": {
        "title": "Oyuncu PC’sinde ekran kartı seçimi: 1080p, 1440p, 4K gerçeği",
        "description": "Ekran kartı alırken AcarTechs’in 2026 rehberi: çözünürlük, VRAM, güç kaynağı ve ikinci el tuzağı.",
        "dek": "Kartın vitrin modeli değil, monitörünüzün hertz’i ve kasanın güç bütçesi karar verir.",
        "body": f"""
<p>Ekran kartı seçimi, oyuncu PC’sinde hâlâ en pahalı ve en çok yanlış yapılan kalemdir. Vitrin, “en yeni” etiketini öne çıkarır. Masada ise monitör çözünürlüğü, kasa hava akışı ve güç kaynağı konuşur. Bu rehber, duyuru metinlerini değil, 2026’da karar verirken işe yarayan soruları sıralar.</p>
<p>1080p 144 Hz oynayan biri ile 1440p 165 Hz oynayan biri aynı karta ihtiyaç duymaz. 4K hedefi, hem kartı hem işlemci darboğazını hem de 32 GB bellek tartışmasını açar. Önce monitör, sonra kart. Tersi, paranın bir kısmını görünmeyen karelere gömer.</p>
<h2>VRAM ve oyun ayarı</h2>
<p>Yüksek doku paketleri VRAM’i hızla doldurur. 8 GB, 1080p’de hâlâ birçok başlıkta yeter; 1440p ultra ve ışın izleme ile sınır görünür. 4K’da 8 GB’ı “gelecek üç yıl” diye almak, ayar düşürme döngüsüne razı olmaktır. AcarTechs, kartı üç yıl tutacaksanız çözünürlüğünüze bir kademe VRAM payı bırakmayı önerir.</p>
{ARTICLE_AD}
<h2>Güç, boy ve ikinci el</h2>
<p>Yeni kartın kutu değeri, 850 W etiketli ama eski bir güç kaynağında anlamını yitirir. Kasa boyu da öyle: üç fanlı kart, dar kasada ısınır ve gürültü üretir. İkinci elde madencilik hikâyesi, fatura ve garanti devri belirsizse ucuzluk değildir.</p>
<p>Ray tracing ve üretken kare (frame generation) pazarlama cümlelerini ayrı okuyun. Üretken kare, akışkanlık verir ama giriş gecikmesini artırabilir. Rekabetçi oynayan biri için ham kare süresi, şık bir 4K vitrin karesinden değerlidir.</p>
<p>Karar cümlesi sade olmalıdır: monitörüm X, hedefim Y fps, kasam Z watt. Bu üçü yazılmadan model adı ezberlemek, düşük değerli tavsiyedir.</p>
""",
    },
    "konsol-oyunculari-icin-sistem-guncellemesi-yayinlandi": {
        "title": "Konsol güncellemesi gelince kontrol listesi",
        "description": "Xbox ve PlayStation sistem güncellemelerini AcarTechs, changelog kopyası değil, oyuncu kontrol listesi olarak yazıyor.",
        "dek": "Güncelleme sonrası siyah ekran paniği çoğu zaman depolama, hesap ve ağ sırasıyla çözülür.",
        "body": f"""
<p>Konsol sistem güncellemeleri, arayüz cümleleriyle duyurulur: sosyal özellik, mağaza hızı, enerji seçenekleri. Oyuncu tarafında asıl risk, güncellemenin ardından oyunun açılmaması, kayıtların görünmemesi veya arkadaş listesinin boşalmasıdır. Bu yazı, changelog’u tekrar etmek yerine güncelleme gecesi ne yapılacağını anlatır.</p>
<p>Güncellemeden önce iki şey yeterlidir: depolamada birkaç GB boşluk ve önemli kayıtlarda bulut senkronunun yeşil olması. “Hemen kur” diye gece yarısı basmak, özellikle yavaş bağlantıda yarım kalan kurulum üretir.</p>
<h2>Kurulum sonrası sıra</h2>
<p>Önce konsolu yeniden başlatın, sonra ağı, sonra mağaza oturumunu kontrol edin. Oyun içi hata çoğu zaman sistemden değil, oyunun kendi küçük yamasından gelir. Sistem güncellemesiyle oyun yamasını aynı anda yüklemek, hangi katmanın kırıldığını gizler.</p>
{ARTICLE_AD}
<h2>Sosyal özellikler ve gizlilik</h2>
<p>Yeni sohbet, etkinlik veya paylaşım düğmeleri varsayılanı açık gelebilir. Çocuk profili olan evlerde güncelleme sonrası gizlilik ekranı tekrar bakılmalıdır. “Sosyal özellik gelişti” cümlesi, varsayılanın sizin ev kurallarınıza uyduğu anlamına gelmez.</p>
<p>AcarTechs, sistem güncellemelerini ürün lansmanı gibi şişirmez. Bunlar bakım işidir. Haber değeri, kırılan bir özellik veya gerçekten işe yarayan bir enerji/depolama kazanımı varsa vardır. Geri kalanı kontrol listesidir.</p>
""",
    },
    "haftanin-oyun-firsatlari-ve-ucretsiz-yapimlari-aciklandi": {
        "title": "Ücretsiz ve indirimli oyunları güvenli takip etme rehberi",
        "description": "Haftalık ücretsiz oyun ve indirim listelerini AcarTechs, tuzak bağlantı ve depolama gerçeğiyle birlikte anlatıyor.",
        "dek": "Ücretsiz yazısı, her zaman bedava ve güvenli demek değildir; mağaza ve süre notu şarttır.",
        "body": f"""
<p>Her hafta bir yerde “ücretsiz oyunlar açıklandı” başlığı döner. Kimi resmi mağaza kampanyasıdır, kimi süreli Plus/Game Pass hakkı, kimi de şüpheli indirme sayfasıdır. AcarTechs bu rehberde fırsat listesini kopyalamaz. Okurun güvenli ve işine yarayan fırsatı ayıklamasını anlatır.</p>
<p>Birinci kural: bağlantı, Xbox, PlayStation, Nintendo, Steam veya Epic’in kendi alan adında mı? Değilse başlık ne kadar çekici olursa olsun kaynak değildir. İkinci kural: ücretsiz, “süreli olarak kütüphaneye ekle” mi, yoksa “bu hafta sonuna kadar oyna, sonra kaybolur” mu? İkisi farklı üründür.</p>
<h2>Depolama ve zaman</h2>
<p>Ücretsiz diye 80 GB indirmek, gerçek bir fırsat olmayabilir. Bitiremeyeceğiniz oyunu kuyruğa almak, asıl oynamak istediğiniz işi geciktirir. Fırsat takipçisinin disiplini, ayda iki başlık kuralıdır.</p>
{ARTICLE_AD}
<h2>Hesap ve bölge</h2>
<p>Kampanyalar bölge, ödeme yöntemi ve yeni hesap kısıtı taşıyabilir. “Herkese ücretsiz” cümlesi, Türkiye mağazasında aynı anda geçerli olmayabilir. Resmi sayfadaki ülke notu, sosyal medya görselinden önce gelir.</p>
<p>Aile hesaplarında çocuk profiline yanlışlıkla eklenen satın alma yöntemi, ücretsiz denilen paketi ücretli yapabilir. Fırsat haberini çocuk hesabında denemeden önce ebeveyn kilitlerini kontrol edin.</p>
<p>Sonuç: iyi fırsat, resmi mağazada, süresi net, sizin cihazınızda ve bu ay gerçekten oynayacağınız oyundur. Geri kalanı gürültüdür.</p>
""",
    },
    "e-spor-turnuvalarinda-final-haftasi-heyecani-basladi": {
        "title": "E-spor final haftasını izlerken bilinmesi gerekenler",
        "description": "E-spor finallerini AcarTechs, skor ezberi değil; format, yayın ve bahis tuzakları açısından anlatıyor.",
        "dek": "Final haftası içerik üretir; izleyici için format, VOD ve resmi yayın adresi yeterlidir.",
        "body": f"""
<p>E-spor final haftaları, skor, kadro ve “tarihi maç” dilinin en çok şiştiği dönemdir. AcarTechs, turnuva haberini iddia diliyle yazmaz. İzleyicinin kaybolmaması için üç şey yeterlidir: format (bo3/bo5, üst-alt tablo), resmi yayın adresi ve maçların VOD olarak kalıp kalmadığı.</p>
<p>Formatı bilmeden skoru okumak yanıltır. Üst tablodan gelen takımın bir maç hakkı daha olması, “elendi” sandığınız geceyi tersine çevirebilir. Bu yüzden başlıkta skor varsa bile yazının içinde format cümlesi olmalıdır.</p>
<h2>Yayın, reklam ve yanıltıcı katman</h2>
<p>Final haftasında sahte yayın linkleri ve bahis pop-up’ları artar. Resmi lig kanalı, takımın kendi kanalından önce gelir. Tarayıcı oyunu veya haber sayfasındaki reklamın, maç skorunu kapatan katman gibi durmaması da yayıncı politikamızın parçasıdır.</p>
{ARTICLE_AD}
<h2>Oyuncu değil izleyiciyseniz</h2>
<p>Kadroları ezberlemek zorunda değilsiniz. Takımın oyun kimliği (erken baskı, geç oyun, harita havuzu) birkaç cümleyle yeter. “Efsane kadro” dili, yeni izleyiciyi dışarıda bırakır. AcarTechs, e-spor yazısını meraklı ama günlük izleyici için yazar.</p>
<p>Bahis, kupon ve “kesin oran” içerikleri bu sitede yer almaz. Final haftası haberi, spor anlatısıdır; kumar daveti değildir.</p>
""",
    },
    "hayatta-kalma-oyunlarinda-yeni-sezon-icerikleri": {
        "title": "Hayatta kalma oyunlarında sezon geçişi: neyi sıfırlar, neyi tutar?",
        "description": "Hayatta kalma ve canlı hizmet oyunlarında sezon içeriğini AcarTechs, FOMO dili olmadan açıklar.",
        "dek": "Yeni sezon, her şeyi silmez; hangisinin sıfırlandığını okumak, yayından daha önemlidir.",
        "body": f"""
<p>Hayatta kalma ve canlı hizmet oyunları, birkaç ayda bir “yeni sezon” başlığıyla döner. Vitrin, yeni harita, yeni zanaat zinciri ve savaş bileti gösterir. Oyuncunun asıl sorusu daha sadedir: ilerlemenin kaçı sıfırlanacak, ev üssü duracak mı, arkadaş grubu aynı sunucuda kalacak mı?</p>
<p>Sezon geçişini FOMO ile okumak, yorgunluk üretir. AcarTechs, bu tür duyurularda üç madde arar: sıfırlanan ilerleme, kalıcı olan kozmetik/hesap, ve yeni oyuncunun bu sezon tek başına girebilme ihtimali. Üçüncü madde yoksa sezon, eski kadroya hizmet eder.</p>
<h2>Bitirme süresi dürüstlüğü</h2>
<p>Yeni zanaat ağacı, 40 saatlik bir ikinci iş ilanı olabilir. Haftada 5 saatlik oyuncu için “kaçırma” dili yanıltıcıdır. Sezonu, bitirebileceğiniz bir ana hat ve isteğe bağlı yan hat olarak okuyun.</p>
{ARTICLE_AD}
<h2>Arkadaş grubu ve sunucu</h2>
<p>Birçok hayatta kalma işi, sunucu silme veya harita yenileme getirir. Grup dağılırsa sezonun “yeni içerik” vaadi teknik olarak doğru, sosyal olarak ölüdür. Duyuruda sunucu politikası yoksa, atlamadan önce resmi yama notuna bakın.</p>
<p>Bu yazı tek bir oyunun changelog’u değildir. Sezon dilini her başlıkta aynı kalıpla yapıştırmak yerine, oyuncunun kendi süresine göre “gireyim / bu sezonu pas geçeyim” kararı vermesini hedefler.</p>
""",
    },
    "yeni-cikacak-aksiyon-oyunu-icin-ilk-oynanis-videosu-geldi": {
        "title": "Oynanış videosu nasıl okunur? Kameradan gerçeğe",
        "description": "İlk oynanış videolarını AcarTechs, fragman heyecanı yerine kamera hilesi, HUD ve tempo dürüstlüğüyle okur.",
        "dek": "Oynanış kesiği kanıt değil, ipucudur; HUD, kamera ve kesilmeyen 3 dakika arayın.",
        "body": f"""
<p>Yeni aksiyon oyunlarının ilk oynanış videoları, fragmandan daha değerli görünür. Bazen öyledir. Bazen yalnızca daha uzun bir reklamdır. AcarTechs, bu videoları haberleştirirken “görüntüler geldi” diye durmaz. Kameranın neyi gizlediğine bakar.</p>
<p>Kesilmeyen 2–3 dakikalık bir parça, 15 saniyelik montajdan daha çok şey söyler. HUD görünüyorsa can, mermi, beceri bekleme süresi ve harita okunabilirliği hakkında fikir çıkar. HUD yoksa video, sinema karesidir; oynanış kanıtı değildir.</p>
<h2>Kamera, hız ve düşman zekâsı</h2>
<p>Omuz arkası kamera titremesi, tempo varmış gibi hissettirir. Asıl soru, düşmanın sizi nasıl cezalandırdığıdır. Sadece oyuncunun sergilediği kombo, yapay zekânın zayıf olduğu bir demoyu gizleyebilir. Kalabalık sahnede çerçeve düşüşü var mı, yok mu; bunu 1080p’den 4K’ya geçerek değil, sabit karede izleyerek anlarsınız.</p>
{ARTICLE_AD}
<h2>Çıkış kararına etkisi</h2>
<p>Oynanış videosu, ön sipariş gerekçesi olmamalıdır. Gerekçe, tarih, platform, deneme (demo/Game Pass) ve inceleme yasağının kalkmasıdır. Video iyiyse istek listesine alın. Sepete koymak için sistem gereksinimi ve oynanışın sizin sevdiğiniz tempo olup olmadığı netleşmelidir.</p>
<p>AcarTechs, stüdyo videosunu kaynak olarak işaretler; kare kare yeniden anlatmaz. Okura bakacağı yerleri verir. Bu, kopya duyuru ile özgün rehber arasındaki farktır.</p>
""",
    },
}

KUNYE_HTML = """
<p>Bu sayfa, AcarTechs yayın kimliğini ve iletişim bilgilerini içerir. Google yayıncı hesabındaki bilgilerle uyumlu tutulur.</p>
<table>
<tbody>
<tr><td><strong>Yayın adı</strong></td><td>AcarTechs</td></tr>
<tr><td><strong>Web adresi</strong></td><td><a href="https://acartechs.com/">https://acartechs.com/</a></td></tr>
<tr><td><strong>Yayın türü</strong></td><td>Bağımsız Türkçe teknoloji, yazılım, yapay zekâ ve oyun yayıncılığı</td></tr>
<tr><td><strong>Yayın dili</strong></td><td>Türkçe</td></tr>
<tr><td><strong>Editoryal sorumluluk</strong></td><td>AcarTechs Editör</td></tr>
<tr><td><strong>E-posta</strong></td><td><a href="mailto:acarr.ffatih@gmail.com">acarr.ffatih@gmail.com</a></td></tr>
<tr><td><strong>Konum</strong></td><td>Türkiye</td></tr>
<tr><td><strong>Reklam envanteri</strong></td><td>Google AdSense. Yetkili satıcı kaydı <a href="https://acartechs.com/ads.txt">acartechs.com/ads.txt</a> dosyasında yayımlanır (pub-4367344438750629).</td></tr>
</tbody>
</table>
<h2>Düzeltme</h2>
<p>Yayımlanan bir içerikte hata görürseniz ilgili bağlantıyla birlikte e-posta gönderin. Haklı düzeltmeler metne işlenir.</p>
"""

YAYIN_HTML = """
<p>AcarTechs, resmi duyuruları olduğu gibi yapıştırmayan bir teknoloji yayıncısıdır. Amaç; kaynağı görülebilen, okura pratik fayda üreten özgün metin yayımlamaktır.</p>
<h2>1. Özgün değer</h2>
<ul>
<li>Başka sitelerin veya marka bloglarının metni izinsiz kopyalanmaz.</li>
<li>Kısa duyuru, yorumsuz derleme veya 100 kelimelik özet yeterli içerik sayılmaz.</li>
<li>Haberlerde bağlam, kim için önemli olduğu ve takip listesi eklenir. Rehberlerde uygulanabilir adımlar yazılır.</li>
<li>Aynı konunun ikinci kopyası yayımlanmaz; varsa kanonik adrese yönlendirilir.</li>
</ul>
<h2>2. Kaynak</h2>
<ul>
<li>Birincil kaynak tercih edilir: resmi blog, ürün sayfası, duyuru.</li>
<li>Kaynak yazının sonunda görünür. Belirsiz iddia kesin yargı gibi yazılmaz.</li>
</ul>
<h2>3. Reklam</h2>
<ul>
<li>Reklam, menüyü, giriş pencerelerini ve mini oyun düğmelerini kapatmaz.</li>
<li>Dolu olmayan reklam alanı sahte “reklam alanı” görseliyle doldurulmaz.</li>
<li>ads.txt dosyası yayıncı kimliğiyle eşleşir.</li>
</ul>
<h2>4. Düzeltme</h2>
<p>Maddi hata <a href="mailto:acarr.ffatih@gmail.com">acarr.ffatih@gmail.com</a> üzerinden bildirilir ve uygunsa güncellenir.</p>
"""

HAKKIMIZDA_HTML = """
<p>AcarTechs, teknoloji, yazılım, yapay zekâ, mobil ve oyun gelişmelerini Türkçe, sade ve özgün bir dille anlatan bağımsız bir yayındır. Saha ofisimiz Türkiye’dedir; iletişim adresi <a href="mailto:acarr.ffatih@gmail.com">acarr.ffatih@gmail.com</a> olarak sabittir.</p>
<p>Kısa marka duyurularını yeniden yayımlamak yayıncılık sayılmaz. Her yazıda okura kalan bir karar çerçevesi olmalıdır: bu özellik kime yarar, ne zaman gelir, alternatif nedir, hangi resmi sayfa kontrol edilir?</p>
<h2>Ne yayımlarız?</h2>
<ul>
<li>Resmi kaynağa dayanan, yoruma ve bağlama sahip haberler.</li>
<li>Abonelik, ekipman, mobil ayar ve tarayıcı oyunları gibi pratik rehberler.</li>
<li>AcarTechs Arcade’de tarayıcıda açılan özgün mini oyunlar.</li>
</ul>
<h2>Ne yayımlamayız?</h2>
<ul>
<li>Kaynaksız iddia, tık tuzağı başlık, kopya envanter ve tekrarlayan aynı haber.</li>
<li>Kullanıcıyı yanıltan reklam yerleşimi, menünün üstünü kapatan katmanlar.</li>
</ul>
<p>Künye ve yayın ilkeleri sayfaları, Google yayıncı hesabındaki kimlik bilgileriyle birlikte okunmalıdır.</p>
"""

ILETISIM_HTML = """
<p>Haber önerisi, düzeltme, iş birliği ve reklam envanteri için e-posta kullanın. Yanıtlar aynı adres üzerinden döner.</p>
<p><strong>Yayın adı:</strong> AcarTechs<br>
<strong>E-posta:</strong> <a href="mailto:acarr.ffatih@gmail.com">acarr.ffatih@gmail.com</a><br>
<strong>Web:</strong> <a href="https://acartechs.com">acartechs.com</a><br>
<strong>Konum:</strong> Türkiye<br>
<strong>ads.txt:</strong> <a href="https://acartechs.com/ads.txt">https://acartechs.com/ads.txt</a></p>
<h2>Düzeltme talepleri</h2>
<p>Hatalı veya eksik bir yazı görürseniz bağlantıyı mailinize ekleyin. Uygun görülen düzeltmeler ilgili sayfada güncellenir.</p>
<h2>Reklam</h2>
<p>Sitede Google AdSense kullanılır. Yayıncı kimliği ads.txt kaydıyla yetkilendirilir. Reklamların menü, üyelik penceresi veya mini oyun düğmelerinin üzerine binmemesi yayın ilkesidir.</p>
"""

OYUN_MAIN = r'''			<section class="acartechs-hot-tags" aria-label="Populer icerikler">
			<strong>Popüler İçerikler</strong>
											<a href="/?s=Google%20AI">#GoogleAI</a>
											<a href="/?s=Apple">#Apple</a>
											<a href="/?s=Samsung">#Samsung</a>
											<a href="/?s=ElektrikliOtomobil">#ElektrikliOtomobil</a>
											<a href="/?s=ChatGPT">#ChatGPT</a>
											<a href="/oyun/">#Oyun</a>
					</section>

<section class="acartechs-category-page">
			<section class="acartechs-category-intro">
				<h1>Oyun</h1>
				<p>AcarTechs Oyun bölümü, Xbox Wire veya PlayStation Blog metnini yeniden dizmek için değil; oyuncunun karar vermesine yardım etmek için vardır. Katalog, fiyat, tarih ve oynanış duyurularını resmi kaynağa bağlar, üstüne kim için anlamlı olduğunu yazarız.</p>
				<p>Aşağıda önce kalıcı rehberler, sonra tekilleştirilmiş haberler, en sonda AcarTechs Arcade mini oyunları yer alır. Reklamlar menünün, açılır listenin ve oyun başlatma düğmelerinin üzerine binmez.</p>
			</section>

			<h2 class="acartechs-section-kicker">Oyuncu rehberleri</h2>
			<div class="acartechs-guide-grid">
				<a class="acartechs-guide-card" href="/oyun-abonelik-servislerine-yeni-yapimlar-eklendi/">
					<span>Rehber</span>
					<strong>Game Pass mi PlayStation Plus mı?</strong>
					<p>Cihaz, katman ve haftalık oyun süresine göre abonelik seçimi.</p>
				</a>
				<a class="acartechs-guide-card" href="/bagimsiz-oyunlar-yaratici-fikirleriyle-one-cikiyor/">
					<span>Rehber</span>
					<strong>Bağımsız oyun nasıl seçilir?</strong>
					<p>Demo, süre ve niş tür üzerinden düşük pişmanlıklı keşif.</p>
				</a>
				<a class="acartechs-guide-card" href="/oyuncu-ekipmanlarinda-fiyat-performans-secimleri/">
					<span>Rehber</span>
					<strong>Ekipmanda fiyat/performans</strong>
					<p>Mouse, kulaklık ve klavyede vitrin ışığından önce bakılacaklar.</p>
				</a>
				<a class="acartechs-guide-card" href="/haftanin-oyun-firsatlari-ve-ucretsiz-yapimlari-aciklandi/">
					<span>Rehber</span>
					<strong>Ücretsiz oyun tuzağı olmasın</strong>
					<p>Resmi mağaza, süre notu ve depolama gerçeği.</p>
				</a>
			</div>

			<section class="acartechs-category-spotlight" aria-label="Oyun one cikan haberler">
				<a class="acartechs-category-main-card" href="/xbox-konsol-fiyatlarinda-agustos-itibariyla-yeni-donem-basliyor/">
					<span class="acartechs-category-media"><img class="acartechs-category-image" src="/wp-content/uploads/2026/06/Bootup_Wire-9c068aa206c9a72d2b1f.png" alt="Xbox konsol fiyatı değişince ne yapılmalı?"></span>
					<div>
						<span>Analiz</span>
						<h2>Xbox konsol fiyatı değişince ne yapılmalı?</h2>
						<p>1 Ağustos 2026 itibarıyla fiyat ve 2 TB model kararı: depolama, zamanlama ve kim için acil.</p>
					</div>
				</a>
				<div class="acartechs-category-mini-grid">
					<a href="/halo-campaign-evolved-temmuzda-oyuncularla-bulusmaya-hazirlaniyor/">
						<span class="acartechs-category-media"><img class="acartechs-category-image" src="/wp-content/uploads/2026/06/acartechs-web-cover-v2-3507-halo-campaign-evolved-temmuzda-oyuncularla-bulusmaya-hazirlani.jpg" alt="Halo Campaign Evolved"></span>
						<strong>Halo Campaign Evolved: tarih ve platform</strong>
					</a>
					<a href="/playstation-plus-haziran-katalogunda-final-fantasy-xvi-one-cikti/">
						<span class="acartechs-category-media"><img class="acartechs-category-image" src="/wp-content/uploads/2026/06/17e388f35e19282ef852a9221ffd1b75764eb79d.jpg" alt="PlayStation Plus haziran kataloğu"></span>
						<strong>PlayStation Plus haziran kataloğu nasıl okunur?</strong>
					</a>
					<a href="/xbox-game-pass-temmuz-listesine-yeni-oyunlar-ekleniyor/">
						<span class="acartechs-category-media"><img class="acartechs-category-image" src="/wp-content/uploads/2026/07/xbox-game-pass-temmuz-2026.jpg" alt="Game Pass temmuz listesi"></span>
						<strong>Game Pass temmuz listesinden nasıl seçilir?</strong>
					</a>
					<a href="/xbox-wire-temmuz-ayi-indie-selects-listesini-yayimladi/">
						<span class="acartechs-category-media"><img class="acartechs-category-image" src="/wp-content/uploads/2026/07/IndieSelects_July2026_Laurel_Wire-95ba9d698f0d81336d6b.jpg" alt="Indie Selects"></span>
						<strong>Indie Selects: bağımsız oyunu eleme rehberi</strong>
					</a>
				</div>
			</section>

			<section class="acartechs-category-list" aria-label="Oyun haber listesi">
<article>
	<a href="/xbox-wire-20-24-temmuz-haftasinin-yeni-oyunlarini-duyurdu/">
		<span class="acartechs-category-media"><img class="acartechs-category-image" src="/wp-content/uploads/2026/07/xbox-next-week-july-20-24-2026.jpg" alt="Haftalık Xbox çıkış listesi"></span>
		<div>
			<span>Oyun</span>
			<h3>Haftalık Xbox çıkış listesi nasıl kullanılır?</h3>
			<p>20-24 Temmuz listesini alışveriş fişi gibi değil, cihaz ve süre süzgeciyle okuyun.</p>
			<small>Acartechs Editör <time datetime="2026-07-21" data-acar-date>21 Temmuz 2026</time></small>
		</div>
	</a>
</article>
<article>
	<a href="/xbox-games-showcase-2026-oyun-dunyasinda-yeni-duyurularla-tamamlandi/">
		<span class="acartechs-category-media"><img class="acartechs-category-image" src="/wp-content/uploads/2026/06/acartechs-web-cover-v2-3506-xbox-games-showcase-2026-oyun-dunyasinda-yeni-duyurularla-tama.jpg" alt="Xbox Games Showcase 2026"></span>
		<div>
			<span>Oyun</span>
			<h3>Xbox Games Showcase 2026 sonrası ne takip edilmeli?</h3>
			<p>Fragman ezberi değil; tarih, cihaz ve Game Pass notu netleşen başlıklar.</p>
			<small>Acartechs Editör <time datetime="2026-06-24" data-acar-date>24 Haziran 2026</time></small>
		</div>
	</a>
</article>
<article>
	<a href="/xbox-insiders-icin-gamertag-oyun-merkezi-ve-istek-listesi-guncellemeleri-geldi/">
		<span class="acartechs-category-media"><img class="acartechs-category-image" src="/wp-content/uploads/2026/06/0.-Hero-ceb40e54016f914fe2bd-1024x576-1.png" alt="Xbox Insider"></span>
		<div>
			<span>Oyun</span>
			<h3>Xbox Insider güncellemesi ne zaman ciddiye alınır?</h3>
			<p>Test halkası ürün vaadi değildir; satın alma kararına temel olmaz.</p>
			<small>Acartechs Editör <time datetime="2026-06-24" data-acar-date>24 Haziran 2026</time></small>
		</div>
	</a>
</article>
<article>
	<a href="/mobil-oyunlarda-grafik-kalitesi-hizla-artiyor/">
		<div>
			<span>Rehber</span>
			<h3>Mobil oyunda grafik ve pil dengesi</h3>
			<p>Vitrin karesi değil; ısınma, kare süresi ve seans konforu.</p>
			<small>Acartechs Editör</small>
		</div>
	</a>
</article>
<article>
	<a href="/oyuncu-bilgisayarlarinda-ekran-karti-secimi-yeniden-gundemde/">
		<div>
			<span>Rehber</span>
			<h3>Ekran kartı seçimi: 1080p, 1440p, 4K</h3>
			<p>Monitör, VRAM ve güç kaynağı yazılmadan model adı ezberlenmez.</p>
			<small>Acartechs Editör</small>
		</div>
	</a>
</article>
			</section>

			<aside class="acartechs-adsense-shell is-horizontal placement-article" aria-label="Reklam">
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

												<div class="acartechs-arcade-banner">
				<div class="acartechs-arcade-banner-copy">
					<span class="acartechs-arcade-banner-kicker">AcarTechs Arcade</span>
					<strong class="acartechs-arcade-banner-title">Mini Oyunlar</strong>
					<p class="acartechs-arcade-banner-desc">Tarayıcıda açılan 10 özgün mini oyun. Reklamlar oyun düğmelerinin üzerine binmez.</p>
				</div>
								<div class="acartechs-arcade-banner-thumbs" aria-label="Oyun onizlemeleri">
					<a class="acartechs-arcade-thumb" href="/brick-blitz/" title="Brick Blitz">
						<span class="acartechs-arcade-thumb-art">
							<img class="acartechs-arcade-thumb-img" src="/assets/arcade/brick-blitz-thumb.webp?v=1784760675" alt="Brick Blitz" width="160" height="160" loading="lazy" decoding="async">
						</span>
						<em>Brick Blitz</em>
					</a>
					<a class="acartechs-arcade-thumb" href="/snake-rewind/" title="Snake Rewind">
						<span class="acartechs-arcade-thumb-art">
							<img class="acartechs-arcade-thumb-img" src="/assets/arcade/snake-rewind-thumb.webp?v=1784760675" alt="Snake Rewind" width="160" height="160" loading="lazy" decoding="async">
						</span>
						<em>Snake Rewind</em>
					</a>
					<a class="acartechs-arcade-thumb" href="/cascade-blocks/" title="Cascade Blocks">
						<span class="acartechs-arcade-thumb-art">
							<img class="acartechs-arcade-thumb-img" src="/assets/arcade/cascade-blocks-thumb.webp?v=1784760675" alt="Cascade Blocks" width="160" height="160" loading="lazy" decoding="async">
						</span>
						<em>Cascade Blocks</em>
					</a>
					<a class="acartechs-arcade-thumb" href="/number-fusion/" title="Number Fusion">
						<span class="acartechs-arcade-thumb-art">
							<img class="acartechs-arcade-thumb-img" src="/assets/arcade/number-fusion-thumb.webp?v=1784760675" alt="Number Fusion" width="160" height="160" loading="lazy" decoding="async">
						</span>
						<em>Number Fusion</em>
					</a>
					<a class="acartechs-arcade-thumb" href="/pixel-glider/" title="Pixel Glider">
						<span class="acartechs-arcade-thumb-art">
							<img class="acartechs-arcade-thumb-img" src="/assets/arcade/pixel-glider-thumb.webp?v=1784760675" alt="Pixel Glider" width="160" height="160" loading="lazy" decoding="async">
						</span>
						<em>Pixel Glider</em>
					</a>
					<a class="acartechs-arcade-thumb" href="/galaxy-defender/" title="Galaxy Defender">
						<span class="acartechs-arcade-thumb-art">
							<img class="acartechs-arcade-thumb-img" src="/assets/arcade/galaxy-defender-thumb.webp?v=1784760675" alt="Galaxy Defender" width="160" height="160" loading="lazy" decoding="async">
						</span>
						<em>Galaxy Defender</em>
					</a>
					<a class="acartechs-arcade-thumb" href="/neon-maze-muncher/" title="Neon Maze Muncher">
						<span class="acartechs-arcade-thumb-art">
							<img class="acartechs-arcade-thumb-img" src="/assets/arcade/neon-maze-muncher-thumb.webp?v=1784760675" alt="Neon Maze Muncher" width="160" height="160" loading="lazy" decoding="async">
						</span>
						<em>Neon Maze Muncher</em>
					</a>
					<a class="acartechs-arcade-thumb" href="/memory-flash/" title="Memory Flash">
						<span class="acartechs-arcade-thumb-art">
							<img class="acartechs-arcade-thumb-img" src="/assets/arcade/memory-flash-thumb.webp?v=1784760675" alt="Memory Flash" width="160" height="160" loading="lazy" decoding="async">
						</span>
						<em>Memory Flash</em>
					</a>
					<a class="acartechs-arcade-thumb" href="/reaction-rush/" title="Reaction Rush">
						<span class="acartechs-arcade-thumb-art">
							<img class="acartechs-arcade-thumb-img" src="/assets/arcade/reaction-rush-thumb.webp?v=1784760675" alt="Reaction Rush" width="160" height="160" loading="lazy" decoding="async">
						</span>
						<em>Reaction Rush</em>
					</a>
					<a class="acartechs-arcade-thumb" href="/runner-byte/" title="Runner Byte">
						<span class="acartechs-arcade-thumb-art">
							<img class="acartechs-arcade-thumb-img" src="/assets/arcade/runner-byte-thumb.webp?v=1784760675" alt="Runner Byte" width="160" height="160" loading="lazy" decoding="async">
						</span>
						<em>Runner Byte</em>
					</a>
				</div>
				<a class="acartechs-arcade-banner-cta" href="/mini-oyunlar/">
					<span>Oyunlara göz at</span>
					<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
				</a>
			</div>
				</section>
'''


def replace_once(html: str, pattern: str, repl: str, flags=0) -> str:
    new, n = re.subn(pattern, repl, html, count=1, flags=flags)
    return new if n else html


def set_meta(html: str, title: str, description: str, slug: str) -> str:
    url = f"https://acartechs.com/{slug}/"
    html = replace_once(html, r"<title>.*?</title>", f"<title>{title} – AcarTechs</title>")
    html = replace_once(
        html,
        r'<link rel="canonical" href="https://acartechs.com/[^"]*">',
        f'<link rel="canonical" href="{url}">',
    )
    html = replace_once(
        html,
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{description}">',
    )
    html = replace_once(
        html,
        r'<meta property="og:title" content="[^"]*">',
        f'<meta property="og:title" content="{title} – AcarTechs">',
    )
    html = replace_once(
        html,
        r'<meta property="og:description" content="[^"]*">',
        f'<meta property="og:description" content="{description}">',
    )
    html = replace_once(
        html,
        r'<meta property="og:url" content="[^"]*">',
        f'<meta property="og:url" content="{url}">',
    )
    return html


def replace_body(html: str, body: str) -> str:
    m = re.search(
        r'(<div class="acartechs-single-body">)(.*?)(</div>\s*</article>)',
        html,
        flags=re.S,
    )
    if not m:
        raise SystemExit("article body not found")
    return html[: m.start()] + m.group(1) + body + m.group(3) + html[m.end() :]


def replace_h1_dek(html: str, title: str, dek: str | None) -> str:
    html = replace_once(html, r"(<h1>)(.*?)(</h1>)", r"\1" + title + r"\3")
    if dek:
        html = replace_once(
            html,
            r'(<header class="acartechs-single-hero">.*?<h1>.*?</h1>\s*)<p>.*?</p>',
            r"\1<p>" + dek + "</p>",
            flags=re.S,
        )
    return html


def strip_editorial_depth(html: str) -> str:
    return re.sub(
        r'<section class="acartechs-editorial-depth">.*?</section>',
        "",
        html,
        flags=re.S,
    )


def rewrite_article(slug: str, data: dict) -> None:
    path = ROOT / slug / "index.html"
    html = path.read_text(encoding="utf-8")
    html = strip_editorial_depth(html)
    html = set_meta(html, data["title"], data["description"], slug)
    html = replace_h1_dek(html, data["title"], data.get("dek"))
    html = replace_body(html, data["body"])
    path.write_text(html, encoding="utf-8")
    print("rewrote", slug)


def clone_static(dest_slug: str, title: str, description: str, h1: str, content: str) -> None:
    src = ROOT / "hakkimizda" / "index.html"
    dest_dir = ROOT / dest_slug
    dest_dir.mkdir(exist_ok=True)
    html = src.read_text(encoding="utf-8")
    html = html.replace("/hakkimizda/", f"/{dest_slug}/")
    html = html.replace("Hakkımızda", title)
    html = set_meta(html, title, description, dest_slug)
    html = replace_once(html, r"(<h1>)(.*?)(</h1>)", r"\1" + h1 + r"\3")
    html = re.sub(
        r'(<div class="acartechs-static-content">)(.*?)(</div>)',
        r"\1" + content + r"\3",
        html,
        count=1,
        flags=re.S,
    )
    (dest_dir / "index.html").write_text(html, encoding="utf-8")
    print("wrote static", dest_slug)


def patch_static_content(slug: str, title: str, description: str, content: str) -> None:
    path = ROOT / slug / "index.html"
    html = path.read_text(encoding="utf-8")
    html = set_meta(html, title, description, slug)
    html = re.sub(
        r'(<div class="acartechs-static-content">)(.*?)(</div>)',
        r"\1" + content + r"\3",
        html,
        count=1,
        flags=re.S,
    )
    path.write_text(html, encoding="utf-8")
    print("patched", slug)


def rebuild_oyun() -> None:
    path = ROOT / "oyun" / "index.html"
    html = path.read_text(encoding="utf-8")
    html = set_meta(
        html,
        "Oyun rehberleri ve özgün analizler",
        "AcarTechs Oyun: kopya duyuru değil, abonelik, donanım ve takvim için özgün rehber ve analiz.",
        "oyun",
    )
    html = re.sub(
        r'\s*<aside class="acartechs-adsense-shell is-horizontal placement-top".*?</aside>',
        "",
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r'(</section>\s*)\s*<section class="acartechs-hot-tags".*?<section class="acartechs-footer-panel">',
        r"\1" + OYUN_MAIN + "\n\n			<section class=\"acartechs-footer-panel\">",
        html,
        count=1,
        flags=re.S,
    )
    path.write_text(html, encoding="utf-8")
    print("rebuilt /oyun/")


def global_link_fix() -> None:
    repls = {
        "/playstation-plus-haziran-katalogunda-final-fantasy-xvi-one-cikti-2/": "/playstation-plus-haziran-katalogunda-final-fantasy-xvi-one-cikti/",
        "/playstation-plus-haziran-kataloguna-final-fantasy-xvi-ve-sonic-x-shadow-generations-eklendi/": "/playstation-plus-haziran-katalogunda-final-fantasy-xvi-one-cikti/",
        "/bagimsiz-oyunlardan-haftanin-dikkat-cekenleri/": "/bagimsiz-oyunlar-yaratici-fikirleriyle-one-cikiyor/",
        "/haftanin-oyun-indirimleri-oyuncularin-ilgisini-cekiyor/": "/haftanin-oyun-firsatlari-ve-ucretsiz-yapimlari-aciklandi/",
        "/oyuncu-ekipmanlarinda-fiyat-performans-secenekleri-araniyor/": "/oyuncu-ekipmanlarinda-fiyat-performans-secimleri/",
        "/konsol-guncellemeleri-sosyal-ozellikleri-gelistiriyor/": "/konsol-oyunculari-icin-sistem-guncellemesi-yayinlandi/",
    }
    count = 0
    for path in ROOT.rglob("index.html"):
        text = path.read_text(encoding="utf-8")
        orig = text
        for a, b in repls.items():
            text = text.replace(a, b)
        if "acartechs-publisher-policy.css" not in text and "</head>" in text:
            text = text.replace(
                "</head>",
                '<link rel="stylesheet" href="/assets/acartechs-publisher-policy.css">\n</head>',
                1,
            )
        if text != orig:
            path.write_text(text, encoding="utf-8")
            count += 1
    print("updated files", count)


def noindex_thin_duplicates() -> None:
    slugs = [
        "playstation-plus-haziran-katalogunda-final-fantasy-xvi-one-cikti-2",
        "playstation-plus-haziran-kataloguna-final-fantasy-xvi-ve-sonic-x-shadow-generations-eklendi",
        "bagimsiz-oyunlardan-haftanin-dikkat-cekenleri",
        "haftanin-oyun-indirimleri-oyuncularin-ilgisini-cekiyor",
        "oyuncu-ekipmanlarinda-fiyat-performans-secenekleri-araniyor",
        "konsol-guncellemeleri-sosyal-ozellikleri-gelistiriyor",
    ]
    tag = "<meta name='robots' content='noindex, follow' />\n"
    for slug in slugs:
        path = ROOT / slug / "index.html"
        if not path.exists():
            continue
        html = path.read_text(encoding="utf-8")
        if "noindex" not in html:
            html = html.replace("<head>", "<head>\n" + tag, 1)
            path.write_text(html, encoding="utf-8")
            print("noindex", slug)


def main() -> None:
    for slug, data in ARTICLES.items():
        rewrite_article(slug, data)
    clone_static(
        "kunye",
        "Künye",
        "AcarTechs künye: yayın adı, iletişim, konum ve ads.txt yayıncı kaydı.",
        "Künye",
        KUNYE_HTML,
    )
    clone_static(
        "yayin-ilkeleri",
        "Yayın İlkeleri",
        "AcarTechs yayın ilkeleri: özgün içerik, kaynak ve reklam yerleşimi kuralları.",
        "Yayın İlkeleri",
        YAYIN_HTML,
    )
    patch_static_content(
        "hakkimizda",
        "Hakkımızda",
        "AcarTechs, resmi duyuruları kopyalamadan özgün teknoloji ve oyun yayını üretir.",
        HAKKIMIZDA_HTML,
    )
    patch_static_content(
        "iletisim",
        "İletişim",
        "AcarTechs iletişim: acarr.ffatih@gmail.com, Türkiye, ads.txt yayıncı kaydı.",
        ILETISIM_HTML,
    )
    rebuild_oyun()
    global_link_fix()
    noindex_thin_duplicates()


if __name__ == "__main__":
    main()

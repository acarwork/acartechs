# -*- coding: utf-8 -*-
from __future__ import annotations
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from thin_boost import BODY_RE, ROOT

B3 = {
    "android-studio-quail-1-yapay-zeka-destekli-hata-analizini-guclendirdi":
        "Quail 1, büyük kod tabanında neden arama süresini kısaltır; önerilen yama sizin test ve güvenlik kapınızı kapatmaz. Bankacılık ve sağlık uygulamasında ajan çıktısı ikinci bir insan incelemesi olmadan Play’e gitmez. AcarTechs bu notu hız katmanı olarak okur.",
    "apple-yeni-app-store-araclariyla-gelistiricilere-daha-fazla-esneklik-sunuyor":
        "Küçük ekip için görünürlük kapısı, büyük yayıncının medya bütçesi değildir. Vergi, KDV ve yerel ödeme görünmeyen satırdır. Esneklik duyurusunu tek dünya sanmayın; ülke kuralı aynı kutuyu farklı bağlar.",
    "chatgpt-icin-yeni-saglik-zekasi-guncellemesi-duyuruldu":
        "OpenAI’nin resmi çerçevesi de destekleyici bilgidir. Kronik hastalıkta sohbet geçmişi tek başına kayıt değildir. Acil belirtilerde 112, uygulama içi ‘daha dikkatli cevap’tan önce gelir. AcarTechs çizgiyi kalın tutar.",
    "cloudflare-oauth-akisini-tum-gelistiricilere-acti":
        "SaaS ve iç portalda paylaşılmış admin anahtarı, standart OAuth’tan tehlikelidir. Kullanıcı hangi sürede hangi kapsamı verdiğini görmelidir. İptal tuşunu ilk günde deneyin; yoksa vitrin akışıdır.",
    "cloudflare-workflows-icin-saga-rollback-destegi-geldi":
        "Dosya yükleme, virüs tarama ve yayın da saga adayıdır. Her adımın ileri ve geri fonksiyonunu isimlendirin. Dış banka telafiyi reddederse insan kuyruğu şarttır. Demo mutlu yolu üretimdeki kısmi başarı değildir.",
    "disney-plus-haziran-listesinde-avatar-fire-and-ash-promiyeri-one-cikiyor":
        "Top 10 sizin zevkiniz değildir. Abonelik katmanında indirme yoksa uçak listesi boştur. İkinci ‘kaçırma’ başlığı Avatar’ı yarıda bırakır. AcarTechs 2 başlık kuralını bu prömiyerde de uygular.",
    "disney-plus-the-doomies-icin-resmi-fragman-ve-yayin-tarihini-paylasti":
        "Sosyal medya karesi spoiler taşır; resmi Disney sayfası tarih ve dildir. Fragman davettir, sözleşme değildir. Korku eşiği, süre ve dil net değilse bu akşamın filmi değildir.",
    "github-copilot-ucretsiz-ve-ogrenci-planlarinda-otomatik-model-secimine-geciyor":
        "Plan sayfasındaki kota, model ailesi ve veri eğitim kutusunu aynı gün okuyun. Öğrenci ile iş hesabını karıştırmayın. API anahtarı sohbet geçmişine yapışmaz. Otomatik model kolaylıktır, sır çizgisini silmez.",
    "github-desktop-3-6-worktree-ve-copilot-entegrasyonunu-genisletti":
        "Öğrenci ve küçük ekipte Desktop yeter; 30 kişide GUI ikinci araçtır. Commit mesajında neyin neden değiştiğini siz yazın. Disk dolunca worktree kolaylığı tersine döner. AcarTechs GUI’yi CLI’nin yerine koymaz.",
    "google-arama-ai-mode-icin-gemini-3-5-flash-donemine-gecti":
        "Reklam birimi AI paragrafının yanında durabilir. ‘Google söyledi’ fatura veya tanı gerekçesi olmaz. Hukuk, sağlık ve güncel fiyat için asıl sayfaya gidin. Flash dipnotu silmez.",
    "google-finance-yeni-uygulama-ve-portfolyo-ozellikleriyle-guncellendi":
        "İki faktör ve cihaz kilidi finans uygulamasında e-postadan önemlidir. Portföy senkronu vergi kaydı tutmaz. Bildirimleri sessize almak serbesttir. AcarTechs yeşil çizgiyi emir saymaz.",
    "google-haziran-pixel-drop-ile-gemini-ve-yaratici-araclari-genisletti":
        "60 Hz ve karanlık tema seyahatte pil kazandırır. Yaratıcı aracı Wi-Fi’de ve kılıfsız deneyin. Sistem güncellemesi özellik listesinden ayrı inebilir. Drop vitrindir, sizin modeliniz karardır.",
    "microsoft-agent-365-ile-kurumsal-yapay-zeka-ajanlarini-yonetmek-istiyor":
        "Lisans koltukları kullanılmayan ajanda yanar. Eğitim lisans kadar önemlidir. SSO ve koşullu erişim ilk 30 günün parçasıdır. Ajan envanteri olmadan üretim yok. Kontrol düzlemi fabrikadan önce gelir.",
    "microsoft-windows-10-esu-suresini-kullanicilar-icin-uzatti":
        "Yazıcı ve muhasebe yazılımı 11’de kırılıyorsa önce o yazılım konuşulur. ‘Hâlâ açılıyor’ güvenlik değildir. Ek süre donanım alışverişini bu çeyreğe sıkıştırmaz; envanter yazdırır. Resmi yaşam döngüsü sayfasını işaretleyin.",
    "netflix-haftalik-top-10-listesinde-i-will-find-you-zirveye-yerlesti":
        "Ayın 25’inde hâlâ izlemiyorsanız duraklatın. Spoiler kareyi açmadan Tudum maddesine bakın. 15 Haziran listesi keşiftir, kanon değildir. AcarTechs ilk hafta zirvesini başyapıt diye yazmaz.",
    "netflix-haftanin-izlenecek-yapimlarini-yeni-listeyle-paylasti":
        "Yaş etiketini fragmandan değil başlık sayfasından okuyun. Yıllık planı bu beş ada bağlamayın. Resmi Tudum, sosyal kareden önce gelir. Haftalık liste süzgeçtir, maraton fişi değildir.",
    "netflix-haziran-2026-takviminde-yeni-diziler-ve-filmler-one-cikiyor":
        "Offline indirme köy ve uçak için takvimden önemlidir. Çocuklu evde Avatar öne çıkar, yetişkin gerilim hafta sonuna kalır. Elemek izlemektir. Haziran takvimi 30 günlük bütçedir.",
    "openai-ajanlarin-is-dunyasindaki-etkisini-yeni-arastirmayla-anlatti":
        "Politika cümlesi yoksa araştırma sızıntı davetidir. Onaysız gönderim yok. Ölçmeden herkes kullansın demeyin. Ajan tekrarlayan adımı keser, sorumluluğu devretmez. AcarTechs slaytı NDA yerine koymaz.",
    "openai-model-davranislarini-yayin-oncesi-simule-eden-yeni-yontemini-anlatti":
        "Kırmızı takım ve politika katmanı simülasyonla birlikte durur. Kullanıcı sohbetindeki her cümle denetlenmiş değildir. Kendi kötü senaryonuzu yazın. Laboratuvar notu sıfır risk vaadi değildir.",
    "openai-partner-network-ile-yapay-zeka-projelerinde-is-ortagi-donemi-basladi":
        "İnsan onayı olmayan otomatik e-posta ilk haftada markayı yakar. 4 kişilik dükkâna ajan orkestrasyonu fazla gelir. Sözleşmede veri, alt işlemci, eğitim maddesi rozetten değerlidir. Kapı hızdır, belge güvencedir.",
    "openai-patch-the-planet-ile-acik-kaynak-guvenligine-ai-destegi-veriyor":
        "Öğrenci katkısı yeniden üretilebilir rapordur, yıldız spam’i değil. Kendi fork’unuzda sessiz yama kullanıcıyı kör bırakabilir. Yarın tüm npm güvenli olmaz. Program kapasitedir, sizin yama disiplininiz ayrıdır.",
    "openai-ve-broadcom-yapay-zeka-icin-jalapeno-inference-cipini-tanitti":
        "Üretim tarihi, watt ve yazılım kilidi netleşmeden ucuz token cümlesi slayttır. Kurum müşterisi SLA ile okur. Eldeki asistanın kalitesi bu kutu gelmeden de sizin onay kuralınızdır. Sunucu oyunudur.",
    "samsung-galaxy-watch-icin-yapay-zeka-destekli-saglik-ozelliklerini-duyurdu":
        "Aile öyküsü ve hekimin takip et dediği kişiye ek göz olabilir. Sporcuda GPS sağlık kartından değerlidir. Kutudaki tıbbi dil gerçek kullanımı değiştirmez. Saat aynadır, reçete değildir.",
    "samsung-vivatech-2026da-baglantili-bakim-vizyonunu-sergiledi":
        "Sigorta veya işveren paylaşımı anlamlı öneri cümlesinin altında gizlenebilir. Satın alma fiyat, Türkiye tarihi ve yazılım yılı netleşince konuşulur. Fuar videosu iç cam fiyatını göstermez. İzin mimarisidir.",
    "whatsapp-kullanici-adi-rezervasyonunu-baslatti":
        "Yedek ve cihaz kilidi durur. Kurumsal hat kişisel addan ayrı dursun. Numara paylaşımını azaltır, anonim sihir değildir. Resmi blog, forum paniğinden önce gelir. Rezervasyon kimlik süzgecidir.",
}


def main() -> None:
    n = 0
    for slug, para in B3.items():
        path = ROOT / slug / "index.html"
        html = path.read_text(encoding="utf-8")
        if "acartechs-boost3" in html:
            continue
        extra = f'\n<section class="acartechs-boost3"><p>{para}</p></section>\n'
        m = BODY_RE.search(html)
        inner = m.group(2)
        if 'class="acartechs-source-note"' in inner:
            inner = inner.replace('<p class="acartechs-source-note"', extra + '<p class="acartechs-source-note"', 1)
        else:
            inner += extra
        html = html[: m.start()] + m.group(1) + inner + m.group(3) + html[m.end() :]
        path.write_text(html, encoding="utf-8")
        n += 1
    print("boost3", n)


if __name__ == "__main__":
    main()

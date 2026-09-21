# -*- coding: utf-8 -*-
from __future__ import annotations
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from thin_boost import BODY_RE, ROOT

P = {
    "disney-plus-the-doomies-icin-resmi-fragman-ve-yayin-tarihini-paylasti":
        "Çocuk profilinde otomatik oynatma fragmanı film sanır. Tarih pencereyse izin günü bağlanmaz. AcarTechs Doomies duyurusunu yaş, ton ve takvim süzgeci olarak tutar.",
    "github-copilot-ucretsiz-ve-ogrenci-planlarinda-otomatik-model-secimine-geciyor":
        "Kota bitince sessizce zayıflayan model ödevi yarım bırakır. İş reposunu okul mailine bağlamayın. Açıklama evet, bitmiş ödev hayır.",
    "github-desktop-3-6-worktree-ve-copilot-entegrasyonunu-genisletti":
        "LFS ve satır sonu Windows worktree’de sürpriz üretir. Müşteri verisi commit taslağına yapışmaz. Disk dolunca kolaylık tersine döner.",
    "google-arama-ai-mode-icin-gemini-3-5-flash-donemine-gecti":
        "Şirket metnini arama kutusuna yapıştırmayın. İki kaynak çelişiyorsa üçüncüyü açın. Flash hızlı giriştir. Hukuk ve sağlık kutuda bitmez.",
    "google-finance-yeni-uygulama-ve-portfolyo-ozellikleriyle-guncellendi":
        "Sahte mağaza ikizini resmi paket adından ayırın. İş telefonunda kişisel izleme listesi açmayın. Yeşil çizgi emir değildir.",
    "microsoft-agent-365-ile-kurumsal-yapay-zeka-ajanlarini-yonetmek-istiyor":
        "Hangi SharePoint ve mailbox kayıt altında değilse POC sızıntıdır. Onaysız gönderim yok. Envanter olmadan üretim yok.",
    "netflix-haftalik-top-10-listesinde-i-will-find-you-zirveye-yerlesti":
        "Birinci bölüm yetmiyorsa bırakın. Çocukta yaş etiketi birinciden önce gelir. Zirve için yıllık kilitlemeyin.",
    "netflix-haziran-2026-takviminde-yeni-diziler-ve-filmler-one-cikiyor":
        "Pazartesi tek dizi, Cuma tek film. Belgesel ile komediyi aynı akşama yığmayın. Takvim 30 günlük bütçedir.",
    "openai-ajanlarin-is-dunyasindaki-etkisini-yeni-arastirmayla-anlatti":
        "Revizyon artmışsa ajan her cümleyi yeniden yazdırıyordur. Fiyat teklifi kötü aday, kod iskeleti iyi adaydır. NDA tüketici ajana yapışmaz.",
    "openai-model-davranislarini-yayin-oncesi-simule-eden-yeni-yontemini-anlatti":
        "Ödeme ve e-posta adımında durdurma yoksa simülasyon kurtarmaz. Sağlık kararı gerekçesi olmaz. Laboratuvar sertifika değildir.",
    "openai-patch-the-planet-ile-acik-kaynak-guvenligine-ai-destegi-veriyor":
        "Bin kırmızı triyajsız bakıcıyı yakar. Lockfile ve tek bakıcı riski sizin listenizdir. 48 saat OS-tarayıcı kuralı bu programdan düşmez.",
    "samsung-vivatech-2026da-baglantili-bakim-vizyonunu-sergiledi":
        "Çocuk ve yaşlıda varsayılan paylaşımı kapatın. Sağlık verisi TV önerisinden ayrı rızadır. Türkiye fiyatı fuar standında yazmaz.",
}

def main() -> None:
    n = 0
    for slug, para in P.items():
        path = ROOT / slug / "index.html"
        html = path.read_text(encoding="utf-8")
        if "acartechs-boost4" in html:
            continue
        extra = f'<section class="acartechs-boost4"><p>{para}</p></section>\n'
        m = BODY_RE.search(html)
        inner = m.group(2)
        if "acartechs-source-note" in inner:
            inner = inner.replace('<p class="acartechs-source-note"', extra + '<p class="acartechs-source-note"', 1)
        else:
            inner += extra
        html = html[: m.start()] + m.group(1) + inner + m.group(3) + html[m.end() :]
        path.write_text(html, encoding="utf-8")
        n += 1
    print("boost4", n)

if __name__ == "__main__":
    main()

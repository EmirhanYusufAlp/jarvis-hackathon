# JARVIS 0.1 - Hackathon Assistant

Bu proje, okulda düzenlenen **Hackathon** kapsamında **6 saat gibi kısıtlı bir sürede** python 3.10.20 ile sıfırdan geliştirilmiş, yapay sinir ağı tabanlı bir terminal asistanı ve chat botu prototipidir (MVP).


Özellikler:

*Yapay Sinir Ağı Desteği:** `scikit-learn` (`MLPClassifier`) kütüphanesi kullanılarak kullanıcının girdilerini anlama, analiz etme ve tahmin etme yeteneği.
*Kalıcı Hafıza & Dinamik Öğrenme:** `SQLite` veritabanı entegrasyonu sayesinde kullanıcının geri bildirimlerine göre (Doğru/Yanlış kontrolü ile) çalışma anında dinamik olarak kendini eğitebilme ve yeni cevaplar öğrenebilme.
*Klasör Bazlı Dinamik Mimari:** Sabit disk yollarından bağımsız, projenin çalıştırıldığı klasörü baz alan (`os.path`) taşınabilir (portable) yapı.


Nasıl Çalıştırılır?

1. Gerekli kütüphaneleri bilgisayarınıza yükleyin:
   "pip install scikit-learn numpy rich pyfiglet keyboard"

2. "Jarvis 0.1 beta.py" çalıştırın ve eğlenin

Hikayesi

Ben şuanki okuluma nakil aldırmadan önce aklımdaki en önemli şey 8.sınıftan beri aşık olduğum ilk aşkımdı.Aramız iyiydi ama açılmamıştım(en büyük hatam ama açıldığımda da artık çok geçti)

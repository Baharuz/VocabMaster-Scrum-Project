# VocabMaster: 6 Sefer ile Kelime Ezberleme Sistemi

Bu proje, **Scrum** metodolojisi kullanılarak geliştirilmiş, yapay zeka destekli bir dil öğrenme ve kelime ezberleme uygulamasıdır. Kullanıcıların kelimeleri kalıcı hafızaya almasını sağlayan özel bir "Spaced Repetition" (Aralıklı Tekrar) algoritması üzerine kurulmuştur.

---

## Ekip Üyeleri 
* **Bahar Uz** - *Backend Developer & AI Architect* 
* **Haktan Tekinel** - *Mobile Developer & UI/UX* 

---

## Kullanılan Teknolojiler
* **Frontend:** React Native (Expo) 
* **Backend:** Python (FastAPI)
* **Veritabanı:** SQLite
* **Yapay Zeka:** Gemini API / OpenAI (Hikaye ve Görsel Üretimi)
* **Proje Yönetimi:** Jira (Scrum Software Space)
**  Jira linki: https://yazilim-yapimi.atlassian.net/jira/software/projects/SCRUM/boards/2/backlog?selectedIssue=SCRUM-4&atlOrigin=eyJpIjoiYzQ4MTYwZGEwZWUxNDU3MTg4N2MwNTI5YmM1MDRiOWIiLCJwIjoiaiJ9 **
* **Kod Kalitesi:** SonarQube & KISS Prensipleri

---

## 6 Sefer Algoritması (Spaced Repetition)
Sistem, bir kelimenin tam olarak öğrenilmesi için 6 farklı zaman diliminde doğru cevaplanmasını şart koşar. Her doğru cevapta kelime bir sonraki aşamaya geçer:
1. **1 Gün Sonra**
2. **1 Hafta Sonra**
3. **1 Ay Sonra**
4. **3 Ay Sonra**
5. **6 Ay Sonra**
6. **1 Yıl Sonra**
*Herhangi bir aşamada yanlış cevap verilirse, kelime süreci sıfırlanır ve başa döner.*

---

## Proje Özellikleri (User Stories)
- **STORY-1:** Kullanıcı Kayıt/Giriş ve Şifre Hatırlatma.
- **STORY-2:** Resim ve Ses destekli Kelime Ekleme Modülü.
- **STORY-3:** 6 Sefer Algoritmalı Dinamik Sınav Sistemi.
- **STORY-4:** Kişiselleştirilebilir Günlük Yeni Kelime Hedefleri.
- **STORY-5:** Başarı Analizi ve PDF Formatında Rapor Çıktısı.
- **STORY-6:** Öğrenilen Kelimelerden Üretilen Wordle (Bulmaca) Oyunu.
- **STORY-7:** AI Destekli Hikaye (Word Chain) ve Görsel Oluşturma.

---

## 🚀 Kurulum ve Çalıştırma

### Backend (Python)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

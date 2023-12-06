import datetime

def selamla():
    print("Merhaba, ben Exo. Size nasıl yardımcı olabilirim?")

def cevapla(soru):
    if soru == "bugün ne gün?" or soru == "bugün tarih?" or soru == "bugün kaç?" or soru == "bugün tarihi nedir?" or soru == "bugün kaçtır?" or soru == "bugün tarihi kaçtır?":
        print("Bugün " + datetime.datetime.now().strftime("%A") + ", " + datetime.datetime.now().strftime("%d %B %Y") + ".")
    else:
        print("Üzgünüm, bu soruyu cevaplayamıyorum.")

def main():
    selamla()
    soru = input("Sorunuz nedir? ")
    cevapla(soru)

if __name__ == "__main__":
    main()

print("  _____           _     _       __  ___  ")
print(" / ____|         (_)   | |     /_ |/ _ \ ")
print("| |     _____   ___  __| |______| | (_) |")
print("| |    / _ \ \ / / |/ _` |______| |\__, |")
print("| |___| (_) \ V /| | (_| |      | |  / / ")
print(" \_____\___/ \_/ |_|\__,_|      |_| /_/  ")
print(" ")
yas=int(input("Lütfen Yaşınızı Giriniz: "))
saat=float(input("Lütfen 21.00 Formatında Giriniz: "))
gun=input("Haftanın Hangi Günündesiniz? (Küçük harfler ile): ")

if gun == "pazartesi" or gun == "salı" or gun == "çarşamba" or gun == "perşembe" or gun == "cuma":
    if saat >= 05.00 and saat <= 21.00:
        if yas >= 20:
            if yas >= 65:
                if saat >= 10.00 and saat <= 13.00:
                    print("sokağa çıkabilirsiniz")
                else:
                    print("sokağa çıkamazsınız")
            else:
                print("sokağa çıkabilirsiniz")
        else:
            if saat >= 13.00 and saat <= 16.00:
                print("sokağa çıkabilirsiniz")
            else:
                print("sokağa çıkamazsınız")
    else:
        print("sokağa çıkamazsınız")

elif gun == "cumartesi" or gun == "pazar":
    print("sokağa çıkamazsınız")
else:
    print("Lütfen geçerli bir gün giriniz!")



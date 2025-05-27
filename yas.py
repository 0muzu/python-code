from datetime import datetime

def yash_hesabla(dogum_tarixi):
    bugun = datetime.now()
    yil = bugun.year - dogum_tarixi.year
    ay = bugun.month - dogum_tarixi.month
    gun = bugun.day - dogum_tarixi.day

    if gun < 0:
        ay -= 1
        onceki_ay = bugun.month - 1 if bugun.month > 1 else 12
        onceki_il = bugun.year if bugun.month > 1 else bugun.year - 1
        gun_sayi = (datetime(onceki_il, onceki_ay % 12 + 1, 1) - datetime(onceki_il, onceki_ay, 1)).days
        gun += gun_sayi

    if ay < 0:
        yil -= 1
        ay += 12

    return yil, ay, gun
il = int(input("Doğum ilini daxil edin: "))
ay = int(input("Doğum ayını daxil edin: "))
gun = int(input("Doğum gününü daxil edin: "))

dogum_tarixi = datetime(il, ay, gun)
yil, ay, gun = yash_hesabla(dogum_tarixi)
print(f"Sizin yaşınız: {yil} il, {ay} ay, {gun} gün")

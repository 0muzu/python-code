il = int(input("Doğum ilini yaz: "))
ay = int(input("Doğum ayını yaz (1-12): "))
gun = int(input("Doğum gününü yaz: "))

# Bugünkü tarixi özümüz təyin edirik (sabit şəkildə)
bugun_il = 2025
bugun_ay = 5
bugun_gun = 27

yas = bugun_il - il

# Əgər hələ ad günü gəlməyibsə, yaşı 1 azaldırıq
if (ay > bugun_ay) or (ay == bugun_ay and gun > bugun_gun):
    yas -= 1

print("Sənin yaşın:", yas)

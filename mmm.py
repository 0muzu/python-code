il = int(input("Doğum ilini yaz: "))
ay = int(input("Doğum ayını yaz (1-12): "))
gun = int(input("Doğum gününü yaz: "))

bugun_il = 2025
bugun_ay = 5
bugun_gun = 27

yas = bugun_il - il

if (ay > bugun_ay) or (ay == bugun_ay and gun > bugun_gun):
    yas -= 1

print("Sənin yaşın:", yas)

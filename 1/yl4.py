# kasutaja sisend
nimi = input("Sisestage oma nimi: ")
lubatud_kiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus (km/h): "))
# arvutused
# vahe = tegelik_kiirus - lubatud_kiirus
# trahv = vahe * 3
trahv = (tegelik_kiirus - lubatud_kiirus) * 3
# arvestame maksimaamääruga
trahv = min(190, trahv)
# väljund
print(nimi + ", kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot.")
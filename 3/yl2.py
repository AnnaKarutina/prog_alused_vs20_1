# kasutaja sisend
# sisetame mitu ringi jänes peab jooksma
ringide_arv = int(input("Sisesta ringide arv: "))
# defineerime juhtiv muutuja
ringi_number = 1 # alustame jooks 1. ringist
# loeme prograndid kokku ka, hetkel neid pole
porgandite_arv = 0
while(ringi_number <= ringide_arv):
    # väljastame, milline ring on parasjagu joostud läbi
    print(str(ringi_number) + ". ring")
    # kas hetkel on paarisarvuline ring?
    if(ringi_number % 2 == 0):
        # siin antakse porgandeid
        # nii palju, milline ringi number on
        print("said " + str(ringi_number) + " porgandeid")
        porgandite_arv = porgandite_arv + ringi_number
        # vaatame palju porgandeid nüüd on
        print("Hetkel on kokku " + str(porgandite_arv) + " porgandeid")
    # suurendame juhtivmuutuja väärtust
    ringi_number += 1
# kõik ringid on läbi
print("Porgandite koguarv on " + str(porgandite_arv))
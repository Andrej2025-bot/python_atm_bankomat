pin = "1234"
zostatok = 1500 
pokusy = 3





while True :
 pokusy = 3
 pristup_povolený = False


 while pokusy > 0 :
    pinkod = input("Vložte kartu a zadajte heslo: \n")

    if pinkod == pin :
        pristup_povolený = True 
        print("Prístup povolený, Vitajte.")
        break
    else :
        pokusy = pokusy - 1
        print("Zlé heslo, zadajte znova. Počet zostávajúcich pokusov: " , pokusy)
 if not pristup_povolený:
    print("Karta zablokovaná. Príliš veľa nesprávných pokusov.")
    exit()
       
    



 while pristup_povolený :
    menu = input("Vyberte si: 1-stav konta, 2-výber hotovosti, 3-vklad hotovosti, 4-Koniec\n")    

    if menu == "1":
        print("Zostatok na účte:" , zostatok)   
    elif menu == "2":
        cash = int(input("Vyberte sumu: 10/20/50/100/200/500\n"))
        povolena_suma = (10,20,50,100,200,500)
        if cash not in povolena_suma:
            print("Suma je neplatná, zadajte znova:")
        else:
            if zostatok >= cash:
               zostatok = zostatok - cash
               print("Výber úspešný.")
               print("Váš zostatok je: ", zostatok)
            else:       
               print("Nedostatok prostriedkov.")    

    elif menu == "3":
        peniaze = int(input("Koľko si prajte vložiť ?\n"))
        pridať_sumu = (10,20,50,100,200,500)
        if   peniaze not in pridať_sumu:
             print("Neplatná suma, vyberte znovu.")
        else:
            zostatok = zostatok + peniaze
            print("Váš nový zostatok: ", zostatok)   

    elif menu == "4":
        print("Ďakujeme, vyberte kartu")
        pristup_povolený = False
        
    else:
        print("Chyba, vyberte znova.") 



           
menyFel = False
menyLoop = True
while True:
    while menyLoop:
        try:
            menyVal = int(input("Meny: Spela mot andra[1], Spela mot datorn[2], Avsluta[3]"))
        except(ValueError):
            print("Välj 1,2,3")
            menyFel = True
        if menyFel:
            print("2")
            pass
        elif menyVal == 1 or menyVal == 2 or menyVal == 3:
            menyLoop = False
        else:
            print("1")
    if menyVal == 1:
        while True:
            print("Spelare 1")
            print('Välj "Sten", "Sax", eller "Påse"')
            spelare1Val = input("Val: ").lower()
            if spelare1Val != "sten" or spelare1Val != "sax" or spelare1Val != "påse":
                print("Välj ett av alternativen")
            else:
                break
        while True:
            print("Spelare 2")
            print('Välj "Sten", "Sax", eller "Påse"')
            spelare2Val = input("Val: ").lower()
            if spelare2Val != "sten" or spelare2Val != "sax" or spelare2Val != "påse":
                print("Välj ett av alternativen")
            else:
                break
        

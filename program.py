import random
menyFel = False
menyLoop = True
spelare1Score = 0
spelare2Score = 0


while True:
    while True:
        while menyLoop:
            någonVann = False
            vinst = 0
            try:
                menyVal = int(input("Meny: Spela mot andra[1], Spela mot datorn[2], Avsluta[3]"))
            except(ValueError):
                print("Välj 1,2,3")
                menyFel = True
            if menyFel:
                pass
            elif menyVal == 1 or menyVal == 2 or menyVal == 3:
                menyLoop = False
            else:
                print("Välj 1,2,3")
        if menyVal == 1:
            while True:
                print("Spelare 1")
                print('Välj "Sten", "Sax", eller "Påse"')
                spelare1Val = input("Val: ").lower()
                if spelare1Val == "sten" or spelare1Val == "sax" or spelare1Val == "påse":
                    break
                else:
                    print("Välj ett av alternativen")
            while True:
                print("Spelare 2")
                print('Välj "Sten", "Sax", eller "Påse"')
                spelare2Val = input("Val: ").lower()
                if spelare2Val == "sten" or spelare2Val == "sax" or spelare2Val == "påse":
                    break
                else:
                    print("Välj ett av alternativen")
            if spelare1Val == "sten" and spelare2Val == "sten":
                pass
            elif spelare1Val == "sten" and spelare2Val == "sax":
                spelare1Score += 1
            elif spelare1Val == "sten" and spelare2Val == "påse":
                spelare2Score += 1
            elif spelare1Val == "sax" and spelare2Val == "sax":
                pass
            elif spelare1Val == "sax" and spelare2Val == "sten":
                spelare2Score += 1
            elif spelare1Val == "sax" and spelare2Val == "påse":
                spelare1Score += 1
            elif spelare1Val == "påse" and spelare2Val == "påse":
                pass
            elif spelare1Val == "påse" and spelare2Val == "sax":
                spelare2Score += 1
            elif spelare1Val == "påse" and spelare2Val == "sten":
                spelare1Score += 1
            print(f"Spelare1: {str(spelare1Score)} Spelare2: {str(spelare2Score)}")
            if spelare1Score + spelare2Score == 3:
                if spelare1Score > spelare2Score:
                    vinst = 1
                    någonVann = True
                elif spelare1Score < spelare2Score:
                    vinst = 2
                    någonVann = True
            else:
                pass
            if någonVann:
                if vinst == 1:
                    print("Spelare 1 vann congratz!")
                    menyLoop = True
                    break
                elif vinst == 2:
                    print("Spelare 2 vann congratz!")
                    menyLoop = True
                    break
                else:
                    print("något gick fel")

        if menyVal == 2:
            while True:
                print('Välj "Sten", "Sax", "Påse"')
                spelarVal = input("Val: ").lower()
                if spelarVal == "sten" or spelarVal == "sax" or spelarVal == "påse":
                    break
                else:
                    print("Välj något av alternativen")
            datorVal = random.randint(1,3)
            
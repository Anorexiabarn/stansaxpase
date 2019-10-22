import random, getpass, pyfiglet, time
menyFel = False
menyLoop = True
spelare1Score = 0
spelare2Score = 0
datorScore = 0
spelareScore = 0
firstStart = 0
font = pyfiglet.Figlet(font="speed")
spelare1Vann = font.renderText("Spelare1\nVann")
spelare2Vann = font.renderText("Spelare2\nVann")
spelareVann = font.renderText("Spelare\nVann")
datorVann = font.renderText("Datorn\nVann")
menyText = font.renderText("Sten\nSax\nPase")
l8r = font.renderText("L8r\nKiddo")
while True:
    while True:
        while menyLoop:
            någonVann = False
            vinst = 0
            spelare1Score = 0
            spelare2Score = 0
            datorScore = 0
            spelareScore = 0
            if firstStart == 0:
                print(menyText)
                firstStart += 1
            else:
                pass
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
                spelare1Val = getpass.getpass("Val: ").lower()
                if spelare1Val == "sten" or spelare1Val == "sax" or spelare1Val == "påse":
                    break
                else:
                    print("Välj ett av alternativen")
            while True:
                print("Spelare 2")
                print('Välj "Sten", "Sax", eller "Påse"')
                spelare2Val = getpass.getpass("Val: ").lower()
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
                    print(spelare1Vann)
                    menyLoop = True
                    break
                elif vinst == 2:
                    print(spelare2Vann)
                    menyLoop = True
                    break
                else:
                    print("något gick fel")

        if menyVal == 2:
            while True:
                print('Välj "Sten", "Sax", "Påse"')
                spelareVal = input("Val: ").lower()
                if spelareVal == "sten" or spelareVal == "sax" or spelareVal == "påse":
                    break
                else:
                    print("Välj något av alternativen")
            datorNumber = random.randint(1,3) # får fatorn att välja ett random number som är sten sax eller påse och sedan ska programmet fungera likadant som när man möter andra spelare.
            if datorNumber == 1:
                datorVal = "sten"
            elif datorNumber == 2:
                datorVal = "sax"
            elif datorNumber == 3:
                datorVal = "påse"

            if spelareVal == "sten" and datorVal == "sten":
                pass
            elif spelareVal == "sten" and datorVal == "sax":
                spelareScore += 1
            elif spelareVal == "sten" and datorVal == "påse":
                datorScore += 1
            elif spelareVal == "sax" and datorVal == "sax":
                pass
            elif spelareVal == "sax" and datorVal == "sten":
                datorScore += 1
            elif spelareVal == "sax" and datorVal == "påse":
                spelareScore += 1
            elif spelareVal == "påse" and datorVal == "påse":
                pass
            elif spelareVal == "påse" and datorVal == "sax":
                datorScore += 1
            elif spelareVal == "påse" and datorVal == "sten":
                spelareScore += 1
            print(f"Datorn valde: {datorVal.capitalize()}")
            print(f"Spelare: {str(spelareScore)} Dator: {str(datorScore)}")
            if spelareScore + datorScore == 3:
                if spelareScore > datorScore:
                    vinst = 1
                    någonVann = True
                elif spelareScore < datorScore:
                    vinst = 2
                    någonVann = True
            else:
                pass
            if någonVann:
                if vinst == 1:
                    print(spelareVann)
                    menyLoop = True
                    break
                elif vinst == 2:
                    print(datorVann)
                    menyLoop = True
                    break
                else:
                    print("något gick fel")
        if menyVal == 3:
            print(l8r)
            time.sleep(3)
            exit()
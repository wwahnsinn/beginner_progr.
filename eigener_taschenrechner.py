while True:

        print("Dies ist ein Taschenrechner")

        while True:

                print("Welche Rechnung möchten Sie durchführen? ")
                print("")

                print("Addition                 [1]")
                print("Subtraktion              [2]")
                print("Multiplikation           [3]")
                print("Division                 [4]")
                print("Rechner verlassen        [0]")
                print("")

                auswahl = int(input("Eingabe bitte ")) 

                if auswahl == 1:
                        print("Addition")
                elif auswahl == 2:
                        print("Subtraktion")
                elif auswahl == 3:
                        print("Multiplikation")
                elif auswahl == 4:
                        print("Division")
                elif auswahl == 0:
                        print("Rechner verlassen")
                        exit()     
                else:
                        print("Falsche Eingabe")
                        break

                zahl_eins = int(input(" Bitte geben Sie die ERSTE Zahl ein "))
                print(zahl_eins)

                zahl_zwei = int(input(" Bitte geben Sie die ZWEITE Zahl ein "))
                print(zahl_zwei)



                if auswahl == 1:
                        print("Ergebnis: ", zahl_eins + zahl_zwei)
                elif auswahl == 2:
                        print("Ergebnis: ", zahl_eins - zahl_zwei)
                elif auswahl == 3:
                        print("Ergebnis: ", zahl_eins * zahl_zwei)
                elif auswahl == 4:
                        print("Ergebnis: ", zahl_eins / zahl_zwei)
                else:
                        print("Ungültige Eingabe")
                        break

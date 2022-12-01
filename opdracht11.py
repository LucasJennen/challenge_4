getal_1 = int(input("Voer het eerste getal in: "))
operator = input("Voeg een operator toe: ")
getal_2 = int(input("Voer het tweede getal in: "))
uitkomst = input(getal_1*getal_2)

if operator == "*":
    print(uitkomst)
else:
    print("Ik herken die operator niet, probeer het opnieuw.")
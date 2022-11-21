while True:

  getal_1 = int(input("Voer het eerste getal in: "))
  operator = input("Voeg een operator toe: ")
  getal_2 = int(input("Voer het tweede getal in: "))
  uitkomst = input("klik = en dan enter voor de uitkomst: ")

  if operator == "+":
    print(uitkomst)
  elif operator == "-":
    print(uitkomst)
  elif operator == "*":
    print(uitkomst)
  elif operator == "/":
    print(uitkomst)
  else:
    print("Ik herken die operator niet, probeer het opnieuw.")
  if uitkomst == "=":
    print(str(getal_1 * getal_2))
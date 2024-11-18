eta = int(input("Inserisci la tua età: "))

if eta < 14:
    biglietto = 10.0
elif eta > 65:
    biglietto = 15.0
else:
    biglietto = 34.0

print(f"In base all'età che hai inserito: {eta} anni, il biglietto costerà: {biglietto} euro.")
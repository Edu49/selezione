"""
Chiedere all'utente il reddito e calcolare le imposte sapendo che
redditi < 15000 aliquota 12%
eccedenze aliquota 22%
"""

reddito = float(input("Inserisci il tuo reddito: "))

if reddito <= 15000:
    tassa = 15000 * 12 / 100
else:
    tassa = 15000 * 12 / 100 + (reddito - 15000) * 22 / 100

print(f"Le imposte che devi pagare sul tuo reddito di {reddito} euro ammontano a: {tassa} euro.")
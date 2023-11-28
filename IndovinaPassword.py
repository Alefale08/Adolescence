password1="ciao"

input1=input("Prova ad indovinare la password.")
if input1==password1:
    print("Bravo hai indovinato.")
    quit()
else:
    input2=input("Vuoi un suggerimento? ").lower()
    if input2 == "si":
        print("La parola è una saluto.")
    else:
        quit()
input3=input("Prova a inserire la password.")
if input3 == password1:
    print("Bravo hai indovinato.")
else:
    input4=input("Vuoi un altro suggerimento?").lower()
    if input4== "si":
        print("Finisce con la ao.")
    else:
        quit()
input5=input("Hai capito la password?").lower()
if input5== "si":
    input6=input("Ultimo tentativo...")
    if input6==password1:
        print("Finalmente ce l'hai fatta.")
    else:
        print("Dopo tutti questi tentativi non ce l'hai fatta.")
else:
    quit()
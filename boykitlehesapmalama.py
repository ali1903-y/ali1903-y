yaş=int(input("Yaşınızı giriniz: "))
boy=float(input("Kilonuzu giriniz: "))
kilo=float(input("Kilonuzu giriniz: "))
bmi= kilo/(boy**2)
print("Beden Vucüt Kitlesi" , round(bmi , 2))             
if bmi<=18.5:
    print("zayıfsınız"),
elif 18.5<=24.9:
    print("Normalsiniz")
elif 25<=29.9:
    print("Fazla kilolusunuz")
else:
    print("Obezsiniz")

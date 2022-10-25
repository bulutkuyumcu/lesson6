"""# Kullanıcıdan boy bilgisi alınız.

# Kullanıcıdan kilo bilgisi alınız.
# Vücut kitle endeksi hesaplayınız ve print format ile yazdırınız.

Kitle Endeks = kg / (boy*boy)

Boy bilgisi metre cinsinden alınmalıdır.

Örnek çıktı : 80 kilo 1.77 boyunda insanın kitle endeksi 25'tir.
Çıktının değerleri örnektir."""


height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bki = weight / (height * height)

print("{} kilosunda {} boyunda kişinin endeksi {}".format(weight,height,bki))
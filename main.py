print("Small Atm System.")

bakiye = 1000
miktar = []


while True:
	print("--- İŞLEMLER ---")
	print("1 - Bakiye Görüntüle ")
	print("2 - Para Yatır ")
	print("3 - Para Çek ")
	print("4 - Çıkış")

	secim = input("Seçiminiz: ")

	if secim == "1":
		print("Bakiyeniz: ", bakiye)
	
	elif secim == "2":
		miktar = int(input("Yatıracağınız Miktarı Giriniz: "))
		print("Para Yatırılıyor..")
		print("Güncel Miktar: ", bakiye + miktar)
	
	elif secim == "3":
		miktar = int(input("Çekeceğiniz Miktar: "))
		print("Kalan Miktar: ", miktar - bakiye)
	
	else:
		print("Çıkış Yapılıyor..")
		break
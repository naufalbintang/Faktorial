while True:
    angka = int(input("Masukkan angka: "))
    data_list = []
    hasil = 1

    if angka != 0:
        while True:
            data_list.append(angka)
            angka -= 1
            
            if angka == 0:
                break
            
        for i in data_list:
            hasil = hasil * i 
        
    else:
        print("Masukkan angka yang valid")

    print(f"{data_list[0]}! = {hasil}")
    
    exit = input("Apakah ingin keluar (y/n)? ")
    if exit.lower() == "y":
        break

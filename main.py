def faktorial(angka):
    '''fungsi untuk menghitung faktorial'''
    hasil = 1
    for i in range(1, angka + 1):
        hasil *= i
    return hasil
    
    
while True:
    angka = int(input('Masukkan angka: '))
    if angka != 0:
        print(f'{angka}! = {faktorial(angka):,.0f}')
    else:
        print('Masukkan angka yang valid!')
    
    # break
    isDone = input('Apakah sudah selesai (y/n)?')
    if isDone.lower() == 'y':
        break
    else:
        None
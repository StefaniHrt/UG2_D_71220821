print(" =============== MAKANAN ===============")
print("1. Telur Bakar   : Rp. 7.000 \n 2. Lele Terbang Mas Bhe  : Rp. 10.000 \n 3. Es Coklat Lempu  : Rp. 5.000 \n 4. Es Doger Langensari   : Rp 13.000")
print("=================== PESANAN ===================")
telur=int(input("Telur Bakar :"))
lele=int(input("Lele Terbang  :"))
coklat=int(input("Es Coklat   :"))
doger=int(input("Es Doger    :"))
htelur=telur*7000
hlele=lele*10000
hcoklat=coklat*5000
hdoger=doger*13000
jumlah=htelur+hlele+hcoklat+hdoger
print(" =============== TOTAL ===============")
print(f"TOTAL TELUR BAKAR x {telur} : Rp {htelur} \n TOTAL LELE TERBANG x {lele} : Rp {hlele} \n TOTAL ES COKLAT x {coklat} : Rp {hcoklat} \n TOTAL ES DOGER x {doger} : Rp {hdoger} \n Jumlah total biaaya yang harus dibayar adalah Rp {jumlah}")

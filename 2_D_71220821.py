no=int(input("Masukkan Nomor Telepon :"))
if no[0:3+1]=="0816":
    print("Anda menggunakan operator indosat")
elif no[0:3+1]=="0814":
    print("Anda menggunakan operator Telkomsel")
else :
    print("Operator anda tidak diketahui")

if a%2==0:
    print("Nomor anda berakhiran genap")
else :
    print("Nomor anda berakhiran ganjil")
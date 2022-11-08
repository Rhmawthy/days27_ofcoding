
#list kelipatan kedua lebih kecil dari 15
angka = [i for i in range (2,15,2)]
print (angka)

# menghapus elemen ke3
print ( 65*"=")
print ("menghapus elemen ke tiga")

angka.remove(4)
print ("update angka",angka)

#sisipkan nilai 5 pada elemen ke tiga
print (65 *"=")
print ("menyisipkan nilai 5 pada elemen ke tiga")

angka.insert(2,5)
print("update angka",angka)

#tampilkan 3 elemen terakhir dari list
print (65 *"=")
print ("menampilkan 3 elemen terakhir dari list")


print ("update angka" , angka[4:])



value1 = {1,2,3,4,5}
value2 = { 3,4,5,6,7}

print(value1|value2)  #union	
print(value1&value2)  #intersection





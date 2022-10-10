sayi= int(input("satir sayisi giriniz:"))
temp1=0
temp2=1
for i in range(sayi):
  temp2+=temp1
  temp1 = temp2-temp1
  print(temp1)
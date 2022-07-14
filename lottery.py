import random
ks=int(input("kaç kolon oynayacaksınız?: "))
kupon=[]
sanslı=set()

for i in range (ks):
    kupon.append(set())
    while len(kupon[i])<6:
        kupon[i].add(random.randint(1,49))

while len(sanslı)<6:
        sanslı.add(random.randint(1,49))
print("ŞANSLI SAYILAR: ")
print(sorted(sanslı))


print("KUPONUNUZ: ")
for i in range (ks):
    print(sorted(kupon[i]))
    print("kaç sayı tuttu: ",6-len((kupon[i]-sanslı)))



 
        
   
    

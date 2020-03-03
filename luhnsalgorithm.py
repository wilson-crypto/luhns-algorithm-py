num = list(input("Enter Credit Card Number: "))

num = list(map(int, num))[::-1] 
# transforming string into int and reverse it

for index in range(1,len(num),2):
    if num[index]<5:
        num[index] = num[index] *2
    else: 
    #doubling number>=5 will give a 2 digit number
        num[index] = ((num[index]*2)//10) + ((num[index]*2)%10)

checksum=sum(num)

print("checksum= {}".format(checksum))

if checksum%10 !=0:
    print('Credit Card Number Not Valid')
else:
    print('Credit Card Number is valid!')
    
# credit card 4137894711755904 is valid 
# credit card 6499802450273568 is invalid
# credit card 8504172191273888 is valid 
# credit card 0043668783485480 is invalid

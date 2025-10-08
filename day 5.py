#the for loop 

for number in range(10):
    print(number* "*")
    
    for numbers in range(10):
        if number %2==0:
            print(number)

            for numbers in range(10):
                if number %2==1:
                    print(number)
#performing the while loop

trial=3
attempt=0

while attempt<trial:
    value=input("Enter the password")
    if value=="umiadzo1236":
        print("log in successfully")
        break
    else:
        print("the password is wrong try again!!")
        attempt+=1
else:
    print("you failed number of attempts are over!!")
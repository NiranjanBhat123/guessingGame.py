import random
print("this game is about finding the mystery number\n")
n = int(input("Enter your guess\n"))
key=random.randint(0,100)
count=0

if(n==key):
    print("congratulations!\n")

else:
    while(n!=key):
        if(n<key):
            print("mystery number is higher")
            n= int(input("try again\n"))
            count= count+1


        elif(n>key):
            print("mystery number is lower")

            n= int(input("try agian\n"))
            count= count+1

print("congratulations!")
print("the mystery number was ",key)
print("you found the mystery number in ",count,"gusses")
with open("highscore.txt","r")as f:
    highscore = int(f.read())

if(count<highscore):
    print("you have broken your record!\n")
    with open("highscore.txt","w") as f:
        f.write(str(count))

else:
    print("oh no! you could not beat your record")







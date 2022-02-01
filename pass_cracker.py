import random as rn

number = int(input("Lütfen Parola giriniz: "))
guess = 0
while (guess != number):
    guess = rn.randint(0,9999)
    print(guess)
print("Parolanız: " + str(number))
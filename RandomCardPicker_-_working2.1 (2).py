import sys
import time
import random


whlste = False
passa = 1
passb = 1
passc = 1
passd = 1

print("--5 Card Dealer--\n\n")

#list of suits
cardsuits = ["of_hearts","of_spades","of_diamonds","of_clubs"]
#list of names
cardnames = ["2_","3_","4_","5_","6_","7_","8_","9_","10_","jack_","queen_","king_","ace_"]

#ignore
slp = random.randint(0,1)
time.sleep(slp)


pickcardsuit = random.choice(cardsuits)
pickcardname = random.choice(cardnames)
cardcombine1 = pickcardname + pickcardsuit
#-----------------------------------
pickcardsuit = random.choice(cardsuits)
pickcardname = random.choice(cardnames)
cardcombine2 = pickcardname + pickcardsuit
#print("cc2Pick1: " + cardcombine2) 

    

#check if cardcombine2 is the same as cardcombine1


if cardcombine2 == cardcombine1:
        whlste = True
else:
    whlste = False
while whlste == True:
    passa = str(passa)
    #print("cc2Pass #" + passa + " " + cardcombine2)
    pickcardsuit = random.choice(cardsuits)
    pickcardname = random.choice(cardnames)
    cardcombine2 = pickcardname + pickcardsuit
    passa = str(passa)
    passa += 1
    if cardcombine2 == cardcombine1:
        whlste = True
    else:
        whlste = False
        

    
    
    

   
#----------------------------------------
pickcardsuit = random.choice(cardsuits)
pickcardname = random.choice(cardnames)
cardcombine3 = pickcardname + pickcardsuit

#print("cc3Pick1: " + cardcombine3) 
#check if cardcombine3 is the same as cardcombine2 or cardcombine1


if (cardcombine3 == cardcombine2) or (cardcombine3 == cardcombine1):
        whlste = True
else:
    whlste = False
while whlste == True:
    passb = str(passb)
    pickcardsuit = random.choice(cardsuits)
    pickcardname = random.choice(cardnames)
    cardcombine3 = pickcardname + pickcardsuit
    #print("cc3Pass #" + passb + " " + cardcombine3)
    passb = int(passb)
    passb += 1
    if (cardcombine3 == cardcombine2) or (cardcombine3 == cardcombine1):
        whlste = True
    else:
        whlste = False
        
    

      
#------------------------------------------
pickcardsuit = random.choice(cardsuits)
pickcardname = random.choice(cardnames)
cardcombine4 = pickcardname + pickcardsuit
#print("cc4Pick1: " + cardcombine4) 

#check if cardcombine4 is the same as cardcombine3 or cardcombine2 or cardcombine1 

if (cardcombine4 == cardcombine3) or (cardcombine4 == cardcombine2) or (cardcombine4 == cardcombine1):
        whlste = True
else:
    whlste = False
while whlste == True:
    passc = str(passc)
    
    pickcardsuit = random.choice(cardsuits)
    pickcardname = random.choice(cardnames)
    cardcombine4 = pickcardname + pickcardsuit
    #print("cc4Pass #" + passc + " " + cardcombine4)
    passc = int(passc)
    passc += 1
    if (cardcombine4 == cardcombine3) or (cardcombine4 == cardcombine2) or (cardcombine4 == cardcombine1):
        whlste = True
    else:
        whlste = False
        
    
           
    
#---------------------------------------------
pickcardsuit = random.choice(cardsuits)
pickcardname = random.choice(cardnames)
cardcombine5 = pickcardname + pickcardsuit
#print("cc5Pick1: " + cardcombine5) 

#check if cardcombine5 is the same as cardcombine4 or cardcombine3 or cardcombine2 or cardcombine1 

if (cardcombine5 == cardcombine4) or (cardcombine5 == cardcombine3) or (cardcombine5 == cardcombine2) or (cardcombine5 == cardcombine1):
        whlste = True
else:
    whlste = False
while whlste == True:
    passd = str(passd)
    
    pickcardsuit = random.choice(cardsuits)
    pickcardname = random.choice(cardnames)
    cardcombine5 = pickcardname + pickcardsuit
    #print("cc5Pass #" + passd + " " + cardcombine5)
    passd = int(passd)
    passd += 1
    if (cardcombine5 == cardcombine4) or (cardcombine5 == cardcombine3) or (cardcombine5 == cardcombine2) or (cardcombine5 == cardcombine1):
        whlste = True
    else:
        whlste = False


#hand1 = cardcombine1 + cardcombine2 + cardcombine3 + cardcombine4 + cardcombine5
#hand2 = cardcombine6 + cardcombine7 + cardcombine8 + cardcombine9 + cardcombine10
#hand2 = cardcombine11 + cardcombine12 + cardcombine13 + cardcombine14 + cardcombine15        
#hand2 = cardcombine16 + cardcombine17 + cardcombine18 + cardcombine19 + cardcombine20    
#hand2 = cardcombine21 + cardcombine22 + cardcombine23 + cardcombine24 + cardcombine25              

#-------------------------------------------

print("Card 1 FINAL: " + cardcombine1)
#Image.open("C:/Users/Jacob/Desktop/Python/Playing Cards/PNG-cards-1.3/" + cardcombine1 + ".png" and "C:/Users/Jacob/Desktop/Python/Playing Cards/PNG-cards-1.3/" + cardcombine2 + ".png").show()


print("Card 2 FINAL: " + cardcombine2)
#Image.open("C:/Users/Jacob/Desktop/Python/Playing Cards/PNG-cards-1.3/" + cardcombine2 + ".png").show()




print("Card 3 FINAL: " + cardcombine3)
#Image.open("C:/Users/Jacob/Desktop/Python/Playing Cards/PNG-cards-1.3/" + cardcombine3 + ".png").show()



print("Card 4 FINAL: " + cardcombine4)
#Image.open("C:/Users/Jacob/Desktop/Python/Playing Cards/PNG-cards-1.3/" + cardcombine4 + ".png").show()




print("Card 5 FINAL: " + cardcombine5)
#Image.open("C:/Users/Jacob/Desktop/Python/Playing Cards/PNG-cards-1.3/" + cardcombine5 + ".png").show()





    
print("\n")

print("Dealing Complete")

input("")
    





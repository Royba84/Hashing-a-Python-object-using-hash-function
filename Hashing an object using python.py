# Hashing a Python object using hash function - Roy Ben Avraham, 12/03/2023 08:03
class SoldierPersonalData:  
    def __init__(self,name,Inumber):  
        self.name = name  
        self.number = Inumber  

#Each soldier has a name and an identifying/private number         
soldier = SoldierPersonalData("Roy",9876543)  
# Calling the hash function and store it in "result"  
result = hash(soldier)
# Print hashing result to the screen  
print(result)  

#Important:
# Note - this hash function is determinstic only within the runtime..
# meaning, if you re-run this code  for the same input, the result will differ.
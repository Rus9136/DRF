from django.test import TestCase


# b = [*a]
# print(b) # [1,2,3,4,5,6]



def printScores(*scores):
   #print(f"Student Name: {student}")
   print(scores)
   # for score in scores:
   #    print(score)


# scores = [1,2,3,4,5,6,'asdf']

# student = 'Jonathan'
printScores("Jonathan", [1,2,3,4,5,6,'asdf'],['ss2'], 'третий параметр')

def printPetNames(owner, *args,**pets):
   fishs =pets.get('scores')
   print(fishs)




#rintPetNames("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], scores= [1,2,3,4,5,6,'grfgyre'])
# mutable, non-duplicates, non-ordering

# listExample = [23, "Okay", True]
# set2Example = set(listExample)

setExample = {12,56,"Test",None}
# set2Example = {12,23,True,False,None,"Bir"}

# print(setExample)
# setExample.add("NewSetElement")
# print(setExample)
# setExample.add("NewSetElement")
# print(setExample)

# print(setExample.difference(set2Example))   # setExample de olub set2Example de olmayani cap edir
# print(set2Example.difference(setExample))   # set2Example de olub setExample de olmayani cap edir
#
# print(setExample.intersection(set2Example))  # bu iki setin kesismesini cap edir
#
# print(setExample.union(set2Example))   # bu iki set i birlesdirir dublicate value yoxdur

# print(setExample)
# setExample.remove(12)    # remove element varsa silir yoxdursa error verir
# print(setExample)
# setExample.discard(12)    #discard element varsa silir yoxdursa hec ne etmir
# print(setExample)
setExample.pop()
print(setExample)
# print(56 in setExample)
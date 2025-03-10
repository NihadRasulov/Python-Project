# d = {}
# print(type(d))
# print(d)
d = {'name': "Javid",'surname':"Aliyev"}

l = (12,34)
new_d = dict(l)

print(d['name'])
d['name'] = 'James'
print(d['name'])

print(d)
d['age'] = 24
print(d)
d['status']=True
print(d)

# 1.ordering
# 2.mutable
# 3.non-duplicate

dict1 = {'items':["item1","item2","item3"],(12,13):"new Item"}
print(dict1)

cities = {(41,39):"Baku",(42,40):"Sumqayit",(38,41):"Guba"}

waschermashine = {(60,60,80):{
                            'model': {
                                'LG':"1500",
                                'Samsung':"1400"}
                            },
                 (60,55,80):"1200"
                }
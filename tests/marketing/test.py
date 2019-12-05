

def test_abc():
    mydict = {}
    ke = []
    value = []
    mobile = '17343057927'
    password = '000000a'
    cid = 'bb235ef3b831c73b4e6a2d2c6651a207e5d4d996d0131e6d31d766f0c899d54e'
    platform = '2'
    did = '422EBA49-CC64-407C-A57D-9BA9501F3D79'


    ke.append(mobile)



    key = ['mobile','password','cid','platform','did']
    list =[mobile,password,cid,platform,did]
 #   print(list)
    for i in range(len(key)):
        for j in range(len(list)):
            if i == j:
                mydict[key[i]]= list[j]
             #   print(mydict)

    print(mydict)






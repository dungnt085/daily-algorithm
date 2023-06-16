def int_to_roman(num:int) -> str:
    romap = [["M",1000],
               ["CM",900],
               ["D",500],
               ["CD",400],
               ["C",100],
               ["XC",90],
               ["L",50],
               ["XL",40],
               ["X",10],
               ["IX",9],
               ["V",5],
               ["IV",4],
               ["I",1],
               ]
    res = ""
    for key, val in romap:
        if num // val:
            count = num//val
            res += key*count
            num = num%val


    return res

num = 1213
res = int_to_roman(num)
print(res)
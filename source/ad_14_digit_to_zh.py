
case = [
  0,
  10,
  100,
  6,
  14,
  104,
  1004,
  10004,
  253245,
  1845692
]


def transfer(num):
    basic = {0:'零',1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九'}
    item = {0:'',1:'十',2:'百',3:'千'}
    item2 = {0:'',1:'万',2:'亿',3:'兆'}
    res = ''
    c = 0
    if num < 0 :
        return False

    if 0 <= num < 10:
        return basic[num]

    while num:
        v = num % 10
        if c//4 and c%4 == 0:
            res = item2[c//4] + res

        if v != 0:
            res = item[c%4] + res

        if v != 0 or (not res) or (v == 0 and res[0] != '零'):
            res = basic[v] + res

        num //= 10
        c += 1
        
    return res

for i in case:
    print(i,transfer(i))

#Dominik Zimny
#25/10/2019
def true(bi):
    bi="1"+bi
    return bi

def false(bi):
    bi="0"+bi
    return bi

num=int(input())
bi=""
if num % 2 != 0:
    bi=true(bi)
else:
    bi=false(bi)
if  num % 4 <2:
    bi=true(bi)
else:
    bi=false(bi)
if num % 8 <4:
    bi=true(bi)
else:
    bi=false(bi)
if num % 16 <8:
    bi=true(bi)
else:
    bi=false(bi)
if num % 32 <16:
    bi=true(bi)
else:
    bi=false(bi)
if num % 64 < 32:
    bi=true(bi)
else:
    bi=false(bi)
if num % 128 < 64:
    bi=true(bi)
else:
    bi=false(bi)
if num % 256 < 128:
    bi=true(bi)
else:
    bi=false(bi)
print(bi)







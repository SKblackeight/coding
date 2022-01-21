file = open('t.png', 'rb')
magic = file.read(16)
a = magic.hex()
print (a[0:2])

b = a[0:2]
if b == '89' or b== 'FF':
    print ("사진파일입니다")
#89=png, FF=jpg
else:
    print ("삭제해라")

    


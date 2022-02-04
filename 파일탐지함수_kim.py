def hello(temp):
    for i in temp:
        file = open(i, 'rb')
        magic = file.read(16)
        b = magic.hex()
        print (b[0:2])

        c = b[0:2]
        if c == '89' or c== 'FF' or c=='ff':
            print ("사진파일입니다")
        else:
            print ("삭제해라")


# def hello2(i):

#     file = open(i, 'rb')
#     magic = file.read(16)
#     b = magic.hex()
#     print (b[0:2])

#     c = b[0:2]
#     if c == '89' or c== 'FF':
#         print ("사진파일입니다")
#     else:
#         print ("삭제해라")



if __name__ == "__main__":
    li=['a.png', 'b.jpg']
    hello(li)
    # hello2('change.png')
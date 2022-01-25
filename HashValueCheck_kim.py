# #-----1 해시값 추출 -----
# import hashlib

# hash = hashlib.md5()
# afile = open('t.png', 'rb')
# buf = afile.read()
# a = hash.update(buf)
# print(str(hash.hexdigest()))

# # print(buf)

# #-----2 두 파일 해시값 비교 -----


# import hashlib

# digests = []
# for filename in ['t.png', 'a.jpg']:
#     hasher = hashlib.md5()
#     with open(filename, 'rb') as f:
#         buf = f.read()
#         hasher.update(buf)
#         a = hasher.hexdigest()
#         digests.append(a)
#         print(a)

# print(digests[0] == digests[1])


#-----3 리스트로 받아오는 코드 -----
import hashlib

def hashcheck(temp):
    for filename in temp:
        hasher = hashlib.md5()
        with open(filename, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
            a = hasher.hexdigest()
            print(a)



if __name__ == "__main__":
    li=['t.png', 'a.jpg']
    hashcheck(li)
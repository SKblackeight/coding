import hashlib

hash = hashlib.md5()
afile = open('t.png', 'rb')
buf = afile.read()
a = hash.update(buf)
print(str(hash.hexdigest()))

# print(buf)

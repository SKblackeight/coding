import hashlib
import os, shutil

a_list =[]
a_name = []

directory = 'address_localPC'
for path, dirs, files in os.walk(directory):
    for names in files:
        filedir = os.path.join(path,names)
        afile = open(filedir, 'rb')
        buf = afile.read()

        filename, fileExtension = os.path.splitext(names)

        hash = hashlib.sha256()
        hash.update(buf)

        a = str(hash.hexdigest())
        a_hash = "".join(a)
        a_list.append(a_hash)
        
        a_filename = str(filename+fileExtension)
        a_hash_name = "".join(a_filename)
        a_name.append(a_hash_name)


x = {'hash': a_list, 'filename': a_name}
print(x)
     
b_list=[]
b_name=[]
directory_compare = 'address_database'
for root, dirs, files in os.walk(directory_compare):
    for names in files:
        
        filedir = os.path.join(root,names)
        afile = open(filedir, 'rb')
        buf = afile.read()
        filename, fileExtension = os.path.splitext(names)
        hash = hashlib.sha256()
        hash.update(buf)
        b =str(hash.hexdigest())
        m = "".join(b)
        b_list.append(m)

        b_filename = str(filename+fileExtension)
        b_hash_name = "".join(b_filename)
        b_name.append(b_hash_name)


y = {'hash': b_list, 'filename': b_name}
print(y)


# os.mkdir("address")  
for xx in x['hash'] :
    for xxx in x['filename']:
        for yy in y['hash']:
            for yyy in y['filename']:
                if xx == yy:
                    print(xxx)
                    file_destination = 'address'
                    shutil.move(directory + xxx, file_destination)
                else:
                    print("no way")

                break
            break
        break
    break
# shutil.rmtree('address')

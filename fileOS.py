import sys
print(sys.getdefaultencoding())


with open('test copy.txt','rb') as f:
    # lines=[line.strip() for line in f]
    data=f.read(10)
    print(data)
    print(f.tell())
    print (f.seek(15))
    
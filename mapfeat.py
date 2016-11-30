#!/usr/bin/python

class Attribute:
    def __init__(self, _type, _name):
        self.type = _type
        self.name = _name
        self.values = []
    def add(self, _value):
        self.values.append(_value)
    def removeDuplicates(self):
        self.values = list(set(self.values))

def load_data( fname ):
    attrs = []
    cnt = 0
    cmap = set([2,3,7,8,10,11,14,16,19,21,23,24,26,27,28,31])

    #NOTICE:there is no '.' in the data file
    for l in open( fname ):
        cnt = cnt + 1
        l.strip('\n')
        l.strip('\r')
        arr = l.split(',')
        
        #the first line is name
        if cnt == 1:
            for i in range(0, 32):
                #only two types of attribute
                if i in cmap:
                    attrs.append(Attribute(1, arr[i+2]))
                else:
                    attrs.append(Attribute(0, arr[i+2]))
            continue;
        for i in range(0, 32):
            #sum the values of class property
            if attrs[i].type == 0:
                continue
            attrs[i].add(arr[i+2])
    for i in range(0, 32):
        attrs[i].removeDuplicates()
    return attrs

def write_featmap( fo, attrs ):
    cnt = 0
    for i in range(0, 32):
        if attrs[i].type == 1:
            continue
        fo.write('%d\t%s\tint\n' % (cnt, attrs[i].name) )
        cnt = cnt + 1
    for i in range(0, 32):
        if attrs[i].type == 0:
            continue
        for j in range(0, len(attrs[i].values)):
            fo.write('%d\t%s=%s\ti\n' % (cnt+j, attrs[i].name.strip(), attrs[i].values[j].strip()) )
        cnt = cnt + len(attrs[i].values)    

#find out the int columns and class columns, and the possiblities of a class column
attrs = load_data( 'data/train.csv' )
fo = open( 'featmap.txt', 'w' )
write_featmap( fo, attrs)
fo.close()

#here we deal with the train file
fo = open( 'car.txt', 'w' )
ln = 0
for l in open( 'data/train.csv' ):
    ln = ln + 1
    if ln == 1:
        continue
    l.strip('\n')
    l.strip('\r')
    arr = l.split(',')
    fo.write(arr[1])
    cnt = 0
    for i in range(0, 32):
        if attrs[i].type == 1:
            continue;
        fo.write( ' %d:%s' % (cnt, arr[i+2]) )
        cnt = cnt + 1
    for i in range(0, 32):
        if attrs[i].type == 0:
            continue
        for j in range(0, len(attrs[i].values)):
            if attrs[i].values[j] == arr[i+2]:
                fo.write(' %d:1' % (cnt+j) )
                break
        cnt = cnt + len(attrs[i].values)    
    fo.write('\n')
fo.close()

#here we deal with the test file
fo = open( 'car.txt.test', 'w' )
ln = 0
for l in open( 'data/test.csv' ):
    ln = ln + 1
    if ln == 1:
        continue
    l.strip('\n')
    l.strip('\r')
    arr = l.split(',')
    fo.write("0")
    # fo.write(arr[1])
    cnt = 0
    for i in range(0, 32):
        if attrs[i].type == 1:
            continue;
        fo.write( ' %d:%s' % (cnt, arr[i+1]) )
        cnt = cnt + 1
    for i in range(0, 32):
        if attrs[i].type == 0:
            continue
        for j in range(0, len(attrs[i].values)):
            if attrs[i].values[j] == arr[i+1]:
                fo.write(' %d:1' % (cnt+j) )
                break
        cnt = cnt + len(attrs[i].values)    
    fo.write('\n')
fo.close()


'''use this script to produce a txt file readable by edmpickevents:
   -usage from a txt file: python EventSelect.py [txtfilename]
   -(to be developped)usage from input (=copy-paste): python EventSelect.py '''
import sys


def getStringFromFile(txtfilename):
    myfile = open(txtfilename,"r")
    data = myfile.readlines()
    return data
    

def convertStringToScheme(data):
    for i in range(3):
        data.pop(0)
    data.pop()
    newdata = []
    for chain in data:
        newdata.append(chain.replace(' ','').replace('\n','').replace('*',' ').split())
    finaldata = []
    for chain in newdata:
        chain.pop(0)
        finaldata.append(':'.join(chain))
    return finaldata

def writetxtfile(data):
    myfile = open('selectedEvents.txt','w')
    last = data[len(data)-1]
    for ev in data:
        if ev!=last:
            myfile.write(ev+'\n')
        else:
            myfile.write(ev)
    myfile.close()

if __name__ == '__main__':

    if len(sys.argv)==2:
        txtfilename = str(sys.argv[1])
        rawdata = getStringFromFile(txtfilename)
    # if len(sys.argv)==1:
    #     rawdata = input('paste scan table here: ')
    #     import pdb;pdb.set_trace()
    data = convertStringToScheme(rawdata)
    writetxtfile(data)

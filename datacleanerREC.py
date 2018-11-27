# tool to clean peeif data for python script
# works with final.txt for PEEIF project
# this script derives REC data

count = 0
# load file

f = open('final.txt', 'r')
w = open('recData.txt', 'w')

# read first line to create header
line = f.readline()

# need size, meter number, annual use and age
# final.txt has year built - from 2016 for age

lineList = line.split(',')
print (lineList[17],lineList[63],lineList[6], lineList[64])
w.write("Size, Name, Age, Use\n")

# loop through each line and extract relevant data
# need size, meter number, annual use and age
# final.txt has year built - from 2016 for age

for nextLine in f:
    thisLine = nextLine.split(',')
    try:
        y = thisLine[6].strip()
        age = 2016 - int(y)
        x = thisLine[63].strip("0")
        z = thisLine[64].strip("0") 
        meter = x.strip(".")
        use = z.strip(".")
    except:
        count = count + 1
        
# only record data if it is a relevant data point (REC House)

    if float(thisLine[17]) > 0 and bool(meter) == True:
        dataList = [thisLine[17], meter, str(age), use]
        print (dataList)
        csv = ','.join(dataList)
        w.write(csv)
        w.write('\n')
        csv = ''
        

# close data files

f.close()
w.close()


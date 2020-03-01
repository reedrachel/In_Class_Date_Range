import sys,time,os,json,datetime,operator

#SELECT * FROM cddata WHERE Date >= 2019-01-01 and Date <= 2019-01-02
#append all json strings to new file called output.txt

dateCount = {}

outfile = open("Output.txt", 'w')
for root,dirs,files in os.walk('data'):
    #print(root,dirs,files)
    path = root.split(os.sep)
    for fn in files:
        fp = root+os.sep+fn
        print(fp)
        f = open(fp, 'r')
        for line in f:
            data = json.loads(line)
            payload = data['payload']
            payload = json.loads(payload)
            #print(payload['received'])
            k =payload['received'].split('T')[0]
            if k == '2019-01-01' or k == '2019-01-02':
                print(k)
                outfile.write(str(data))

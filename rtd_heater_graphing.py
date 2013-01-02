f = open('heater_rtd_test.txt','r')
file = f.read()
f.close()

#Skip the first 5 lines with status information
n = 0
for i in range(0,5):
    n = file.find('\n',n+1)

#Split the files into separate lines
file = file[n+1:].split('\n')

row = file[2]

print row.split('\t')
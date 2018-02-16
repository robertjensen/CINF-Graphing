backend = 'agg'
import csv
from datetime import datetime
from dateutil.parser import parse
import matplotlib.pyplot as plt
import defaults as d
import numpy as np

fig = plt.figure()
#fig.subplots_adjust(left=0.1)
#fig.subplots_adjust(bottom=d.bottom_room)
#fig.subplots_adjust(top=1-d.bottom_room)
#fig.subplots_adjust(right=d.right_room*1.08) 
#fig.subplots_adjust(wspace=0.25)
#fig.subplots_adjust(hspace=0.25)

ratio = d.ratio
fig_width = d.width
fig_width = fig_width /2.54     # width in cm converted to inches
fig_height = fig_width*ratio
#fig.set_size_inches(fig_width,fig_height)

rows = []
with open('wind.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        for i in range(0, len(row)):
            row[i] = row[i].replace(',','.')
        rows.append(row)
print(rows[0][00:35])
print(rows[1][00:35])
print(rows[5][0])
for i in range(3, len(rows)):
    rows[i][0] = datetime.strptime(rows[i][0], "%Y-%m-%d %H:%M:%S")

data = np.array(rows[3:8000])
time_data = data[:,0]
nummeric_data = data[:,1:]

x_size, y_size = nummeric_data.shape
for i in range(0, x_size):
    for j in range(0, y_size):
        if nummeric_data[i, j] == '':
            nummeric_data[i, j] = 'NaN'
nummeric_data = nummeric_data.astype(np.float)

axis = fig.add_subplot(1,1,1)
#axis.plot(time_data, nummeric_data[:,30], 'r-',label="Offshore - DK1")
#axis.plot(time_data, nummeric_data[:,31], 'g-',label="Offshore - DK2")
#axis.plot(time_data, nummeric_data[:,32], 'k-',label="Onshore - DK1")
#axis.plot(time_data, nummeric_data[:,33], 'c-',label="Onshore - DK2")
axis.plot(time_data,
          nummeric_data[:,30] +
          nummeric_data[:,31] +
          nummeric_data[:,32] +
          nummeric_data[:,33], 'k-',label="Total")

axis.legend(loc = 2,prop={"size":8})

#axis.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize,axis='both',pad=d.pad)
#axis.set_ylabel('Power / W', fontsize=d.y_axis_font)
#axis.set_xlabel('Temperature / C', fontsize=d.x_axis_font)




#plt.tight_layout()
plt.show()
#plt.savefig('power_versus_temp.png',dpi=300)



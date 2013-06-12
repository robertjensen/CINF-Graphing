#backend = 'agg'
execfile('std_header.py')
from scipy import optimize


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
fig.set_size_inches(fig_width,fig_height)


data = {}
#data[60]   = np.array([[1350,-10,11],[1400,8,26],[1425,16,32],[1450,23,39],[1475,30,45],[1500,36,50],[1525,42,56],[1550,48,61],[1650,69,80],[1750,87,97],[2000,125,133],[2500,186,193],[3000,237,243],[4000,324,328],[5000,399,403]])
data[100]  = np.array([[1350,-19,17],[1400,1,31],[1425,10,37],[1450,17,43],[1475,25,49],[1500,31,54],[1525,37,60],[1550,43,65],[1600,55,74],[1650,65,83],[1750,83,100],[2000,122,136],[2250,155,167],[2500,184,195],[3000,235,245],[3500,281,289],[4000,322,330],[4500,361,368],[5000,397,404],[5500,432,439],[6000,466,472],[6500,498,505],[7000,530,536],[7500,560,566],[8000,590,596]])
#data[200]  = np.array([[1400,-19,43],[1425,-8,49],[1450,1,54],[1475,10,60],[1500,17,65],[1525,25,70],[1550,31,74],[1650,55,92],[1750,74,108],[2000,115,142],[2500,178,200],[3000,230,249],[4000,318,334],[5000,394,408]])
#data[500]  = np.array([[1550,-19,100],[1650,17,115],[1750,43,129],[2000,92,161],[2500,161,216],[3000,216,263],[4000,306,346],[5000,383,419]])
#data[1000] = np.array([[2000,43,189],[2500,129,240],[3000,190,285],[4000,285,364],[5000,365,436]])

brightness_data = {}
brightness_data[2000] = np.array([[50,126,132],[100,122,136],[150,119,139],[200,115,142],[250,111,146],[300,108,149],[400,100,155],[500,92,161],[750,70,176],[1000,43,189],[1200,17,200],[1300,1,205]])


axis_array = []
axis = fig.add_subplot(1,1,1)

#range = np.arange(1200,9500)
#fitfunc = lambda p, x: p[0]*((x-p[2])**0.5)+p[1]       # Target function
#errfunc = lambda p, x, y: fitfunc(p, x) - y # Distance to the target function
#p0 = [8,130,990] # Initial guess for the parameters
#p1, success = optimize.leastsq(errfunc, p0[:], args=(data[100][:,0],data[100][:,1]+273),maxfev=10000)
#print p1, success
#axis.plot(range,p1[0]*((range-p1[2])**0.5)+p1[1],'r-')

#p2, success = optimize.leastsq(errfunc, p0[:], args=(data[100][:,0],data[100][:,2]+273),maxfev=10000)
#print p2, success
#axis.plot(range,p2[0]*((range-p2[2])**0.5)+p2[1],'r--')

#d_100 = (data[100][:,2] + data[100][:,1])/2.0
#p3, success = optimize.leastsq(errfunc, p0[:], args=(data[100][:,0],d_100+273),maxfev=10000)
#print p3, success
#axis.plot(range,p3[0]*((range-p3[2])**0.5)+p3[1],'r--')


#axis.plot(data[60][:,0], data[60][:,1], 'r-')
#axis.plot(data[60][:,0], data[60][:,2], 'r--')
#axis.plot(data[60][:,0], (data[60][:,2]+data[60][:,1])/2.0, 'r--')

#axis.plot(data[100][:,0], data[100][:,1]+273, 'b.')
#axis.plot(data[100][:,0], data[100][:,2]+273, 'bo')
#axis.plot(data[100][:,0], (data[100][:,2]+data[100][:,1])/2.0+273, 'b--')

#axis.plot(data[200][:,0], data[200][:,1], 'g-')
#axis.plot(data[200][:,0], data[200][:,2], 'g--')
#axis.plot(data[200][:,0], (data[200][:,2]+data[200][:,1])/2.0, 'c--')

#axis.plot(data[500][:,0], data[500][:,1], 'k-')
#axis.plot(data[500][:,0], data[500][:,2], 'k--')
#axis.plot(data[500][:,0], (data[500][:,2]+data[500][:,1])/2.0, 'k--')

#axis.plot(data[1000][:,0], data[1000][:,1], 'c-')
#axis.plot(data[1000][:,0], data[1000][:,2], 'c--')
#axis.plot(data[1000][:,0], (data[1000][:,2]+data[1000][:,1])/2.0, 'c--')

#axis.set_xticks([2.5,5,7.5,10,12.5,15,17.5,20,25,30,35])

#axis.legend(loc = 2,prop={"size":8})


axis.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize,axis='both',pad=d.pad)
"""
axis.set_xlabel('Brightness', fontsize=d.y_axis_font)
axis.set_ylabel('Temperature / C', fontsize=d.x_axis_font)
axis.set_xscale('log')
axis.set_yscale('log')
axis.set_ylim(220,900)
axis.set_xlim(1200,9000)
"""

axis.plot(brightness_data[2000][:,0], brightness_data[2000][:,1]+273, 'b.')
axis.plot(brightness_data[2000][:,0], brightness_data[2000][:,2]+273, 'bo')
axis.plot(brightness_data[2000][:,0], (brightness_data[2000][:,2]+brightness_data[2000][:,1])/2.0+273, 'b--')

axis.set_xlabel('Contrast', fontsize=d.y_axis_font)
axis.set_ylabel('Temperature / C', fontsize=d.x_axis_font)
#axis.set_ylim(220,900)
#axis.set_xlim(1200,9000)


#plt.tight_layout()
plt.show()
#plt.savefig('power_versus_temp.png',dpi=300)

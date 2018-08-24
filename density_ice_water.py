backend = 'agg'

exec(open("std_header.py").read())
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
# https://www.engineeringtoolbox.com/ice-thermal-properties-d_576.html
data['ice'] = np.array([[-100, 925.7], [-90, 924.9], [-80, 924.1], [-70, 923.3], [-60, 922.4], [-50, 921.6], [-40, 920.8], [-35, 920.4], [-25, 919.6], [-20, 919.4], [-15, 919.4], [-10, 918.9], [-5, 917.5], [0, 916.2]])
# https://www.simetric.co.uk/si_water.htm
# https://www.engineeringtoolbox.com/water-density-specific-weight-d_595.html
data['water'] = np.array([[0.1, 0.999847], [0.5, 0.999872], [1, 0.99990], [2, 0.999941], [3, 0.999965], [4, 0.999973], [5, 0.999965], [6, 0.999941], [7, 0.999902], [8, 0.999849], [9, 0.999781], [10, 0.9997000], [15, 0.9991026], [20, 0.9982067], [30, 0.9956488], [40, 0.9922152], [50, 0.98804], [60, 0.9832], [75, 0.97484], [80, 0.9718], [100, 0.95835]])

axis_array = []

axis = fig.add_subplot(1,1,1)

axis.plot(data['ice'][:,0], data['ice'][:,1]/1000, '-', label="Is")
axis.plot(data['water'][:,0], data['water'][:,1], '-', color='orange', label="Vand")
axis.plot(data['water'][0:12,0], data['water'][0:12,1], '-', color='chocolate', label="Vand")
#axis.set_ylim(0,15)
#axis.set_xlim(0,305)
#axis.set_xticks([2.5,5,7.5,10,12.5,15,17.5,20,25,30,35])

#axis.legend(loc = 2,prop={"size":8})

axis.tick_params(direction='in', length=d.ticklength, width=1, colors='k',
                 labelsize=d.labelsize,axis='both',pad=d.pad)
axis.set_ylabel('Densitet / g/cm$^3$', fontsize=d.y_axis_font)
axis.set_xlabel('Temperatur / C', fontsize=d.x_axis_font)

a = plt.axes([.25, .65, .2, .15], axisbg='w')
a.plot(data['water'][0:12,0], data['water'][0:12,1], '-', color='chocolate')
a.tick_params(direction='in', length=d.ticklength, width=1, colors='k',
              labelsize=d.labelsize-1,axis='both',pad=d.pad)
plt.setp(a, xlim=(0, 10), ylim=(0.9996, 1.00),xticks=[2, 4, 6, 8, 10],
         yticks=[0.9997, 0.9998, 0.9999])


#plt.tight_layout()
#plt.show()
plt.savefig('vand_tthed.png',dpi=300)

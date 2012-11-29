backend = 'agg'
execfile('std_header.py')

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
data['vac'] = np.array([[40,0.85],[100,2.9],[150,4.4],[200,6.2],[250,8.6],[300,13.3],[350,24]])
data['atm'] = np.array([[40,1.5],[100,7],[150,10.7],[200,14.9],[250,19.1],[350,34.9]])
data['ins'] = np.array([[40,0.3],[80,1.3],[100,1.7],[125,2.3],[150,3.2],[175,4],[200,5.2],[225,6.3],[250,7.5],[275,9.5],[300,12.5],[325,18.4]])
data['cut'] = np.array([[40,0.3],[80,1.0],[100,1.4],[125,1.9],[150,2.5],[175,3.3],[200,4.1],[225,5],[250,6.1],[275,7.5],[300,9.4],[325,12.0],[350,15.7]])

axis_array = []

axis = fig.add_subplot(1,1,1)

axis.plot(data['vac'][:,0], data['vac'][:,1], 'r.',label="Vacuum")
axis.plot(data['atm'][:,0], data['atm'][:,1], 'b.',label="Air")
axis.plot(data['ins'][:,0], data['ins'][:,1], 'k.',label="Double bonded")
axis.plot(data['cut'][:,0], data['cut'][:,1], 'g.',label="Cut through Si")
axis.set_ylim(0,15)
axis.set_xlim(0,305)
#axis.set_xticks([2.5,5,7.5,10,12.5,15,17.5,20,25,30,35])

axis.legend(loc = 2,prop={"size":8})

axis.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize,axis='both',pad=d.pad)
axis.set_ylabel('Power / W', fontsize=d.y_axis_font)
axis.set_xlabel('Temperature / C', fontsize=d.x_axis_font)




#plt.tight_layout()
plt.show()
#plt.savefig('power_versus_temp.png',dpi=300)

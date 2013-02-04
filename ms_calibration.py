#backend = 'agg'
execfile('std_header.py')
from scipy import optimize

fig = plt.figure()
fig.subplots_adjust(left=0.1)
fig.subplots_adjust(bottom=d.bottom_room)
fig.subplots_adjust(top=1-d.bottom_room)
fig.subplots_adjust(right=d.right_room*1.08) 
fig.subplots_adjust(wspace=0.25)
fig.subplots_adjust(hspace=0.25)

ratio = d.ratio*1.1
#fig_width = d.width
fig_width = 13
fig_width = fig_width /2.54     # width in cm converted to inches
fig_height = fig_width*ratio
fig.set_size_inches(fig_width,fig_height)


#Get Mass-spectrums
spectrums = {}
integrations_28 = {}
integrations_40 = {}
initial_spectrum = 3149

cursor.execute("SELECT unix_timestamp(time) FROM measurements_microreactorNG where id = 3121")
timestamp = np.array(cursor.fetchall())
start_time = timestamp[0]

for i in range(0,10):
    #print str(config.temperatures[i]) + " " + str(i + config.initial_db)
    cursor.execute("SELECT x,y*1e9 FROM xy_values_microreactorNG where measurement = " + str(i + initial_spectrum))
    spectrums[i] = np.array(cursor.fetchall())
    cursor.execute("SELECT unix_timestamp(time) FROM measurements_microreactorNG where id = " + str(i + initial_spectrum))
    timestamp = np.array(cursor.fetchall())
    print timestamp[0]-start_time
    
    #print len(spectrums[i][:,0])
    
    x_values = spectrums[i][20:40,0]
    y_values = spectrums[i][20:40,1]
    y_values = y_values - min(y_values)
    fitfunc = lambda p, x: p[0]*math.e**(-1*((x-p[2])**2)/p[1])       # Target function
    errfunc = lambda p, x, y: fitfunc(p, x) - y # Distance to the target function
    p0 = [0.1,1,28] # Initial guess for the parameters
    p1, success = optimize.leastsq(errfunc, p0[:], args=(x_values, y_values),maxfev=1000)
    if success>1:
        print i
    integrations_28[i] = p1[0] * math.sqrt(p1[1])


data = {}
#M28
cursor.execute("SELECT x/60000,y*1e9 FROM xy_values_microreactorNG where measurement = 3121")
data['M28'] = np.array(cursor.fetchall())
#M40
cursor.execute("SELECT x/60000,y*1e9 FROM xy_values_microreactorNG where measurement = 3123")
data['M40'] =  np.array(cursor.fetchall())

#axis_array = []
axis = fig.add_subplot(1,1,1)


#axis.plot(x_values,y_values,'r-')
#X_values = np.arange(2700,2900)/100.0
#axis.plot(X_values,fitfunc(p1, X_values),'b-')


axis.plot(data['M28'][:,0]/60.0, data['M28'][:,1], 'r-')
axis.plot(data['M40'][:,0]/60.0, data['M40'][:,1], 'g-')
#axis.set_ylim(0.2,100)
#axis_array[i].set_xlim(1100,0)

axis.tick_params(direction='in', length=d.ticklength, width=2, colors='k',labelsize=d.labelsize,axis='both',pad=d.pad)
    
axis.set_ylabel('Ion Current / nA', fontsize=d.y_axis_font)
axis.set_xlabel('Time / Hours', fontsize=d.x_axis_font)


#axis2 = axis.twinx()
#axis2.plot(data['TEMPERATURE'][:,0], data['TEMPERATURE'][:,1], 'b-')
#axis2.set_ylabel('Temperature / $^\circ$C', fontsize=d.y_axis_font)

#arrow = dict(facecolor='black',arrowstyle='->')
#axis.annotate('CO', xy=(200, 12),  xycoords='data', xytext=(110, 5), textcoords='data', arrowprops=arrow, horizontalalignment='right', verticalalignment='center',fontsize=d.arrowfont,)
#axis.annotate('CO$_2$', xy=(200, 0.7),  xycoords='data', xytext=(300, 1.4), textcoords='data', arrowprops=arrow, horizontalalignment='right', verticalalignment='center',fontsize=d.arrowfont,)
#axis.annotate('Temp', xy=(420, 35),  xycoords='data', xytext=(540, 60), textcoords='data', arrowprops=arrow, horizontalalignment='right', verticalalignment='center',fontsize=d.arrowfont,)


#plt.tight_layout()
plt.show()
#plt.savefig('dibenzothiophene_optimized.png',dpi=900)

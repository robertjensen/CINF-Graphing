backend = 'agg'
execfile('std_header.py')

#Mass of NH3: 17.0265491
#Mass of OH: 17.0027397

def MassToTime(mass):
    #time =  2.97122929 * (mass**0.5)
    time =  2.9671 * (mass**0.5)   
    corr_time = time + 0.17
    return corr_time 

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


data = {}
#Methanol + oxygen
cursor.execute("SELECT x*1000000,y*1000 FROM xy_values_tof where measurement = 1166")
data['rt'] = np.array(cursor.fetchall())

cursor.execute("SELECT x*1000000,y*1000 FROM xy_values_tof where measurement = 1171")
data['350'] = np.array(cursor.fetchall())

axis_array = []

LINEWIDTH = 0.5
arrow = dict(facecolor='black',arrowstyle='->')
font = d.arrowfont

gs = gridspec.GridSpec(2, 3)
#gs.update(wspace=0.6,hspace=0.7)

axis = plt.subplot(gs[0, :])

axis.plot(data['rt'][:,0], data['rt'][:,1], 'r-',linewidth=LINEWIDTH)
axis.plot(data['350'][:,0], data['350'][:,1], 'b-',linewidth=LINEWIDTH)
axis.set_xlim(0,29)
axis.set_xticks([5,10,15,20,25])

mass_ticks = np.array([1,2,5,10,15,20,30,40,50,60,70,80])

axis3 = axis.twiny()
axis3.set_xlim(0,29)
axis3.set_xticks(MassToTime(mass_ticks))
axis3.set_xticklabels(mass_ticks)
axis3.set_xlabel('Mass / amu', fontsize=d.x_axis_font)
axis3.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize-1,axis='both',pad=d.pad)
#axis3.ticklabel_format(useOffset=False)
axis.set_yticks((0,5,10,15,20))
axis.set_ylim(-1,25)

p = axis.axvspan(18.5, 21, facecolor='#26aaf7', alpha=0.25)
p = axis.axvspan(21.8, 23.5, facecolor='#25dd37', alpha=0.25)
p = axis.axvspan(26.6, 28.1, facecolor='#b6fa77', alpha=0.25)


axis.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize,axis='both',pad=d.pad)
#axis.set_ylabel('Response / mV', fontsize=d.y_axis_font)
axis.set_ylabel('')
#axis.set_xlabel('Flight Time / $\mu$s', fontsize=8)
axis.set_xlabel('')



axis = plt.subplot(gs[1,0])
#axis.set_ylabel('Response / mV', fontsize=d.y_axis_font)
axis.set_ylabel('')
axis.set_yticks((2.5,5,7.5))
axis.plot(data['rt'][:,0], data['rt'][:,1], 'r-',linewidth=LINEWIDTH)
axis.plot(data['350'][:,0], data['350'][:,1], 'b-',linewidth=LINEWIDTH)
p = axis.axvspan(18.5, 21, facecolor='#26aaf7', alpha=0.25)
axis.set_xlim(18.5,21)
axis.set_ylim(-0.2,10)
axis.set_xticks([19,19.5,20,20.5])
axis.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize,axis='both',pad=d.pad)
axis3 = axis.twiny()
mass_ticks = np.array([40,42,44,46,48])
axis3.set_xlim(18.5,21)
axis3.set_xticks(MassToTime(mass_ticks))
axis3.set_xticklabels(mass_ticks)
axis3.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize-1,axis='both',pad=d.pad)



axis = plt.subplot(gs[1,1])
axis.set_ylabel('')
axis.plot(data['rt'][:,0], data['rt'][:,1], 'r-',linewidth=LINEWIDTH)
axis.plot(data['350'][:,0], data['350'][:,1], 'b-',linewidth=LINEWIDTH)
axis.set_xticks([22,22.5,23])
p = axis.axvspan(21.8,23.5, facecolor='#25dd37', alpha=0.25)
axis.set_xlim(21.8,23.5)
axis.set_ylim(-0.2,22)
axis.set_yticks([5,10,15,20])
axis.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize,axis='both',pad=d.pad)
axis.ticklabel_format(useOffset=False)
#axis.annotate('H', xy=(3.2, 10),  xycoords='data', xytext=(3.52, 17), textcoords='data', arrowprops=arrow, horizontalalignment='right', verticalalignment='top',fontsize=font,)
#axis.annotate('H$_2$', xy=(4.35, 10),  xycoords='data', xytext=(4.2, 20), textcoords='data', arrowprops=arrow, horizontalalignment='right', verticalalignment='top',fontsize=font,)
axis.set_xlabel('Flight Time / $\mu$s', fontsize=d.x_axis_font)
axis3 = axis.twiny()
mass_ticks = np.array([54,56,58,60])
axis3.set_xlim(21.8,23.5)
axis3.set_xticks(MassToTime(mass_ticks))
axis3.set_xticklabels(mass_ticks)
axis3.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize-1,axis='both',pad=d.pad)

axis = plt.subplot(gs[1,2])
axis.set_ylabel('')
axis.plot(data['rt'][:,0], data['rt'][:,1], 'r-',linewidth=LINEWIDTH)
axis.plot(data['350'][:,0], data['350'][:,1], 'b-',linewidth=LINEWIDTH)
axis.set_xlim(26.5,28.1)
axis.set_ylim(-1,22)
axis.set_xticks([27,27.5,28])
axis.set_yticks((5,10,15,20))
axis.ticklabel_format(useOffset=False)
p = axis.axvspan(26.5, 28.1, facecolor='#b6fa77', alpha=0.25)
axis.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize,axis='both',pad=d.pad)
#axis.annotate('O', xy=(12.04, 10),  xycoords='data', xytext=(12.05, 69), textcoords='data', arrowprops=arrow, horizontalalignment='right', verticalalignment='top',fontsize=font,)
axis3 = axis.twiny()
mass_ticks = np.array([80,82,84,86])
axis3.set_xlim(26.5,28.1)
axis3.set_xticks(MassToTime(mass_ticks))
axis3.set_xticklabels(mass_ticks)
axis3.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize-1,axis='both',pad=d.pad)

fig.text(0.02, 0.5, 'Response / mV', fontsize=d.y_axis_font, ha='center', va='center', rotation='vertical')

#plt.show()
plt.savefig('thiophene_hds_combined.png',dpi=900)

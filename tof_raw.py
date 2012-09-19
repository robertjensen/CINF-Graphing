backend = 'agg'
execfile('std_header.py')

#Mass of NH3: 17.0265491
#Mass of OH: 17.0027397

#Correct this expression to spectrum 403
def MassToTime(mass):
    time = 2.97938950943 * (mass**0.497905494751)
    corr_time = time + 0.19 
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
cursor.execute("SELECT x*1000000,y*1000 FROM xy_values_tof where measurement = 830")
data['ch'] = np.array(cursor.fetchall())

axis_array = []

LINEWIDTH = 0.5
arrow = dict(facecolor='black',arrowstyle='->')
font = d.arrowfont

gs = gridspec.GridSpec(2, 3)
#gs.update(wspace=0.6,hspace=0.7)

axis = plt.subplot(gs[0, :])

axis.plot(data['ch'][:,0], data['ch'][:,1], 'r-',linewidth=LINEWIDTH)
axis.set_ylim(0,20)
axis.set_xlim(0,40)
axis.set_xticks([2.5,5,7.5,10,12.5,15,17.5,20,25,30,35])

mass_ticks = np.array([1,2,5,10,15,20,30,40,50,60,70,80,90,100,120,140,160,180])

axis3 = axis.twiny()
axis3.set_xlim(0,40)
axis3.set_xticks(MassToTime(mass_ticks))
axis3.set_xticklabels(mass_ticks)
axis3.set_xlabel('Mass / amu', fontsize=d.x_axis_font)
axis3.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize-1,axis='both',pad=d.pad)
#axis3.ticklabel_format(useOffset=False)
axis.set_yticks((0,25,50,75))
axis.set_ylim(-5,80)

p = axis.axvspan(12, 16.5, facecolor='#26aaf7', alpha=0.25)
p = axis.axvspan(29.5, 34, facecolor='#25dd37', alpha=0.25)
p = axis.axvspan(36.5, 37.3, facecolor='#b6fa77', alpha=0.25)


axis.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize,axis='both',pad=d.pad)
#axis.set_ylabel('Response / mV', fontsize=d.y_axis_font)
axis.set_ylabel('')
#axis.set_xlabel('Flight Time / $\mu$s', fontsize=8)
axis.set_xlabel('')



axis = plt.subplot(gs[1,0])
#axis.set_ylabel('Response / mV', fontsize=d.y_axis_font)
axis.set_ylabel('')
axis.set_yticks((0,10,20,30,40))
axis.plot(data['ch'][:,0], data['ch'][:,1], 'r-',linewidth=LINEWIDTH)
p = axis.axvspan(12, 16.5, facecolor='#26aaf7', alpha=0.25)
axis.set_xlim(12,16.5)
axis.set_ylim(-5,30)
axis.set_xticks([13,13,14,15,16])
axis.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize,axis='both',pad=d.pad)
axis3 = axis.twiny()
mass_ticks = np.array([18,20,22,24,26,28])
axis3.set_xlim(12,16.5)
axis3.set_xticks(MassToTime(mass_ticks))
axis3.set_xticklabels(mass_ticks)
axis3.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize-1,axis='both',pad=d.pad)



axis = plt.subplot(gs[1,1])
axis.set_ylabel('')
axis.set_yticks((0,1,2,3,4))
axis.set_xticks((15,29,30,31,32,33,34))
axis.plot(data['ch'][:,0], data['ch'][:,1], 'r-',linewidth=LINEWIDTH)
p = axis.axvspan(29.5, 34, facecolor='#25dd37', alpha=0.25)
axis.set_xlim(29.5,34)
axis.set_ylim(-2,5)
axis.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize,axis='both',pad=d.pad)
axis.ticklabel_format(useOffset=False)
#axis.annotate('H', xy=(3.2, 10),  xycoords='data', xytext=(3.52, 17), textcoords='data', arrowprops=arrow, horizontalalignment='right', verticalalignment='top',fontsize=font,)
#axis.annotate('H$_2$', xy=(4.35, 10),  xycoords='data', xytext=(4.2, 20), textcoords='data', arrowprops=arrow, horizontalalignment='right', verticalalignment='top',fontsize=font,)
axis.set_xlabel('Flight Time / $\mu$s', fontsize=d.x_axis_font)
axis3 = axis.twiny()
mass_ticks = np.array([100,110,120,130])
axis3.set_xlim(29.5,34)
axis3.set_xticks(MassToTime(mass_ticks))
axis3.set_xticklabels(mass_ticks)
axis3.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize-1,axis='both',pad=d.pad)

axis = plt.subplot(gs[1,2])
axis.set_ylabel('')
axis.set_yticks((25,50,75,100,125))
#axis.set_xticks((12,12.5))
axis.plot(data['ch'][:,0], data['ch'][:,1], 'r-',linewidth=LINEWIDTH)
axis.set_xlim(36.5,37.3)
axis.set_ylim(-5,80)
axis.set_xticks([36.6,36.8,37,37.2])
axis.set_yticks((0,20,40,60,80))
axis.ticklabel_format(useOffset=False)
p = axis.axvspan(36.5, 37.3, facecolor='#b6fa77', alpha=0.25)
axis.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize,axis='both',pad=d.pad)
#axis.annotate('O', xy=(12.04, 10),  xycoords='data', xytext=(12.05, 69), textcoords='data', arrowprops=arrow, horizontalalignment='right', verticalalignment='top',fontsize=font,)
#axis.annotate('NH$_2$', xy=(12.055, 47),  xycoords='data', xytext=(12.22, 82), textcoords='data', arrowprops=arrow, horizontalalignment='right', verticalalignment='top',fontsize=font,)
#axis.annotate('OH', xy=(12.414, 50),  xycoords='data', xytext=(12.33, 66), textcoords='data', arrowprops=arrow, horizontalalignment='right', verticalalignment='top',fontsize=font,)
#axis.annotate('NH$_3$', xy=(12.425, 85),  xycoords='data', xytext=(12.35, 130), textcoords='data', arrowprops=arrow, horizontalalignment='right', verticalalignment='top',fontsize=font,)
axis3 = axis.twiny()
mass_ticks = np.array([153,154,155,156,157,158])
axis3.set_xlim(36.5,37.3)
axis3.set_xticks(MassToTime(mass_ticks))
axis3.set_xticklabels(mass_ticks)
axis3.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize-1,axis='both',pad=d.pad)

fig.text(0.02, 0.5, 'Response / mV', fontsize=d.y_axis_font, ha='center', va='center', rotation='vertical')



#plt.tight_layout()
plt.show()
plt.savefig('dibenzothiophene.png',dpi=300)

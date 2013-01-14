#backend = 'agg'
execfile('../std_header.py')
import scipy
import scipy.ndimage

#datafile_dir = 'real_image_test'
datafile_dir = 'first_image_test'
sys.path.append('./' + datafile_dir + '/')
import dimensions as dim

f = open(datafile_dir + '/datafile.txt','r')
file = f.read()
f.close()

file = file.strip()
#Skip the first 5 lines with status information
n = 0
for i in range(0,5):
    n = file.find('\n',n+1)

#Split the files into separate lines
file = file[n+1:].split('\n')

rows = file[1]
rows = rows.strip()
cells = rows.split('\t')

data = {}
#Create the placeholder for all the data
for cell in cells:
    cell = cell.replace('  ',' ')
    cell = cell.replace('  ',' ')
    cell = cell.replace(':','')
    items = cell.split(' ')
    data[items[0]] = np.array([0,0])

#Fill in the data
for rows in file:
    rows = rows.strip()
    cells = rows.split('\t')

    #The time stamp is always the first row
    #Currently the measurement setup is limited by the fact that a single
    #timestamp is assigned to the complete row, however, the data structure
    #is prepared for seperate timestamps
    cell_time = float(cells[0][6:])

    for cell in cells:
        cell = cell.replace('  ',' ')
        cell = cell.replace('  ',' ')
        cell = cell.replace(':','')
        items = cell.split(' ')
        data[items[0]] = np.vstack([data[items[0]],[cell_time,float(items[1])]])

fig = plt.figure()
axis = fig.add_subplot(1,1,1)
ratio = d.ratio
fig_width = d.width
fig_width = fig_width /2.54     # width in cm converted to inches
fig_height = fig_width*ratio
fig.set_size_inches(fig_width,fig_height)

image = True
if image:
	reactor_length = 27.0#mm
	pix_pr_mm = (dim.right_edge - dim.left_edge) / reactor_length

	img = scipy.misc.imread(datafile_dir + '/216.845384121.png')
	img = img[:,:,0] # Image is black and white, remove color information
	img = scipy.ndimage.rotate(img,-8)
	img = img[dim.crop['left']:-1*dim.crop['right'],dim.crop['top']:-1*dim.crop['bottom']]
	#print img.min()
	#print img.max()
	print img.shape
MAXTEMP = 64
MINTEMP = 24
	scale_f = 1.0 * img.shape[0]/max(img[40,:])
	print scale_f
	#Reactor position: 2mm - 12mm from top
	print max(img[40,:])
	a = plt.imshow(img,cmap=plt.cm.gray)
	axis.plot(np.arange(0,img.shape[1]), 1.0*img[40,:]*img.shape[0]/max(img[40,:]), 'r-',label="Profile")

	c = plt.Circle([42,40], radius=23,color="g",fill=False)
	fig.gca().add_artist(c)

	# Not correct position
	b = plt.Rectangle([15,10],8,60,color="g",fill=False)
	fig.gca().add_artist(b)

	# Not correct position
	b = plt.Rectangle([30,10],10,60,color="g",fill=False)
	fig.gca().add_artist(b)

	# Not correct position
	b = plt.Rectangle([55,10],12,60,color="g",fill=False)
	fig.gca().add_artist(b)

	a = plt.axes([.6, .62, .28, .1], axisbg='w')
	a.plot(np.arange(19,65), img[40,19:65], 'r-',label="Profile")
	a.tick_params(direction='in', length=3, width=1, colors='k',labelsize=6,axis='both',pad=3)
	plt.setp(a, xlim=(19,65), ylim=(0,500),xticks=[20,30], yticks=[59,100,200])
	plt.setp(a, xlim=(19,65),xticks=[20,30])
	axis.set_xlim(0,img.shape[1]-1)
	axis.set_ylim(0,img.shape[0]-1)

	pos_ticks = np.array([0,5,10,15,20,25])
	axis.set_xticks(pos_ticks*pix_pr_mm+dim.left_edge)
	axis.set_xticklabels(pos_ticks)
	axis.set_xlabel('Pos / mm', fontsize=d.x_axis_font)

	#print a.norm.vmin
	#print a.norm.vmax


overview = False
if overview:
	axis.plot(data['T1'][1:,0], data['T1'][1:,1], 'r-',label="H1")
	axis.plot(data['T2'][1:,0], data['T2'][1:,1], 'b-',label="H2")
	axis.plot(data['T3'][1:,0], data['T3'][1:,1], 'm-',label="H3")
	axis.plot(data['RTD_temp'][1:,0], data['RTD_temp'][1:,1], 'c-',label="RTD")

	#axis.plot(data['R1'][:,0], data['R1'][:,1], 'r-',label="R1")
	#axis.plot(data['I1'][:,0], data['I1'][:,1], 'g-',label="VR1")
	#axis.plot(data['V1'][:,0], ((data['PS_Voltage'][:,1]-data['I1'][:,1])/data['I1'][:,1])-data['R1'][:,1], 'b-',label="R1 calc")

	axis2 = axis.twinx()
	axis2.plot(data['PS_Voltage'][1:,0], data['PS_Voltage'][1:,1], 'k-',label="PS Voltage")	
	axis.set_xlim(0,305)
	#axis.set_xticks([2.5,5,7.5,10,12.5,15,17.5,20,25,30,35])

	axis.legend(loc = 2,prop={"size":8})

	axis.tick_params(direction='in', length=d.ticklength, width=1, colors='k',labelsize=d.labelsize,axis='both',pad=d.pad)
	axis.set_ylabel('Temperature / C', fontsize=d.y_axis_font)
	axis2.set_ylabel('Bias / V', fontsize=d.y_axis_font)
	axis.set_xlabel('Time / s', fontsize=d.x_axis_font)


#plt.tight_layout()
plt.show()
#plt.savefig('power_versus_temp.png',dpi=300)

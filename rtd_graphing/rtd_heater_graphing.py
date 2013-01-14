#backend = 'agg'
execfile('../std_header.py')
import scipy
import scipy.ndimage
from matplotlib.backends.backend_pdf import PdfPages

def read_datafile(datafile_dir):
	#datafile_dir = 'real_image_test'
	#datafile_dir = 'first_image_test'
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

	return data 


#datafile_dir = 'real_image_test'
datafile_dir = 'first_image_test'
sys.path.append('./' + datafile_dir + '/')
import dimensions as dim

data = read_datafile(datafile_dir)
pp = PdfPages('multipage.pdf')

overview = True
if overview:

	fig = plt.figure()
	axis = fig.add_subplot(1,1,1)
	ratio = d.ratio
	fig_width = d.width
	fig_width = fig_width /2.54     # width in cm converted to inches
	fig_height = fig_width*ratio
	fig.set_size_inches(fig_width,fig_height)

	axis.plot(data['T1'][1:,0], data['T1'][1:,1], 'r-',label="H1")
	axis.plot(data['T2'][1:,0], data['T2'][1:,1], 'b-',label="H2")
	axis.plot(data['T3'][1:,0], data['T3'][1:,1], 'm-',label="H3")
	axis.plot(data['RTD_temp'][1:,0], data['RTD_temp'][1:,1], 'c-',label="RTD")

	for time in dim.images.keys():
		axis.vlines(time,axis.get_ylim()[0],axis.get_ylim()[1],linestyles='dotted')

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

	plt.savefig(pp, format='pdf')
	plt.close()

for timestamp in sorted(dim.images.keys()):

	i = 0
	while data['PS_Voltage'][i,0] < timestamp:
		i = i+1
	bias = data['PS_Voltage'][i-1,1]
	T1  = "T1:   {0:.1f}C".format(data['T1'][i-1,1])
	T2  = "T2:   {0:.1f}C".format(data['T2'][i-1,1])
	T3  = "T3:   {0:.1f}C".format(data['T3'][i-1,1])
	RTD = "RTD: {0:.1f}C".format(data['RTD_temp'][i-1,1])
	
	fig = plt.figure()
	axis = fig.add_subplot(1,1,1)
	ratio = d.ratio
	fig_width = 15
	fig_width = fig_width /2.54     # width in cm converted to inches
	fig_height = fig_width*ratio
	fig.set_size_inches(fig_width,fig_height)
	fig.subplots_adjust(bottom=0.075)
	fig.subplots_adjust(right=0.7)

	axis.text(0,1.2,'Bias = ' + str(bias) + 'V',fontsize=14,transform = axis.transAxes)
	axis.text(1.05,1.000,T1,fontsize=10,transform = axis.transAxes)
	axis.text(1.05,0.925,T2,fontsize=10,transform = axis.transAxes)
	axis.text(1.05,0.850,T3,fontsize=10,transform = axis.transAxes)
	axis.text(1.05,0.775,RTD,fontsize=10,transform = axis.transAxes)

	image = True
	if image:
		reactor_length = 27.0#mm
		pix_pr_mm = (dim.right_edge - dim.left_edge) / reactor_length
	
		img_timestamp = timestamp
		img = scipy.misc.imread(datafile_dir + '/' + str(img_timestamp) + '.png')
		img = img[:,:,0] # Image is black and white, remove color information
		img = scipy.ndimage.rotate(img,dim.rotation)
		img = img[dim.crop['left']:-1*dim.crop['right'],dim.crop['top']:-1*dim.crop['bottom']]
	
		scale_f = 0.95 * img.shape[0]/max(img[40,:])
		a = plt.imshow(img,cmap=plt.cm.gray)
		axis.plot(np.arange(0,img.shape[1]), scale_f * img[40,:], 'r-',label="Profile")
	
		min_temp = dim.images[img_timestamp][0] * 1.0
		max_temp = dim.images[img_timestamp][1] * 1.0
		tickmarks = np.arange(10*int(1+math.floor(min_temp/10)),10*int(1+math.floor(max_temp/10)),10)
		
		scale_temp = 255/(max_temp-min_temp)
		axis.set_yticks((scale_temp * (tickmarks - min_temp)) * scale_f)
		axis.set_yticklabels(tickmarks)
	
		# Heater 3, 1mm from top, 1mm wide
		b = plt.Rectangle([1*pix_pr_mm + dim.left_edge,10],1*pix_pr_mm,60,color="g",fill=False)
		fig.gca().add_artist(b)
	
		# Heater 2, 6.6mm from top, 1mm wide
		b = plt.Rectangle([6.6*pix_pr_mm + dim.left_edge,10],1*pix_pr_mm,60,color="g",fill=False)
		fig.gca().add_artist(b)
	
		# Heater 1, 12.9 from top, 2mm wide
		b = plt.Rectangle([12.9*pix_pr_mm + dim.left_edge,10],2*pix_pr_mm,60,color="g",fill=False)
		fig.gca().add_artist(b)
	
		#Reactor position: 2mm - 12mm from top
		c = plt.Circle([42,40], radius=23,color="g",fill=False)
		fig.gca().add_artist(c)
	
		reactor_left  =  int(dim.left_edge + 2*pix_pr_mm)
		reactor_right = int(dim.left_edge + 12*pix_pr_mm)
		
		zoom_data = img[40,reactor_left:reactor_right] / scale_temp + min_temp
		a = plt.axes([.6, .16, .28, .2], axisbg='w')
		a.plot(np.arange(reactor_left,reactor_right), zoom_data, 'r-',label="Profile")
		a.tick_params(direction='in', length=3, width=1, colors='k',labelsize=6,axis='both',pad=3)
		plt.setp(a, xlim=(reactor_left,reactor_right), ylim=(min(zoom_data)-0.1,max(zoom_data) + 0.1),xticks=[])#, yticks=[59,100,200])
	
		b = plt.axes([.6, .4, .28, .2], axisbg='w')

		b.plot(data['T1'][i-5:i+5,0], data['T1'][i-5:i+5,1], 'r-',label="H1")
		b.plot(data['T2'][i-5:i+5,0], data['T2'][i-5:i+5,1], 'b-',label="H2")
		b.plot(data['T3'][i-5:i+5,0], data['T3'][i-5:i+5,1], 'm-',label="H3")
		b.plot(data['RTD_temp'][i-5:i+5,0], data['RTD_temp'][i-5:i+5,1], 'c-',label="RTD")

		b.tick_params(direction='in', length=3, width=1, colors='k',labelsize=6,axis='both',pad=3)
		#plt.setp(b, xlim=(reactor_left,reactor_right), ylim=(min(zoom_data)-0.1,max(zoom_data) + 0.1),xticks=[])#, yticks=[59,100,200])
	
		pos_ticks = np.array([0,5,10,15,20,25])
		axis.set_xlim(0,img.shape[1]-1)
		axis.set_ylim(0,img.shape[0]-1)
		axis.set_xticks(pos_ticks*pix_pr_mm+dim.left_edge)
		axis.set_xticklabels(pos_ticks)
		axis.set_xlabel('Pos / mm', fontsize=d.x_axis_font)
		axis.set_ylabel('Thermographic temperature / C', fontsize=d.x_axis_font)
	
	plt.savefig(pp, format='pdf')
	plt.close()


#plt.tight_layout()
plt.savefig(pp, format='pdf')
plt.close()
pp.close()

#plt.show()
#plt.savefig('power_versus_temp.png',dpi=300)

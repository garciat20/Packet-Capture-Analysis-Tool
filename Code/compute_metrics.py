def compute(ip_address, res):
	data_for_csv = [] #13 pieces of data can be placed here
	"13 items are computed/returned here"

	# results(data_for_csv)

def results(compute_data):
	"""
	Compile results into csv file via unpacking variables from compute()
	"""
	# unpack list of items returned = compute_data
	filename="project2_output.csv"
	file = open(filename,"w")
	# need to finish formatting the csv file here

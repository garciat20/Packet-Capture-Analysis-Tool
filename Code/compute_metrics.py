def compute(ip_address, res, file_num):
	data_for_csv = [] #13 pieces of data can be placed here
	"13 items are computed/returned here"

	# results(data_for_csv, file_num)

def results(compute_data, file_num):
	"""
	Compile results into csv file via unpacking variables from compute()
	"""
	# unpack list of items returned = compute_data
	filename="project2_output.csv"
	file = open(filename,"w")
	file.write(f"Node{file_num}")
	# need to finish formatting the csv file here

def compute(ip_address, res, file_num):
	"""
	13 items are computed/returned here
	NOTE: 
	res is a list of lists that contain information about seq number, time, source etc (check below)
	
	What res looks like: [sequence number, time, source (ip_addressed being passed in this func), destination, protocol, length, echo, "ping", "reply" OR "request" ...]

	what we want (most likey im probz missing something)

	index | item

	1 : item
	2 : source ip
	3 :	destination ip
	5 :	length
	8 : reply/request
	11 : ttl (we need this for hops)
	"""
	
	data_for_csv = [] #13 pieces of data can be placed here

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

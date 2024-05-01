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

	num_requests_sent = 0
	num_requests_received = 0
	
	num_replies_sent = 0
	num_replies_received = 0
	
	total_bytes_sent = 0
	total_bytes_received = 0
	
	hop_count = 0
	windows_hop = 129

	total_data_sent = 0
	total_data_received = 0

	avg_ping_RTT = 0
	total_RTT = 0
	total_packets = 0

	echo_request_throughput = 0

	echo_request_goodput = 0

	avg_reply_delay = 0
	
	curr_time = 0
	previous_time = 0


	for seqNum, time, source, dest, prot, length, echo_type, id, seq, ttl in res:
		
		previous_time = curr_time
		curr_time = time

		if source == ip_address:
			if "reply" in echo_type:
				num_replies_sent += 1
				total_RTT += curr_time - previous_time
			else:
				num_requests_sent +=1
				total_bytes_sent += length
				total_data_sent += (length - 28)
		else:
			if "reply" in echo_type:
				num_replies_received += 1
			else:
				num_requests_received += 1
				total_bytes_received += length
				total_data_received += (length - 28)
		total_packets += 1


	for index in range(len(res)):
		if res[index][8] == "reply" :
			if res[index][3] == ip_address: #destination
				hop_count += windows_hop - int(res[11])

	print(hop_count)
	echo_request_throughput = total_bytes_sent / total_RTT

	echo_request_goodput = total_data_sent / total_RTT

	avg_ping_RTT = total_RTT / total_packets

	data_for_csv.append(num_requests_sent)
	data_for_csv.append(num_requests_received)
	data_for_csv.append(num_replies_sent)
	data_for_csv.append(num_replies_received)

	data_for_csv.append(total_bytes_sent)
	data_for_csv.append(total_bytes_received)
	data_for_csv.append(total_data_sent)
	data_for_csv.append(total_data_received)

	data_for_csv.append(avg_ping_RTT)
	data_for_csv.append(echo_request_throughput)
	data_for_csv.append(echo_request_goodput)
	data_for_csv.append(avg_reply_delay)
	#Below is where hop count will go, fill in variable name
	data_for_csv.append("Average Hop Count Here")

	results(data_for_csv, file_num)

def format(file, data):
	#All 0s are placeholders, to be filled when compute_metrics is complete
	file.write("\n")
	file.write("Echo Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received")
	file.write(data[0] + "," + data[1] + "," + data[2] + "," + data[3])
	file.write("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)")
	file.write(data[4] + "," + data[6])
	file.write("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)")
	file.write(data[5] + "," + data[7])
	file.write ("\n")

	file.write("Average RTT (milliseconds)," + data[8])
	file.write("Echo Request Throughput (kB/sec)," + data[9])
	file.write("Echo Request Goodput (kB/sec)," + data[10])
	file.write("Average Reply Delay (microseconds)," + data[11])
	file.write("Average Echo Request Hop Count," + data[12])

def results(compute_data, file_num):
	"""
	Compile results into csv file via unpacking variables from compute()
	"""
	# unpack list of items returned = compute_data
	filename="project2_output.csv"
	with open(filename, "w") as file:
		file.write(f"Node {file_num}")
		# need to finish formatting the csv file here
		format(file, compute_data)
		file.close()
	

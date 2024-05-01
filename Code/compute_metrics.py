def compute(ip_address, res, file_num):
	"""
	13 summarys are computed/returned here
	NOTE: 
	res is a list of lists that contain information about seq number, time, source etc (check below)
	
	What res looks like: [sequence number, time, source (ip_addressed being passed in this func), destination, protocol, length, echo, "ping", "reply" OR "request" ...]

	what we want (most likey im probz missing something)

	index | summary

	1 : time
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
	
	rtt_time= 0
	replay_delay_time = 0

	total_replay_delay_time =0 

	total_rtt_time = 0


	for summary in res :
		if summary[8] == "reply" :
			if summary[2] == ip_address :
				num_replies_sent += 1 # replies sent
			elif summary[3] == ip_address :
				num_replies_received += 1 #replies received
		if summary[8] == "request" :
			if summary[2] == ip_address :
				num_requests_sent += 1 #requests sent
				total_bytes_sent += int(summary[5]) #request bytes sent
				total_data_sent += int(summary[5]) -  28 # idk if its 28 i didnt double check bru
			elif summary[3] == ip_address :
				num_requests_received += 1 #received requestes
				total_bytes_received += int(summary[5]) #request bytes received
				total_data_received += int(summary[5]) - 28 #total data recieved

	#average round trip time,echo request throughput/goodput
#  Average Reply Delay (in microseconds)
# • Defined as the time between a node receiving
# an Echo Request packet and sending an Echo
# Reply packet back to the source

	for i in range(len(res)):
		if res[i][8] == "request" :
			if res[i][2] == ip_address :
				rtt_time += 1
				total_rtt_time += (float(res[i+1][1]))-(float(res[i][1]))

	# avg reply delay
	for i in range(len(res)):
		if res[i][8] == "request" :
			if res[i][3] == ip_address :
				replay_delay_time += 1
				total_replay_delay_time += (float(res[i+1][1]))-(float(res[i][1]))	

	# hop count 
	for index in range(len(res)):
		if res[index][8] == "reply" :
			if res[index][3] == ip_address: #destination
				hop_ttl = res[i][11].split("=")
				hop_count += (windows_hop - int(hop_ttl[1]))

	print(hop_count)

	avg_rtt = (total_rtt_time / rtt_time) #avg ping round trip time  1
	echo_request_throughput = total_bytes_sent / total_rtt_time

	avg_hop = hop_count/ num_requests_sent # 2
	echo_request_goodput = total_data_sent / total_RTT # 3

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
	data_for_csv.append(avg_hop)

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
	# unpack list of summarys returned = compute_data
	filename="project2_output.csv"
	with open(filename, "w") as file:
		file.write(f"Node {file_num}")
		# need to finish formatting the csv file here
		format(file, compute_data)
		file.close()
	

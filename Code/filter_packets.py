
def output_file(filename,filenum):
	"""
	Extracts raw text file to retrieve ICMP Echo Request and ICMP Echo Reply packets to a new file
	"""
	filtered_filename = f"Node{filenum}_filtered.txt"
	
	f = open(filename, "r")
	filtered_file = open(filtered_filename,"w")
	lines = f.readlines()

	for line in lines:
		if "ping" in line: # focus on the messages generated by the ping program
			filtered_file.write(line)
	f.close()
	filtered_file.close()

def filter() :
	output_file("Captures/Node1.txt",1)
	output_file("Captures/Node1.txt",2)
	output_file("Captures/Node1.txt",3)
	output_file("Captures/Node1.txt",4)
	

from filter_packets import *
from packet_parser import *
from compute_metrics import *

"we're storing parsed data of a summary line (idk if thats the right term) in place with these lists"
node_1_data = []
node_2_data = []
node_3_data = []
node_4_data = []

filter()

parse("Node1_filtered.txt", node_1_data)
parse("Node2_filtered.txt", node_2_data)
parse("Node3_filtered.txt", node_3_data)
parse("Node4_filtered.txt", node_4_data)

# filename="project2_output.csv"
# file = open(filename,"w")

compute("192.168.100.1",node_1_data, 1) #1st ip address of every file and the data we parsed
compute("192.168.100.1",node_2_data, 2) #1st ip address of every file and the data we parsed
compute("192.168.100.1",node_3_data, 3) #1st ip address of every file and the data we parsed
compute("192.168.100.1",node_4_data, 4) #1st ip address of every file and the data we parsed

# file.close()


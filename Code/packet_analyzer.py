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

compute()

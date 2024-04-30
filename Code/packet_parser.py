def parse(filtered_file, data):
	"""
	Before you can compute metrics, you must parse
	the filtered raw text files and read packet fields
	into your tool
	• You may choose to parse the summary line text or
	the hex (bonus points will be awarded for parsing
	the hex)
	• The fields you need will be determined by the
	metrics you need to compute
	=====
	All 13 metrics you collect will be on a “per node basis.
	• You will be calculating three categories of metrics
	• Data size metrics (8 metrics)
	• Time based metrics (4 metrics)
	• Distance metric (1 metric)
	
	NOTE: i beleieve we have the summary line from when we filtered the file,
	however we need to split/strip to make it more coding friendly
	"""
	
	f = open(filtered_file, "r")
	lines = f.readlines()
	"""
	['1444 1442.007091    192.168.100.1         192.168.200.2         ICMP     642    Echo (ping) reply    id=0x0001, seq=148/37888, ttl=128 (request in 1443)']]
	['1444', '1442.007091', '192.168.100.1', '192.168.200.2', 'ICMP', '642', 'Echo', '(ping)', 'reply', 'id=0x0001,', 'seq=148/37888,', 'ttl=128', '(request', 'in', '1443)']
	"""

	# 13 pieces of data
	for line in lines: 
		data.append(line.strip().split())

	
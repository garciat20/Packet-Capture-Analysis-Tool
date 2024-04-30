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

	# 13 pieces of data
	for line in lines: 
		data.append(line.strip().split())

	
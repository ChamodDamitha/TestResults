csv_file = open("latency.csv", "w")
csv_file.write("Timestamp,Average latency (ms)" + "\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    
    str = "";

    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break
	if line[0] == "[" and line[-19:-1]  == "logStreamPublisher":
		#print(line)	
		str += line.split("]")[0].split(",")[0].replace("[","") + ","
	elif line[0:17] == "Event: avgLatency":
		#print(line.split(":"))	
		str += line.split(":")[2] + "\n"
		csv_file.write (str)
		print(str)
		str = ""
	

extractData("event_stream_log.txt")

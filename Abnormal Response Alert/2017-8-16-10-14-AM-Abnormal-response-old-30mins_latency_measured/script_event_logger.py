csv_file = open("performance_log.csv", "w")
csv_file.write("Timestamp,Average latency (ms),Average throughput (events/second)"+"\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    
    str = "";

    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break

	if line[0] == "[" and line[-19:-1]  == "logStreamPublisher":
		str += line.split("]")[0].split(",")[0].replace("[","") + ","
	elif line[0:17] == "Event: avgLatency":
		str += line.split(":")[2]
	elif line[0:10] == "throughput":
		str += line.split(":")[1] + "\n"
		csv_file.write (str)
		print(str)
		str = ""
	

extractData("event_stream_log.txt")

csv_file = open("stream_sample_dropping.csv", "w")
csv_file.write("Accuracy" + "\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    
    str = "";

    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break
	elif line[0:15] == "[java] Accuracy":
		str = line.split(":")[1] + "\n"
		csv_file.write (str)
		print(str)
		str = ""

extractData("producer_event_log.txt")

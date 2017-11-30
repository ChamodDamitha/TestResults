csv_file = open("feedback_consumer_event_log.csv", "w")
csv_file.write("events count, average value, timeSpent"+"\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    	
    i = 0		
    for line in log_file_content:
        line = line.strip()
	if line[0:12] == "[java] Event":
		i += 1
		msgStr = line.split(":")
		strr = str(i) + "," + msgStr[3].split(",")[0].strip() + "," + msgStr[4].strip() + "\n"
		csv_file.write (strr)
		print(strr)
	

extractData("consumer_log.txt")

csv_file = open("feedback_producer_event_log.csv", "w")
csv_file.write("event count, events value, impact"+"\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    	
    i = 0		
    for line in log_file_content:
        line = line.strip()
	if line[0:12] == "[java] Value":
		i += 1
		msgStr = line.split(":")
		strr = str(i) + "," + msgStr[1].strip() + "," + msgStr[3].strip() + "\n"
		csv_file.write (strr)
		print(strr)
	

extractData("producer_log.txt")

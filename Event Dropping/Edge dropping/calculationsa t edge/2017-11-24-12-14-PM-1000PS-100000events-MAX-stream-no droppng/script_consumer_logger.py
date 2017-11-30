csv_file = open("consumer_event_log.csv", "w")
csv_file.write("event count, max, time spent" + "\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    
    counts = []		
    i = 1;	
    for line in log_file_content:
        line = line.strip()
	if line[0:12] == "[java] Event":
		msgStr = line.split(":")
		strr = str(i) + "," + msgStr[3].split(",")[0].strip() + ", " + msgStr[4].strip() + "\n"
		i += 1
		csv_file.write (strr)
		print(strr)
		
	

extractData("consumer_log.txt")

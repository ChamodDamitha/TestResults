csv_file = open("feedback_event_log.csv", "w")
csv_file.write("events count, event value, event impact"+"\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    
    counts = []		

    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break
	elif line[0:12] == "[java] Event":
		msgStr = line.split(":")
		str = msgStr[1].split("=")[1].strip() + "," + msgStr[2].split("=")[1].strip() + "," + msgStr[3].split("=")[1].strip() + "\n"
		csv_file.write (str)
		print(str)
	

extractData("producer_log.txt")

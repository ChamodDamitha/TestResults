csv_file = open("no_dropping.csv", "w")
csv_file.write("Average Humidity - no dropping" + "\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    
    str = "";

    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break
	elif line[0:25] == "[java] Event: avgHumidity":
		str = line.split(":")[2].split(",")[0] + "\n"
		csv_file.write (str)
		print(str)
		str = ""
	

extractData("event_log.txt")

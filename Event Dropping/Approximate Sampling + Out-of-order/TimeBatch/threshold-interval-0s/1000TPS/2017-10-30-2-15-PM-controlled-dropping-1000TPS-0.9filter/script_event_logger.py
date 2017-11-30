csv_file = open("event_log.csv", "w")
csv_file.write("events in window,avgHumidity"+"\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()

    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break
	elif line[0:24] == "[java] Event: avgHumdity":
		str = line.split(":")[3].split(",")[0] + "," + line.split(":")[2].split(",")[0] + "\n"
		csv_file.write (str)
		print(str)
	

extractData("consumer_log.txt")

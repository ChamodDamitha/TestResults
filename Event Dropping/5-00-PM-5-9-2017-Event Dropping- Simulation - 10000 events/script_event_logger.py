csv_file = open("stream_sample_dropping.csv", "w")
csv_file.write("Average Humidity" + "\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    
    str = "";

    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break
	elif line[0:25] == "[java] controlled dropped":
		str = line.split(":")[1] + "\n"
		csv_file.write (str)
		print(str)
		str = ""
	elif line[0:27] == "[java] uncontrolled dropped":
		str = line.split(":")[1] + "\n"
		csv_file.write (str)
		print(str)
		str = ""

extractData("event_log.txt")

csv_file = open("event_log.csv", "w")
csv_file.write("event,avgHumidity"+"\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    
    str = "";

    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break
	elif line[0:12] == "[java] count":
		count = line.split(":")[1].strip()
		#print(count)
		if count == "0":
			str += count + ", 0\n"
			csv_file.write (str)
			print(str)
			str = ""
		else:
			str += count + "," 
	elif line[0:25] == "[java] Event: avgHumidity":
		str += line.split(":")[2].split(",")[0] + "\n"
		csv_file.write (str)
		print(str)
		str = ""
	

extractData("consumer_log.txt")

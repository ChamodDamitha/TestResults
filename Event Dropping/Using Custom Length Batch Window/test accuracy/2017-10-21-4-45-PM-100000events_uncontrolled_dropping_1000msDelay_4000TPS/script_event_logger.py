csv_file = open("event_log.csv", "w")
csv_file.write("events in window,avgHumidity"+"\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    
    counts = []		

    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break
	elif line[0:12] == "[java] count":
		count = line.split(":")[1].strip()
		#print(count)
		if count == "0":
			str = count + ", 0\n"
			csv_file.write (str)
			print(str)
		else:
			counts.append(count) 
	elif line[0:25] == "[java] Event: avgHumidity":
		str = counts.pop(0) + "," + line.split(":")[2].split(",")[0] + "\n"
		csv_file.write (str)
		print(str)
	

extractData("consumer_log.txt")

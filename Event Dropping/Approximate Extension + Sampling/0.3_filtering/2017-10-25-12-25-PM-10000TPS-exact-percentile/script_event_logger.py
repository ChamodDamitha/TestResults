csv_file = open("event_log.csv", "w")
csv_file.write("event, 50th_percentile"+"\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    i = 0
    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break
	elif line[0:12] == "[java] Event":
		i+=1
		percentile = line.split(":")[2].strip().split(",")[0].strip()
		print(str(i) + "," + percentile)
		csv_file.write(str(i) + "," + percentile + "\n")
	
extractData("consumer_log.txt")

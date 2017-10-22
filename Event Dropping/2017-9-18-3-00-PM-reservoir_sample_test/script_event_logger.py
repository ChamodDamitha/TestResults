csv_file = open("reservor_sample.csv", "w")
csv_file.write("Reservoir_sample, Dropped Count" + "\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    
    str = "";

    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break
	elif line[0:23] == "[java] Reservoir_sample":
		str = line.split(":")[1].split(",")[0] + ", 1\n"
		csv_file.write (str)
		print(str)
		str = ""
	

extractData("producer_event_log.txt")

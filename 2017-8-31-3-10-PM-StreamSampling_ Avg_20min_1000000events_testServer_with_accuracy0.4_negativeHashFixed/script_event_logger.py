csv_file = open("avgHumidity_with_accuracy_0.4.csv", "w")
csv_file.write("Average Humidity" + "\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    
    str = "";

    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break
	elif line[0:25] == "[java] Event: avgHumidity":
		str = line.split(":")[2] + "\n"
		csv_file.write (str)
		print(str)
		str = ""
	

extractData("consumer_log_with_approximate_dropping.txt")

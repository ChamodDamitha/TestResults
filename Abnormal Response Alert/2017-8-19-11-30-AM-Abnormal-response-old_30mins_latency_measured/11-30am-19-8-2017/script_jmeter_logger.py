csv_file = open("throughput.csv", "w")
csv_file.write("Events Sent, Average throughput (events/second)"+"\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    str = ""

    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break
	if(line[0:61] == "[java] [main] INFO  org.wso2.carbon.sample.performance.Client"):
		line_arr = line.split(":")
		str = line_arr[1].split(" ")[1] + ", " + line_arr[2].strip() + "\n"
		csv_file.write (str)
		print(str)

extractData("thrift_log.txt")

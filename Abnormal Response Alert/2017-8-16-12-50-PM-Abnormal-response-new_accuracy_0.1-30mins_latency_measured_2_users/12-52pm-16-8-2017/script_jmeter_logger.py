csv_file = open("jmeter_log_test.csv", "w")
csv_file.write("Time elapsed, Average throughput (events/second)"+"\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    

    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break

	if line[0:9] == "summary =":
		line_arr = line.split("in")[1].strip().split(" ")
		#print(line_arr)
		str = line_arr[0] + ", " + line_arr[4].split("/")[0] + "\n"
		csv_file.write (str)
		print(str)
	

extractData("new-version-apim-analytics.txt")

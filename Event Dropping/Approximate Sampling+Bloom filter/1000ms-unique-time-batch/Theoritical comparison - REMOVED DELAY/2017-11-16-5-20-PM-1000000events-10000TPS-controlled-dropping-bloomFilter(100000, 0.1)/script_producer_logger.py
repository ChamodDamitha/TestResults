csv_file = open("producer_results_log.csv", "w")
csv_file.write("event count, Expected distinct count" + "\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    
    counts = []		
    for line in log_file_content:
        line = line.strip()
	if line[0:11] == "[java] Time":
		msgStr = line.split(":")
		strr = str(int(msgStr[3].strip())/10) + "\n"
		csv_file.write (strr)
		print(strr)
		
	

extractData("producer_log.txt")

csv_file = open("producer_results_log.csv", "w")
csv_file.write("event count, Expected sum" + "\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    
    counts = []	
    i = 1		
    for line in log_file_content:
        line = line.strip()
	if line[0:17] == "[java] ACTUAL SUM":
		msgStr = line.split(":")
		strr = str(i) + ", " + msgStr[1].strip() + "\n"
		csv_file.write (strr)
		print(strr)
		i += 1
		
	

extractData("producer_log.txt")

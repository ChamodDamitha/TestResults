csv_file = open("approximate_cardinality.csv", "w")
csv_file.write("Approximate Cardinality - Error = 25%" + "\n")
def extractData(filepath):
    log_file = open(filepath, "r")
    log_file_content = log_file.readlines()
    
    str = "";

    for line in log_file_content:
        line = line.strip()
	if line == "" :
		break
	elif line[0:5] == "Event":
		str = line.split(",")[1].split(":")[1].strip() + "\n"
		csv_file.write (str)
		print(str)
		str = ""
	

extractData("approximate_cardinality.txt")
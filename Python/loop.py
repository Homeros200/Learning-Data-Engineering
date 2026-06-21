#Check whether any filename appears more than once 
#Print "Duplicate found" if a duplicate exists, 
#otherwise print "All files are unique."
file_list = [
    "report.csv", 
    "data.xlsx", 
    "summary.docx", 
    "report.csv", 
    "data.csv"
]
dublicate = file_list 

for file in file_list :
    if file_list.count(file) > 1:
        print(f"Dublicate exsist: {file}")
        break
else:
    print("All files are unique.")
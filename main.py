import csv  ## import csv pkg
 
with open('data.csv', mode ='r')as file:   ## open data.csv and refer it as a file
  csvFile = csv.reader(file,delimiter=';') ## read csv content
  next(csvFile) ## skip the header 
  for lines in csvFile:  ## loop every line 
        print(lines) ## print the each row 

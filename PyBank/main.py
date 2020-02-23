#importing the necessary modules
import os
import csv

#defined variables, I set all to zero to later declare it as a string if needed. 

count_of_row = 0
profit_total = 0
avg_total = 0
gr_increase = 0
gr_decrease = 0 
gr_mn_increase = 0
gr_mn_decrease = 0
#ave_value=[]
#sets the location of the csv file 
budget_data = os.path.join('..','PyBank','budget_data.csv')
#open the csv file 
with open (budget_data) as csvfile:
# converts the data into delimited sting, understanding that the comma seperate each data set into each column
    budget_reader = csv.reader(csvfile, delimiter= ",")
#skips the header
    csv_reader = next(csvfile) 
#create the for loop to access the file data
    for row in budget_reader:
     #count the row total  
       count_of_row += 1
     #sums the total of profit and loses
       profit_total += int(row[1])
       avg_total =(profit_total/count_of_row)  #- put the months in an array, list the previous row array and the 

 #gets greatest increase           
       if int(row[1]) > gr_increase:
        gr_increase = int(row[1])
        gr_mn_increase= str(row[0])

#get the greatest decrease, however its not handling the negative numbers. 
    if int(row[1]) < gr_decrease:
        gr_decrease = int(row[1])    
        gr_mn_decrease= str(row[0])

#print to terminal, did not set to F string as I wanted to test defining integers and string 
    print("Financial Analysis:")
    print("---------------------------------")
    print("Total Months:", int(count_of_row))
    print("Total Profit/Losses:", "$" ,int(profit_total))
    print("Total Average:", "$", int(avg_total))
    print("Total Months Increase:", "$", int(gr_increase) , str(gr_mn_increase))    
    print("Total Months Decrease:","$", int(gr_decrease) , str(gr_mn_decrease))  

#print to a text file 
#create the file and specify the Path of the file 
bgt_data = os.path.join ("..", "PyBank", "print_buget_data.txt")
#open the file and set it to write
file=open(bgt_data, 'w', encoding ='utf-8')
#Define what output to print to the TXT file 
file.write(f"Financial Analysis \n")
file.write(f'------------------------------------ \n')
file.write(f'Total Months: {count_of_row} \n')
file.write(f'Total Profit/Losses: ${profit_total} \n')
file.write(f'${avg_total} \n')
file.write(f"Total Increase: ${(gr_increase)} {(gr_mn_increase)} \n")  
file.write(f'Total Decrease: ${(gr_decrease)} {(gr_mn_decrease)} \n')
file.close


#ref site https://dfrieds.com/python/read-in-csv-files.html   https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python 
#https://www.programiz.com/python-programming/file-operation
#
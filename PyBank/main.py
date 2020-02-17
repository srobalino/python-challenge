import os
import csv

budget_data = os.path.join('..','PyBank','budget_data.csv')
count_of_row = 0
profit_total = 0
avg_total = 0
gr_increase = 0
gr_decrease = 0 
gr_mn_increase = 0
gr_mn_decrease = 0
with open (budget_data) as csvfile:
   
    budget_reader = csv.reader(csvfile, delimiter= ",")
    csv_reader = next(csvfile)

    for row in budget_reader:
     #count the row total  
       count_of_row += 1
     #sums the total of profit and loses
       profit_total += int(row[1])
       avg_total =(profit_total/count_of_row)

 #gets greatest increase           
       if int(row[1]) > gr_increase:
        gr_increase = int(row[1])
        gr_mn_increase= row[0]

#get the greatest decrease
    if int(row[1]) < gr_decrease:
        gr_decrease = int(row[1])
        gr_mn_decrease= row[0]

    print("Financial Analysis:")
    print("---------------------------------")
    print("Total Months:", int(count_of_row))
    print("Total Profit/Losses:", int(profit_total))
    print(int(avg_total))
    print("Total Increase:", int(gr_increase) , str(gr_mn_increase))    
    print("Total Decrease", int(gr_decrease) , str(gr_mn_decrease))  
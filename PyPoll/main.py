import os 
import csv

tl_votes = 0
name = []
length = []
percent_vote =0
tl_v_won = 0

election_data = os.path.join ('..','PyPoll','election_data.csv')

with open (election_data, newline="", encoding='utf-8') as csvfile:
    election_reader = csv.reader(csvfile, delimiter= ",")
    csv_reader = next(csvfile)
    
    for row in election_reader:
        tl_votes +=1
  
     
name.append(row[2])
print(tl_votes)
print(name)
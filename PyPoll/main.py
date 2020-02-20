import os 
import csv

tl_votes= 0

election_data = os.path.join('..','PyPoll','election_data.csv')

with open (election_data) as csvfile:
    election_reader = csv.reader(csvfile, delimiter= ",")
    csv_reader = next(csvfile)

for row in csv_reader:
     tl_votes =+ 1

<<<<<<< HEAD
#Import Files
import os
import csv

#Create analysis function:
def analyze_election(file):

    #Declare Variables
    total_votes = 0 
    candidate_list = []
    candidate_votes = {}
    percent_votes_won = []
    winner = ""
    vote_list = []
    candidate_won =[]
    
   

    #Create file path for csv import
    csvpath = os.path.join('Resources', 'election_data.csv')

    # Open the csv and read data with csv reader
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter =',')
        
        #Save the header row
        csv_header = next(csvfile)

        #Create the 'for' loop to loop through each row in election_data.csv
        for row in csvreader:
            voterID = row[0]
            county = row [1]
            candidate = row [2]

            #Add one to the count of total votes to get total number of votes cast
            total_votes += 1

             #Create a list of candidates who received votes and the amount they received
            
            if candidate not in candidate_list:
                candidate_list.append(candidate)
                vote_list.append(1)
            else:
                vote_list[candidate_list.index(candidate)] +=1

                #Percentage of votes each candidate won
                percent_votes_won = [(100/total_votes) * x for x in vote_list] 

                #Winner based on popular vote
                winner= candidate_list[vote_list.index(max(vote_list))]


    #Create a string for printing and save as a text file
    analysis = f"""
    Total Votes:: {total_votes}
    Total Votes Won: {percent_votes_won}
    Winner: {winner}""" 

    #Print the final analysis
    print(analysis)

    #Create a text file using the final analysis
    output_file = "output.txt"
    with open(output_file,"w") as doc:
        doc.write(analysis)

#Create the file path for csv import   
file = os.path.join("election_data.csv")
analyze_election(file)

#Run the function on the path file = os.path.join('election_data.csv')
=======
#Import Files
import os
import csv

#Create analysis function:
def analyze_election(file):

    #Declare Variables
    total_votes = 0 
    candidate_list = []
    candidate_votes = {}
    percent_votes_won = []
    winner = ""
    vote_list = []
    candidate_won =[]
    
   

    #Create file path for csv import
    csvpath = os.path.join('Resources', 'election_data.csv')

    # Open the csv and read data with csv reader
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter =',')
        
        #Save the header row
        csv_header = next(csvfile)

        #Create the 'for' loop to loop through each row in election_data.csv
        for row in csvreader:
            voterID = row[0]
            county = row [1]
            candidate = row [2]

            #Add one to the count of total votes to get total number of votes cast
            total_votes += 1

             #Create a list of candidates who received votes and the amount they received
            
            if candidate not in candidate_list:
                candidate_list.append(candidate)
                vote_list.append(1)
            else:
                vote_list[candidate_list.index(candidate)] +=1

                #Percentage of votes each candidate won
                percent_votes_won = [(100/total_votes) * x for x in vote_list] 

                #Winner based on popular vote
                winner= candidate_list[vote_list.index(max(vote_list))]


    #Create a string for printing and save as a text file
    analysis = f"""
    Total Votes:: {total_votes}
    Total Votes Won: {percent_votes_won}
    Winner: {winner}""" 

    #Print the final analysis
    print(analysis)

    #Create a text file using the final analysis
    output_file = "output.txt"
    with open(output_file,"w") as doc:
        doc.write(analysis)

#Create the file path for csv import   
file = os.path.join("election_data.csv")
analyze_election(file)

#Run the function on the path file = os.path.join('election_data.csv')
>>>>>>> cd330fa6b1d88cd00bb90ef8b9e8398cec61f050
#analyze_election
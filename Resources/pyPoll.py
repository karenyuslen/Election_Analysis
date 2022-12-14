# The data we must retrieve 
# 1, the total number of votes made
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the election based on popular vote.

# add our dependenciess
import csv
import os

# Assign a variable to LOAD a file from a path 
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to SAVE the file to a path 
# for this to work we had to create a folde named analysis in election analysis
# the folder gives election_analysis.txt a place to be saved
file_to_save = os.path.join("analysis", "election_analysis.txt")


# initialize total votes.
#  We inizialize here so that everytime we run the file 
#    the total starts off at 0
total_votes = 0   

#empty LIST of candidate options
candidate_options = []

#empty DICTIIONARY
candidate_votes = {}

#empty Winning candidate
winning_candidate = ""

# empty winning count
winning_count = 0

#empty winning percentage
winning_percentage = 0


# OPEN the election results and  the file
with open(file_to_load) as election_data:

     # READ the file object with the reader function.
      file_reader = csv.reader(election_data)

     # read the header row.
      headers = next(file_reader)
      #print(headers)

     # Print each row in the CSV file.
      for row in file_reader:

          # add to total vote count
          total_votes = total_votes +1

          #print the candidate name from each row
          candidate_name = row[2]


          #if the candidate doesnt match any existing candidate then..
          if candidate_name not in candidate_options:

               # add the candidate name to the candidate list
               candidate_options.append(candidate_name)

               #begin tracking candidates vote count by
               #  making each candidate a key and their vote count 0
               candidate_votes[candidate_name] = 0

          #add a vote to the candidates count
          candidate_votes[candidate_name] += 1


# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
     # 2. Retrieve vote count of a candidate.
     votes = candidate_votes[candidate_name]
     # 3. Calculate the percentage of votes.
     vote_percentage = float(votes) / float(total_votes) * 100
     # 4. Print the candidate name and percentage of votes.
     print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


     # Determine winning vote count and candidate
     # 1. Determine if the votes are greater than the winning count.
     if (votes > winning_count) and (vote_percentage > winning_percentage):
          # 2. If true then set winning_count = votes and winning_percent =
          # vote_percentage.
          winning_count = votes
          winning_percentage = vote_percentage
          # 3. Set the winning_candidate equal to the candidate's name.
          winning_candidate = candidate_name


winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)




     
# The data we must retrieve 
# 1, the total number of votes made
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the election based on popular vote.

# add our dependenciess
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

     # Read the file object with the reader function.
      file_reader = csv.reader(election_data)

     # Print the header row.
      headers = next(file_reader)
      print(headers)

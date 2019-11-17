import csv
import os

input_file = os.path.join("/Users/Liz/Desktop/", "election_data.csv")
output_file = os.path.join("/Users/Liz/Desktop/", "election_analysis.txt")

total_votes = 0
candidate_choices = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

with open(input_file) as votes:
    reader = csv.reader(votes)

    header = next(reader)

# add all candidates & votes
    for row in reader:

        print(". ", end=""),

        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidate_choices:
            candidate_choices.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

voter_choice = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
        f"{voter_choice}\n"
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
print(results)

with open(output_file, "w") as txt_file:
    txt_file.write(results)
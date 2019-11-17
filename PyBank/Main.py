import csv
import os

input_file = os.path.join("/Users/Liz/Desktop/", "budget_data.csv")
output_file = os.path.join("/Users/Liz/Desktop/", "budget_analysis.txt")

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]
total_net = 0

with open(input_file) as finances:
    reader = csv.reader(finances)

    header = next(reader)

    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1])

    for row in reader:

        # total months
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # net total profit/loss
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# profit/loss change over total
net_average = sum(net_change_list) / len(net_change_list)

summary = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(summary)

with open(output_file, "w") as txt_file:
    txt_file.write(summary)
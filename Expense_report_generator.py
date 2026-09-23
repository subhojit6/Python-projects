file_path = "C:/Users/subho/Downloads/transactions.csv"
report_path = "C:/Users/subho/Downloads/report.csv"

def read_csv(file_path):
    with open(file_path, "r") as file:
        file.readline()
        total = 0
        category_totals = {}
        for line in file:
            line = line.strip()
            data = line.split(",")
            amount = float(data[2])
            category = data[3]
            category_totals[category] = category_totals.get(category, 0) + amount
            total += amount

    with open(report_path, "w") as file:
        file.write("EXPENSE REPORT\n")
        file.write("==============\n")
        file.write(f"Total spent: ${total}\n")
        file.write("\n")
        file.write("By category:")
        for key, value in category_totals.items():
            file.write(f"{key.capitalize()}: ${value}\n")

read_csv(file_path)
    
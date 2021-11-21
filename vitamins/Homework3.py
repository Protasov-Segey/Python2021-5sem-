import json
import csv

json_data = []
description = ["vitamin", "vitamers", "solubility", "daily_requirement", "deficiency_diseases"]
path = 'C:\\Users\\serik\\Desktop\\GitHab\\Python2021\\vitamins\\vitamins(1)'

сsv_file = open("vitamins.csv", "w")
file_writer = csv.writer(csv_file)
file_writer.writerow(description)

for file_name in os.listdir(path):
    with open(file_name) as curr_file: 
        curr_file_read = curr_file.readlines()
        for i in range(len(curr_file_read)-1) :
            curr_file_read[i] = curr_file_read[i].strip()
        curr_file_read[1] = curr_file_read[1].split(', ')
        curr_file_read[4] = curr_file_read[4].split(', ')
        file_writer.writerow(curr_file_read)                 # здесь теперь записывается каждый файл на преобразование в csv формат
        for j in range(len(description)):
            d = {description[j] : curr_file_read[j] for j in range(len(description))}
        json_data.append(d)

сsv_file.close()

with open("vitamins.json", "w") as json_file :
    json.dump(json_data, json_file)

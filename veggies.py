
#write a csv file
import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

with open('/home/tamako/Development/python-lessons/vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'color', 'name length'])  # Write the header row
    for veg in vegetables:
        writer.writerow([veg['name'], veg['color'], len(veg['name'])])
 
#read the csv file
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(rows)


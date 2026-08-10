import csv

csv_files = [
    'data/daily_sales_data_0.csv', 
    'data/daily_sales_data_1.csv', 
    'data/daily_sales_data_2.csv'
]

final_data = []

for file_path in csv_files:
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        
        for row in reader:
            product = row[0]
            price_string = row[1]
            quantity = int(row[2])
            date = row[3]
            region = row[4]
            
            if product == 'pink morsel':
                price = float(price_string.replace('$', ''))
                sales = price * quantity
                final_data.append([sales, date, region])

with open('formatted_data.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['sales', 'date', 'region'])
    writer.writerows(final_data)

print("Finished formatting the data!")
import csv 
import json
import datetime
import statistics

def parse_txt(file_name):
    """
    Reads a .txt file formated in lines.
    Climate Data: Temperature, humidity and pressure.
    Returns a list of dictionaries with one dictionary for every line with the data.
    """
    data=[]
    current_date = datetime.date(2025, 1, 1)
    with open(file_name) as file:
        for line in file:
            line=line.strip()
            parts=line.split(',')
            temperature=int(parts[0].split(':')[1].strip())
            humidity=int(parts[1].split(':')[1].strip())
            pressure=int(parts[2].split(':')[1].strip())
            data.append({
                'date': current_date.isoformat(),
                'temperature':temperature, 
                'humidity': humidity, 
                'pressure': pressure
            })

            # Incrementamos la fecha en un día
            current_date += datetime.timedelta(days=1)
    return data

def parse_csv(file_name):
    """
    Reads a .csv file formated in lines.
    Climate Data: Temperature, humidity and pressure.
    Returns a list of dictionaries with one dictionary for every line with the data.
    """
    data=[]
    with open(file_name, encoding='utf-8') as file:
        reader= csv.DictReader(file)
        for row in reader:
            data.append({
                'date': row['fecha'],
                'temperature':int(row['temperatura']), 
                'humidity': int(row['humedad']), 
                'pressure': int(row['presion'])
            })
    return data

def parse_json(file_name):
    """
    Reads a .json file formated in lines.
    Climate Data: Temperature, humidity and pressure.
    Returns a list of dictionaries with one dictionary for every line with the data.
    """
    data=[]
    with open(file_name, 'r',encoding='utf-8') as file:
        json_data=json.load(file)
        for item in json_data:
            data.append({
                'date': item['fecha'],
                'temperature':int(item['temperatura']), 
                'humidity': int(item['humedad']), 
                'pressure': int(item['presion'])
            })
    return data

def unify_data(list_of_datasets):
    """
    combines lists of dictionaries in one list
    """
    unified=[]
    for dataset in list_of_datasets:
        unified.extend(dataset)
    return unified

def calculate_statistics(data):
    """
    calculates descriptive statistics for  Temperature, humidity and pressure.
    returns a dictionary with the calculations.
    """
    date = [row['date'] for row in data] 
    temperature = [row['temperature'] for row in data] 
    humidity = [row['humidity'] for row in data] 
    pressure = [row['pressure'] for row in data]

    stats = {
        'temperature':{
            'mean': statistics.mean(temperature),
            'median': statistics.median(temperature),
            'mode': statistics.mode(temperature),
            'stdev': statistics.stdev(temperature)
        }, 
        'humidity':{
            'mean': statistics.mean(humidity),
            'median': statistics.median(humidity),
            'mode': statistics.mode(humidity),
            'stdev': statistics.stdev(humidity)
        }, 
        'pressure':{
            'mean': statistics.mean(pressure),
            'median': statistics.median(pressure),
            'mode': statistics.mode(pressure),
            'stdev': statistics.stdev(pressure)
        }
    } 

    return stats

def write_report(data, stats, filename="climate_report.txt"):
    """
    Generates a report in a .txt file that compiles the stats of the given data.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('CLIMATE REPORT\n')
        file.write(f'Days analyzed: {len(data)}\n')
        file.write('='*40 + '\n\n')

        file.write("CLIMATE TEMPERATURE STATISTICS\n")
        file.write(f"- Mean: {stats['temperature']['mean']}\n")
        file.write(f"- Median: {stats['temperature']['median']}\n")
        file.write(f"- Mode: {stats['temperature']['mode']}\n")
        file.write(f"- Standar Deviation: {stats['temperature']['stdev']}\n\n")

        file.write("CLIMATE HUMIDITY STATISTICS\n")
        file.write(f"- Mean: {stats['humidity']['mean']}\n")
        file.write(f"- Median: {stats['humidity']['median']}\n")
        file.write(f"- Mode: {stats['humidity']['mode']}\n")
        file.write(f"- Standar Deviation: {stats['humidity']['stdev']}\n\n")

        file.write("CLIMATE PRESSURE STATISTICS\n")
        file.write(f"- Mean: {stats['pressure']['mean']}\n")
        file.write(f"- Median: {stats['pressure']['median']}\n")
        file.write(f"- Mode: {stats['pressure']['mode']}\n")
        file.write(f"- Standar Deviation: {stats['pressure']['stdev']}\n\n")

    print(f"Report generated: {filename}")

if __name__ == "__main__":
    # 2. Parse input data
    txt_data = parse_txt("january_climate.txt")
    csv_data = parse_csv("february_climate.csv")
    json_data = parse_json("march_climate.json")

    # 3. Unify all data
    all_data = unify_data([txt_data, csv_data, json_data])

    # 4. Calculate statistics
    stats = calculate_statistics(all_data)

    # 5. Generate report
    write_report(all_data, stats, filename="climate_report.txt")
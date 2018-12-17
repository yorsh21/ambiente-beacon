import csv
import datetime
import random
import json

with open('devices.json', 'r') as infile:
    devices = json.load(infile)

for device in devices:
    date = datetime.datetime(year=2017, month=1, day=1)

    record = []
    record.append(int(random.randint(20, 32)))
    record.append(int(random.randint(57, 65)))
    record.append(int(random.randint(50, 100)))
    record.append(int(random.randint(75, 85)))

    for i in range(364):
        #text_date = date.strftime("%d-%m-%Y")
        text_date = date.strftime("%Y-%m-%d")

        autumn = [3, 4, 5, 6]
        winter = [7, 8, 9]
        spring = [10, 11]
        summer = [12, 1, 2]
        prev = record[:]
        record = []

        # otoño
        if date.month in autumn:
            if (random.randint(0,2) == 1):
                record.append(int(random.randint(17, 24)))
                record.append(int(random.randint(71, 84)))
                record.append(int(random.randint(50, 100)))
                record.append(int(random.randint(75, 85)))
                record.append(text_date)
            else:
                record.append(prev[0] + int(random.randint(-2, 2)))
                record.append(prev[1] + int(random.randint(-5, 5)))
                record.append(prev[2] + int(random.randint(-10, 10)))
                record.append(prev[3] + int(random.randint(-4, 4)))
                record.append(text_date)


        # invierno
        elif date.month in winter:
            if (random.randint(0,2) == 1):
                record.append(int(random.randint(10, 18)))
                record.append(int(random.randint(78, 84)))
                record.append(int(random.randint(190, 250)))
                record.append(int(random.randint(75, 85)))
                record.append(text_date)
            else:
                record.append(prev[0] + int(random.randint(-2, 2)))
                record.append(prev[1] + int(random.randint(-5, 5)))
                record.append(prev[2] + int(random.randint(-10, 10)))
                record.append(prev[3] + int(random.randint(-4, 4)))
                record.append(text_date)


        # primavera
        elif date.month in spring:
            if (random.randint(0,2) == 1):
                record.append(int(random.randint(18, 25)))
                record.append(int(random.randint(63, 78)))
                record.append(int(random.randint(150, 170)))
                record.append(int(random.randint(75, 85)))
                record.append(text_date)
            else:
                record.append(prev[0] + int(random.randint(-2, 2)))
                record.append(prev[1] + int(random.randint(-5, 5)))
                record.append(prev[2] + int(random.randint(-10, 10)))
                record.append(prev[3] + int(random.randint(-4, 4)))
                record.append(text_date)


        # verano
        elif date.month in summer:
            if (random.randint(0,2) == 1):
                record.append(int(random.randint(25, 34)))
                record.append(int(random.randint(57, 65)))
                record.append(int(random.randint(50, 100)))
                record.append(int(random.randint(75, 85)))
                record.append(text_date)
            else:
                record.append(prev[0] + int(random.randint(-2, 2)))
                record.append(prev[1] + int(random.randint(-5, 5)))
                record.append(prev[2] + int(random.randint(-10, 10)))
                record.append(prev[3] + int(random.randint(-4, 4)))
                record.append(text_date)


        device["data"].append(record)
        date += datetime.timedelta(days=1)


with open('data2017.js', 'w', newline='') as outfile:
    json.dump(devices, outfile)

store = open('data2017.js', "r")
text = store.read()
store.close()

output = open('data2017.js', "w")
output.write("let sensors = " + text)
output.close()
    
print("Finished")


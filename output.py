import serial, time,csv, datetime
#Change communication port number to appropriate port number
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["time", "motion"]
    writer.writerow(field)

serport=serial.Serial('COM3',115200)
while True:
    # using now() to get current time
    current_time = datetime.datetime.now()
    buffer=serport.readline()
    print(buffer.decode())
    with open('output.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([current_time, buffer.decode()])
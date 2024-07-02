import serial
import csv
import datetime

# Change communication port number to appropriate port number
serport = serial.Serial('/dev/cu.usbserial-57670014761', 115200)

total_movement_time = 0
total_idle_time = 0
avg_movement_time = 0
avg_idle_time = 0
movement_count = 0
idle_count = 0
previous_time = None
previous_state = None

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "State", "Duration", "Total Idle Time", "Total Movement Time", "Average Idle Time", "Average Movement Time"])

while True:
    current_time = datetime.datetime.now()
    buffer = serport.readline().decode().strip()

    if "Movement detected!" in buffer:
        current_state = "Movement"
        movement_count += 1
    elif "No movement." in buffer:
        current_state = "Idle"
        idle_count += 1
    else:
        current_state = "Unknown"

    if previous_state is not None:
        duration = round((current_time - previous_time).total_seconds(), 2)
        if previous_state == "Movement":
            total_movement_time += duration
            avg_movement_time = total_movement_time / movement_count
        elif previous_state == "Idle":
            avg_idle_time = total_idle_time / idle_count
            total_idle_time += duration

    with open('output.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([current_time, current_state, duration if previous_state else 0, total_movement_time, total_idle_time, avg_movement_time, avg_idle_time])

    previous_time = current_time
    previous_state = current_state

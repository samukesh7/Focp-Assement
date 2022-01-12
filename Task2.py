print("Speed Analysis Version 1.0")
data = [] # List for storing the data
while True:
    read = input("Enter the next reading: ")

    if read == "": # Ending the loop if read is empty
        break

    if ((read[0].upper() != "U") and (read[0].upper()!= "E")) or any(char.isalpha() for char in read[1:]):
        print("Invalid Input Format!")
        continue
    
    if read.capitalize()[0] == "U":
        data_in_miles = float(read[1:])
        data.append(data_in_miles)
    elif read.capitalize()[0] == "E":
        data_in_km = float(read[1:])
        data.append(data_in_km/1.60934)

if data == []:
    print("No Readings Entered. \nNothing to do.")

else:
    print("Reading Summary")

    max_data_miles = max(data)
    max_data_km = max_data_miles * 1.60934
    min_data_miles = min(data)
    min_data_km = min_data_miles * 1.60934
    average_data_miles = sum(data)/len(data)
    average_data_km = average_data_miles * 1.60934
    print(f"Max Speed : {max_data_km:.1f} kph,{max_data_miles:.1f} mph")
    print(f"Min Speed : {min_data_km:.1f} kph,{min_data_miles:.1f} mph")
    print(f"Avg Speed : {average_data_km:.1f} kph,{average_data_miles:.1f} mph")
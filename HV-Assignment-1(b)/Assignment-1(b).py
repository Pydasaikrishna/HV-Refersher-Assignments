

#------------------------ printing both keys and values without any input ------------------------
Car = {'Audi' : 'Grey', 'Benz' : 'Blue', 'Verna' : 'Black'}
Data = open("Data_2.txt","a")

print(Car.keys())
print(Car.keys(),file=Data)

print(Car.values())
print(Car.values(),file=Data)

print(Car)
print(Car,file=Data)



# ------------------------- Code Entering the both Car Names and Colours ----------------------------
Car_1 = input("Enter the first Car Name: ")
Colour_1 = input("Enter the Colour for first Car: ")

Car_2 = input("Enter the second Car Name: ")
Colour_2 = input("Enter the Colour for second Car: ")

Car_3 = input("Enter the third Car Name: ")
Colour_3 = input("Enter the Colour for third Car: ")


Car = {Car_1 : Colour_1,Car_2 : Colour_2,Car_3 : Colour_3}

Data = open("Data_2.txt","a")    #creating the file named as "Data_2.txt"

print(Car)
print(Car,file=Data)





#---------------------------- Coding Entering the Car Names---------------------------------
Car_1 = input("Enter first car name: ")
Car_2 = input("Enter second Car name: ")
Car_3 = input("Enter Third Car name: ")
# Car_1,Car_2,Car_3 are the inputs for "keys"

Car = {Car_1 : 'Grey',Car_2 : 'Blue',Car_3 : 'Yellow'}

Data = open("Data_2.txt","a")    #opening the text file named as "Data_2.txt"
# we can use "w" in place of "a"---- here, a=append the data and w=write the data 

print(Car.values())
print(Car.values(),file=Data)         #printing the values from dictonary

print(Car.keys())
print(Car.keys(),file=Data)           #printing the keys from dictonary

for i,p in Car.items():
      print(i,p)
      print(i,p,file=Data)

print(Car)
print(Car,file=Data)                 #printing both the Values and Keys

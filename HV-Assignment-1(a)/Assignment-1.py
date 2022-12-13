Data = open("Data_1.txt","a")      #creating the file named as "Data_1.txt"

Number_1 = int(input("Enter Number_1: "))
Number_2 = int(input("Enter Number_2: "))
Number_3 = int(input("Enter Number_3: "))
Number_4 = int(input("Enter Number_4: "))
Number_5 = int(input("Enter Number_5: "))

Total = Number_1 + Number_2 + Number_3 + Number_4 + Number_5     #adding the all positive numbers

if (Number_1 >= 0) or (Number_2 >= 0) or (Number_3 >= 0) or (Number_4 >= 0) or (Number_5 >= 0):
    print("The sum of all Positive Numbers: ",Total)
    print("The sum of all Positive Numbers:",Total,file=Data)
else:
    print("Please enter the Positive Numbers")
    print("Please enter the Positive Numbers",file=Data)


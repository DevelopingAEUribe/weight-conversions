# Adam Edwards-Uribe
# section 85214-66
# 10/16/22
# Project 9

#this program will ask the user to input a particular letter assigned to a particular measure/weight conversion.
print('This program will convert Inches to Centimeters, Centimeters to Inches,')
print('Grams to Ounces, Kilometers to Miles, or Miles to Kilometers.')
print()

#Functions for measurement/weight calculations.
def ouncesToGrams(ounces):
    return ounces*(28.3495231)

def GramsToOunces(grams):
    return grams/(28.3195231)

def InchesToCentimeters(inches):
    return inches*(2.54)
    
def CentimetersToInches(cent):
    return cent*(0.393701)
    
def KmToMiles(km):
    return km*(0.621371)

def MilesToKm(miles):
    return miles*(1.60934)

# int variable
runAgain = 'y'

#start program loop
while runAgain == 'y':

#get user letter input
    print("Enter I to convert from Inches to Centimeters.\nEnter C to convert Centimeters to Inches.\nEnter O to convert from Ounces to Grams.\nEnter G to convert Grams to ounces.\nEnter M to convert Miles to Kilometers.\nEnter K to convert Kilometers to Miles.")
    print()
    n= str(input("Enter the type of conversion you would like to do: ").upper())
    print()
#Display user input conversions
    if n=='O':
        ounces=int(input("Enter a measure/weight to convert: "))
        print()
        print(ounces," Ounces equals ","{:.2f}".format(ouncesToGrams(ounces)),"grams\n")
    elif n=='G':
        grams=int(input("Enter a measure/weight to convert: "))
        print()
        print(grams,"grams equals ","{:.2f}".format(GramsToOunces(grams)),"ounces\n")
    elif n=='I':
        inches=int(input("Enter a measure/weight to convert: "))
        print()
        print(inches,"inches equals ","{:.2f}".format(InchesToCentimeters(inches)),"centimeters\n")
    elif n=='C':
        centimeters=int(input("Enter a measure/weight to convert: "))
        print()
        print(centimeters,"centimeters equals ","{:.2f}".format(CentimetersToInches(centimeters)),"inches\n")
    elif n=='K':
        km=int(input("Enter a measure/weight to convert: "))
        print()
        print(km,"kilometers equals ","{:.2f}".format(KmToMiles(km)),"miles\n")
    elif n=='M':
        miles=int(input("Enter a measure/weight to convert: "))
        print()
        print(miles,"miles equals ","{:.2f}".format(MilesToKm(miles)),"kilometers\n")
 
#User input for run again loop
    runAgain= input('Would you like to run the program again? (y/n): ')
    runAgain = runAgain.lower()

#error check for run again input
    while runAgain != 'y' and runAgain != 'n':
       runAgain = input('INPUT ERROR: Please enter a y or n: ')
       runAgain = runAgain.lower ()
       print()
#exit message       
print('Have a nice day.')
    
       

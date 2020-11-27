########## CONVERT CELSIUS TO FAHRENHEIT and Vice Versa ##########



# ask user for current temp and store in a variable
currentTemp = input('ENTER YOUR CURRENT TEMPERATURE: ')

# ask user if their current temp is in Celsius or Fahrenheit
geo = input('CELCIUS OR FAHRENHEIT? ( C OR F ): ')


# perform equation
if geo == "c" or geo == "C":
    currentTempCel = currentTemp
else:
    if geo == "f" or geo == "F":
        currentTempFahr = currentTemp

# create variables for Celsius equation


# from Fahrenheit to Celsius
currentTempFromFahr = (float(currentTemp) * 1.8 + 32)

# from Celsius to Fahrenheit
currentTempFromCel = (float(currentTemp) / 1.8 - 32)


# display answer
if geo == "c" or geo == "C":
    print("Your current temperautre is " + "\n" 
    + currentTemp + " Celsius" + "\n"
    + str(currentTempFromFahr) + " Fahrenheit")
else:
    if geo == "f" or geo == "F":
        print("Your current temperautre is " + "\n" 
        + currentTemp + " Fahrenheit" + "\n"
        + str(currentTempFromCel) + " Celsius")
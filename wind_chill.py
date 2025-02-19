def calculates_wind(t, v):
    """
    it calculates the wind chill in fahrenheit
    """
    # for wind_speed in range(5, 61, 5):
    wind_chill = 35.74 + (0.6215 * t) - 35.75 * (v ** 0.16) + (0.4275 * t) * (v ** 0.16)
    return wind_chill

def converts_fahrenheit(t):
    fahrenheit = t * (9 / 5) + 32
    return fahrenheit

# it will loop the whole code again if the user wants to try another temperature
while True:
    # prompt the temperature from the user
    temperature = float(input("What is the temperature? "))

    # it will loop the question for fahrenheit or celsius
    while True:
        # ask if the temperature is in fahrenheit or in celcius
        fahrenheit_or_celcius = str(input("Fahrenheit or Celsius (F/C)? ")).lower()

        if fahrenheit_or_celcius == "f" or fahrenheit_or_celcius == "c":
            break
        
        else:
            print("Sorry, you need to insert C or F for the temperature.")

    # if the temperature is in fahrenheit
    if fahrenheit_or_celcius == "f":
        print()
        for wind_speed in range(5, 61, 5):
            result = calculates_wind(temperature, wind_speed)
            print(f"At temperature {temperature}°F, and wind speed {wind_speed}mph, the windchill is: {result:.2f}°F")

    # if the temperature is in celsius
    elif fahrenheit_or_celcius == "c":
        temperature = converts_fahrenheit(temperature)

        print()
        for wind_speed in range(5, 61, 5):
            result = calculates_wind(temperature, wind_speed)
            print(f"At temperature {temperature}°F, and wind speed {wind_speed}mph, the windchill is: {result:.2f}°F")
    
    print()
    another_temperature = str(input("Do you want to try another temperature? ")).lower()

    if another_temperature == "n":
        print("Thank you for using. Goodbye.")
        break

    elif another_temperature == "s":
        print()
        print("New temperature:")

# Write a program that displays a table of the Celsius temperatures 0 through 20
# and their Fahrenheit equivalents. The formula for converting a temperature
# from Celsius to Fahrenheit is F = ( 9 / 5 )C + 32
# or Fahrenheit = 9.0/5.0 * Celsius + 32
# 10/28/2018
# CTI-110 P4HW2-Celsius to Fahrenheit Table
# Christian Carter

print("Celsius temperature\tFahrenheit Equivalent" )
for currentCelsiusTemperature in range( 21 ):
    fahrenheitTemperatureEquivalent = ( 9 / 5 ) * currentCelsiusTemperature + 32
    print( currentCelsiusTemperature,"\t\t\t\t", format( fahrenheitTemperatureEquivalent, ".1f" ) )

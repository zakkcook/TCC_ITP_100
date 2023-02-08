"""
write a program that uses nested loops to draw this pattern:

*******
******
*****
****
***
**
*
"""

rows = 7
result = ""

for r in range(rows, 0, -1):  # Loop from 7(rows) to 1
    result = ""  # Set result to empty string each time we start
    for star in range(0, rows):  # Loop from 0 to 6 (e.g. 7times, based on row)
        result = result + "*"  # Add a star to the result

    print(result)  # print the result
    result = ""  # reset result to be an empty string
    rows = rows - 1  # Reset next stars_tto_print to be the next count

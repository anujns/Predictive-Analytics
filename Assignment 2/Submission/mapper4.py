#!/usr/bin/python3
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split("\t")

    employeeId = "NA"
    name_column = "NA"
    sal = "NA"
    passcode = "NA"
    country = "NA"

    # Skipping the first row.
    if line[0] == "Employee ID":
        continue

    # If the the data is from join 1.
    if len(line) < 3:
        employeeId = line[0]
        name_column = line[1]

    # If the data is from join 2.
    else:
        employeeId = line[0]
        sal = line[1] + "," + line[2]
        country = line[3]
        passcode = line[4]

    print ('{}\t{}\t{}\t{}\t{}'.format(employeeId,name_column,sal,country,passcode))



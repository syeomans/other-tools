"""
This is me playing around with the Smartsheet API, trying to re-create some of Tyler's work.
"""

import pyodbc
import config
import decimal
from datetime import datetime

def get_2D_array():
	"""
	Runs a query and returns a 2-dimensional array of table data

	:return: List of lists. Outer index is a row, and inner index is a column.  
	:rtype: List
	"""
	# Connection to SQL Server
	sql_connection = pyodbc.connect(config.sql.get('connection'))

	# get Cursor object using the connection
	cursor = sql_connection.cursor()

	# run query
	cursor.execute(config.sql.get('query'))

	# Get the number of columns in the SQL table 
	numColumns = len(cursor.fetchone())

	# Create 2D array
	newTable = []
	for row in cursor:
		newRow = []
		for i in range(0, numColumns):
			# Change decimals to floats
			if isinstance(row[i], decimal.Decimal):
				newRow.append(float(row[i]))
			# Change unicodes to strings and remove extra whitespace
			elif isinstance(row[i], unicode):
				newRow.append(str(row[i].strip()))
			# Add to return structure
			else:
				newRow.append(row[i])
		newTable.append(newRow)
	return(newTable)


# Connection to SQL Server
sql_connection = pyodbc.connect(config.sql.get('connection'))

# get Cursor object using the connection
cursor = sql_connection.cursor()

# run query
cursor.execute(config.sql.get('query'))

# Get the number of columns in the SQL table 
numColumns = len(cursor.fetchone())
outfile = open("output.txt", "w")
for row in cursor:
	outStr = row[0]
	for i in range(1,numColumns):
		outStr += "\t" + str(row[i])
	#print(type(row))
	outfile.write(outStr +"\n")
	# print(row[2])
outfile.close()




# Smartsheet formatting constants
CURRENCY = ',,,,,,,,,,,13,2,1,2,'  # currency + decimalCount + thousandsSeparator + numberFormat
PERCENT = ',,,,,,,,,,,,1,,3,'  # decimalCount + numberFormat
CURRENCY_BOLD = ',,1,,,,,,,,,13,2,1,2,'  # bold + currency + decimalCount + thousandsSeparator + numberFormat
PERCENT_BOLD = ',,1,,,,,,,,,,1,,3,'  # bold + decimalCount + numberFormat
BOLD = ',,1,,,,,,,,,,,,,'  # bold
NONE = ',,,,,,,,,,,,,,,' # no formatting
"""
Format Descriptor Table
Position	Lookup Property		Example Value		Format String
0			fontFamily			0 = Arial, default	"0,,,,,,,,,,,,,,,"
1			fontSize			0 = 8 pt, default	",0,,,,,,,,,,,,,,"
2			bold				1 = on				",,1,,,,,,,,,,,,,"
3			italic				1 = on				",,,1,,,,,,,,,,,,"
4			underline			1 = on				",,,,1,,,,,,,,,,,"
5			strikethrough		1 = on				",,,,,1,,,,,,,,,,"
6			horizontalAlign		2 = center			",,,,,,2,,,,,,,,,"
7			verticalAlign		2 = middle			",,,,,,,2,,,,,,,,"
8			color (text)		4 = #FEEEF0			",,,,,,,,4,,,,,,,"
9			color (background)	8 = #E6F5FE			",,,,,,,,,8,,,,,,"
10			color (taskbar)		9 = #F3E5FA			",,,,,,,,,,9,,,,,"
11			currency			13 = USD			",,,,,,,,,,,13,,,,"
12			decimalCount		3 = 3 decimal places",,,,,,,,,,,,3,,,"
13			thousandsSeparator	1 = on				",,,,,,,,,,,,,1,,"
14			numberFormat		2 = currency		",,,,,,,,,,,,,,2,"
15			textWrap			1 = on				",,,,,,,,,,,,,,,1"
"""





# myTable = get_2D_array()
# for entry in myTable:
# 	print(entry)

weekday = datetime.now().weekday()
print(weekday)


print("Done")
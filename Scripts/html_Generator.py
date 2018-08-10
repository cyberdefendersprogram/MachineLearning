import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# define scopes accept requests
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] 

# create credentials from json keyfile
credentials = ServiceAccountCredentials.from_json_keyfile_name('your key file name', scope)

# authorize the credential
gc = gspread.authorize(credentials)

# Open spreadsheet
wks = gc.open('Your spreadsheet name').sheet1

# Read each row of the spreadsheet
for i in range(0,len(wks.get_all_records())):
	row = wks.get_all_records()[i]

	# data quality table
	df = pd.read_csv("../network/"+row["Name of dataset"].replace(" ","")+".csv")
	columns = pd.DataFrame(list(df.columns.values[1:]))
	#DataFrame with data types
	data_types = pd.DataFrame(df.dtypes, columns=['Data Type'])

	#DataFrame with Count
	data_count = pd.DataFrame(df.count(), columns=['Count'])

	#DataFrame with unique values
	unique_value_counts = pd.DataFrame(columns=['Unique Values'])
	for v in list(df.columns.values):
	    unique_value_counts.loc[v] = [df[v].nunique()]

	missing_data_counts = pd.DataFrame(df.isnull().sum(), columns=['Missing Values'])
	data_quality_report = data_types.join(data_count).join(unique_value_counts).join(missing_data_counts)
	
	# Open a new html file
	f = open(row["Name of dataset"].replace(" ","")+".html",'w')

	'''
	Customize content of html files
	'''
	message = "<html style='margin-left:50px'>"
	message += "<head></head>"
	message += "<body>" 
	message += "<a href='http://www.secrepo.com/'>Home</a>" 
	message += "<h1>" + row["Name of dataset"].upper() + "</h1>"
	message += "<p>Download: <a href='http://www.secrepo.com'>"+row["Name of dataset"]+" </a> Zip File</p>"
	message += "<h3>Abstract</h3>"
	message += "<ul>"
	message += "<table style='border: 1px solid black'>"
	message += "<tr>"
	message += "<th style='border: 1px solid black'>Number of Instances:</th>"
	message += "<th style='border: 1px solid black'>"+str(row['num of instances'])+"</th>"
	message += "<th style='border: 1px solid black'>Security Area:</th>"
	message += "<th style='border: 1px solid black'>"+row['Security Area']+"</th>"
	message += "</tr>"
	message += "<tr>"
	message += "<th style='border: 1px solid black'>Number of Attributes: </th>"
	message += "<th style='border: 1px solid black'>"+str(row['Number of attributes'])+"</th>"
	message += "<th style='border: 1px solid black'>Date Donated: </th>"
	message += "<th style='border: 1px solid black'>"+ str(row['Data Donated'])+"</th>"
	message += "</tr>"
	message += "<tr>"
	message += "<th style='border: 1px solid black'>Missing Values? </th>"
	message += "<th style='border: 1px solid black'>"+str(row['Missing data'])+"</th>"
	message += "<th style='border: 1px solid black'>Associated ML Tasks: </th>"
	message += "<th style='border: 1px solid black'>"+ str(row['Associated Tasks'])+"</th>"
	message += "</tr>"
	message += "</table>"
	message += "</ul>"
	message += "<h3>Source</h3>"

	# Split elements of Source section
	source = row["Source"].split(",")
	for item in source:
		message += "<p style='width: 600px'>"+item+"</p>"
	message += "<h3>Dataset Information</h3>"
	message += "<p style='width: 600px'>"+row["Information"]+"</p>"
	message += "<h3>Attribute Information</h3>"
	message += "<ul>"
	message += data_quality_report.to_html()
	message += "</ul>"
	message += "<h3>Relevant Papers</h3>"

	# Split elemnts Relevant Papers section
	relevant = row["Relevant Papers"].split(";")
	for item in relevant:
		message += "<p style='width: 600px'>"+item.split("|")[0]+"<a href='"+item.split("|")[1]+"'>"+item.split("|")[1]+"</a></p>"
	message += "<h3>Associate Data Science Notebook</h3>"
	message += "<a href='"+row['Associate Data Science Notebook:']+"'>"+row['Associate Data Science Notebook:']+"</a>"
	message += "</body>"
	message += "</html>"

	# Write the content into the file
	f.write(message)

	# Close the file after work
	f.close()
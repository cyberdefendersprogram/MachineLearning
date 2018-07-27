import csv

# Create a log file into a csv file so we can manipulate it with pandas
dhcp_path = '/Users/citlalingalvan/Downloads/dhcp.log'
with open('output.csv', 'w+', encoding='utf-8') as csvfile:
    w = csv.writer(csvfile, dialect='excel')
    with open(dhcp_path, encoding="utf8") as file:
        lines = file.read().split('\n')
        files = []
        for line in lines:
            files.append(line.split('\t'))
        w.writerows(files)
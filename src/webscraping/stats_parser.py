from bs4 import BeautifulSoup

import csv
content = open('/Users/Avadhoot/Downloads/usage_201509.html', 'r').read()
soup = BeautifulSoup(content, 'html.parser')

ATag = soup.find("a", {"name":"DAYSTATS"})
TableElement = ATag.next_element.next_element.next_element;
rows = []
for row in TableElement.find_all('tr'):
    rows.append([val.text.encode('utf8') for val in row.find_all('td')])

with open('output_file.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(row for row in rows if row)

file_names = ['daily.csv', 'hourly.csv', 'top100urls.csv',
              'top10urlsbykbytes.csv',
              'top10entry.csv','top10exitpages.csv','top30sites.csv',
              'top10sites.csv','top30referres.csv','top20searchstrings.csv',
              'top15agents.csv','top30countries.csv','extra.csv','extra.csv','extra.csv']

index = 0
file_index = 0
f = open(file_names[file_index], 'wb')
writer = csv.writer(f)

while(len(rows[index]) == 0):
    index += 1;
while index < len(rows):
    writer.writerow(rows[index])
    index += 1
    if(len(rows[index]) == 0):
        file_index = file_index + 1
        if(file_index < len(file_names)-1):
            f = open(file_names[file_index], 'wb')
            writer = csv.writer(f)
        while(len(rows[index]) == 0):
            index += 1;
            if(index == len(rows)):
                break



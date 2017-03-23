from bs4 import BeautifulSoup
import csv
import os

data_folder = "../../data/SciMaps-Webalizer-Data/"
out_data_folder = "../../data/output/"

def extract_data(filename):
    content = open(data_folder + filename, 'r').read()
    soup = BeautifulSoup(content, 'html.parser')

    ATag = soup.find("a", {"name":"DAYSTATS"})
    TableElement = ATag.next_element.next_element.next_element;
    rows = []
    for row in TableElement.find_all('tr'):
        rows.append([val.text.encode('utf8') for val in row.find_all('td')])

    with open('output_file.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(row for row in rows if row)

        out_file_names = ['daily.csv', 'hourly.csv', 'top100urls.csv',
                  'top10urlsbykbytes.csv',
                  'top10entry.csv','top10exitpages.csv','top30sites.csv',
                  'top10sites.csv','top30referres.csv','top20searchstrings.csv',
                  'top15agents.csv','top30countries.csv','extra.csv','extra.csv','extra.csv']

    index = 0
    file_index = 0
    out_file_name_prefix = filename.replace(".html", "_")
    f = open(out_data_folder + out_file_name_prefix + out_file_names[file_index], 'wb')
    writer = csv.writer(f)

    while(len(rows[index]) == 0):
        index += 1;
    while index < len(rows):
        writer.writerow(rows[index])
        index += 1
        if(len(rows[index]) == 0):
            file_index = file_index + 1
            if(file_index < len(out_file_names)-1):
                f = open(out_data_folder + out_file_name_prefix + out_file_names[file_index],'wb')
                writer = csv.writer(f)
            while(len(rows[index]) == 0):
                index += 1;
                if(index == len(rows)):
                    break




for filename in os.listdir(data_folder):
    if filename.endswith(".html"):
        extract_data(filename)
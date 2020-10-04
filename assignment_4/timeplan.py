from bs4 import BeautifulSoup
import pandas as pd
import requests

timeplan_url = "http://timeplan.uit.no/emne_timeplan.php?sem=20h&module%5B%5D=BED-2056-1&View=list"
scraped_content = BeautifulSoup(
    requests.get(timeplan_url).content, "html.parser")
course_tables = scraped_content.find_all('tr', class_='table-primary')
timeplan = pd.DataFrame(columns=['Dato', 'Tid', 'Emnekode'])

for table_rows in course_tables:
    table_data = table_rows.find_all('td')
    timeplan = timeplan.append({'Dato': table_data[0].text,
                                'Tid': table_data[1].text,
                                'Emnekode': table_data[3].text}, ignore_index=True)

print(timeplan)

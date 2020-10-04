from bs4 import BeautifulSoup
import pandas as pd
import requests


python_url = "https://www.datacamp.com/courses/tech:python"
r_url = "https://www.datacamp.com/courses/tech:r"

# Scrape the content from page
scraped_content_python = BeautifulSoup(
    requests.get(python_url).content, "html.parser")
scraped_content_r = BeautifulSoup(requests.get(r_url).content, "html.parser")

# Extract courses from content
python_courses = scraped_content_python.find_all(
    'h4', class_='course-block__title')
r_courses = scraped_content_r.find_all('h4', class_='course-block__title')
python_courses = [body.text for body in python_courses]
r_courses = [body.text for body in r_courses]

# Create dataframe for both languages
dataframe_python = pd.DataFrame({"tech": python_courses})
dataframe_python["language"] = 'Python'
dataframe_r = pd.DataFrame({"tech": r_courses})
dataframe_r["language"] = 'R'

# concat and print
dataframe = pd.concat([dataframe_python, dataframe_r])
print(dataframe)

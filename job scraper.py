from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl

data = []

for i in range(2, 11):
    url = f'https://resume.brightspyre.com/jobs?page={i}'  # Assuming pagination is controlled by a page parameter

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find all job titles and links
    result = soup.find_all(class_='text-decoration-none title-job')
    lastdate = soup.find_all(class_='text-muted')

    for job, last in zip(result, lastdate):
        job_title = job.text.strip()  # Extract and clean the job title text
        job_link = job.get('href')  # Extract the href attribute (link)
        last_date = last.text.strip()  # Extract and clean the last date text

        # Construct full URL for the job link
        full_link = f"https://resume.brightspyre.com{job_link}" if job_link else ''

        # Append the extracted information to the data list
        data.append({
            'Job Title': job_title,
            'Last Date': last_date,
            'Link': full_link
        })

# Convert the list of job data into a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel("morejobs2.xlsx", index=False)

print("Data has been saved to 'morejobs.xlsx'")


import json
import time

import requests
from bs4 import BeautifulSoup


def get_jobs():
    times_jobs = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?'
        'searchType=personalizedSearch&from=submit&searchTextSrc=ft&'
        'searchTextText=&txtKeywords=python&txtLocation='
    )
    times_jobs = BeautifulSoup(times_jobs.text, 'lxml')
    job_cards = times_jobs.find_all('li', class_='clearfix job-bx wht-shd-bx')
    jobs = []
    for job_card in job_cards:
        published_date = job_card.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            skills = list(
                map(
                    lambda skill: {"name": skill},
                    job_card.find('span', class_='srp-skills').text
                    .replace(' ', '')
                    .replace('\n', '')
                    .strip()
                    .split(",")
                )
            )
            company_name = (job_card
                            .find('h3', class_='joblist-comp-name').text
                            .replace(' ', '')
                            .replace('\n', '')
                            .strip())
            more_info = job_card.header.h2.a['href']
            job = {
                "company": company_name,
                "skills": f'{skills}',
                "more_info": more_info
            }
            jobs.append(job)
    return json.dumps(jobs)

counter = 0
while True:
    jobs = get_jobs()
    print(get_jobs())
    seconds = 10
    print(f'{counter}: Waiting {seconds} seconds...')
    counter += 1
    time.sleep(seconds * 60)

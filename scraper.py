import requests
from lxml import html
import re

def get_course_summary(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)
    course_summary_elements = tree.xpath('//*[@id="page-content"]/section/p')
    
    if course_summary_elements:
        summary = course_summary_elements[0].text_content().strip()
    else:
        summary = "Summary not found."
    
    return summary

def main():
    with open('courses(1).txt', 'r') as f:
        urls = f.readlines()

    with open('course_summaries.txt', 'w') as f:
        for url in urls:
            url = url.strip()
            summary = get_course_summary(url)

            # Extract course section and number from the URL
            match = re.search(r'/courses/(\w+)/(\d+)\.html', url)
            if match:
                course_section = match.group(1)
                course_num = match.group(2)
            else:
                course_section = "Unknown"
                course_num = "Unknown"

            f.write(f'{course_section} {course_num}: {summary}\n')

if __name__ == '__main__':
    main()

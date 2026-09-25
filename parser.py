import re

from bs4 import BeautifulSoup

def extract_position_table(text):
    tables = re.findall(r"<table\b[^>]*>[\s\S]*?<\/table>", text)[0]
    return tables

def extract_position_rows(tables):
    soup = BeautifulSoup(tables, "html.parser")
    data = soup.find_all("tr")
    if not data:
        return None

    return data[1:]

def get_position_information(position, previous_company):
    soup = BeautifulSoup(str(position), "html.parser")
    table_data = soup.find_all("td")
    if len(table_data) < 5:
        return 

    company = table_data[0].find("a")
    return {
        "company": company.get_text() if company else previous_company,
        "role": table_data[1].get_text(),
        "location": table_data[2].get_text(),
        "link": table_data[3].find("a").get("href"),
        "days_posted": int(table_data[-1].get_text()[:1])
    }
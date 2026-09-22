from bs4 import BeautifulSoup

def extract_simplify_postings(html):
    soup = BeautifulSoup(html, "html.parser")
    data = soup.find_all("tr")
    if not data:
        return None

    return data[1:]

def get_position_information(position, previous_company = None):
    soup = BeautifulSoup(str(position), "html.parser")
    table_data = soup.find_all("td")
    if len(table_data) < 5:
        return None

    company = table_data[0].find("a")
    return {
        "company": company.get_text() if company else previous_company,
        "role": table_data[1].get_text(),
        "location": table_data[2].get_text(),
        "link": table_data[3].find("a").get("href"),
        "days_posted": table_data[-1].get_text()
    }

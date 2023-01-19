import requests
import selectorlib
import ast
from mail_send import send_mail
import time




URL = "http://programmer100.pythonanywhere.com/tours/"
with open("headers.txt", "r") as file:
    h = file.read()


headers_dict = ast.literal_eval(h.strip("HEADERS ="))

def scrape(url):
            # Scrapes page source from URL
    r = requests.get(url, headers=headers_dict)
    text = r.text
    return text

def extraction(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value



if __name__ == "__main__":

    while True:
        scraped_data = scrape(URL)
        print(extraction(scraped_data))
        content = extraction(scraped_data)
        send_mail(content)
        time.sleep(60)

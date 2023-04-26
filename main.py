from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas as pd
from collections import defaultdict
from environs import Env


def get_age_ending(age):
    if 4 < age % 100 < 21:
        return f'{age} лет'
    num = age % 10
    if num == 1:
        return f'{age} год'
    if 1 < num < 5:
        return f'{age} года'
    return f'{age} лет'


if __name__ == '__main__':
    env = Env()
    env.read_env()

    wines_excel_path = env('WINES_EXCEL_PATH')
    categorized_wines = defaultdict(list)
    for wine in pd.read_excel(wines_excel_path, keep_default_na=False).to_dict(orient='records'):
        categorized_wines[wine['Категория']].append(wine)

    env = Environment(loader=FileSystemLoader('.'),
                      autoescape=select_autoescape(['html', 'xml']))

    template = env.get_template('template.html')

    current_year = datetime.date.today().year
    company_foundation_year = 1920
    rendered_page = template.render(
        company_age=get_age_ending(current_year - company_foundation_year),
        categorized_wines=categorized_wines
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

from bs4 import BeautifulSoup
from urllib.parse import urljoin

def parse_html(html_content, base_url):
    links = []
    forms = []
    hidden_inputs = []
    scripts = []

    soup = BeautifulSoup(html_content, "html.parser")


    # Extract all <a> href links
    for a_tag in soup.find_all("a", href=True):
        full_url = urljoin(base_url, a_tag["href"])
        links.append(full_url)

     # Extract all <form> tags
    for form_tag in soup.find_all("form"):
        forms.append(str(form_tag))

    # Extract all <input type="hidden">
    for input_tag in soup.find_all("input", type="hidden"):
        hidden_inputs.append(str(input_tag))

    # Extract all <script src="">
    for script_tag in soup.find_all("script", src=True):
        script_url = urljoin(base_url, script_tag["src"])
        scripts.append(script_url)

    return links, forms, hidden_inputs, scripts


import os
import requests
from urllib.parse import urlparse

def download_html(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"[!] Failed to download HTML from {url}: {e}")
        return ""

def download_scripts(script_urls, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for script_url in script_urls:
        try:
            response = requests.get(script_url, timeout=10)
            response.raise_for_status()

            parsed_url = urlparse(script_url)
            filename = os.path.basename(parsed_url.path)

            if not filename:
                filename = f"script_{script_urls.index(script_url)}.js"

            script_path = os.path.join(output_folder, filename)
            with open(script_path, "w", encoding="utf-8") as f:
                f.write(response.text)

            print(f"[+] Downloaded: {filename}")
        except Exception as e:
            print(f"[!] Failed to download script {script_url}: {e}")


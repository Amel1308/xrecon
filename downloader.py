import os
import random
import requests
from urllib.parse import urlparse

# Random User-Agents za spoofing
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
]

def download_html(url):
    if not url.startswith("https://"):
        if url.startswith("http://"):
            url = url.replace("http://", "https://")
        else:
            url = "https://" + url

    headers = {
        "User-Agent": random.choice(USER_AGENTS)
    }

    try:
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        response.raise_for_status()
        print(f"[+] Successfully fetched HTML from {url}")
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"[!] HTTP error while fetching {url}: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"[!] Request error while fetching {url}: {req_err}")
    except Exception as err:
        print(f"[!] Unknown error while fetching {url}: {err}")
    
    return ""

def download_scripts(script_urls, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for script_url in script_urls:
        if not script_url.startswith("https://"):
            if script_url.startswith("http://"):
                script_url = script_url.replace("http://", "https://")
            else:
                script_url = "https://" + script_url

        headers = {
            "User-Agent": random.choice(USER_AGENTS)
        }

        try:
            response = requests.get(script_url, headers=headers, timeout=10, allow_redirects=True)
            response.raise_for_status()

            parsed_url = urlparse(script_url)
            filename = os.path.basename(parsed_url.path)

            if not filename:
                filename = f"script_{script_urls.index(script_url)}.js"

            script_path = os.path.join(output_folder, filename)
            with open(script_path, "w", encoding="utf-8") as f:
                f.write(response.text)

            print(f"[+] Downloaded: {filename}")
        except requests.exceptions.HTTPError as http_err:
            print(f"[!] HTTP error while downloading script {script_url}: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"[!] Request error while downloading script {script_url}: {req_err}")
        except Exception as err:
            print(f"[!] Unknown error while downloading script {script_url}: {err}")



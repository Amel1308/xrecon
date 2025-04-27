import os
import re

def extract_endpoints(scripts_folder, output_file):
    if not os.path.exists(scripts_folder):
        print("[!] Scripts folder does not exist.")
        return

    endpoints = set()

    js_files = [f for f in os.listdir(scripts_folder) if f.endswith(".js")]

    for js_file in js_files:
        file_path = os.path.join(scripts_folder, js_file)

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

                # Find potential endpoints
                matches = re.findall(r'["\'](\/[a-zA-Z0-9_\/\-\.\?\=\&]+)["\']', content)

                for match in matches:
                    endpoints.add(match)
        except Exception as e:
            print(f"[!] Failed to read {js_file}: {e}")

    if endpoints:
        with open(output_file, "w", encoding="utf-8") as f:
            for endpoint in sorted(endpoints):
                f.write(endpoint + "\n")

        print(f"[+] Extracted {len(endpoints)} endpoints.")
    else:
        print("[!] No endpoints found.")


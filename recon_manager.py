import os

def clean_and_merge_outputs(output_dir="./outputs"):
    files_to_clean = [
        "urls.txt",
        "forms.txt",
        "hidden_inputs.txt",
        "scripts.txt",
        "api_endpoints.txt"
    ]

    for filename in files_to_clean:
        filepath = os.path.join(output_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()

            # Remove duplicates and empty lines
            cleaned_lines = sorted(set(line.strip() for line in lines if line.strip()))

            # Overwrite file with cleaned content
            with open(filepath, "w", encoding="utf-8") as f:
                for line in cleaned_lines:
                    f.write(line + "\n")

            print(f"[+] Cleaned and updated: {filename}")


import argparse
from logo import print_logo
from parser import parse_html
from downloader import download_html, download_scripts
from output_manager import save_outputs
from js_extractor import extract_endpoints
from recon_manager import clean_and_merge_outputs

def get_target():
    parser = argparse.ArgumentParser(description="XRecon - Fast and modular web reconnaissance tool.")
    parser.add_argument("-d", "--domain", help="Target domain to scan", required=False)
    args = parser.parse_args()

    if args.domain:
        return args.domain
    else:
        return input("Enter target domain: ")

def main():
    print_logo()

    # 1. Get the target URL
    target = get_target()

    # 2. Download the HTML content
    html_content = download_html(target)

    # 3. Parse HTML to extract links, forms, hidden inputs, and script sources
    links, forms, hidden_inputs, script_sources = parse_html(html_content, target)

    # 4. Save all extracted data to the outputs folder
    save_outputs(links, forms, hidden_inputs, script_sources, output_dir="./outputs")

    # 5. Download all linked JavaScript files
    download_scripts(script_sources, output_folder="./outputs/scripts")

    # 6. Extract potential API endpoints from the JavaScript files
    extract_endpoints("./outputs/scripts", "./outputs/api_endpoints.txt")

    # 7. Clean and merge all outputs into final files
    clean_and_merge_outputs("./outputs")

if __name__ == "__main__":
    main()











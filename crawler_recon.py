from logo import print_logo
from parser import parse_html
from downloader import download_html, download_scripts
from output_manager import save_outputs
from js_extractor import extract_endpoints
from recon_manager import clean_and_merge_outputs

def main():
    print_logo()


     # 1. Get the target URL from the user
    target_url = input("Enter the target URL: ").strip()

    # 2. Download the HTML content
    html_content = download_html(target_url)

    # 3. Parse HTML to extract links, forms, hidden inputs, and script sources
    links, forms, hidden_inputs, script_sources = parse_html(html_content, target_url)

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










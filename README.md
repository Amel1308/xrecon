# XRecon 🕷️

**XRecon** is a powerful, modular, and lightweight web reconnaissance tool designed to automate the initial information gathering phase during penetration testing.  
It crawls web applications, extracts endpoints, forms, hidden inputs, and JavaScript files to help you quickly map the attack surface.

> 🚀 Built with love by **Amel Žiga**.

---

## ✨ Features

- Full HTML parsing (links, forms, hidden inputs, scripts)
- JavaScript endpoint extraction
- Clean URL normalization and duplicate filtering
- Organized output in structured files
- Easy to extend and customize
- Minimalistic and blazing fast

---

## 🛠️ Installation

🚀 Installation

Clone the repository:

git clone https://github.com/Amel1308/xrecon.git
cd xrecon

Install the required libraries:

pip install requests beautifulsoup4 argparse tldextract

⚡ Usage
Run with manual target input:

python3 xrecon.py

    You will be prompted to enter a target domain manually.

Example:

Enter target domain: target.com

Run by passing the target directly via command-line:

python3 xrecon.py -d terget_url.com

    The scan will start immediately without manual input.

📁 Output Structure

After scanning, the results will be organized inside the outputs/ directory:

outputs/
├── links.txt            # Extracted internal and external links
├── forms.txt            # Extracted form actions
├── hidden_inputs.txt    # Hidden form fields
├── scripts/             # Downloaded JavaScript files
│   └── *.js
├── api_endpoints.txt    # Extracted endpoints from JavaScript
└── final_summary.txt    # Cleaned and merged results

📷 Example Terminal Output

🕷️  XRecon
Created by Amel Žiga

[+] Starting reconnaissance for: yahoo.com
[+] Downloading HTML content...
[+] Parsing links, forms, and scripts...
[+] Saving results to outputs/
[+] Downloading and analyzing JavaScript files...
[+] Reconnaissance completed successfully.

📚 Contributing

We welcome contributions!
Feel free to open issues, suggest new features, or create pull requests.
📄 License

This project is licensed under the MIT License.

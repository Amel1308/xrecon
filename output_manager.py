import os

def save_outputs(links, forms, hidden_inputs, script_sources, output_dir="./outputs"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(os.path.join(output_dir, "urls.txt"), "w", encoding="utf-8") as f:
        for link in links:
            f.write(link + "\n")

    with open(os.path.join(output_dir, "forms.txt"), "w", encoding="utf-8") as f:
        for form in forms:
            f.write(form + "\n\n")

    with open(os.path.join(output_dir, "hidden_inputs.txt"), "w", encoding="utf-8") as f:
        for hidden_input in hidden_inputs:
            f.write(hidden_input + "\n")

    with open(os.path.join(output_dir, "scripts.txt"), "w", encoding="utf-8") as f:
        for script in script_sources:
            f.write(script + "\n")


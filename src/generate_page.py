from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        md_contents = file.read()

    with open(template_path, "r") as file:
        html_template = file.read()

    title = extract_title(md_contents)
    translated_html = markdown_to_html_node(md_contents)._to_html()
    full_html = html_template.replace("{{ Title }}", title).replace("{{ Content }}", translated_html)

    with open(dest_path, "w") as file:
        file.write(full_html)

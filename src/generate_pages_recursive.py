import os
from src.generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if os.path.isfile(dir_path_content):
        html_dest_dir_path = dest_dir_path.replace(".md", ".html")
        generate_page(dir_path_content, template_path, html_dest_dir_path, basepath)
        return
    else:
        all_files = os.listdir(dir_path_content)
        for file in all_files:
            updated_dir_path_content = os.path.join(dir_path_content, file)
            updated_dest_dir_path = os.path.join(dest_dir_path, file)
            generate_pages_recursive(updated_dir_path_content, template_path, updated_dest_dir_path, basepath)

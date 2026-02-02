from copy_to_public_folder import copy_to_public_folder
from generate_page import generate_page

def main():
    copy_to_public_folder()
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()

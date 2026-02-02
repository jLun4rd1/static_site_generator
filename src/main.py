from copy_to_public_folder import copy_to_public_folder
from generate_pages_recursive import generate_pages_recursive

def main():
    copy_to_public_folder()
    generate_pages_recursive("content/", "template.html", "public/")

if __name__ == "__main__":
    main()

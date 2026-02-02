import sys
from src.copy_to_public_folder import copy_to_public_folder
from src.generate_pages_recursive import generate_pages_recursive

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_to_public_folder()
    generate_pages_recursive("content/", "template.html", "docs/", basepath)

if __name__ == "__main__":
    main()

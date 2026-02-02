def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.replace("# ", "").strip()
    raise Exception("No title found in markdown")

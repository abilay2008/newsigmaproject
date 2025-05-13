from pyscript import Element
import re

def clean_line(line):
    return line.strip().lower().replace(",", "").replace(".", "")

def logical_search(line):
    return "python" in line and "project" in line and "error" not in line

def regex_search(line, pattern=r"\bpython\b"):
    return re.search(pattern, line)

def search_text(*args):
    textarea = Element("input-text")
    raw_text = textarea.element.value
    lines = raw_text.splitlines()
    results = []

    for line in lines:
        cleaned = clean_line(line)
        if logical_search(cleaned) or regex_search(cleaned):
            results.append(cleaned)

    results.sort()
    Element("output").write("\n".join(results))

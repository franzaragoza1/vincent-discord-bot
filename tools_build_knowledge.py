"""Genera vincentbot/knowledge.md a partir de la guía y la FAQ de la web (vincent-ai-web)."""
import re, sys, importlib.util
from bs4 import BeautifulSoup
web, out = sys.argv[1], sys.argv[2]

def md(html):
    soup = BeautifulSoup(html, "html.parser")
    for a in soup.find_all("a"):
        href = a.get("href", "")
        if href.startswith("#"): a.replace_with(a.get_text())
        else: a.replace_with(f"{a.get_text()} ({href})")
    for h in soup.find_all("h3"): h.replace_with(f"\n### {h.get_text()}\n")
    for li in soup.find_all("li"): li.replace_with(f"- {li.get_text(' ', strip=True)}\n")
    for tr in soup.find_all("tr"):
        tr.replace_with(" | ".join(c.get_text(" ", strip=True) for c in tr.find_all(["td", "th"])) + "\n")
    for s in soup.find_all("summary"): s.replace_with(f"\nQ: {s.get_text(' ', strip=True)}\nA: ")
    t = soup.get_text("\n")
    t = re.sub(r"[ \t]+", " ", t); t = re.sub(r"\n\s*\n+", "\n\n", t)
    return t.strip()

gdoc = BeautifulSoup(open(f"{web}/guide.html", encoding="utf-8").read(), "html.parser")
parts = []
for main in gdoc.find_all("main", attrs={"data-lang-block": True}):
    head = "SETUP GUIDE (English UI names)" if main["data-lang-block"] == "en" else "GUÍA DE CONFIGURACIÓN (nombres de la interfaz en español)"
    parts.append(f"# {head}\n")
    for sec in main.find_all("section", class_="gsec"):
        title = sec.find(class_="ph").find("span").get_text(" ", strip=True)
        parts.append(f"## {title}\n{md(str(sec.find(class_='gbody')))}\n")

idx = BeautifulSoup(open(f"{web}/index.html", encoding="utf-8").read(), "html.parser")
faq = idx.find(id="faq")
items = []
for d in faq.find_all("details"):
    q = d.find("summary"); p = d.find("p")
    items.append(f"Q: {q.get_text(' ', strip=True)}\nA: {p.get_text(' ', strip=True)}")
parts.append("# WEBSITE FAQ (English)\n" + "\n\n".join(items))
items = []
for d in faq.find_all("details"):
    q = d.find("summary"); p = d.find("p")
    items.append(f"P: {q.get('data-es','')}\nR: {BeautifulSoup(p.get('data-es',''),'html.parser').get_text(' ', strip=True)}")
parts.append("# FAQ DE LA WEB (español)\n" + "\n\n".join(items))
open(out, "w", encoding="utf-8").write("\n\n".join(parts) + "\n")
print(out, len(open(out).read()))

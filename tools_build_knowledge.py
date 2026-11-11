"""Genera vincentbot/knowledge.md a partir de la guía y la FAQ de la web (vincent-ai-web)."""
import re, sys, importlib.util
from bs4 import BeautifulSoup
web, guide_dir, out = sys.argv[1], sys.argv[2], sys.argv[3]

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

def load(n):
    s = importlib.util.spec_from_file_location(n, f"{guide_dir}/{n}.py"); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

parts = []
for lang, name in [("en", "content_en"), ("es", "content_es")]:
    c = load(name)
    head = "SETUP GUIDE (English UI names)" if lang == "en" else "GUÍA DE CONFIGURACIÓN (nombres de la interfaz en español)"
    parts.append(f"# {head}\n")
    for i, t, e, h in c.SECTIONS:
        parts.append(f"## {t}\n{md(h)}\n")

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

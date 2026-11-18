#!/usr/bin/env python3
"""md-wiki: varre uma pasta de .md e gera um INDEX.md com titulo, links entre notas e notas orfas."""
import pathlib, re, sys
def indexar(raiz):
    raiz = pathlib.Path(raiz); notas = {}
    for f in sorted(raiz.rglob("*.md")):
        if f.name == "INDEX.md": continue
        t = f.read_text(errors="ignore"); m = re.search(r"^#\s+(.+)", t, re.M)
        notas[f.stem] = (m.group(1) if m else f.stem, set(re.findall(r"\[\[([^\]|]+)", t)))
    ref = {l for _, ls in notas.values() for l in ls}
    linhas = ["# Indice", ""] + [f"- [[{k}]] {t} ({len(ls)} links)" for k, (t, ls) in notas.items()]
    orf = [k for k in notas if k not in ref]
    return "\n".join(linhas + ["", "## Orfas (ninguem aponta para elas)"] + [f"- {k}" for k in orf])
if __name__ == "__main__": print(indexar(sys.argv[1] if len(sys.argv) > 1 else "."))

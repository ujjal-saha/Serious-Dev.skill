#!/usr/bin/env python3
"""Search the library-first catalog.

Usage:
    python scripts/find_lib.py read excel
    python scripts/find_lib.py parse json --lang cpp
    python scripts/find_lib.py --list

The catalog is the set of tables in the ../references/*.md files.
Each table row looks like:  | Package | Install | Use it for |
"""

import argparse
import re
import sys
from pathlib import Path

REFERENCES = Path(__file__).resolve().parent.parent / "references"

# File name -> friendly language name. Extra words people may type -> file name.
LANG_ALIASES = {
    "python": "python", "py": "python",
    "javascript": "javascript", "js": "javascript", "typescript": "javascript",
    "ts": "javascript", "node": "javascript", "nodejs": "javascript",
    "cpp": "cpp", "c++": "cpp", "cxx": "cpp", "c": "cpp",
    "java": "java",
    "go": "go", "golang": "go",
    "rust": "rust", "rs": "rust",
    "csharp": "csharp", "c#": "csharp", "dotnet": "csharp", ".net": "csharp",
    "php": "other-languages", "ruby": "other-languages", "rb": "other-languages",
    "other": "other-languages", "other-languages": "other-languages",
}

STOPWORDS = {
    "a", "an", "the", "to", "of", "in", "for", "and", "with", "from", "my",
    "i", "it", "on", "is", "how", "do", "or", "some", "using", "use",
}


def stem(word):
    """Very small stemmer so 'scraping', 'scrape' and 'scraper' all match."""
    w = word.lower()
    for suffix in ("ing", "ers", "er", "ed", "es", "s", "e"):
        if w.endswith(suffix) and len(w) - len(suffix) >= 4:
            return w[: -len(suffix)]
    return w


def load_catalog():
    rows = []
    for md in sorted(REFERENCES.glob("*.md")):
        lang = md.stem
        for line in md.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 3:
                continue
            if cells[0].lower() == "package" or set(cells[0]) <= {"-", " "}:
                continue  # header or divider row
            rows.append({"lang": lang, "package": cells[0],
                         "install": cells[1], "use": cells[2]})
    return rows


def main():
    parser = argparse.ArgumentParser(description="Search the library-first catalog.")
    parser.add_argument("words", nargs="*", help="what you want to do, for example: read excel")
    parser.add_argument("--lang", help="filter by language, for example python, cpp, js, java, go, rust, csharp")
    parser.add_argument("--top", type=int, default=8, help="how many results to show (default 8)")
    parser.add_argument("--list", action="store_true", help="show how many packages are in each language")
    args = parser.parse_args()

    rows = load_catalog()

    if args.list:
        counts = {}
        for r in rows:
            counts[r["lang"]] = counts.get(r["lang"], 0) + 1
        for lang, n in sorted(counts.items()):
            print(f"{lang}: {n}")
        print(f"total: {len(rows)}")
        return 0

    if not args.words:
        parser.print_help()
        return 1

    if args.lang:
        key = LANG_ALIASES.get(args.lang.lower())
        if key is None:
            print(f"Unknown language '{args.lang}'. Try: python, js, cpp, java, go, rust, csharp, php, ruby.")
            return 1
        rows = [r for r in rows if r["lang"] == key]

    stems = [stem(w) for w in re.findall(r"[\w#+.]+", " ".join(args.words))
             if w.lower() not in STOPWORDS]
    stems = [s for s in stems if s]
    if not stems:
        print("Please give at least one keyword.")
        return 1

    scored = []
    for r in rows:
        text = f"{r['package']} {r['use']}".lower()
        hits = sum(1 for s in stems if s in text)
        if hits:
            # small bonus when the package name itself matches
            bonus = 0.5 if any(s in r["package"].lower() for s in stems) else 0
            scored.append((hits + bonus, r))

    scored.sort(key=lambda t: (-t[0], t[1]["lang"], t[1]["package"].lower()))

    if not scored:
        print("No match in the catalog.")
        print("Next step: check the standard library. If it cannot do the job, do a quick web")
        print("search (1 to 3 searches) and check the package on its official registry page")
        print("(PyPI, npm, crates.io, pkg.go.dev, Maven Central, NuGet, vcpkg).")
        print("See the 'Quick web search' section in SKILL.md.")
        return 0

    for _, r in scored[: args.top]:
        print(f"[{r['lang']}] {r['package']}")
        print(f"    install: {r['install']}")
        print(f"    use for: {r['use']}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:  # output was cut short, for example with | head
        sys.exit(0)

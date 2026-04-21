"""
MkDocs hook: restructure pymdownx.tabbed HTML for PDF output.

Material renders tabs as:
  .tabbed-labels  [label, label, label]
  .tabbed-content [block, block, block]

WeasyPrint (no JS) only shows the :checked block. This hook rewrites each
.tabbed-set so every label immediately precedes its block, producing stacked
sections instead of a broken tab widget — but only when building for PDF.
"""

import os

from bs4 import BeautifulSoup


def on_page_content(html, page, config, files):
    if not os.environ.get("ENABLE_PDF_EXPORT"):
        return html

    soup = BeautifulSoup(html, "html.parser")

    all_tab_sets = soup.select(".tabbed-set")

    # Process innermost tab sets first so inner restructuring is done before
    # the outer tab set is touched — avoids stale references in nested tabs.
    def nesting_depth(tag):
        return len(tag.find_parents(class_="tabbed-set"))

    for tab_set in sorted(all_tab_sets, key=nesting_depth, reverse=True):
        labels = tab_set.select(".tabbed-labels > label")
        blocks = tab_set.select(".tabbed-content > .tabbed-block")

        if not labels or len(labels) != len(blocks):
            continue

        # Build replacement: [label, block, label, block, ...]
        new_contents = []
        for label, block in zip(labels, blocks):
            label.extract()
            block.extract()
            new_contents.append(label)
            new_contents.append(block)

        # Clear the tab set and insert the flat structure
        tab_set.clear()
        for el in new_contents:
            tab_set.append(el)

    return str(soup)

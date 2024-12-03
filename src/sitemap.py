#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: AGPL-3.0-or-later

from typing import List
import os

dirs: List[str] = ["figs/html", "html"]

URL = "https://certseeds-fork.github.io/twhhu-rfc-translater-zh-cn/"


def get_html_relative_path(path: str) -> List[str]:
    # visit path and list all sub files
    abs_path: str = f"./{path}/"
    list: List[str] = []
    for root, dirs, files in os.walk(abs_path):
        for file in files:
            if file.endswith(".html"):
                list.append(file)
    return list


def get_url_element(path: str) -> str:
    url_element: str = f"""    <url>
        <loc>{URL}{path}</loc>
    </url>
"""
    return url_element


def main() -> None:
    xml: str = get_head()
    xml += get_url_element("index.html")
    for dir in dirs:
        files: List[str] = get_html_relative_path(dir)
        for file in files:
            print(f"{dir}/{file}")
            xml += get_url_element(f"{dir}/{file}")
    xml += get_footer()
    with open("./public/sitemap.xml", "w") as f:
        f.write(xml)


def get_head() -> str:
    head: str = """<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:xhtml="http://www.w3.org/1999/xhtml">
"""
    return head


def get_footer() -> str:
    return "</urlset>"


if __name__ == "__main__":
    main()

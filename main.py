#!/usr/bin/env python3
import os
import shutil
import sys
import zipfile

DEFAULT_META = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<app version="1">
  <name>Wii Homebrew</name>
  <coder>Homebrew</coder>
  <version>1.0</version>
  <release_date>20260905000000</release_date>
  <short_description>Homebrew application</short_description>
  <long_description>Built with devkitPPC.</long_description>
  <arguments>
    <arg/>
  </arguments>
</app>
"""


def main():
    cwd = os.getcwd()
    dols = sorted(f for f in os.listdir(cwd) if f.lower().endswith(".dol"))

    if not dols:
        print(f"No .dol file found in '{cwd}'.")
        sys.exit(1)

    if len(dols) > 1:
        print(f"Multiple .dol files found, please leave only one: {dols}")
        sys.exit(1)

    dol = dols[0]
    src = os.path.join(cwd, dol)
    boot = os.path.join(cwd, "boot.dol")

    if os.path.abspath(src) != os.path.abspath(boot):
        print(f"-> renaming {dol} to boot.dol")
        shutil.move(src, boot)

    meta = os.path.join(cwd, "meta.xml")
    if not os.path.isfile(meta):
        print("-> meta.xml not found, creating default meta.xml")
        with open(meta, "w", encoding="utf-8") as f:
            f.write(DEFAULT_META)

    icon = os.path.join(cwd, "icon.png")
    if not os.path.isfile(icon):
        print("-> icon.png not found, not packaging it")

    zip_name = os.path.join(cwd, os.path.splitext(dol)[0] + ".zip")
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(boot, "boot.dol")
        zf.write(meta, "meta.xml")
        if os.path.isfile(icon):
            zf.write(icon, "icon.png")

    os.remove(boot)
    print(f"-> created: {zip_name} (boot.dol deleted)")
    with zipfile.ZipFile(zip_name) as zf:
        for name in zf.namelist():
            print(f"   contains: {name}")


if __name__ == "__main__":
    main()

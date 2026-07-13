#!/usr/bin/env python3
"""
Generate README.md
"""

import sys
import os
from pathlib import Path
from urllib.parse import quote

def slugify_name(filename):
    # Remove .svg extension
    name = filename[:-4]
    # Remove board prefix (e.g., 'power-' or 'sensors-')
    parts = name.split('-', 1)
    if len(parts) > 1:
        return parts[1]
    return name

def generate_readme(board_name, board_title):
    exports_dir = Path(board_name) / "preview"

    # Discover all SVG files
    svg_files = sorted(exports_dir.glob("*.svg"), reverse=True)
    schematic_files = [f.name for f in svg_files if not f.name.endswith("-pcb.svg") and not f.name.endswith("-asy.svg")]
    assembly_files = [f.name for f in svg_files if f.name.endswith("-asy.svg")]
    # Build markdown
    lines = [
        f"# {board_title}",
        "",
    ]

    # Schematic section (if any)
    lines.append("## Schematic")
    lines.append("")
    for sch_file in schematic_files:
        display_name = slugify_name(sch_file)
        encoded_path = quote(f"./preview/{sch_file}")
        lines.append(f"![{display_name}]({encoded_path})")
    lines.append("")

    # PCB Layout section (if any)
    lines.append("## PCB Layout")
    lines.append("")
    for pcb_file in [ f"{board_name}-front-pcb.svg", f"{board_name}-back-pcb.svg"]:
        display_name = slugify_name(pcb_file) or "PCB"
        encoded_path = quote(f"./preview/{pcb_file}")
        lines.append(f"![{display_name}]({encoded_path})")
    lines.append("")

    # assembly section (if any)
    for asy_file in assembly_files:
        display_name = slugify_name(asy_file)
        encoded_path = quote(f"./preview/{asy_file}")
        lines.append(f"![{display_name}]({encoded_path})")
    lines.append("")

    # Write README
    readme_path = Path(board_name) / "README.md"
    readme_path.write_text("\n".join(lines))
    print(f"Generated {readme_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 generate_readme.py <board_name> <board_title>", file=sys.stderr)
        sys.exit(1)

    board_name = sys.argv[1]
    board_title = sys.argv[2]
    generate_readme(board_name, board_title)

#!/usr/bin/env python3

from json import loads as json_loads
from os import path, mkdir
import sys

def main():
    old_colors_file = "./original/colors.json"
    original_theme_dir = "./original"
    original_theme_name = "KvRecolor"
    output_dir = "./out"
    output_theme_name = ""

    if len(sys.argv) == 2:
        output_theme_name = "KvRecolor"
    elif len(sys.argv) == 3:
        output_theme_name = sys.argv[2]
    else:
        print("usage: ./recolor.py <colors.json> [theme name]")
        sys.exit(1)

    new_colors_file = sys.argv[1]

    if path.exists(old_colors_file) == False:
        print("Error: can't find original colors file")
        sys.exit(1)
    if path.exists(new_colors_file) == False:
        print("Error: can't find new colors file")
        sys.exit(1)

    old_colors = parse_json(file_to_string(old_colors_file))
    new_colors = parse_json(file_to_string(new_colors_file))

    original_kvconfig_path = f"{original_theme_dir}/{original_theme_name}/{original_theme_name}.kvconfig"
    original_svg_path = f"{original_theme_dir}/{original_theme_name}/{original_theme_name}.svg"

    if path.exists(original_kvconfig_path) == False:
        print("Error: can't find original kvconfig file")
        sys.exit(1)
    if path.exists(original_svg_path) == False:
        print("Error: can't find new svg file")
        sys.exit(1)

    new_kvconfig = replace_colors(file_to_string(original_kvconfig_path), old_colors, new_colors)
    new_svg = replace_colors(file_to_string(original_svg_path), old_colors, new_colors)

    if path.exists(output_dir) == False:
        mkdir(output_dir)
    if path.exists(f"{output_dir}/{output_theme_name}") == False:
        mkdir(f"{output_dir}/{output_theme_name}")

    with open(f"{output_dir}/{output_theme_name}/{output_theme_name}.kvconfig", "w") as file:
        file.write(new_kvconfig)

    with open(f"{output_dir}/{output_theme_name}/{output_theme_name}.svg", "w") as file:
        file.write(new_svg)

def file_to_string(path):
    with open(path, "r") as file:
        file_content = file.read()
    return file_content

def parse_json(file):
    try:
        json_dict = json_loads(file)
    except ValueError:
        print("Error: could not parse JSON")
        sys.exit(1)
    return json_dict

def replace_colors(file_content, old_colors, new_colors):
    for color in old_colors:
        file_content = file_content.replace(old_colors[color].lower(), new_colors[color].upper())
        file_content = file_content.replace(old_colors[color].upper(), new_colors[color].upper())
    return file_content

main()

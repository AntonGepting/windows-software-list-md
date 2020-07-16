#!/usr/bin/env python3
import yaml
import os
from jinja2 import Environment, FileSystemLoader


PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    # loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    loader=FileSystemLoader(os.path.join(PATH)),
    trim_blocks=False)

INPUT_FILE = 'software.yml'
TEMPLATE_FILE = 'README.md.j2'
OUTPUT_FILE = 'README.md'

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def create_index_html():
    with open(INPUT_FILE) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    with open(OUTPUT_FILE, 'w') as f:
        # print(data['software'])
        output = render_template(TEMPLATE_FILE, data)
        # print(output)
        f.write(output)




def main():
    create_index_html()

if __name__ == "__main__":
    main()

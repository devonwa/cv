#!/usr/bin/python

import os
import shutil
import subprocess
import sys
import tempfile

from jinja2 import Environment, FileSystemLoader
import yaml


TEMPLATES_DIR = 'templates'
OUTPUT_DIR = 'output'
TEX_OPTIONS = {"block_start_string": '<<*',
               "block_end_string": '*>>',
               "variable_start_string": '<<',
               "variable_end_string": '>>',
               "comment_start_string": '<#',
               "comment_end_string": '#>'}

build_pdf = True


def generate_all():
    """Render all templates in the template directory."""
    for f in os.listdir(TEMPLATES_DIR):
        extension = f.split(".")[-1]

        options = {"trim_blocks": True}
        if extension == "tex":
            options.update(TEX_OPTIONS)

        loader = FileSystemLoader(TEMPLATES_DIR)
        env = Environment(loader=loader, **options)
        template = env.get_template(f)
        file_path = generate(template)

        if extension == "tex":
            options = TEX_OPTIONS
        else:
            env = Environment(loader=loader)

        if build_pdf and extension == "tex":
            build_pdf_from_tex(file_path)


def generate(template, file_path=None):
    """Render a template and return output file path."""
    if not file_path:
        file_path = os.path.join(OUTPUT_DIR, template.name)

    with open("cv.yaml") as f:
        data = yaml.safe_load(f)
    output = template.render(**data)

    with open(file_path, 'w') as f:
        f.write(output)

    return file_path


def build_pdf_from_tex(file_path):
    """Build a PDF from a tex file."""
    fp = os.path.abspath(file_path)
    output_dir = os.path.dirname(fp)
    cwd = os.getcwd()
    tmp_dir = tempfile.mkdtemp()
    os.chdir(tmp_dir)

    try:
        name = os.path.basename(fp).split(".")[0] + ".pdf"
        code = subprocess.call(['pdflatex', fp])
        shutil.copy(name, output_dir)
    finally:
        shutil.rmtree(tmp_dir)

    os.chdir(cwd)



def main():
    """Parse command line arguments."""
    args = sys.argv[1:]

    generate_all()


#if __name__ == "__main__":
main()

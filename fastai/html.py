"`fastai.html` contains essential html functions"
from .imports.core import *

def _treat_html(o:str)->str:
    o = str(o)
    to_replace = {'\n':'\\n', '<':'&lt;', '>':'&gt;', '&':'&amp;'}
    for k,v in to_replace.items(): o = o.replace(k, v)
    return o

def text2html_table(items:Collection[Collection[str]])->str:
    "Put the texts in `items` in an HTML table, `widths` are the widths of the columns in %."
    html_code = f"""<table border="1" class="dataframe">"""
    html_code += f"""  <thead>\n    <tr style="text-align: right;">\n"""
    for i in items[0]: html_code += f"      <th>{_treat_html(i)}</th>"
    html_code += f"    </tr>\n  </thead>\n  <tbody>"
    html_code += "  <tbody>"
    for line in items[1:]:
        html_code += "    <tr>"
        for i in line: html_code += f"      <td>{_treat_html(i)}</td>"
        html_code += "    </tr>"
    html_code += "  </tbody>\n</table>"
    return html_code

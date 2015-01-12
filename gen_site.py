#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

'''
Generate site on github
'''

import os, shutil, markdown2

CURRENT_DIR = os.path.split(os.path.abspath(__file__))[0]

def main():
    copy_apidocs()
    templ = load_template()
    for f in os.listdir(CURRENT_DIR):
        if f.endswith('.md'):
            md2html(templ, f[:-3])

def md2html(templ, filename):
    print('generate %s.md to %s.html...' % (filename, filename))
    with open(os.path.join(CURRENT_DIR, filename + '.md'), 'r') as f:
        s = f.read()
    repl = '<!-- MAIN CONTENT -->'
    pos = templ.find(repl)
    if pos==(-1):
        print('ERROR: invalid template.')
        return
    html = templ[:pos] + '\n<!-- BEGIN CONTENT -->\n' + str((markdown2.markdown(s))) + '\n<!-- END CONTENT -->\n' + templ[pos + len(repl):]
    with open(os.path.join(CURRENT_DIR, filename + '.html'), 'w') as f:
        f.write(html)

def copy_apidocs():
    src_dir = os.path.join(os.path.split(CURRENT_DIR)[0], 'jsonstream')
    target = os.path.join(CURRENT_DIR, 'apidocs')
    if os.path.isdir(target):
        print('remove existing apidocs...')
        shutil.rmtree(target)
    print('copying apidocs...')
    shutil.copytree(os.path.join(src_dir, 'target', 'apidocs'), target)

def load_template():
    print('load html template...')
    with open(os.path.join(CURRENT_DIR, 'TEMPLATE.html'), 'r') as f:
        return f.read()

if __name__=='__main__':
    main()

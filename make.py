import os
import pymustache
import string
import sys
import yaml

BASE = os.path.dirname(__file__)
NAME = 'chillax_du_relzen'
COLOR_SCHEME = os.path.join(BASE, 'colors', '{}.vim'.format(NAME))
TEMPLATE = os.path.join(BASE, 'chillax_du_relzen.tpl.vim')


def fg(group):
    return group[0]


def bg(group):
    return group[1]


def style(group):
    return group[2]


def color(c, i):
    if c is None:
        return None

    if isinstance(c, str):
        return c

    return c[i]


def ctermfg(group):
    return color(fg(group), 0)


def ctermbg(group):
    return color(bg(group), 0)


def guifg(group):
    try:
        return color(fg(group), 1)
    except IndexError:
        return ctermfg(group)


def guibg(group):
    try:
        return color(bg(group), 1)
    except IndexError:
        return ctermbg(group)


def create_palette(conf):
    colours = {}
    for g, v in conf['scheme'].items():
        colours[g] = {
            'fg': ctermfg(v),
            'bg': ctermbg(v),
            'fg_gui': guifg(v),
            'bg_gui': guibg(v),
            'style': style(v),
        }
    return [{'name': name, 'conf': vals} for name, vals in colours.items()]


def make(conf):
    """ Compile the colour scheme """
    with open(TEMPLATE) as t:
        template = t.read()
        content = pymustache.render(template, {'scheme': conf})

    with open(COLOR_SCHEME, 'w') as color_scheme:
        color_scheme.write(content)


if __name__ == "__main__":
    try:
        conf = yaml.load(open(sys.argv[1]))
    except IndexError:
        print("Give me something, can't read your mind.")
        sys.exit(-1)
    make(create_palette(conf))

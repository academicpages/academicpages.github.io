#!/usr/bin/env python3

class Colorschemes:
    def __init__(self, schemes):
        self.schemes = schemes

    def render(self, out):
        default_scheme = Colorscheme('')

        for property in default_scheme.__dict__:
            out.write('{% macro ')
            out.write(property)
            out.write('() %}')
            out.write('{% if config.extra.colorscheme %}')
            for id, scheme in enumerate(self.schemes):
                if id == 0:
                    out.write('{% if config.extra.colorscheme == "' + scheme.name + '" %}')
                else:
                    out.write('{% elif config.extra.colorscheme == "' + scheme.name + '" %}')
                out.write(scheme.__getattribute__(property))
            out.write('{% else %}')
            out.write(default_scheme.__getattribute__(property))
            out.write('{% endif %}')
            out.write('{% else %}')
            out.write(default_scheme.__getattribute__(property))
            out.write('{% endif %}')
            out.write('{% endmacro %}\n')


class Colorscheme:
    def __init__(self, name):
        self.name = name
        self.background = "black"
        self.navbar_style = "light"
        self.navbar_shadow = "navbar-shadow"
        self.style = "info"

def main():
    default = Colorscheme("default")

    ocean = Colorscheme("ocean")
    ocean.navbar_style = "link"
    ocean.style = "link"
    ocean.navbar_shadow = ""

    forest = Colorscheme("forest")
    forest.navbar_style = "success"
    forest.style = "success"
    forest.navbar_shadow = ""

    colorschemes = Colorschemes([default, ocean, forest])

    with open('templates/colors.html', 'w') as f:
        colorschemes.render(f)

if __name__ == '__main__':
    main()



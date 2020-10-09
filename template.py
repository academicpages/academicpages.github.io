#!/usr/bin/env python3

import pystache, datetime, argparse, os.path

class Template:
    template = """
---
title: {{long_title}}
date: {{date}}
permalink: /posts/{{year}}/{{month}}/{{short_title}}/
tags:
---
    """.strip()

    def __init__(self, long_title, date, short_title=None, max_short_title_words=4, force=False):
        self.long_title = long_title
        self.date = date

        if short_title is None:
            self._short_title_words = long_title.lower().split()[0:max_short_title_words]
        else:
            self._short_title_words = short_title.lower().split()

        self.short_title = "-".join(self._short_title_words)

        if not force and len(self._short_title_words) > max_short_title_words:
            raise RuntimeError(f"Short title '{self.short_title}' has more than {max_short_title_words}")

        assert " " not in self.short_title

        self.contents = self.fill_contents(self.template, self.long_title, self.short_title, self.date)
        self.path = self.template_path(self.short_title, self.date)

    @staticmethod
    def fill_contents(template, long_title, short_title, date):
        payload = {
            "long_title": long_title,
            "short_title": short_title,
            "date": str(date),
            "year": date.year,
            "month": date.month
        }

        return pystache.render(template, payload)

    @staticmethod
    def template_path(short_title, date, directory="_posts"):
        filename = str(date) + "-" + short_title + ".md"
        return os.path.join(directory, filename)

    def write(self):
        yn = input(f"Write to {self.path}? [y/N] ")

        if yn.lower() == "y":
            with open(self.path, "w") as f:
                f.write(self.contents)

            print("Wrote")
        else:
            print("Not writing")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("long_title")
    p.add_argument("-s", "--short_title")
    p.add_argument("-f", "--force", action="store_true")
    args = p.parse_args()

    t = Template(args.long_title, datetime.date.today(), short_title=args.short_title, force=args.force)
    t.write()

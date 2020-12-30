#!/usr/bin/env python3

import pystache, datetime, argparse, os.path, unicodedata, re

class Template:
    template = """
---
title: {{title}}
date: {{date}}
permalink: /posts/{{year}}/{{month}}/{{slug}}/
tags:
---
    """.strip()

    @staticmethod
    def slugify(value, allow_unicode=False):
        """
        Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
        Remove characters that aren't alphanumerics, underscores, or hyphens.
        Convert to lowercase. Also strip leading and trailing whitespace.

        Borrowed from Django: https://docs.djangoproject.com/en/2.1/_modules/django/utils/text/#slugify
        """
        value = str(value)
        if allow_unicode:
            value = unicodedata.normalize('NFKC', value)
        else:
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
        value = re.sub(r'[^\w\s-]', '', value).strip().lower()
        return re.sub(r'[-\s]+', '-', value)

    def __init__(self, title, date, slug=None):
        self.title = title
        self.date = date

        if slug is None:
            self.slug = self.slugify(title)
        else:
            self.slug = slug

        self.contents = self.fill_contents(self.template, self.title, self.slug, self.date)
        self.path = self.template_path(self.slug, self.date)

    @staticmethod
    def fill_contents(template, title, slug, date):
        payload = {
            "title": title,
            "slug": slug,
            "date": str(date),
            "year": date.year,
            "month": date.month
        }

        return pystache.render(template, payload)

    @staticmethod
    def template_path(slug, date, directory="_posts"):
        filename = str(date) + "-" + slug + ".md"
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
    p.add_argument("title")
    p.add_argument("-s", "--slug")
    args = p.parse_args()

    t = Template(args.title, datetime.date.today(), slug=args.slug)
    t.write()

from nbconvert.writers.base import WriterBase


class HelloWriter(WriterBase):
    def write(self, output, resources, notebook_name=None, **kw):
        with open("hello.txt", "w") as outfile:
            outfile.write("hello world")

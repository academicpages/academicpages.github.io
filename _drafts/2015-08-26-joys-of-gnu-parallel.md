---
date: '2015-08-26'
slug: joys-of-gnu-parallel
title: Joys of gnu parallel
---

I often have to perform a task of this form: given some paired input files `left_input.1`, `left_input.2`, `...` and `right_input.1`, `right_input.2`, `...`, I need to make some output files `output.1`, `output.2`, `...`.

I used to do this by writing a bash loop:
``


    for i in 1 2 3 4 5
    do
        script --left=left.$i --right=right.$i --output=output.$i
    done



which I hated for a number of reasons: I need to type in the `1 2 3 4 5` by hand, the loop runs one-by-one, and it takes up multiple lines.

I found a solution that involves more keystrokes but which I think is more elegant:
`parallel --xapply script --left={1} --right={2} --output={3} ::: left.* ::: right.* ::: output.*`
This only works if the files `output.*` already exist, but I can use a little sed command to create the names I want. Just replace the `output.*` with ``ls left.* | sed 's/left/output/'``!

**Edit:** Many thanks to Ole, whose comment is below. You can put a Perl regex inside the curly braces and instead write `parallel script --left={} --right={=s/left/right/=} --output={=s/left/output/=} ::: left.*`
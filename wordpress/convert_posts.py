#!/usr/bin/env python
"""
This scripts goes through the wordpress posts and re-formats them for use
in the _posts folder. It should be run from the wordpress folder.
"""

import os

path = os.path.normpath(os.path.join(os.getcwd(), 'posts'))
files = os.listdir(path)

for fname in files:
    # Set up new file name
    date = fname.split('-', 1)[0]
    date = '-'.join((date[0:4], date[4:6], date[6:8]))
    newf = date + '-' + fname.split('-', 1)[1]
    newf = os.path.normpath(os.path.join('../_posts/', newf))

    # Read file
    with open(os.path.join('posts', fname), 'r') as f:
        lines = f.readlines()

    # Grab the index of content start line
    i = 0
    for line in lines:
        if line.startswith('#'):
            break
        else:
            i += 1

    # Parse header lines
    header = lines[0:i-1]
    header = {h.split(':', 1)[0]: h.split(':', 1)[1].strip() for h in header}
    newheader = 'title: ' + header['title'] + '\n'
    newheader += '#link: ' + header['link'] + '\n'
    newheader += 'permalink: /posts/' + date[0:4] + '/' + date[5:7] \
        + '/' + header['post_name'] + '\n'
    newheader += 'date: ' + date + '\n'

    # Write new file
    print(date)
    #print('Writing {}'.format(newf))
    with open(newf, 'w') as f:
        f.write('---\n')
        f.write(newheader)
        f.write('---\n')
        f.write('\n')
        # Note, we're not writing the title line here
        f.write(''.join(lines[i+1:]))

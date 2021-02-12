import os, sys

f = open('results.yml', 'r')
name = ''
lines = ''
for l in f:
    cs = l.split()

    if '-' in cs[0]:

        if name is not '':
            fout = open('../_publications/'+name+'.md', 'w')
            fout.write('---\n')
            fout.write(lines.strip()+'\n')
            # fout.write('---\n')
            fout.close()
            lines = ''

        name = l.replace('- ', '').replace(':', '').strip()
    else:
        lines += l.strip() + '\n'

    if 'date' in l:
        name = l.strip().replace('date: ', '') + '-' + name
        print name

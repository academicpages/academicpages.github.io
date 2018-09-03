nb=$1

jupyter nbconvert $nb --to markdown
mv ${nb%.ipynb}.md ~/github/cduvallet.github.io/_posts/
mv ${nb%.ipynb}_files ~/github/cduvallet.github.io/images/

#find ./ -type f -exec ls -lt {} + | head -n 10

#git add -A

#git add ./*/* ./*

git commit -a -m "$@"
git push


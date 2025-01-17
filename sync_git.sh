
# To push to github. Just run: ./sync_git.sh "changes made"

#find ./ -type f -exec ls -lt {} + | head -n 10

#git add -A

#git add ./*/* ./*

git commit -a -m "$@"
git push

# To update talkmap. Run "python ../talkmap.py" in the folder of _talks/
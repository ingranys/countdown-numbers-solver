#!/usr/bin/env bash
# Source : https://stackoverflow.com/questions/40865597/generate-changelog-from-commit-and-tag
# Usage : 
# Step 1) Update project url https://github.com/<username>/<repository>/commit/
# Step 2) Go to root git folder
# Step 3) Run shell script : sh changelog-builder.sh > CHANGELOG.md
previous_tag=0
for current_tag in $(git tag --sort=-creatordate)
do

if [ "$previous_tag" != 0 ];then
    tag_date=$(git log -1 --pretty=format:'%ad' --date=short ${previous_tag})
    printf "## ${previous_tag} (${tag_date})\n\n"
    git log ${current_tag}...${previous_tag} --pretty=format:'*  %s [View](https://github.com/ingranys/countdown-numbers-solver/commit/%H)' --reverse | grep -v Merge
    printf "\n\n"
fi
previous_tag=${current_tag}
done

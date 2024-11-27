#!/bin/bash
# Add it as cronjob
# */5 * * * * /ansible/check_and_deploy.sh >> /var/log/check_and_deploy.log 2>&1
 

REPO_DIR="/ansible"
BRANCH="master"
ANSIBLE_PLAYBOOK="/ansible/playbook.yml"
LAST_COMMIT_FILE="/ansible/last_commit_hash"

cd "$REPO_DIR" || exit

git fetch origin "$BRANCH"

LATEST_COMMIT=$(git rev-parse origin/"$BRANCH")

if [ ! -f "$LAST_COMMIT_FILE" ] || [ "$(cat "$LAST_COMMIT_FILE")" != "$LATEST_COMMIT" ]; then
    echo "New commit detected: $LATEST_COMMIT"
    
    git reset --hard origin/"$BRANCH"

    ansible-playbook -i inventory "$ANSIBLE_PLAYBOOK"

    echo "$LATEST_COMMIT" > "$LAST_COMMIT_FILE"

    echo "Deployment and testing complete."
else
    echo "No new commits detected."
fi

#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname "$0")/.."
python3 scripts/check-site.py
if [[ -n "$(git status --porcelain --untracked-files=no)" ]]; then
  echo 'Commit your changes before publishing GitHub Pages.' >&2
  exit 1
fi
pages_commit=$(git subtree split --prefix=dist HEAD)
git -c credential.helper= -c 'credential.helper=!gh auth git-credential' push github "$pages_commit:refs/heads/gh-pages"
echo 'Website files pushed to gh-pages. GitHub Pages will deploy that branch.'

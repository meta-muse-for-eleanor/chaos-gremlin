#!/usr/bin/env bash
# Install the Chaos Gremlin skill for Muse.
#
# Copies this repository (minus .git) into Muse's custom skills folder,
# where Muse discovers it automatically in new conversations.
#
# Usage:
#   ./install.sh
#   SKILL_DEST=/some/other/path ./install.sh
set -euo pipefail

DEST="${SKILL_DEST:-$HOME/workspace/custom-skills/chaos_gremlin}"
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ "$SRC" = "$DEST" ]; then
  echo "Already installed at $DEST"
  exit 0
fi

mkdir -p "$DEST"
# Copy everything except the git history and local caches.
if command -v rsync >/dev/null 2>&1; then
  rsync -a --exclude '.git' --exclude '__pycache__' "$SRC"/ "$DEST"/
else
  (cd "$SRC" && tar --exclude='.git' --exclude='__pycache__' -cf - .) | (cd "$DEST" && tar -xf -)
fi

chmod +x "$DEST/scripts/gremlin.py"
echo "Installed Chaos Gremlin to $DEST"
echo "Try it: python3 \"$DEST/scripts/gremlin.py\" fortune --mood chaotic"
echo "In Muse, start a new conversation or ask Muse to search for the 'chaos_gremlin' skill."

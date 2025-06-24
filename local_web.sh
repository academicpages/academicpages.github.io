#!/usr/bin/env bash
PORT=4000
LRPORT=35729

# --- free LiveReload port if busy ---
if lsof -i tcp:"$LRPORT" >/dev/null 2>&1; then
  echo "Killing previous LiveReload on port $LRPORT…"
  kill -INT "$(lsof -ti tcp:"$LRPORT")"
fi

# --- launch Jekyll (foreground) ---
bundle exec jekyll serve \
  --port "$PORT" \
  --livereload --livereload-port "$LRPORT" \
  --incremental \
  --open-url          # opens default browser when ready :contentReference[oaicite:7]{index=7}

# Script ends when you press Ctrl-C in this terminal

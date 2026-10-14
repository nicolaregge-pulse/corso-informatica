#!/bin/bash
# Esporta il gioco della talpa 1INF per il browser e obbliga i browser a riscaricarlo (numero nell'indirizzo del pacchetto).
cd "$(dirname "$0")/../talpa-1inf" || exit 1
G=${GODOT:-/tmp/claude-0/-home-user-corso-godot/d65eff9d-e028-5dc2-8095-966645bd40b0/scratchpad/godot/Godot_v4.7-stable_linux.x86_64}
"$G" --headless --path . --export-release "Web" ../docs/giochi/talpa-1inf/index.html >/dev/null 2>&1; rm -rf .godot
sed -i "s/\"executable\":\"index\"/\"executable\":\"index\",\"mainPack\":\"index.pck?v=$(date -u +%Y%m%d%H%M%S)\"/" ../docs/giochi/talpa-1inf/index.html
grep -o '"mainPack":"[^"]*"' ../docs/giochi/talpa-1inf/index.html

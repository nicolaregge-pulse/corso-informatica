#!/bin/bash
# Hook di STOP: fa rispettare la regola "TUTTO VERSIONATO".
# Blocca la fine del turno se il repo PUBBLICO o PRIVATO ha modifiche non
# committate/non pushate. Avvisa (senza bloccare) sugli script in scratchpad
# non ancora versionati. Ricorsione-safe (rispetta stop_hook_active).

input=$(cat 2>/dev/null)
if [[ "$(printf '%s' "$input" | jq -r '.stop_hook_active' 2>/dev/null)" == "true" ]]; then
  exit 0
fi

PUB="/home/user/corso-godot"
PRIV="/home/user/corso-informatica-riservato"
problems=""

check_repo() {
  local d="$1" name="$2"
  git -C "$d" rev-parse --git-dir >/dev/null 2>&1 || return 0
  if [[ -n "$(git -C "$d" status --porcelain 2>/dev/null)" ]]; then
    problems+="- Repo $name: modifiche non committate o file non tracciati. Committa e pusha ($d)."$'\n'
    return
  fi
  local br
  br="$(git -C "$d" branch --show-current 2>/dev/null)"
  if [[ -n "$br" ]] && git -C "$d" rev-parse "origin/$br" >/dev/null 2>&1; then
    local ahead
    ahead="$(git -C "$d" rev-list "origin/$br..HEAD" --count 2>/dev/null)"
    [[ -n "$ahead" && "$ahead" -gt 0 ]] && problems+="- Repo $name: $ahead commit non pushati. Fai push ($d)."$'\n'
  fi
}

check_repo "$PUB" "PUBBLICO"
check_repo "$PRIV" "PRIVATO"

if [[ -n "$problems" ]]; then
  printf 'REGOLA "TUTTO VERSIONATO" non rispettata:\n%sVersiona (commit + push) prima di terminare.\n' "$problems" >&2
  exit 2
fi

# --- avviso (non blocca): script .py/.js in scratchpad non versionati ---
tracked="$( { git -C "$PUB" ls-files 2>/dev/null; git -C "$PRIV" ls-files 2>/dev/null; } | sed 's#.*/##' | sort -u )"
orphans=""
for sp in /tmp/claude-*/*corso-godot*/*/scratchpad; do
  [[ -d "$sp" ]] || continue
  while IFS= read -r f; do
    b="$(basename "$f")"
    printf '%s\n' "$tracked" | grep -qxF "$b" || orphans+="$b "
  done < <(find "$sp" -maxdepth 1 -type f \( -name '*.py' -o -name '*.js' \) 2>/dev/null)
done
if [[ -n "$orphans" ]]; then
  msg="Nota: script in scratchpad non ancora versionati (se sono strumenti/generatori, salvali su Git): ${orphans}"
  printf '{"systemMessage": "%s"}\n' "$(printf '%s' "$msg" | sed 's/\\/\\\\/g; s/"/\\"/g')"
fi
exit 0

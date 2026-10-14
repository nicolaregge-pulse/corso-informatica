#!/bin/bash
# Aspetta che GitHub Pages abbia pubblicato l'ultimo commit (REGISTRO-ERRORI #79): il link si dà al prof SOLO dopo «PUBBLICATO».
# Uso: bash strumenti/aspetta_pubblicazione.sh   (dalla cartella del repository pubblico, dopo il push)
H=$(git rev-parse HEAD); R=nicolaregge-pulse/corso-informatica
for i in $(seq 1 60); do
  S=$(gh api "repos/$R/actions/runs?head_sha=$H&per_page=5" --jq '[.workflow_runs[]|select(.name|test("Pages"))][0]|(.status+" "+(.conclusion//""))' 2>/dev/null)
  case "$S" in
    "completed success") echo "PUBBLICATO ${H:0:7}"; exit 0;;
    "completed cancelled") # superato da un commit più nuovo: aspetto quello
      N=$(gh api "repos/$R/actions/runs?per_page=1" --jq '.workflow_runs[0].head_sha'); [ "$N" != "$H" ] && H=$N;;
    "completed "*) echo "PUBBLICAZIONE FALLITA: $S"; exit 1;;
  esac
  sleep 10
done
echo "NON ANCORA PUBBLICATO dopo 10 minuti: $S"; exit 2

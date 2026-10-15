#!/bin/bash
# Installa il controllo automatico delle classi come «pre-commit» nei due repository (15/10/2026).
# Ogni commit che tocca comandi, compiti in coda o pagine per i ragazzi passa da strumenti/controlla_classe.py:
# se una lingua, un corso di Classroom o una consegna «copia e incolla» è sbagliata, il commit si ferma.
C=/home/user/corso-godot/strumenti/controlla_classe.py
for R in /home/user/corso-godot /home/user/corso-informatica-riservato; do
  [ -d "$R/.git" ] || continue
  cat > "$R/.git/hooks/pre-commit" <<HOOK
#!/bin/bash
F=\$(git diff --cached --name-only --diff-filter=AM | grep -E '^(comandi|coda)/[^/]+\.json\$|^docs/.*\.html\$')
[ -z "\$F" ] && exit 0
python3 $C \$F || { echo "Commit fermato dal controllo delle classi: correggi e riprova."; exit 1; }
HOOK
  chmod +x "$R/.git/hooks/pre-commit"; echo "installato in $R"
done

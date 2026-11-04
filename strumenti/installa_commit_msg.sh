#!/bin/bash
# Installa il hook git «commit-msg» nel repository PUBBLICO (04/11/2026, regola R1 di CLAUDE.md).
# Ogni commit del pubblico passa da .claude/hooks/controllo_nomi.py: se il messaggio contiene il
# cognome di un allievo (elenchi del riservato) il commit si ferma. Se il riservato non c'è, passa.
P=/home/user/corso-informatica
cat > "$P/.git/hooks/commit-msg" <<HOOK
#!/bin/bash
[ -f "$P/.claude/hooks/controllo_nomi.py" ] || exit 0
python3 "$P/.claude/hooks/controllo_nomi.py" "\$1"
HOOK
chmod +x "$P/.git/hooks/commit-msg" && echo ok

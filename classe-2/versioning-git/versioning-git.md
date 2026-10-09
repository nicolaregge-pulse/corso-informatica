# Versioni e Git: la storia del nostro Treno blindato

**Versione 1.0** — 09/10/2026 · Classe 2INF · lezione frontale di 1 ora

Testo per la tua AI: chiedile di spiegarti ogni parola nella tua lingua.

## 01 I link della lezione

1. Il grafo delle versioni (clicca i pallini) · 版本图（点圆点）

```
https://nicolaregge-pulse.github.io/corso-informatica/giochi/grafo/
```

2. Tutte le versioni del vostro treno, giocabili · 你们火车游戏的所有版本，都可以玩

```
https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-blindato/versioni/
```

3. Il changelog del treno (la lista dei cambiamenti) · 火车游戏的更新日志

```
https://github.com/nicolaregge-pulse/corso-informatica/blob/main/docs/giochi/treno-blindato/CHANGELOG.md
```

4. La storia dei commit del ramo treno-2inf · treno-2inf 分支的提交历史

```
https://github.com/nicolaregge-pulse/corso-informatica/commits/treno-2inf
```

5. Il grafo vero di Git su GitHub (Network) · GitHub 上真正的 Git 图

```
https://github.com/nicolaregge-pulse/corso-informatica/network
```

6. Il fork della 3INF: il loro treno · 3INF 的 fork：他们的火车

```
https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-3inf/
```

7. La versione 2.0 su Godot · Godot 上的 2.0 版本

```
https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-godot/
```

## 02 Le 10 parole, con il nostro gioco

1. **Versione.** Una «fotografia» del progetto in un momento preciso, con un numero. Il vostro treno è passato da v0.0 (prima idea, finestrino laterale) a v0.11 (i punteggi si salvano sempre): 12 versioni in un giorno.
   1.1 中文：版本：项目在某个时刻的「照片」，有一个编号。你们的火车从 v0.0 到 v0.11，一天12个版本。
   1.2 Prova: Apri «Tutte le versioni» e gioca la v0.0 e la v0.11: cosa è cambiato?
2. **Git e GitHub.** Git è il programma che ricorda TUTTA la storia del progetto: chi ha cambiato cosa, quando e perché. GitHub è il sito dove il progetto (il repository) sta online. Il nostro repository si chiama corso-informatica.
   2.1 中文：Git 是记住项目全部历史的程序：谁、什么时候、改了什么、为什么。GitHub 是放项目（仓库 repository）的网站。
   2.2 Prova: Apri «La storia dei commit»: ogni riga è un salvataggio.
3. **Commit.** Un salvataggio nella storia di Git, con un messaggio che spiega il cambiamento. Esempio vero di ieri: 7724900 «Treno blindato v0.11: i punteggi si salvano sempre». Il numero strano (7724900) è il codice del commit.
   3.1 中文：提交（commit）：Git 历史里的一次保存，带一句说明。昨天的例子：7724900「v0.11：分数总是保存」。
   3.2 Prova: Trova nella storia il commit della v0.5 (la Pull Request #104).
4. **Branch (ramo).** Una linea di lavoro separata. Si apre un ramo per provare una cosa nuova senza rompere il gioco che funziona. Il vostro gioco sta nel ramo treno-2inf; il prof ha provato le «immagini della classe» su un ramo a parte.
   4.1 中文：分支（branch）：一条单独的工作线，用来试新东西而不弄坏能玩的游戏。你们的游戏在 treno-2inf 分支。
   4.2 Prova: Nel grafo: quante linee (rami) vedi?
5. **Fork (copia).** La copia di un progetto intero che cresce per conto suo. Ieri la 3INF ha fatto il fork del vostro treno alla v0.11 e lo ha portato alla v1.4 (montagna, Black Panter, Nash…); anche la 1INF.
   5.1 中文：复刻（fork）：整个项目的复制，自己继续发展。昨天 3INF 在 v0.11 复制了你们的火车，做到了 v1.4。
   5.2 Prova: Nel grafo: da quale vostra versione parte la linea verde della 3INF?
6. **Push.** Mandare i propri commit dal PC al repository online (GitHub). Ieri, dopo ogni versione, il prof ha fatto il push: per questo il gioco sul sito cambiava da solo.
   6.1 中文：推送（push）：把自己的提交从电脑发送到网上的仓库（GitHub）。
   6.2 Prova: Perché il gioco sul telefono cambiava senza scaricare niente?
7. **Pull.** Il contrario del push: prendere da GitHub l'ultima versione e portarla sul proprio PC. La v0.11 del treno «chiede sempre alla rete la versione nuova»: è un pull automatico.
   7.1 中文：拉取（pull）：和 push 相反，从 GitHub 把最新版本拿到自己的电脑上。
   7.2 Prova: Quando fai un pull, cosa ricevi?
8. **Pull Request (proposta di modifica).** «Ho fatto una modifica: la vuoi nel progetto?». Qualcuno la controlla e, se va bene, fa il MERGE (la unisce). Ieri le vostre richieste su Classroom erano Pull Request: la #104 della squadra MOTORE FISICA è diventata la v0.5.
   8.1 中文：合并请求（Pull Request）：「我做了一个修改，你要放进项目吗？」检查后如果可以就合并（merge）。#104 变成了 v0.5。
   8.2 Prova: Chi decide se una Pull Request entra nel gioco?
9. **Changelog (registro dei cambiamenti).** La lista, versione per versione, di cosa è cambiato e perché. Il treno ha il suo CHANGELOG.md: chi gioca sa cosa c'è di nuovo, chi programma sa dove cercare un errore.
   9.1 中文：更新日志（changelog）：每个版本改变了什么、为什么的清单。
   9.2 Prova: Apri il changelog: qual è la novità della v0.7?
10. **Numeri delle versioni (major.minor).** v0.x = prove; 1.0 = prima versione stabile (il fork della 3INF parte da 1.0); 1.1, 1.2 = piccole aggiunte (minor); 2.0 = cambio grosso (major): il gioco rifatto con Godot è la v2.0.
   10.1 中文：版本号：v0.x 是试验；1.0 第一个稳定版本；1.1、1.2 小改动（minor）；2.0 大改变（major），用 Godot 重做的游戏就是 2.0。
   10.2 Prova: Perché la versione Godot non si chiama v1.5?

## 03 Changelog

1. v1.0 (09/10/2026) — prima versione.

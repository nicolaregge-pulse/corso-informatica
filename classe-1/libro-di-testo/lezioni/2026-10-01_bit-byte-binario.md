# Bit, byte e numeri binari

**Versione 1.0** — 29/10/2026
*Libro parziale della 1INF: la lezione del 01/10/2026. Fa parte del libro di testo della classe (libro-classe1). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 01/10/2026, 2 ore, Tecnologia.
2. **Argomenti:** Sistema decimale e binario, il bit, il byte (8 bit), conversione da binario a decimale con il metodo delle caselle (128…1), multipli KB, MB, GB; esercitazione di 16 esercizi consegnata su Classroom.

### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Il computer usa solo 0 e 1 (bit). 8 bit fanno un byte. Per passare da binario a decimale si sommano i valori delle caselle con 1.</p><p lang="ar" dir="rtl">الحاسوب يستعمل 0 و1 فقط (بِت). ٨ بِت = بايت واحد. للتحويل من الثنائي إلى العشري نجمع قيم الخانات التي فيها 1.</p><p lang="zh">电脑只用 0 和 1（比特）。8 个比特是一个字节。二进制转十进制：把有 1 的格子的数值加起来。</p></div>

### La teoria e l'esercitazione

Classe 1 · spiegazione base · italiano · solo binario→decimale

**In questa lezione facciamo UNA direzione: dal BINARIO al DECIMALE** (da 0 e 1 al numero di tutti i giorni).

#### 1. I numeri di tutti i giorni

Noi contiamo con **dieci cifre**: 0 1 2 3 4 5 6 7 8 9. Con queste dieci cifre scriviamo
**qualsiasi** numero. Questo si chiama **sistema decimale** («deci» vuol dire dieci).

#### 2. Dentro il computer: acceso o spento

Il computer è fatto di **tantissimi piccoli interruttori**. Un interruttore può stare solo
in **due modi**: acceso o spento. Il computer usa questi due stati: **acceso = 1**, **spento = 0**.

#### 3. Il bit

Un **bit** è la cosa più piccola: **una sola cifra, 0 oppure 1**. La parola "bit"
viene dall'inglese **Binary Digit** = **cifra binaria**. Tutto, dentro il computer, è fatto di bit.

#### 4. Contare con solo 0 e 1 (il binario)

Con due cifre si conta così: 0, 1… poi le cifre finiscono, quindi si scrive **10, 11, 100, 101,
110, 111…** È come il **contachilometri** dell'auto: quando una rotella arriva in fondo, gira quella accanto.

#### 5. Il byte

Mettiamo insieme **8 bit**: questo si chiama **byte**. Un byte ha **8 caselle**, ognuna
con uno 0 o un 1. Una **lettera** scritta nel computer occupa **1 byte**.

#### 6. Da binario a decimale (il metodo delle caselle)

Ogni casella ha un **valore**. Da destra verso sinistra: **1, 2, 4, 8, 16, 32, 64, 128**
(ogni volta il doppio). Per trovare il numero: guarda dove c'è un **1** e **somma** i valori.

**Esempio (come alla lavagna):**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 0 | 0 | 1 | 1 | 1 | 0 |

Ci sono gli **1** sotto 64, 8, 4, 2 → **64 + 8 + 4 + 2 = 78**. Quindi `01001110 = 78`.

La lavagna della nostra lezione: BIT, Byte = 8 bit e la conversione 01001110 = 64+8+4+2 = 78.

**Trucco con le dita:** ogni dito è un bit (alzato = 1, abbassato = 0). Con
**una mano** conti fino a **31**, con **due mani** fino a **1023**!

#### 7. Quanto «pesa» (i multipli)

1 byte = 8 bit. Poi: **1 KB = 1024 byte**, **1 MB = 1024 KB**, **1 GB = 1024 MB**.
Una foto pesa qualche **MB**; un film qualche **GB**.

#### Tanti esempi: byte → decimale

Dato il byte, somma i valori dove c'è un 1: trovi il numero. Gli 1 sono evidenziati.

`00000011`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |

= 2 + 1 = **3**

`00000101`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |

= 4 + 1 = **5**

`00001010`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |

= 8 + 2 = **10**

`00001101`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |

= 8 + 4 + 1 = **13**

`00010011`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 |

= 16 + 2 + 1 = **19**

`00011011`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 0 | 1 | 1 | 0 | 1 | 1 |

= 16 + 8 + 2 + 1 = **27**

`00101010`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |

= 32 + 8 + 2 = **42**

`00110010`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 |

= 32 + 16 + 2 = **50**

`01000000`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

= 64 = **64**

`01001110`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 0 | 0 | 1 | 1 | 1 | 0 |

= 64 + 8 + 4 + 2 = **78**

`01010101`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |

= 64 + 16 + 4 + 1 = **85**

`01100100`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 |

= 64 + 32 + 4 = **100**

`01111000`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |

= 64 + 32 + 16 + 8 = **120**

`01111111`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

= 64 + 32 + 16 + 8 + 4 + 2 + 1 = **127**

`10000010`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |

= 128 + 2 = **130**

`10010110`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 |

= 128 + 16 + 4 + 2 = **150**

`10101010`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |

= 128 + 32 + 8 + 2 = **170**

`11001000`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |

= 128 + 64 + 8 = **200**

`11010010`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |

= 128 + 64 + 16 + 2 = **210**

`11100001`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 |

= 128 + 64 + 32 + 1 = **225**

`11110000`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |

= 128 + 64 + 32 + 16 = **240**

`11111010`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 |

= 128 + 64 + 32 + 16 + 8 + 2 = **250**

`11111111`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

= 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = **255**

`01100011`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 1 | 0 | 0 | 0 | 1 | 1 |

= 64 + 32 + 2 + 1 = **99**

## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.

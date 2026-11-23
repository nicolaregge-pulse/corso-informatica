/* Controlla una specifica fabbrica/post/<id>.json con la STESSA funzione del motore (PB_valida_ di classroom_pubblica_v1.0.gs).
 * Uso: node fabbrica/valida_post_v1.0.js <file.json> [bozza|pubblica] [pubb]   -> stampa JSON {err:[],avv:[]}, esce 0 se err e' vuoto. */
'use strict';
const fs = require('fs'), vm = require('vm'), path = require('path');
const m = { exports: {} };
vm.runInNewContext(fs.readFileSync(path.join(__dirname, 'classroom_pubblica_v1.0.gs'), 'utf8'), { module: m, console });
const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const az = process.argv[3], req = az ? { azione: az, pubb: process.argv[4] ? Number(process.argv[4]) : undefined } : null;
const r = m.exports.PB_valida_(spec, req);
console.log(JSON.stringify(r));
process.exit(r.err.length ? 1 : 0);

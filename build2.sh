#!/bin/bash
F=public/index.html
# topbar
cat >> $F << 'H1'
<div id="topbar"><div class="logo-wrap"><div class="logo-text"><span class="lf">F</span><span class="lk">KART</span></div><div class="logo-sub">Force Kart Racing</div></div><div id="race-title"><h2 id="race-name">DEMO - KGV Endurance</h2><p id="race-sub">Race #26021 &middot; KGV Granja Viana</p></div><div id="timer-block"><div class="timer-lbl">Decorrido</div><div class="timer-val" id="t-elapsed">00:00:00</div><div class="timer-remain" id="t-remain">Falta: --:--:--</div></div></div>
H1
cat >> $F << 'H2'
<div id="infobar"><span class="info-badge demo">&#9888; MODO DEMO</span><span class="info-badge">Race #26021 &middot; KGV Granja Viana</span><span class="info-badge btn" onclick="FK.upd()">&#8635; Atualizar</span><span id="wxbar">Carregando clima...</span><span id="clock-span" style="font-size:11px;color:var(--mut);margin-left:auto"></span></div>
H2
cat >> $F << 'H3'
<div id="tabs"><div class="tab active" data-tab="ranking">&#10006; Ranking</div><div class="tab" data-tab="box">&#128295; Box</div><div class="tab" data-tab="karts">&#127950; Karts</div><div class="tab" data-tab="crono">&#9201; Crono</div><div class="tab" data-tab="estrategia">&#128203; Estrategia</div><div class="tab" data-tab="projecao">&#127919; Projecao</div><div class="tab" data-tab="comparativo">&#128200; Comparativo</div><div class="tab" data-tab="rival">&#9876; Rival VxV</div><div class="tab" data-tab="mapa">&#128506; Mapa</div><div class="tab" data-tab="tracados">&#128194; Tracados</div><div class="tab" data-tab="pilotos">&#128100; Pilotos</div></div>
H3
echo "H1-H3 done: $(wc -c < $F) bytes"

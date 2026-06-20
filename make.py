# FKART v2.3 - Complete HTML Generator
f = open('public/index.html', 'w')
html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>FKART Endurance Monitor v2.3</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--acc:#F7C600;--acc2:#CC2200;--bg:#0c0d0f;--card:#13151a;--txt:#e8eaf0;--mut:#7a8099;--border:#1e2130}
body{background:var(--bg);color:var(--txt);font-family:'Segoe UI',Arial,sans-serif;font-size:13px;min-height:100vh;display:flex;flex-direction:column}
.topbar{background:linear-gradient(135deg,#0a0b0e,#111318);border-bottom:2px solid var(--acc2);padding:8px 16px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
.logo-text{font-style:italic;font-weight:900;font-size:24px;letter-spacing:1px;line-height:1}
.logo-f{color:#999}
.logo-kart{background:linear-gradient(90deg,#CC2200,#FF6600);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.logo-sub{font-size:9px;color:#666;letter-spacing:3px;text-transform:uppercase;margin-top:2px}
.infobar{display:flex;gap:12px;align-items:center;flex:1;flex-wrap:wrap}
.info-badge{background:rgba(247,198,0,0.1);border:1px solid rgba(247,198,0,0.3);border-radius:6px;padding:4px 10px;font-size:11px}
.info-badge span{color:var(--acc);font-weight:700}
.wx-bar{font-size:11px;color:var(--mut);margin-left:auto}
.tabs{display:flex;background:#0a0b0e;border-bottom:1px solid var(--border);overflow-x:auto;flex-shrink:0}
.tabs::-webkit-scrollbar{height:3px}
.tabs::-webkit-scrollbar-thumb{background:var(--acc2)}
.tab{padding:10px 14px;cursor:pointer;border-bottom:2px solid transparent;color:var(--mut);font-size:12px;white-space:nowrap;transition:all .2s;user-select:none}
.tab:hover{color:var(--txt);background:rgba(255,255,255,0.04)}
.tab.on{color:var(--acc);border-bottom-color:var(--acc);background:rgba(247,198,0,0.06)}
.content{flex:1;overflow:auto;padding:12px}
.pane{display:none}
.pane.on{display:block}
.card{background:var(--card);border:1px solid var(--border);border-radius:8px;padding:12px;margin-bottom:8px}
h3{color:var(--acc);font-size:13px;margin-bottom:10px;text-transform:uppercase;letter-spacing:1px}
.kart-num{display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;font-weight:900;font-size:14px;border:2px solid var(--border);color:var(--txt)}
.kart-num.my{background:var(--acc);color:#000;border-color:var(--acc);box-shadow:0 0 12px rgba(247,198,0,0.4)}
table{width:100%;border-collapse:collapse}
th{text-align:left;color:var(--mut);font-size:10px;text-transform:uppercase;padding:6px 8px;border-bottom:1px solid var(--border)}
td{padding:7px 8px;border-bottom:1px solid rgba(30,33,48,0.5);font-size:12px}
tr.my-kart td{background:rgba(247,198,0,0.07);color:var(--acc)}
tr.my-kart td:first-child{border-left:3px solid var(--acc)}
.pos-badge{display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:4px;font-weight:700;font-size:11px;background:rgba(255,255,255,0.05)}
.pos-badge.p1{background:linear-gradient(135deg,#FFD700,#FFA000);color:#000}
.pos-badge.p2{background:linear-gradient(135deg,#C0C0C0,#888);color:#000}
.pos-badge.p3{background:linear-gradient(135deg,#CD7F32,#8B4513);color:#fff}
.gap-badge{font-size:10px;color:var(--mut)}
.comp-bar-wrap{background:#1a1d26;border-radius:4px;height:20px;overflow:hidden;margin:2px 0}
.comp-bar{height:100%;display:flex;align-items:center;padding:0 6px;font-size:10px;font-weight:700;transition:width .5s}
.tr-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:10px}
.tr-card{background:var(--card);border:1px solid var(--border);border-radius:8px;overflow:hidden;cursor:pointer;transition:all .2s}
.tr-card:hover{border-color:var(--acc);transform:translateY(-2px)}
.tr-thumb{width:100%;height:100px;object-fit:cover;background:#1a1d26}
.tr-info{padding:8px}
.tr-num{font-weight:900;font-size:16px;color:var(--acc)}
.tr-dist{color:var(--mut);font-size:11px}
.tr-dif{display:inline-block;font-size:10px;padding:2px 6px;border-radius:3px;margin-top:4px;font-weight:700}
.dif-fcil,.dif-facil,.dif-fcil{background:rgba(102,187,106,0.2);color:#66bb6a}
.dif-mdio,.dif-medio,.dif-mdio{background:rgba(79,195,247,0.2);color:#4fc3f7}
.dif-difcil,.dif-dificil,.dif-difcil{background:rgba(255,167,38,0.2);color:#ffa726}
.dif-expert{background:rgba(204,34,0,0.2);color:#ef5350}
.tr-filters{display:flex;gap:6px;margin-bottom:12px;flex-wrap:wrap}
.tr-filters button{padding:5px 12px;border:1px solid var(--border);background:var(--card);color:var(--mut);border-radius:4px;cursor:pointer;font-size:11px}
.tr-filters button.on{border-color:var(--acc);color:var(--acc);background:rgba(247,198,0,0.1)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.85);z-index:100;align-items:center;justify-content:center}
.overlay.show{display:flex}
.modal{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px;max-width:600px;width:90%;max-height:90vh;overflow-y:auto}
.modal img{width:100%;border-radius:8px;margin-bottom:12px}
.modal-close{float:right;background:none;border:none;color:var(--mut);font-size:20px;cursor:pointer;padding:0 4px}
.mapa-stats{display:flex;gap:12px;flex-wrap:wrap;margin-top:10px}
.stat-box{background:var(--card);border:1px solid var(--border);border-radius:6px;padding:8px 12px;text-align:center}
.stat-box .val{font-size:18px;font-weight:700;color:var(--acc)}
.stat-box .lbl{font-size:10px;color:var(--mut);text-transform:uppercase}
.ph{display:flex;align-items:center;justify-content:center;height:200px;color:var(--mut);font-size:14px;border:1px dashed var(--border);border-radius:8px}
footer{text-align:center;padding:8px;color:#333;font-size:10px;border-top:1px solid #111;letter-spacing:2px}
canvas{border-radius:8px;max-width:100%}
</style>
</head>
<body>
"""
f.write(html)
body = """<div class="topbar">
<div><div class="logo-text"><span class="logo-f">F</span><span class="logo-kart">KART</span></div><div class="logo-sub">Force Kart Racing</div></div>
<div class="infobar">
<div class="info-badge">KGV <span id="race-status">AO VIVO</span></div>
<div class="info-badge">Tempo: <span id="elapsed">00:45:30</span></div>
<div class="info-badge">Falta: <span id="remaining">02:14:30</span></div>
<div class="info-badge">Lider: <span id="leader-info">013</span></div>
<div class="wx-bar" id="wxbar">KGV - Granja Viana</div>
</div>
</div>
<div class="tabs" id="tabs">
<div class="tab on" data-tab="ranking">&#127937; Ranking</div>
<div class="tab" data-tab="box">&#128295; Box</div>
<div class="tab" data-tab="karts">&#127950; Karts</div>
<div class="tab" data-tab="crono">&#9201; Crono</div>
<div class="tab" data-tab="estrategia">&#128203; Estrategia</div>
<div class="tab" data-tab="projecao">&#127919; Projecao</div>
<div class="tab" data-tab="comp">&#128200; Comparativo</div>
<div class="tab" data-tab="rival">&#9876; Rival VxV</div>
<div class="tab" data-tab="mapa">&#128506; Mapa</div>
<div class="tab" data-tab="tracados">&#128194; Tracados</div>
<div class="tab" data-tab="pilotos">&#128100; Pilotos</div>
</div>
<div class="content">
<div class="pane on" id="pane-ranking">
<div class="card"><h3>&#127937; Classificacao Geral</h3>
<table><thead><tr><th>Pos</th><th>Kart</th><th>Piloto</th><th>Cat</th><th>Voltas</th><th>Melhor</th><th>Ultima</th><th>Gap</th><th>Diff</th></tr></thead>
<tbody id="placar-body"></tbody></table></div></div>
<div class="pane" id="pane-box"><div class="ph">&#128295; Box - Em breve</div></div>
<div class="pane" id="pane-karts"><div class="ph">&#127950; Karts - Em breve</div></div>
<div class="pane" id="pane-crono"><div class="ph">&#9201; Cronometro - Em breve</div></div>
<div class="pane" id="pane-estrategia"><div class="ph">&#128203; Estrategia - Em breve</div></div>
<div class="pane" id="pane-projecao"><div class="ph">&#127919; Projecao - Em breve</div></div>
<div class="pane" id="pane-comp">
<div class="card"><h3>&#128200; Comparativo Top Karts</h3><div id="comp-body"></div></div></div>
<div class="pane" id="pane-rival"><div class="ph">&#9876; Rival VxV - Em breve</div></div>
<div class="pane" id="pane-mapa">
<div class="card"><h3>&#128506; Mapa Virtual - Tracado 101</h3>
<canvas id="mapa-canvas" width="800" height="500"></canvas>
<div class="mapa-stats">
<div class="stat-box"><div class="val">1015m</div><div class="lbl">Distancia</div></div>
<div class="stat-box"><div class="val">~43s</div><div class="lbl">Por volta</div></div>
<div class="stat-box"><div class="val">~83</div><div class="lbl">Voltas/h</div></div>
<div class="stat-box"><div class="val">INICIANTE</div><div class="lbl">Dificuldade</div></div>
</div></div></div>
<div class="pane" id="pane-tracados">
<div class="card"><h3>&#128194; Tracados KGV - Granja Viana</h3>
<div class="tr-filters">
<button class="on" onclick="FK.filterTr(this,'all')">Todos (31)</button>
<button onclick="FK.filterTr(this,'FCIL')">Facil</button>
<button onclick="FK.filterTr(this,'MDIO')">Medio</button>
<button onclick="FK.filterTr(this,'DIFCIL')">Dificil</button>
<button onclick="FK.filterTr(this,'EXPERT')">Expert</button>
<button onclick="FK.filterTr(this,'suspenso')">Suspenso</button>
</div>
<div class="tr-grid" id="tr-grid"></div></div></div>
<div class="pane" id="pane-pilotos">
<div class="card"><h3>&#128100; Pilotos FKART</h3><div id="pilotos-body"></div></div></div>
</div>
<div id="tr-overlay" class="overlay" onclick="if(event.target===this)FK.closeTr()">
<div class="modal">
<button class="modal-close" onclick="FK.closeTr()">&#10005;</button>
<img id="tr-modal-img" src="" alt="">
<h3 id="tr-modal-num"></h3>
<div id="tr-modal-info" style="color:var(--mut);font-size:13px;line-height:1.8"></div>
</div></div>
<footer>FORCE KART RACING &middot; SINCE 2004 &middot; TEAM RACE</footer>
"""
f.write(body)
js1 = """<script>
var FK={
myKarts:['064','037'],
raceTotal:10800,
raceElapsed:2730,
_mapW:800,_mapH:500,_mapPts:null,_mapAnim:null,_kartT:0,
tr:[
{n:'101',d:1015,dif:'INICIANTE',st:'ativo',id:'1-F3_03fnAFBHmhaV3JKA2Y41R_a78SNI'},
{n:'102',d:990,dif:'DIFCIL',st:'ativo',id:'19Lc7SLZjsBSJ0fJ2teYhTf-oJB0JDoHs'},
{n:'103',d:883,dif:'MDIO',st:'ativo',id:'1etBHmTjF8R9m3XoNOgvE4CoCEqWFDVFO'},
{n:'104',d:838,dif:'MDIO',st:'ativo',id:'1CQQ_tW1RLjaUyjKFPKH67iowDkRrQEYM'},
{n:'105',d:730,dif:'FCIL',st:'ativo',id:'1T13YhSkt4PqljsSDCm8JUC_i5nlInCx4'},
{n:'106',d:705,dif:'FCIL',st:'ativo',id:'1jdO7TsqIM_MeV2zD05BU3lr2RSsO54GZ'},
{n:'107',d:678,dif:'MDIO',st:'ativo',id:'1EZQ65yA2rMQSUMiF5sc9Z3QbK4aDMGJS'},
{n:'108',d:770,dif:'MDIO',st:'ativo',id:'17BQ6ZEu9XVIUMHyh1Xr8hPOf7Mw3A7sX'},
{n:'111',d:945,dif:'MDIO',st:'ativo',id:'1vvR9l1DQoBQ-Q2mrqXbc3xJK8cj5opOt'},
{n:'112',d:920,dif:'DIFCIL',st:'ativo',id:'1vAa2rUhjSnfj-bEjg3rZ7x188vVvVK4k'},
{n:'113',d:865,dif:'MDIO',st:'ativo',id:'1lWKl9W5lr_faefpYb_0PVB6qTEx5E2zW'},
{n:'114',d:975,dif:'DIFCIL',st:'ativo',id:'18TCk_XAzaJd0e9oNvT-91NYvjwnsSZYG'},
{n:'115',d:1000,dif:'DIFCIL',st:'ativo',id:'1kk8KUNoSl67hTLcXP-CMrez1rPi-AIaQ'},
{n:'116',d:840,dif:'MDIO',st:'ativo',id:'18M-T3vUwTURglFb2jJmikK5QHe8_10oq'},
{n:'119',d:820,dif:'MDIO',st:'ativo',id:'1IYSJzkU0tWJWFDJ9YNH9LJXgvk2pdmeE'},
{n:'120',d:795,dif:'MDIO',st:'ativo',id:'1J2Clo0CXofNTlvJKPGtxuliQx5Vospki'},
{n:'121',d:800,dif:'FCIL',st:'ativo',id:'1ErXEWT45s-jboAZYHTtmq6vuJYh-LHy6'},
{n:'122',d:750,dif:'DIFCIL',st:'ativo',id:'1lykN-8WUNupCPGxlqQ8vXh996aH4Bami'},
{n:'123',d:720,dif:'DIFCIL',st:'ativo',id:'104OHUK1IGbXWKtLOt72Gf-Rx0PVqj2Zi'},
{n:'124',d:655,dif:'FCIL',st:'ativo',id:'1ebCy2nmkQKoTdzCsqFy6Fr4kHQslO1A3'},
{n:'125',d:625,dif:'FCIL',st:'ativo',id:'14xgWCCKlqe732TV1zNVdWG8vyammTaaQ'},
{n:'126',d:710,dif:'MDIO',st:'ativo',id:'1x7hPmVVNrKA8ffT6hp-URxNXhHNJCOUQ'},
{n:'127',d:680,dif:'MDIO',st:'ativo',id:'1l83dhc_53hZaUzyxoGn61lg3IGBQkIlM'},
{n:'132',d:615,dif:'FCIL',st:'ativo',id:'1djH1V3vXilSFndMyja6oOpUubS5hbTo6'},
{n:'134',d:625,dif:'FCIL',st:'ativo',id:'1mzcg8QC3VVr_m3DHkkfMnsM1n7gaB0if'},
{n:'137',d:825,dif:'MDIO',st:'ativo',id:'1yKnU0bXTwBAbR7NcR4QmlnXoU-tIQztG'},
{n:'138',d:780,dif:'DIFCIL',st:'ativo',id:'1AHfFKbIEBf-O_d8nhaCz6TR-HnrrSQvM'},
{n:'139',d:755,dif:'MDIO',st:'suspenso',id:'1JKAnh60DvkQG-hOwjfdtGWnU_qEZ8cC7'},
{n:'140',d:590,dif:'FCIL',st:'suspenso',id:'1ftP0JKXYAY1lTyqgRNSesgTeAdlwfwnE'},
{n:'141',d:660,dif:'EXPERT',st:'ativo',id:'1uPZ0ruXh4dTjomKFiNgaGW_cKk2SBijf'},
{n:'145',d:950,dif:'DIFCIL',st:'suspenso',id:'1f7_ecT9GE4gj6L7ZG8BH3A0QYS-0zX45'}
],
"""
f.write(js1)
js2 = """demo_data:[
{pos:1,kart:'013',t:'PICOLE',cat:'SUPER PRO',laps:52,last:'00:51.800',best:'00:51.491',diff:'+0.000',gap:'+0.000'},
{pos:2,kart:'027',t:'TROVAO',cat:'SUPER PRO',laps:52,last:'00:51.900',best:'00:51.650',diff:'+0.159',gap:'+0.159'},
{pos:3,kart:'064',t:'FKART PILOTO A',cat:'SUPER PRO',laps:51,last:'00:52.300',best:'00:52.200',diff:'+0.709',gap:'+1 volta'},
{pos:4,kart:'088',t:'RELAMPAGO',cat:'ELITE',laps:51,last:'00:52.500',best:'00:52.380',diff:'+0.889',gap:'+1 volta'},
{pos:5,kart:'045',t:'TUBARAO',cat:'ELITE',laps:50,last:'00:52.600',best:'00:52.500',diff:'+1.009',gap:'+2 voltas'},
{pos:6,kart:'037',t:'FKART PILOTO B',cat:'ELITE',laps:50,last:'00:52.700',best:'00:52.650',diff:'+1.159',gap:'+2 voltas'},
{pos:7,kart:'071',t:'AGUIA',cat:'AMADOR',laps:49,last:'00:53.100',best:'00:52.900',diff:'+1.409',gap:'+3 voltas'},
{pos:8,kart:'002',t:'LEAO',cat:'AMADOR',laps:49,last:'00:53.200',best:'00:53.000',diff:'+1.509',gap:'+3 voltas'},
{pos:9,kart:'033',t:'TOURO',cat:'AMADOR',laps:48,last:'00:53.500',best:'00:53.300',diff:'+1.809',gap:'+4 voltas'},
{pos:10,kart:'055',t:'COBRA',cat:'AMADOR',laps:48,last:'00:53.800',best:'00:53.600',diff:'+2.109',gap:'+4 voltas'},
{pos:11,kart:'019',t:'FALCAO',cat:'AMADOR',laps:47,last:'00:54.000',best:'00:53.800',diff:'+2.309',gap:'+5 voltas'},
{pos:12,kart:'077',t:'LOBO',cat:'AMADOR',laps:47,last:'00:54.200',best:'00:54.000',diff:'+2.509',gap:'+5 voltas'},
{pos:13,kart:'099',t:'JOSE NETO',cat:'AMADOR',laps:47,last:'00:54.500',best:'00:54.200',diff:'+2.709',gap:'+0.350'}
],
"""
f.write(js2)
js3 = """isMy:function(k){return FK.myKarts.indexOf(k)>=0;},
tab:function(name){
document.querySelectorAll('.tab').forEach(function(t){t.classList.remove('on');});
document.querySelectorAll('.pane').forEach(function(p){p.classList.remove('on');});
var t=document.querySelector('.tab[data-tab="'+name+'"]');
var p=document.getElementById('pane-'+name);
if(t)t.classList.add('on');
if(p)p.classList.add('on');
if(name==='mapa')FK.drawMap101();
if(name==='tracados')FK.rTracados('all');
if(name==='pilotos')FK.rPilotos();
if(name==='comp')FK.rComp();
},
upd:function(){FK.rPlacar();},
render:function(){FK.rPlacar();FK.rComp();FK.rTracados('all');FK.rPilotos();FK.loadWx();FK.startClock();FK.startTimer();},
startClock:function(){
setInterval(function(){
FK.raceElapsed+=1;
var e=FK.raceElapsed;
var h=Math.floor(e/3600);var m=Math.floor((e%3600)/60);var s=e%60;
var el=document.getElementById('elapsed');
if(el)el.textContent=(h>0?(h<10?'0'+h:h)+':':'')+(m<10?'0'+m:m)+':'+(s<10?'0'+s:s);
var rem=FK.raceTotal-e;
if(rem<0)rem=0;
var rh=Math.floor(rem/3600);var rm=Math.floor((rem%3600)/60);var rs=rem%60;
var rel=document.getElementById('remaining');
if(rel)rel.textContent=(rh>0?(rh<10?'0'+rh:rh)+':':'')+(rm<10?'0'+rm:rm)+':'+(rs<10?'0'+rs:rs);
},1000);
},
startTimer:function(){setInterval(function(){FK.upd();},30000);},
rPlacar:function(){
var data=FK.demo_data;
var html='';
data.forEach(function(d){
var my=FK.isMy(d.kart);
var pc='';
if(d.pos===1)pc='p1';else if(d.pos===2)pc='p2';else if(d.pos===3)pc='p3';
html+='<tr class="'+(my?'my-kart':'')+'">'+
'<td><span class="pos-badge '+pc+'">'+d.pos+'</span></td>'+
'<td><span class="kart-num'+(my?' my':'')+'">'+d.kart+(my?' &#11088;':'')+'</span></td>'+
'<td style="font-weight:'+(my?'700':'400')+'">'+d.t+'</td>'+
'<td class="gap-badge">'+d.cat+'</td>'+
'<td style="color:var(--acc)">'+d.laps+'</td>'+
'<td style="color:'+(my?'var(--acc)':'var(--txt)')+'">'+d.best+'</td>'+
'<td>'+d.last+'</td>'+
'<td class="gap-badge">'+d.gap+'</td>'+
'<td class="gap-badge">'+d.diff+'</td>'+
'</tr>';
});
var el=document.getElementById('placar-body');
if(el)el.innerHTML=html;
var l=FK.demo_data[0];
var li=document.getElementById('leader-info');
if(li)li.textContent=l.kart+' ('+l.t+') - '+l.laps+' voltas';
},
rComp:function(){
var data=FK.demo_data.slice(0,8);
var best=parseFloat(data[0].best.replace(':','').replace(':','.'));
var html='';
data.forEach(function(d){
var my=FK.isMy(d.kart);
var t=parseFloat(d.best.replace(':','').replace(':','.'));
var pct=Math.min(100,Math.round((best/t)*100));
var color=my?'#F7C600':'#4fc3f7';
html+='<div style="margin-bottom:8px">'+
'<div style="display:flex;justify-content:space-between;margin-bottom:3px">'+
'<span style="font-weight:'+(my?'700':'400')+';color:'+(my?'var(--acc)':'var(--txt)')+'">'+
'#'+d.pos+' Kart '+d.kart+' - '+d.t+(my?' &#11088;':'')+'</span>'+
'<span style="color:var(--mut);font-size:11px">'+d.best+'</span></div>'+
'<div class="comp-bar-wrap"><div class="comp-bar" style="width:'+pct+'%;background:'+color+'">'+pct+'%</div></div>'+
'</div>';
});
var el=document.getElementById('comp-body');
if(el)el.innerHTML=html;
},
"""
f.write(js3)
js4 = """rTracados:function(filter){
if(!filter)filter='all';
var g=document.getElementById('tr-grid');
if(!g)return;
var html='';
FK.tr.forEach(function(t){
var show=filter==='all'||t.st===filter||t.dif===filter;
if(!show)return;
var dc='dif-'+t.dif.toLowerCase().replace(/[^a-z]/g,'');
var th='https://drive.google.com/thumbnail?id='+t.id+'&sz=w400';
html+='<div class="tr-card" onclick="FK.openTr(\\\''+t.n+'\\\')">'+
'<img class="tr-thumb" src="'+th+'" alt="'+t.n+'" loading="lazy" onerror="this.style.background=\'#1a1d26\'">'+
'<div class="tr-info">'+
'<div class="tr-num">'+t.n+'</div>'+
'<div class="tr-dist">'+t.d+'m</div>'+
'<span class="tr-dif '+dc+'">'+t.dif+(t.st==='suspenso?' - SUSPENSO':'')+'</span>'+
'</div></div>';
});
if(!html)html='<p style="color:var(--mut);padding:20px">Nenhum tracado encontrado</p>';
g.innerHTML=html;
},
filterTr:function(btn,filter){
document.querySelectorAll('.tr-filters button').forEach(function(b){b.classList.remove('on');});
btn.classList.add('on');
FK.rTracados(filter);
},
openTr:function(num){
var t=FK.tr.find(function(x){return x.n===num;});
if(!t)return;
document.getElementById('tr-modal-img').src='https://drive.google.com/thumbnail?id='+t.id+'&sz=w800';
document.getElementById('tr-modal-num').textContent='Tracado '+t.n;
var dc='dif-'+t.dif.toLowerCase().replace(/[^a-z]/g,'');
document.getElementById('tr-modal-info').innerHTML=
'Distancia: <strong style="color:var(--acc)">'+t.d+'m</strong><br>'+
'Dificuldade: <span class="tr-dif '+dc+'">'+t.dif+'</span><br>'+
'Status: '+(t.st==='ativo'?'<span style="color:#66bb6a">&#10003; Ativo</span>':'<span style="color:#ef5350">&#9888; Suspenso</span>')+'<br>'+
'Tempo estimado: ~'+Math.round(t.d/23.6)+'s por volta';
document.getElementById('tr-overlay').classList.add('show');
},
closeTr:function(){document.getElementById('tr-overlay').classList.remove('show');},
rPilotos:function(){
var html='<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px">';
[{kart:'064',name:'FKART PILOTO A',cat:'SUPER PRO',role:'Titular'},
{kart:'037',name:'FKART PILOTO B',cat:'ELITE',role:'Titular'}].forEach(function(p){
html+='<div class="card" style="border-color:var(--acc)">'+
'<div style="display:flex;align-items:center;gap:12px">'+
'<span class="kart-num my">'+p.kart+'</span>'+
'<div><div style="font-weight:700;color:var(--acc)">'+p.name+'</div>'+
'<div style="color:var(--mut);font-size:11px">'+p.cat+' &middot; '+p.role+'</div></div></div></div>';
});
html+='</div>';
var el=document.getElementById('pilotos-body');
if(el)el.innerHTML=html;
},
loadWx:function(){
var url='https://api.open-meteo.com/v1/forecast?latitude=-23.6014&longitude=-46.8575&current=temperature_2m,weathercode,windspeed_10m,winddirection_10m,windgusts_10m,precipitation_probability&timezone=America/Sao_Paulo';
var req=new XMLHttpRequest();req.open('GET',url);
req.onload=function(){try{
var d=JSON.parse(req.responseText).current;
var wc=d.weathercode;
var icon=wc===0?'Limpo':wc<=2?'Parcialmente nublado':wc<=3?'Nublado':wc<=67?'Chuva':'Neve';
var dirs=['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSO','SO','OSO','O','ONO','NO','NNO'];
var di=Math.round(d.winddirection_10m/22.5)%16;
var wxEl=document.getElementById('wxbar');
if(wxEl)wxEl.innerHTML='KGV | '+icon+' | '+d.windspeed_10m+'km/h '+dirs[di]+' | '+
'<span style="color:var(--acc)">'+d.temperature_2m+'C</span> | '+
'<strong style="color:'+(d.precipitation_probability>=30?'#4fc3f7':'#66bb6a')+'">'+(d.precipitation_probability>=30?'Chuva possivel':'Sem chuva')+'</strong>';
}catch(e){var el2=document.getElementById('wxbar');if(el2)el2.textContent='KGV - Granja Viana';}};
req.onerror=function(){var el3=document.getElementById('wxbar');if(el3)el3.textContent='KGV - Granja Viana';};
req.send();setInterval(function(){FK.loadWx();},600000);
},
"""
f.write(js4)
js5 = """_map101pts:function(){var W=800,H=500;return [[0.12,0.22],[0.18,0.18],[0.28,0.15],[0.40,0.14],[0.52,0.14],[0.62,0.15],[0.72,0.18],[0.80,0.24],[0.84,0.32],[0.82,0.40],[0.76,0.46],[0.68,0.50],[0.60,0.52],[0.54,0.56],[0.52,0.64],[0.54,0.72],[0.60,0.78],[0.68,0.82],[0.76,0.82],[0.82,0.78],[0.86,0.70],[0.84,0.62],[0.78,0.58],[0.70,0.56],[0.62,0.60],[0.56,0.68],[0.50,0.76],[0.42,0.80],[0.32,0.80],[0.22,0.76],[0.14,0.68],[0.10,0.58],[0.10,0.46],[0.12,0.34],[0.12,0.22]].map(function(p){return[p[0]*W,p[1]*H];});},
drawMap101Static:function(){
var cv=document.getElementById('mapa-canvas');if(!cv)return;
var ctx=cv.getContext('2d');var W=FK._mapW,H=FK._mapH;
cv.width=W*2;cv.height=H*2;cv.style.width=W+'px';cv.style.height=H+'px';ctx.scale(2,2);
ctx.fillStyle='#0a0c10';ctx.fillRect(0,0,W,H);
ctx.fillStyle='rgba(0,40,0,0.3)';ctx.beginPath();ctx.ellipse(W*0.5,H*0.5,W*0.44,H*0.38,0,0,Math.PI*2);ctx.fill();
var pts=FK._map101pts();FK._mapPts=pts;
var sectors=[{from:0,to:5,color:'#F7C600'},{from:5,to:17,color:'#4fc3f7'},{from:17,to:pts.length-1,color:'#81c784'}];
sectors.forEach(function(s){ctx.beginPath();ctx.moveTo(pts[s.from][0],pts[s.from][1]);for(var i=s.from+1;i<=s.to&&i<pts.length;i++)ctx.lineTo(pts[i][0],pts[i][1]);ctx.strokeStyle=s.color;ctx.lineWidth=7;ctx.lineCap='round';ctx.lineJoin='round';ctx.shadowColor=s.color;ctx.shadowBlur=8;ctx.stroke();ctx.shadowBlur=0;});
ctx.beginPath();ctx.moveTo(pts[0][0],pts[0][1]);ctx.lineTo(pts[1][0],pts[1][1]);ctx.strokeStyle='#ef5350';ctx.lineWidth=4;ctx.shadowColor='#ef5350';ctx.shadowBlur=10;ctx.stroke();ctx.shadowBlur=0;
var corners=[0,4,8,11,15,20,25,30];corners.forEach(function(ci,i){if(ci>=pts.length)return;ctx.beginPath();ctx.arc(pts[ci][0],pts[ci][1],7,0,Math.PI*2);ctx.fillStyle='rgba(255,255,255,0.15)';ctx.fill();ctx.strokeStyle='#fff';ctx.lineWidth=1.5;ctx.stroke();ctx.font='bold 9px sans-serif';ctx.fillStyle='#fff';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('C'+(i+1),pts[ci][0],pts[ci][1]);});
ctx.beginPath();ctx.arc(W*0.47,H*0.47,38,0,Math.PI*2);ctx.fillStyle='rgba(13,15,20,0.85)';ctx.fill();ctx.strokeStyle='#2e3348';ctx.lineWidth=1.5;ctx.stroke();ctx.font='bold 18px sans-serif';ctx.fillStyle='#F7C600';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('101',W*0.47,H*0.44);ctx.font='10px sans-serif';ctx.fillStyle='#7a8099';ctx.fillText('1015m',W*0.47,H*0.51);
var legend=[{c:'#F7C600',l:'S1'},{c:'#4fc3f7',l:'S2'},{c:'#81c784',l:'S3'},{c:'#ef5350',l:'S/F'}];
legend.forEach(function(item,i){var lx=16,ly=H-64+(i*15);ctx.fillStyle=item.c;ctx.fillRect(lx,ly,16,8);ctx.font='10px sans-serif';ctx.fillStyle='#aaa';ctx.textAlign='left';ctx.textBaseline='middle';ctx.fillText(item.l,lx+20,ly+4);});
},
drawMap101:function(){FK.drawMap101Static();if(FK._mapAnim)cancelAnimationFrame(FK._mapAnim);FK._kartT=0;FK.animateKart();},
animateKart:function(){
var pts=FK._map101pts();if(!pts||pts.length<2)return;
FK._kartT+=0.008;if(FK._kartT>=pts.length-1)FK._kartT=0;
var seg=Math.floor(FK._kartT);var frac=FK._kartT-seg;if(seg>=pts.length-1)seg=pts.length-2;
var x=pts[seg][0]+(pts[seg+1][0]-pts[seg][0])*frac;var y=pts[seg][1]+(pts[seg+1][1]-pts[seg][1])*frac;
FK.drawMap101Static();
var cv=document.getElementById('mapa-canvas');if(!cv)return;
var ctx=cv.getContext('2d');ctx.save();ctx.scale(2,2);
ctx.beginPath();ctx.ellipse(x,y,14,10,0,0,Math.PI*2);ctx.fillStyle='#F7C600';ctx.shadowColor='#F7C600';ctx.shadowBlur=12;ctx.fill();ctx.shadowBlur=0;
ctx.font='bold 8px sans-serif';ctx.fillStyle='#000';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('064',x,y);ctx.restore();
FK._mapAnim=requestAnimationFrame(FK.animateKart);}
"""
f.write(js5)
js6 = """};
document.querySelectorAll('.tab').forEach(function(t){
t.addEventListener('click',function(){FK.tab(t.getAttribute('data-tab'));});
});
document.addEventListener('DOMContentLoaded',function(){FK.render();});
if(document.readyState!=='loading')FK.render();
</script>
</body>
</html>
"""
f.write(js6)
f.close()
import os
sz=os.path.getsize('public/index.html')
print(f"COMPLETE: {sz} bytes")

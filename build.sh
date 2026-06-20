#!/bin/bash
F=public/index.html
echo -n "" > $F
printf '<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n<title>FKART Endurance Monitor v2.3</title>\n' >> $F
printf '<style>\n*{margin:0;padding:0;box-sizing:border-box}\n' >> $F
printf ':root{--acc:#F7C600;--acc2:#CC2200;--bg:#0c0d0f;--card:#13151a;--txt:#e8eaf0;--mut:#7a8099;--border:#1e2130}\n' >> $F
printf 'body{background:var(--bg);color:var(--txt);font-family:-apple-system,BlinkMacSystemFont,sans-serif;min-height:100vh;overflow-x:hidden}\n' >> $F
printf '#topbar{display:flex;align-items:center;justify-content:space-between;padding:8px 16px;background:#0a0b0d;border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}\n' >> $F
printf '.logo-wrap{display:flex;flex-direction:column;line-height:1}\n.logo-text{font-size:22px;font-weight:900;font-style:italic;letter-spacing:-1px}\n' >> $F
printf '.logo-text .lf{color:#999}.logo-text .lk{background:linear-gradient(90deg,#cc2200,#ff6600);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}\n' >> $F
printf '.logo-sub{font-size:7px;color:#555;letter-spacing:2px;text-transform:uppercase;margin-top:1px}\n' >> $F
printf '#race-title{text-align:center;flex:1}#race-title h2{font-size:14px;font-weight:700;color:var(--txt)}#race-title p{font-size:11px;color:var(--mut)}\n' >> $F
printf '#timer-block{text-align:right}.timer-lbl{font-size:9px;color:var(--mut);text-transform:uppercase;letter-spacing:1px}\n' >> $F
printf '.timer-val{font-size:26px;font-weight:900;color:var(--acc);letter-spacing:2px;font-variant-numeric:tabular-nums}.timer-remain{font-size:11px;color:var(--mut)}\n' >> $F
printf '#infobar{background:#0e0f12;border-bottom:1px solid var(--border);padding:5px 16px;display:flex;align-items:center;gap:12px;flex-wrap:wrap}\n' >> $F
printf '.info-badge{background:var(--card);border:1px solid var(--border);border-radius:4px;padding:3px 8px;font-size:11px;cursor:pointer;color:var(--txt)}\n' >> $F
printf '.info-badge.demo{background:#2a1f00;border-color:#a07800;color:#F7C600}.info-badge.btn{background:#1a1d26;border-color:#2e3348}\n' >> $F
printf '#wxbar{flex:1;font-size:11px;color:var(--mut)}\n' >> $F
printf '#tabs{display:flex;gap:2px;padding:6px 12px 0;background:#0a0b0d;border-bottom:1px solid var(--border);overflow-x:auto}\n' >> $F
printf '.tab{padding:7px 14px;font-size:12px;font-weight:600;border-radius:6px 6px 0 0;cursor:pointer;color:var(--mut);white-space:nowrap;border:1px solid transparent;border-bottom:none;background:#0e0f12;user-select:none}\n' >> $F
printf '.tab.active{color:var(--acc);background:var(--bg);border-color:var(--border)}.tab:hover:not(.active){color:var(--txt);background:#141620}\n' >> $F
printf '#content{padding:16px;min-height:calc(100vh - 160px)}.pane{display:none}.pane.active{display:block}\n' >> $F
printf 'table{width:100%%;border-collapse:collapse;font-size:13px}\n' >> $F
printf 'th{padding:8px 10px;text-align:left;color:var(--mut);font-size:11px;text-transform:uppercase;letter-spacing:.5px;border-bottom:1px solid var(--border);font-weight:600}\n' >> $F
printf 'td{padding:9px 10px;border-bottom:1px solid #191b22;vertical-align:middle}tr:hover td{background:#161820}\n' >> $F
printf 'tr.my-kart td{background:#1a1600!important;border-left:2px solid var(--acc)}tr.my-kart:hover td{background:#201c00!important}\n' >> $F
printf '.kart-num{display:inline-flex;align-items:center;justify-content:center;width:36px;height:24px;border-radius:4px;font-weight:800;font-size:13px;background:#1e2130;color:var(--txt)}.kart-num.my{background:var(--acc);color:#000}\n' >> $F
printf '.pos-badge{width:28px;height:28px;border-radius:50%%;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:13px;background:#1e2130;color:var(--txt)}\n' >> $F
printf '.pos-badge.p1{background:#F7C600;color:#000}.pos-badge.p2{background:#9e9e9e;color:#000}.pos-badge.p3{background:#cd7f32;color:#000}\n' >> $F
printf '.gold{color:var(--acc);font-weight:700}.red{color:#ef5350}.green{color:#66bb6a}.mut{color:var(--mut)}\n' >> $F
printf '.card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:16px;margin-bottom:12px}\n' >> $F
printf '.card h3{font-size:13px;font-weight:700;margin-bottom:12px;color:var(--mut);text-transform:uppercase;letter-spacing:.5px}\n' >> $F
printf '.ph{text-align:center;padding:60px 20px;color:var(--mut)}.ph h3{font-size:18px;font-weight:700;margin-bottom:8px;color:var(--txt)}.ph p{font-size:13px}\n' >> $F
printf '.tracado-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:12px}\n' >> $F
printf '.tr-card{background:var(--card);border:1px solid var(--border);border-radius:10px;overflow:hidden;cursor:pointer;transition:.2s}\n' >> $F
printf '.tr-card:hover{border-color:var(--acc);transform:translateY(-2px)}\n' >> $F
printf '.tr-thumb{width:100%%;height:110px;object-fit:cover;background:#0a0c10}.tr-info{padding:10px}.tr-num{font-size:20px;font-weight:900;color:var(--acc)}\n' >> $F
printf '.tr-dist{font-size:12px;color:var(--mut)}.tr-dif{display:inline-block;padding:2px 7px;border-radius:3px;font-size:10px;font-weight:700;margin-top:4px}\n' >> $F
printf '.dif-iniciante,.dif-facil{background:#1b3a1b;color:#66bb6a}.dif-medio{background:#2a2a00;color:#F7C600}\n' >> $F
printf '.dif-dificil{background:#3a1b1b;color:#ef5350}.dif-expert{background:#2d1b3a;color:#ce93d8}.dif-suspenso{background:#1e2130;color:#7a8099;text-decoration:line-through}\n' >> $F
printf '.tr-overlay{position:fixed;inset:0;background:rgba(0,0,0,.85);z-index:200;display:none;align-items:center;justify-content:center}.tr-overlay.show{display:flex}\n' >> $F
printf '.tr-modal{background:var(--card);border:1px solid var(--border);border-radius:14px;max-width:500px;width:90%%;max-height:90vh;overflow-y:auto}\n' >> $F
printf '.tr-modal-img{width:100%%;aspect-ratio:16/9;object-fit:contain;background:#0a0c10}.tr-modal-body{padding:20px}\n' >> $F
printf '.tr-modal-body h2{font-size:28px;font-weight:900;color:var(--acc);margin-bottom:4px}\n' >> $F
printf '.tr-filters{display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap}\n' >> $F
printf '.tr-filters button{padding:5px 12px;border-radius:6px;border:1px solid var(--border);background:var(--card);color:var(--mut);font-size:12px;cursor:pointer}\n' >> $F
printf '.tr-filters button.on{background:#1a1600;border-color:var(--acc);color:var(--acc)}\n' >> $F
printf '#mapa-canvas{display:block;margin:0 auto;border-radius:12px;max-width:100%%}\n' >> $F
printf '.map-stats{display:flex;gap:16px;justify-content:center;margin-top:12px;flex-wrap:wrap}.map-stat{text-align:center}\n' >> $F
printf '.map-stat-val{font-size:18px;font-weight:900;color:var(--acc)}.map-stat-lbl{font-size:10px;color:var(--mut);text-transform:uppercase;letter-spacing:.5px}\n' >> $F
printf 'footer{text-align:center;padding:20px;color:#333;font-size:10px;letter-spacing:2px;text-transform:uppercase;border-top:1px solid var(--border);margin-top:20px}\n' >> $F
printf '</style></head>\n<body>\n' >> $F
echo "CSS done: $(wc -c < $F) bytes"

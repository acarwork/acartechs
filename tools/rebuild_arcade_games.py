# -*- coding: utf-8 -*-
"""Rebuild all mini-games (except Brick Blitz) as solid, playable single-file games."""
from pathlib import Path

PUBLIC = Path(r"C:\Users\facar\acartechs-deploy\public")

SHELL = r'''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,maximum-scale=1,user-scalable=no"/>
<title>__TITLE__ – AcarTechs Arcade</title>
<meta name="description" content="__DESC__"/>
<link rel="canonical" href="https://acartechs.com/__SLUG__/"/>
<style>
:root{--bg0:#04060f;--neon:#22d3ee;--neon2:#a78bfa;--pink:#f472b6;--gold:#fbbf24;--text:#eef6ff;--muted:#94a3b8;--panel:rgba(6,12,28,.94);--line:rgba(125,211,252,.25)}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100%;overflow:hidden;background:radial-gradient(900px 500px at 20% 0%,#1e1b4b 0%,transparent 55%),linear-gradient(165deg,#04060f,#0a1230 55%,#050a16);color:var(--text);font-family:Inter,Segoe UI,system-ui,sans-serif;touch-action:none;user-select:none}
#app{position:relative;width:100%;height:100%;min-height:100dvh}
canvas#game{display:block;width:100%;height:100%;background:#03060f;object-fit:contain}
.screen{position:absolute;inset:0;display:none;align-items:center;justify-content:center;padding:16px;z-index:5;overflow:auto}
.screen.is-on{display:flex}
.panel{width:min(520px,100%);background:var(--panel);border:1px solid var(--line);border-radius:18px;box-shadow:0 30px 80px rgba(0,0,0,.45);padding:22px 18px 16px;text-align:center;backdrop-filter:blur(12px)}
.logo{font-size:clamp(26px,6.5vw,44px);font-weight:900;letter-spacing:.03em;background:linear-gradient(90deg,#67e8f9,#a78bfa 50%,#f472b6);-webkit-background-clip:text;background-clip:text;color:transparent}
.logo small{display:block;margin-top:8px;font-size:11px;letter-spacing:.24em;color:var(--neon);font-weight:800}
.genre{display:inline-block;margin:8px 0;padding:4px 10px;border-radius:999px;border:1px solid rgba(34,211,238,.35);background:rgba(34,211,238,.1);color:var(--neon);font-size:11px;font-weight:900;letter-spacing:.08em;text-transform:uppercase}
.tagline{color:var(--muted);font-size:13px;margin:8px 0 14px;line-height:1.45}
.btn-col{display:grid;gap:8px}
.btn{appearance:none;border:1px solid rgba(125,211,252,.28);background:linear-gradient(180deg,rgba(56,189,248,.16),rgba(15,23,42,.5));color:var(--text);font-weight:800;font-size:14px;border-radius:12px;padding:12px 14px;cursor:pointer}
.btn:hover{border-color:rgba(34,211,238,.6)}
.btn.primary{background:linear-gradient(135deg,#22d3ee,#818cf8 55%,#c084fc);color:#06101f;border:none}
.btn.ghost{background:transparent}
.btn.danger{background:linear-gradient(135deg,#fb7185,#e11d48);border:none;color:#fff}
.lang-switch{display:inline-grid;grid-template-columns:1fr 1fr;gap:8px;min-width:120px;margin:0 0 12px}
.lang-switch button{appearance:none;border:1px solid rgba(125,211,252,.28);background:rgba(15,23,42,.55);color:var(--muted);font-size:12px;font-weight:900;border-radius:10px;padding:10px;cursor:pointer}
.lang-switch button.is-on{background:linear-gradient(135deg,rgba(34,211,238,.32),rgba(129,140,248,.34));border-color:rgba(34,211,238,.7);color:#fff}
.menu-tools{display:flex;justify-content:space-between;align-items:center;margin-top:12px;gap:8px;flex-wrap:wrap}
.sound-toggle{font-size:12px;font-weight:700;color:var(--muted);cursor:pointer;background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:999px;padding:7px 11px}
.sound-toggle.is-on{color:var(--neon)}
.howto{text-align:left;color:#cbd5e1;font-size:13px;line-height:1.5;margin:8px 0 14px}
.howto li{margin:0 0 7px 16px}
.level-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin:10px 0 14px}
.level-btn{appearance:none;border:1px solid rgba(125,211,252,.25);background:rgba(15,23,42,.55);color:#e2e8f0;border-radius:10px;padding:12px 4px;font-weight:800;cursor:pointer}
.level-btn.is-locked{opacity:.35;cursor:not-allowed}
.level-btn .stars{display:block;font-size:10px;color:var(--gold);margin-top:3px}
.hud{position:absolute;top:10px;left:10px;right:10px;z-index:6;display:none;pointer-events:none;gap:6px;justify-content:space-between;align-items:flex-start}
.hud.is-on{display:flex}
.hud-group{display:flex;flex-wrap:wrap;gap:5px}
.chip{background:rgba(2,8,20,.78);border:1px solid var(--line);border-radius:999px;padding:6px 10px;font-size:11px;font-weight:800;color:#e2e8f0}
.chip b{color:var(--neon);margin-left:3px}
.hud-actions{display:flex;gap:5px;pointer-events:auto}
.icon-btn{width:36px;height:36px;border-radius:11px;border:1px solid var(--line);background:rgba(2,8,20,.85);color:#e2e8f0;font-weight:900;cursor:pointer}
.toast{position:absolute;left:50%;top:38%;transform:translate(-50%,-50%);z-index:4;display:none;text-align:center;pointer-events:none;text-shadow:0 8px 24px #000}
.toast.is-on{display:block}
.toast h2{font-size:clamp(24px,5vw,40px);font-weight:900}
.toast p{color:var(--muted);font-weight:600}
.stars-big{font-size:28px;color:var(--gold);letter-spacing:4px;margin:6px 0}
.fs-note{font-size:11px;color:var(--muted)}
</style>
</head>
<body>
<div id="app">
<canvas id="game" width="__CW__" height="__CH__" aria-label="__TITLE__"></canvas>
<div class="hud" id="hud">
  <div class="hud-group">
    <div class="chip"><span data-i18n="hudScore">SKOR</span> <b id="hudScore">0</b></div>
    <div class="chip"><span data-i18n="hudLevel">LEVEL</span> <b id="hudLevel">1</b></div>
    <div class="chip"><span data-i18n="hudLives">CAN</span> <b id="hudLives">3</b></div>
    <div class="chip"><span id="hudExtraLabel">—</span> <b id="hudExtra">0</b></div>
  </div>
  <div class="hud-actions">
    <button class="icon-btn" id="btnPause" type="button">II</button>
    <button class="icon-btn" id="btnSoundHud" type="button">🔊</button>
    <button class="icon-btn" id="btnExit" type="button">✕</button>
  </div>
</div>
<div class="toast" id="toast"><h2 id="toastTitle"></h2><p id="toastText"></p></div>

<section class="screen is-on" id="screenMenu">
  <div class="panel">
    <div class="logo">__TITLE__<small>ACARTECHS ARCADE</small></div>
    <span class="genre" data-i18n="genre">__GENRE_TR__</span>
    <p class="tagline" data-i18n="tagline">__TAG_TR__</p>
    <div class="lang-switch"><button type="button" id="btnLangTr" class="is-on">TR</button><button type="button" id="btnLangEn">EN</button></div>
    <div class="btn-col">
      <button class="btn primary" id="btnStart" type="button" data-i18n="btnStart">BAŞLA</button>
      <button class="btn" id="btnLevels" type="button" data-i18n="btnLevels">LEVEL SEÇ</button>
      <button class="btn" id="btnFullscreen" type="button" data-i18n="btnFullscreen">TAM EKRANDA OYNA</button>
      <button class="btn" id="btnHow" type="button" data-i18n="btnHow">NASIL OYNANIR</button>
      <button class="btn ghost" id="btnExitMenu" type="button" data-i18n="btnExitMenu">ÇIKIŞ / ARCADE</button>
    </div>
    <div class="menu-tools">
      <button class="sound-toggle is-on" id="btnSoundMenu" type="button">🔊 Ses: Açık</button>
      <span class="fs-note" data-i18n="fsNote">ESC menü · P pause</span>
    </div>
  </div>
</section>
<section class="screen" id="screenLevels"><div class="panel"><div class="logo" style="font-size:28px" data-i18n="levelsTitle">LEVEL SEÇ</div><div class="level-grid" id="levelGrid"></div><div class="btn-col"><button class="btn primary" id="btnLevelsBack" type="button" data-i18n="btnBackMenu">MENÜYE DÖN</button></div></div></section>
<section class="screen" id="screenHow"><div class="panel"><div class="logo" style="font-size:28px" data-i18n="howTitle">NASIL OYNANIR</div><ul class="howto" id="howList"></ul><div class="btn-col"><button class="btn primary" id="btnHowBack" type="button" data-i18n="btnBackMenu">MENÜYE DÖN</button></div></div></section>
<section class="screen" id="screenPause"><div class="panel"><div class="logo" style="font-size:34px" data-i18n="pauseTitle">DURAKLATILDI</div><div class="btn-col"><button class="btn primary" id="btnResume" type="button" data-i18n="btnResume">DEVAM ET</button><button class="btn" id="btnRestart" type="button" data-i18n="btnRestart">YENİDEN BAŞLAT</button><button class="btn" id="btnPauseMenu" type="button" data-i18n="btnMainMenu">ANA MENÜ</button><button class="btn danger" id="btnPauseExit" type="button" data-i18n="btnExit">ÇIKIŞ</button></div></div></section>
<section class="screen" id="screenOver"><div class="panel"><div class="logo" style="font-size:30px" id="overTitle">GAME OVER</div><div class="stars-big" id="overStars"></div><p class="tagline" id="overStats"></p><div class="btn-col"><button class="btn primary" id="btnNext" type="button" data-i18n="btnNext">SONRAKİ LEVEL</button><button class="btn" id="btnReplay" type="button" data-i18n="btnReplay">TEKRAR OYNA</button><button class="btn" id="btnOverMenu" type="button" data-i18n="btnMainMenu">ANA MENÜ</button><button class="btn ghost" id="btnOverHome" type="button" data-i18n="btnArcadeHome">ARCADE ANA SAYFA</button></div></div></section>
</div>
<script>
(function(){
"use strict";
var LANG="tr", MAX_LEVEL=12, CW=__CW__, CH=__CH__;
var I18N={
 tr:{genre:"__GENRE_TR__",tagline:"__TAG_TR__",langLabel:"Dil",btnStart:"BAŞLA",btnLevels:"LEVEL SEÇ",btnFullscreen:"TAM EKRANDA OYNA",btnHow:"NASIL OYNANIR",btnExitMenu:"ÇIKIŞ / ARCADE",soundOn:"🔊 Ses: Açık",soundOff:"🔇 Ses: Kapalı",fsNote:"ESC menü · P pause",howTitle:"NASIL OYNANIR",howItems:__HOW_TR__,levelsTitle:"LEVEL SEÇ",btnBackMenu:"MENÜYE DÖN",pauseTitle:"DURAKLATILDI",btnResume:"DEVAM ET",btnRestart:"YENİDEN BAŞLAT",btnMainMenu:"ANA MENÜ",btnExit:"ÇIKIŞ",btnReplay:"TEKRAR OYNA",btnNext:"SONRAKİ LEVEL",btnArcadeHome:"ARCADE ANA SAYFA",hudScore:"SKOR",hudLevel:"LEVEL",hudLives:"CAN",gameOver:"OYUN BİTTİ",levelClear:"LEVEL TAMAM",congrats:"TEBRİKLER!",stats:"Skor: {score} · Level: {level} · En iyi: {best}"},
 en:{genre:"__GENRE_EN__",tagline:"__TAG_EN__",langLabel:"Language",btnStart:"START",btnLevels:"SELECT LEVEL",btnFullscreen:"PLAY FULLSCREEN",btnHow:"HOW TO PLAY",btnExitMenu:"EXIT / ARCADE",soundOn:"🔊 Sound: On",soundOff:"🔇 Sound: Off",fsNote:"ESC menu · P pause",howTitle:"HOW TO PLAY",howItems:__HOW_EN__,levelsTitle:"SELECT LEVEL",btnBackMenu:"BACK TO MENU",pauseTitle:"PAUSED",btnResume:"RESUME",btnRestart:"RESTART",btnMainMenu:"MAIN MENU",btnExit:"EXIT",btnReplay:"PLAY AGAIN",btnNext:"NEXT LEVEL",btnArcadeHome:"ARCADE HOME",hudScore:"SCORE",hudLevel:"LEVEL",hudLives:"LIVES",gameOver:"GAME OVER",levelClear:"LEVEL CLEAR",congrats:"CONGRATS!",stats:"Score: {score} · Level: {level} · Best: {best}"}
};
function t(k,vars){var p=I18N[LANG]||I18N.tr,v=p[k]; if(v==null)v=I18N.tr[k]!=null?I18N.tr[k]:k; if(typeof v==="string"&&vars)Object.keys(vars).forEach(function(x){v=v.replace(new RegExp("\\{"+x+"\\}","g"),String(vars[x]));}); return v;}
function applyLang(lang){
 LANG=lang==="en"?"en":"tr"; document.documentElement.lang=LANG; var pack=I18N[LANG];
 document.querySelectorAll("[data-i18n]").forEach(function(n){var k=n.getAttribute("data-i18n"); if(pack[k]!=null&&typeof pack[k]==="string")n.textContent=pack[k];});
 var how=document.getElementById("howList"); if(how){how.innerHTML=""; (pack.howItems||[]).forEach(function(it){var li=document.createElement("li"); li.innerHTML=it; how.appendChild(li);});}
 document.getElementById("btnLangTr").classList.toggle("is-on",LANG==="tr");
 document.getElementById("btnLangEn").classList.toggle("is-on",LANG==="en");
 setSound(S.soundOn,true); buildLevelGrid();
}
var S={mode:"menu",ready:false,soundOn:true,score:0,best:0,lives:3,level:1,maxUnlocked:1,running:false,stars:0,levelStars:{},lastTs:0,dpr:1,W:CW,H:CH,shake:0,flash:0,particles:[],keys:{},pointer:null,win:false};
var canvas=document.getElementById("game"), ctx=canvas.getContext("2d");
var screens={menu:document.getElementById("screenMenu"),levels:document.getElementById("screenLevels"),how:document.getElementById("screenHow"),pause:document.getElementById("screenPause"),over:document.getElementById("screenOver")};
var audioCtx=null, musicTimer=null;
function ensureAudio(){if(audioCtx)return; var AC=window.AudioContext||window.webkitAudioContext; if(AC)audioCtx=new AC();}
function beep(f,d,type,g,slide){if(!S.soundOn||!audioCtx||!(f>0))return; var t0=audioCtx.currentTime,o=audioCtx.createOscillator(),gn=audioCtx.createGain(); o.type=type||"square"; o.frequency.setValueAtTime(f,t0); if(slide)o.frequency.exponentialRampToValueAtTime(Math.max(40,slide),t0+d); gn.gain.setValueAtTime(0.0001,t0); gn.gain.exponentialRampToValueAtTime(g||0.07,t0+0.01); gn.gain.exponentialRampToValueAtTime(0.0001,t0+d); o.connect(gn); gn.connect(audioCtx.destination); o.start(t0); o.stop(t0+d+0.02);}
function sfx(n){if(!S.soundOn)return; ensureAudio(); if(!audioCtx)return; if(n==="ui")beep(520,0.05,"square",0.04); else if(n==="ok")beep(660,0.08,"triangle",0.05); else if(n==="bad")beep(140,0.2,"sawtooth",0.08,60); else if(n==="win"){beep(523,0.1,"square",0.06); setTimeout(function(){beep(659,0.12,"square",0.06);},90);} else if(n==="coin")beep(990,0.07,"square",0.045); else if(n==="shot")beep(320,0.05,"square",0.04,180); else if(n==="move")beep(240,0.04,"square",0.03); else if(n==="jump")beep(420,0.09,"triangle",0.06,680);}
function startMusic(){stopMusic(); if(!S.soundOn)return; ensureAudio(); if(!audioCtx)return; var notes=__MUSIC__,i=0; function tick(){if(!S.soundOn||S.mode!=="play")return; var f=notes[i%notes.length]; if(f>0)beep(f,0.1,"triangle",0.014); i++; musicTimer=setTimeout(tick,240);} tick();}
function stopMusic(){if(musicTimer){clearTimeout(musicTimer); musicTimer=null;}}
function setSound(on,silent){S.soundOn=!!on; var lab=S.soundOn?t("soundOn"):t("soundOff"); var mb=document.getElementById("btnSoundMenu"), hb=document.getElementById("btnSoundHud"); if(mb){mb.textContent=lab; mb.classList.toggle("is-on",S.soundOn);} if(hb)hb.textContent=S.soundOn?"🔊":"🔇"; if(!silent){if(S.soundOn&&S.mode==="play")startMusic(); else stopMusic();}}
function clamp(v,a,b){return Math.max(a,Math.min(b,v));}
function rand(a,b){return a+Math.random()*(b-a);}
function showScreen(name){Object.keys(screens).forEach(function(k){screens[k].classList.toggle("is-on",k===name);}); document.getElementById("hud").classList.toggle("is-on", name===null && S.mode==="play");}
function updateHud(){document.getElementById("hudScore").textContent=String(S.score|0); document.getElementById("hudLevel").textContent=String(S.level); document.getElementById("hudLives").textContent=String(S.lives); if(S.ready&&typeof onHudExtra==="function")onHudExtra();}
function showToast(title,text){var el=document.getElementById("toast"); document.getElementById("toastTitle").textContent=title; document.getElementById("toastText").textContent=text||""; el.classList.add("is-on"); clearTimeout(showToast._t); showToast._t=setTimeout(function(){el.classList.remove("is-on");},1100);}
function burst(x,y,col,n,spd){for(var i=0;i<n;i++){var a=Math.random()*Math.PI*2,s=rand(spd*0.3,spd); S.particles.push({x:x,y:y,vx:Math.cos(a)*s,vy:Math.sin(a)*s,life:rand(0.2,0.55),max:0.55,r:rand(1.2,3),color:col});}}
function updateParticles(dt){for(var i=S.particles.length-1;i>=0;i--){var p=S.particles[i]; p.life-=dt; p.x+=p.vx*dt; p.y+=p.vy*dt; p.vy+=40*dt; if(p.life<=0)S.particles.splice(i,1);}}
function drawParticles(){S.particles.forEach(function(p){ctx.globalAlpha=Math.max(0,p.life/(p.max||0.5)); ctx.fillStyle=p.color; ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,Math.PI*2); ctx.fill();}); ctx.globalAlpha=1;}
function palette(level){var pal=[["#0b1535","#22d3ee","#a78bfa"],["#1a0b2e","#f472b6","#c084fc"],["#052e1a","#4ade80","#2dd4bf"],["#2a0a0a","#fb7185","#fbbf24"],["#0c1a2e","#38bdf8","#818cf8"],["#1e1b4b","#e879f9","#67e8f9"],["#0f172a","#f59e0b","#ef4444"],["#042f2e","#2dd4bf","#a3e635"],["#1c1917","#f97316","#fde047"],["#172554","#60a5fa","#c4b5fd"],["#3b0764","#d946ef","#22d3ee"],["#450a0a","#f43f5e","#fbbf24"]]; return pal[(level-1)%pal.length];}
function isFs(){return !!(document.fullscreenElement||document.webkitFullscreenElement);}
function enterFs(){var el=document.documentElement,r=el.requestFullscreen||el.webkitRequestFullscreen; if(r)r.call(el).catch(function(){});}
function exitFs(){var e=document.exitFullscreen||document.webkitExitFullscreen; if(e&&isFs())e.call(document);}
function goMenu(){S.mode="menu"; S.running=false; stopMusic(); showScreen("menu");}
function pauseGame(){if(S.mode!=="play")return; S.mode="pause"; S.running=false; stopMusic(); showScreen("pause");}
function resumeGame(){if(S.mode!=="pause")return; S.mode="play"; S.running=true; showScreen(null); startMusic();}
function calcStars(score,target){if(score>=target*1.5)return 3; if(score>=target)return 2; return 1;}
function levelComplete(bonus){
 S.running=false; S.win=true; S.mode="over"; stopMusic(); sfx("win");
 var target=LEVEL_TARGET(S.level); S.stars=calcStars(S.score+(bonus||0), target);
 var prev=S.levelStars[S.level]|0; if(S.stars>prev)S.levelStars[S.level]=S.stars;
 if(S.level>=S.maxUnlocked && S.level<MAX_LEVEL)S.maxUnlocked=S.level+1;
 if(S.score>S.best)S.best=S.score;
 document.getElementById("overTitle").textContent=S.level>=MAX_LEVEL?t("congrats"):t("levelClear");
 document.getElementById("overStars").textContent=["","★","★★","★★★"][S.stars]||"★";
 document.getElementById("overStats").textContent=t("stats",{score:S.score|0,level:S.level,best:S.best|0});
 document.getElementById("btnNext").style.display=S.level<MAX_LEVEL?"":"none";
 showScreen("over");
}
function gameOver(){
 S.running=false; S.win=false; S.mode="over"; stopMusic(); sfx("bad");
 if(S.score>S.best)S.best=S.score;
 document.getElementById("overTitle").textContent=t("gameOver");
 document.getElementById("overStars").textContent="";
 document.getElementById("overStats").textContent=t("stats",{score:S.score|0,level:S.level,best:S.best|0});
 document.getElementById("btnNext").style.display="none";
 showScreen("over");
}
function buildLevelGrid(){
 var g=document.getElementById("levelGrid"); g.innerHTML="";
 for(var i=1;i<=MAX_LEVEL;i++){
  var b=document.createElement("button"); b.type="button"; b.className="level-btn"+(i>S.maxUnlocked?" is-locked":"");
  var st=S.levelStars[i]|0; b.innerHTML=i+'<span class="stars">'+(st?("★".repeat(st)):"·")+"</span>";
  (function(lv){b.onclick=function(){if(lv>S.maxUnlocked)return; ensureAudio(); startLevel(lv);};})(i);
  g.appendChild(b);
 }
}
function startLevel(n){
 try{
  S.level=n|0; S.score=0; S.lives=3; S.win=false; S.particles=[]; S.shake=0; S.flash=0; S.keys={};
  gameReset();
  S.ready=true; S.mode="play"; S.running=true; showScreen(null); updateHud(); startMusic(); sfx("ok");
  showToast("LEVEL "+n,"");
 }catch(err){console.error(err); alert("Oyun yüklenemedi: "+err.message);}
}
function resize(){S.W=CW; S.H=CH; S.dpr=Math.min(window.devicePixelRatio||1,2); canvas.width=Math.round(S.W*S.dpr); canvas.height=Math.round(S.H*S.dpr);}
function canvasPos(e){
  var rect=canvas.getBoundingClientRect(), scale=Math.min(rect.width/S.W,rect.height/S.H);
  var ox=rect.left+(rect.width-S.W*scale)/2, oy=rect.top+(rect.height-S.H*scale)/2;
  var cx=e.clientX!=null?e.clientX:(e.touches&&e.touches[0]?e.touches[0].clientX:0);
  var cy=e.clientY!=null?e.clientY:(e.touches&&e.touches[0]?e.touches[0].clientY:0);
  return {x:(cx-ox)/scale, y:(cy-oy)/scale};
}
function loop(ts){
  if(!S.lastTs)S.lastTs=ts; var dt=Math.min(0.033,(ts-S.lastTs)/1000); S.lastTs=ts;
  if(S.mode==="play"&&S.running&&S.ready){
    try{gameUpdate(dt);}catch(e){console.error(e); S.running=false;}
    updateParticles(dt);
    if(S.shake>0)S.shake=Math.max(0,S.shake-dt*8);
    if(S.flash>0)S.flash=Math.max(0,S.flash-dt*3);
  }
  drawFrame();
  requestAnimationFrame(loop);
}
function drawFrame(){
  var dpr=S.dpr; ctx.setTransform(dpr,0,0,dpr,0,0); ctx.clearRect(0,0,S.W,S.H);
  var sx=0,sy=0; if(S.shake>0){sx=(Math.random()-0.5)*S.shake*12; sy=(Math.random()-0.5)*S.shake*12;}
  ctx.save(); ctx.translate(sx,sy);
  var pal=palette(S.level);
  var g=ctx.createLinearGradient(0,0,0,S.H); g.addColorStop(0,pal[0]); g.addColorStop(1,"#03060f");
  ctx.fillStyle=g; ctx.fillRect(-10,-10,S.W+20,S.H+20);
  // ambient stars
  ctx.fillStyle="rgba(180,200,255,0.15)";
  for(var i=0;i<40;i++){ctx.fillRect((i*97+S.level*13)%S.W,(i*53)%S.H,2,2);}
  if(S.ready){try{gameDraw(ctx,pal);}catch(e){}}
  drawParticles();
  ctx.fillStyle="rgba(0,0,0,0.06)"; for(var y=0;y<S.H;y+=3)ctx.fillRect(0,y,S.W,1);
  if(S.flash>0){ctx.fillStyle="rgba(248,113,113,"+(S.flash*0.3)+")"; ctx.fillRect(0,0,S.W,S.H);}
  ctx.restore();
}
function leaveArcade(){stopMusic(); if(isFs())exitFs(); location.href="/mini-oyunlar/";}
function handleExit(){if(S.mode==="play"){S.mode="pause"; S.running=false; stopMusic();} if(isFs())exitFs(); goMenu();}
window.addEventListener("keydown",function(e){
  if(e.code==="Escape"){e.preventDefault(); handleExit(); return;}
  if(e.code==="KeyP"){e.preventDefault(); if(S.mode==="play")pauseGame(); else if(S.mode==="pause")resumeGame();}
  if(S.mode==="play"&&typeof onKeyDown==="function")onKeyDown(e);
});
window.addEventListener("keyup",function(e){if(typeof onKeyUp==="function")onKeyUp(e);});
canvas.addEventListener("mousedown",function(e){S.pointer=canvasPos(e); if(S.mode==="play"&&typeof onPointer==="function")onPointer(S.pointer,"down");});
canvas.addEventListener("mousemove",function(e){S.pointer=canvasPos(e); if(S.mode==="play"&&typeof onPointer==="function")onPointer(S.pointer,"move");});
canvas.addEventListener("mouseup",function(e){S.pointer=canvasPos(e); if(S.mode==="play"&&typeof onPointer==="function")onPointer(S.pointer,"up");});
canvas.addEventListener("touchstart",function(e){if(!e.touches[0])return; S.pointer=canvasPos(e.touches[0]); if(S.mode==="play"&&typeof onPointer==="function")onPointer(S.pointer,"down");},{passive:true});
canvas.addEventListener("touchmove",function(e){if(!e.touches[0])return; S.pointer=canvasPos(e.touches[0]); if(S.mode==="play"&&typeof onPointer==="function")onPointer(S.pointer,"move");},{passive:true});
canvas.addEventListener("touchend",function(e){var tch=e.changedTouches&&e.changedTouches[0]; if(tch)S.pointer=canvasPos(tch); if(S.mode==="play"&&typeof onPointer==="function")onPointer(S.pointer||{x:0,y:0},"up");},{passive:true});
document.getElementById("btnStart").onclick=function(){ensureAudio(); if(audioCtx&&audioCtx.state==="suspended")audioCtx.resume(); startLevel(1);};
document.getElementById("btnFullscreen").onclick=function(){ensureAudio(); enterFs(); startLevel(1);};
document.getElementById("btnLevels").onclick=function(){S.mode="levels"; buildLevelGrid(); showScreen("levels"); sfx("ui");};
document.getElementById("btnLevelsBack").onclick=goMenu;
document.getElementById("btnHow").onclick=function(){S.mode="how"; showScreen("how"); sfx("ui");};
document.getElementById("btnHowBack").onclick=goMenu;
document.getElementById("btnExitMenu").onclick=leaveArcade;
document.getElementById("btnResume").onclick=resumeGame;
document.getElementById("btnRestart").onclick=function(){startLevel(S.level);};
document.getElementById("btnPauseMenu").onclick=goMenu;
document.getElementById("btnPauseExit").onclick=leaveArcade;
document.getElementById("btnReplay").onclick=function(){startLevel(S.level);};
document.getElementById("btnNext").onclick=function(){if(S.level<MAX_LEVEL)startLevel(S.level+1);};
document.getElementById("btnOverMenu").onclick=goMenu;
document.getElementById("btnOverHome").onclick=leaveArcade;
document.getElementById("btnPause").onclick=pauseGame;
document.getElementById("btnExit").onclick=handleExit;
document.getElementById("btnSoundMenu").onclick=function(){setSound(!S.soundOn);};
document.getElementById("btnSoundHud").onclick=function(){setSound(!S.soundOn);};
document.getElementById("btnLangTr").onclick=function(){applyLang("tr");};
document.getElementById("btnLangEn").onclick=function(){applyLang("en");};
document.addEventListener("fullscreenchange",function(){if(!isFs()&&S.mode==="play")pauseGame();});
resize(); window.addEventListener("resize",resize); applyLang("tr"); showScreen("menu"); requestAnimationFrame(loop);

/* ===== GAME ===== */
__GAME__
})();
</script>
</body>
</html>
'''


def jsa(items):
    import json
    return json.dumps(items, ensure_ascii=False)


def build(meta, game_js):
    html = SHELL
    repl = {
        "__TITLE__": meta["title"],
        "__SLUG__": meta["slug"],
        "__DESC__": meta["desc"],
        "__GENRE_TR__": meta["genre_tr"],
        "__GENRE_EN__": meta["genre_en"],
        "__TAG_TR__": meta["tag_tr"],
        "__TAG_EN__": meta["tag_en"],
        "__HOW_TR__": jsa(meta["how_tr"]),
        "__HOW_EN__": jsa(meta["how_en"]),
        "__CW__": str(meta.get("cw", 480)),
        "__CH__": str(meta.get("ch", 720)),
        "__MUSIC__": meta.get("music", "[196,220,247,262,294,262,247,220]"),
        "__GAME__": game_js,
    }
    for k, v in repl.items():
        html = html.replace(k, v)
    return html


# ============ GAMES ============

GAMES = {}

GAMES["snake-rewind"] = (
    {
        "title": "Snake Rewind",
        "slug": "snake-rewind",
        "desc": "Izgara yılan, hedef yem, geri sarma, 12 level.",
        "genre_tr": "Arcade · Yılan",
        "genre_en": "Arcade · Snake",
        "tag_tr": "Yem topla, büyü, duvarlardan kaç · R ile geri sar",
        "tag_en": "Eat, grow, avoid walls · rewind with R",
        "how_tr": [
            "<b>Hareket:</b> Ok tuşları / WASD / kaydır",
            "<b>Hedef:</b> Level yem sayısına ulaş",
            "<b>R:</b> Son adımları geri al (sınırlı)",
            "<b>Can:</b> Duvar/kuyruk çarpınca can düşer",
            "<b>12 level:</b> Hız ve engeller artar",
        ],
        "how_en": [
            "<b>Move:</b> Arrows / WASD / swipe",
            "<b>Goal:</b> Reach the food quota",
            "<b>R:</b> Rewind recent steps (limited)",
            "<b>Lives:</b> Wall/self hits cost a life",
            "<b>12 levels:</b> Faster with more walls",
        ],
        "cw": 480, "ch": 640,
        "music": "[196,220,247,262,294,262,247,220]",
    },
    r'''
var CELL=20,COLS,ROWS,snake,dir,nextDir,food,goal,eaten,acc,step,rewinds,history,walls;
function LEVEL_TARGET(lv){return 100+lv*50;}
function gameReset(){
  COLS=Math.floor(S.W/CELL); ROWS=Math.floor(S.H/CELL);
  var cx=(COLS/2)|0, cy=(ROWS/2)|0;
  snake=[{x:cx,y:cy},{x:cx-1,y:cy},{x:cx-2,y:cy}];
  dir={x:1,y:0}; nextDir={x:1,y:0};
  goal=5+S.level; eaten=0; acc=0; step=Math.max(0.075,0.2-S.level*0.009);
  rewinds=2+((S.level/3)|0); history=[]; walls=[];
  if(S.level>=3){
    for(var i=0;i<S.level+3;i++){
      var wx=2+((i*7+3)%Math.max(1,COLS-4)), wy=2+((i*5+1)%Math.max(1,ROWS-4));
      if(Math.abs(wx-cx)<3&&Math.abs(wy-cy)<2) continue;
      walls.push({x:wx,y:wy});
    }
  }
  placeFood(); onHudExtra();
}
function occ(x,y){
  if(snake.some(function(s){return s.x===x&&s.y===y;})) return true;
  if(walls.some(function(w){return w.x===x&&w.y===y;})) return true;
  return false;
}
function placeFood(){
  for(var t=0;t<300;t++){
    var f={x:(Math.random()*COLS)|0,y:(Math.random()*ROWS)|0};
    if(!occ(f.x,f.y)){food=f; return;}
  }
  food={x:1,y:1};
}
function onHudExtra(){
  document.getElementById("hudExtraLabel").textContent=LANG==="en"?"GOAL":"HEDEF";
  document.getElementById("hudExtra").textContent=eaten+"/"+goal+" · R"+rewinds;
}
function tryRewind(){
  if(rewinds<=0||!history.length) return;
  rewinds--; var snap=history.pop();
  snake=snap.snake.map(function(p){return {x:p.x,y:p.y};});
  dir={x:snap.dir.x,y:snap.dir.y}; nextDir={x:dir.x,y:dir.y};
  sfx("ok"); onHudExtra();
}
function gameUpdate(dt){
  if(S.keys.left&&dir.x!==1) nextDir={x:-1,y:0};
  if(S.keys.right&&dir.x!==-1) nextDir={x:1,y:0};
  if(S.keys.up&&dir.y!==1) nextDir={x:0,y:-1};
  if(S.keys.down&&dir.y!==-1) nextDir={x:0,y:1};
  acc+=dt;
  while(acc>=step){
    acc-=step;
    history.push({snake:snake.map(function(p){return {x:p.x,y:p.y};}),dir:{x:dir.x,y:dir.y}});
    if(history.length>50) history.shift();
    dir=nextDir;
    var h={x:snake[0].x+dir.x,y:snake[0].y+dir.y};
    var hit=h.x<0||h.y<0||h.x>=COLS||h.y>=ROWS||occ(h.x,h.y);
    if(hit){
      S.lives--; S.shake=0.55; S.flash=0.4; sfx("bad"); updateHud();
      if(S.lives<=0){gameOver(); return;}
      var cx=(COLS/2)|0, cy=(ROWS/2)|0;
      snake=[{x:cx,y:cy},{x:cx-1,y:cy},{x:cx-2,y:cy}]; dir={x:1,y:0}; nextDir={x:1,y:0};
      continue;
    }
    snake.unshift(h);
    if(h.x===food.x&&h.y===food.y){
      eaten++; S.score+=12+S.level*3; sfx("coin");
      burst(food.x*CELL+CELL/2,food.y*CELL+CELL/2,"#fbbf24",12,170);
      placeFood(); onHudExtra(); updateHud();
      if(eaten>=goal){S.score+=60*S.level; levelComplete(60*S.level); return;}
    } else snake.pop();
  }
}
function gameDraw(ctx,pal){
  ctx.strokeStyle="rgba(255,255,255,0.05)"; ctx.lineWidth=1;
  for(var x=0;x<=COLS;x++){ctx.beginPath();ctx.moveTo(x*CELL,0);ctx.lineTo(x*CELL,ROWS*CELL);ctx.stroke();}
  for(var y=0;y<=ROWS;y++){ctx.beginPath();ctx.moveTo(0,y*CELL);ctx.lineTo(COLS*CELL,y*CELL);ctx.stroke();}
  walls.forEach(function(w){ctx.fillStyle=pal[2]; ctx.fillRect(w.x*CELL+2,w.y*CELL+2,CELL-4,CELL-4);});
  ctx.fillStyle="#fbbf24"; ctx.shadowColor="#fbbf24"; ctx.shadowBlur=12;
  ctx.beginPath(); ctx.arc(food.x*CELL+CELL/2,food.y*CELL+CELL/2,CELL*0.32,0,Math.PI*2); ctx.fill(); ctx.shadowBlur=0;
  snake.forEach(function(s,i){
    ctx.fillStyle=i===0?pal[1]:pal[2];
    ctx.fillRect(s.x*CELL+2,s.y*CELL+2,CELL-4,CELL-4);
    if(i===0){ctx.fillStyle="#0f172a"; ctx.fillRect(s.x*CELL+6,s.y*CELL+6,3,3); ctx.fillRect(s.x*CELL+11,s.y*CELL+6,3,3);}
  });
}
function onKeyDown(e){
  if(e.code==="ArrowLeft"||e.code==="KeyA"){S.keys.left=true;e.preventDefault();}
  if(e.code==="ArrowRight"||e.code==="KeyD"){S.keys.right=true;e.preventDefault();}
  if(e.code==="ArrowUp"||e.code==="KeyW"){S.keys.up=true;e.preventDefault();}
  if(e.code==="ArrowDown"||e.code==="KeyS"){S.keys.down=true;e.preventDefault();}
  if(e.code==="KeyR") tryRewind();
}
function onKeyUp(e){
  if(e.code==="ArrowLeft"||e.code==="KeyA")S.keys.left=false;
  if(e.code==="ArrowRight"||e.code==="KeyD")S.keys.right=false;
  if(e.code==="ArrowUp"||e.code==="KeyW")S.keys.up=false;
  if(e.code==="ArrowDown"||e.code==="KeyS")S.keys.down=false;
}
var sw0=null;
function onPointer(p,type){
  if(type==="down") sw0={x:p.x,y:p.y};
  if(type==="up"&&sw0){
    var dx=p.x-sw0.x, dy=p.y-sw0.y;
    if(Math.abs(dx)>18||Math.abs(dy)>18){
      if(Math.abs(dx)>Math.abs(dy)){ if(dx>0&&dir.x!==-1)nextDir={x:1,y:0}; if(dx<0&&dir.x!==1)nextDir={x:-1,y:0}; }
      else { if(dy>0&&dir.y!==-1)nextDir={x:0,y:1}; if(dy<0&&dir.y!==1)nextDir={x:0,y:-1}; }
    }
    sw0=null;
  }
}
'''
)

GAMES["cascade-blocks"] = (
    {
        "title": "Cascade Blocks",
        "slug": "cascade-blocks",
        "desc": "Aynı renk gruplarını patlat, zincir bonus, 12 level.",
        "genre_tr": "Bulmaca · Blok",
        "genre_en": "Puzzle · Blocks",
        "tag_tr": "2+ aynı renk grubunu patlat · zincir kur",
        "tag_en": "Pop groups of 2+ matching colors · chain combos",
        "how_tr": [
            "<b>Kontrol:</b> Tıkla / dokun",
            "<b>Kural:</b> En az 2 komşu aynı renk",
            "<b>Zincir:</b> Üst üste patlatmalar bonus verir",
            "<b>Hedef:</b> Level puanına ulaş",
            "<b>12 level:</b> Grid ve renk artar",
        ],
        "how_en": [
            "<b>Controls:</b> Tap groups",
            "<b>Rule:</b> At least 2 adjacent same color",
            "<b>Chains:</b> Consecutive pops bonus",
            "<b>Goal:</b> Reach score target",
            "<b>12 levels:</b> Larger grids, more colors",
        ],
        "cw": 420, "ch": 700,
        "music": "[262,294,330,349,392,349,330,294]",
    },
    r'''
var COLS,ROWS,grid,colors,chain,PAL=["#22d3ee","#a78bfa","#f472b6","#fbbf24","#4ade80","#fb7185"];
function LEVEL_TARGET(lv){return 350+lv*160;}
function gameReset(){
  COLS=6+Math.min(2,(S.level/4)|0); ROWS=9+Math.min(2,(S.level/3)|0);
  colors=Math.min(6,3+((S.level-1)/2)|0); chain=0; grid=[];
  for(var y=0;y<ROWS;y++){grid[y]=[]; for(var x=0;x<COLS;x++) grid[y][x]=(Math.random()*colors)|0;}
  onHudExtra();
}
function onHudExtra(){
  document.getElementById("hudExtraLabel").textContent=LANG==="en"?"TARGET":"HEDEF";
  document.getElementById("hudExtra").textContent=String(LEVEL_TARGET(S.level));
}
function cellAt(p){
  var pad=14, top=70, bw=(S.W-pad*2)/COLS, bh=(S.H-top-pad)/ROWS;
  var x=((p.x-pad)/bw)|0, y=((p.y-top)/bh)|0;
  if(x<0||y<0||x>=COLS||y>=ROWS) return null;
  return {x:x,y:y,bw:bw,bh:bh,pad:pad,top:top};
}
function flood(x,y,c,seen){
  var key=y+"_"+x; if(x<0||y<0||x>=COLS||y>=ROWS||grid[y][x]!==c||seen[key]) return [];
  seen[key]=1; var out=[{x:x,y:y}];
  [[1,0],[-1,0],[0,1],[0,-1]].forEach(function(d){out=out.concat(flood(x+d[0],y+d[1],c,seen));});
  return out;
}
function gravity(){
  for(var x=0;x<COLS;x++){
    var stack=[];
    for(var y=ROWS-1;y>=0;y--) if(grid[y][x]!=null) stack.push(grid[y][x]);
    for(var y2=ROWS-1;y2>=0;y2--){
      var idx=ROWS-1-y2;
      grid[y2][x]=idx<stack.length?stack[idx]:null;
    }
  }
  // refill empties
  for(var y=0;y<ROWS;y++) for(var x=0;x<COLS;x++) if(grid[y][x]==null) grid[y][x]=(Math.random()*colors)|0;
  // compact empty columns leftward
  var nonempty=[];
  for(var x=0;x<COLS;x++){
    var has=false; for(var y=0;y<ROWS;y++) if(grid[y][x]!=null) has=true;
    if(has){var col=[]; for(var y=0;y<ROWS;y++) col.push(grid[y][x]); nonempty.push(col);}
  }
  while(nonempty.length<COLS){var nc=[]; for(var y=0;y<ROWS;y++) nc.push((Math.random()*colors)|0); nonempty.push(nc);}
  for(var x=0;x<COLS;x++) for(var y=0;y<ROWS;y++) grid[y][x]=nonempty[x][y];
}
function gameUpdate(dt){}
function gameDraw(ctx,pal){
  var pad=14, top=70, bw=(S.W-pad*2)/COLS, bh=(S.H-top-pad)/ROWS;
  ctx.fillStyle="rgba(0,0,0,0.28)"; ctx.fillRect(pad-4,top-4,S.W-pad*2+8,ROWS*bh+8);
  for(var y=0;y<ROWS;y++) for(var x=0;x<COLS;x++){
    var c=grid[y][x]; if(c==null) continue;
    ctx.fillStyle=PAL[c%PAL.length]; ctx.shadowColor=PAL[c%PAL.length]; ctx.shadowBlur=8;
    var rx=pad+x*bw+3, ry=top+y*bh+3;
    roundRect(ctx,rx,ry,bw-6,bh-6,8); ctx.fill();
  }
  ctx.shadowBlur=0;
  ctx.fillStyle="#e2e8f0"; ctx.font="bold 14px Inter,sans-serif"; ctx.textAlign="center";
  ctx.fillText((S.score|0)+" / "+LEVEL_TARGET(S.level), S.W/2, 42);
}
function roundRect(ctx,x,y,w,h,r){ctx.beginPath();ctx.moveTo(x+r,y);ctx.arcTo(x+w,y,x+w,y+h,r);ctx.arcTo(x+w,y+h,x,y+h,r);ctx.arcTo(x,y+h,x,y,r);ctx.arcTo(x,y,x+w,y,r);ctx.closePath();}
function onPointer(p,type){
  if(type!=="down"||S.mode!=="play") return;
  var c=cellAt(p); if(!c) return;
  var col=grid[c.y][c.x]; if(col==null) return;
  var group=flood(c.x,c.y,col,{});
  if(group.length<2){sfx("bad"); chain=0; return;}
  group.forEach(function(g){
    burst(c.pad+g.x*c.bw+c.bw/2, c.top+g.y*c.bh+c.bh/2, PAL[col%PAL.length], 6, 130);
    grid[g.y][g.x]=null;
  });
  chain++; var pts=Math.floor(group.length*group.length*6*chain*(1+S.level*0.04));
  S.score+=pts; sfx("coin"); gravity(); updateHud(); onHudExtra();
  if(S.score>=LEVEL_TARGET(S.level)) levelComplete(120);
}
function onKeyDown(e){}
function onKeyUp(e){}
'''
)

GAMES["number-fusion"] = (
    {
        "title": "Number Fusion",
        "slug": "number-fusion",
        "desc": "Sayıları kaydırıp birleştir, hedef karta ulaş.",
        "genre_tr": "Bulmaca · Sayı",
        "genre_en": "Puzzle · Numbers",
        "tag_tr": "Kaydır, birleştir, hedef değere ulaş",
        "tag_en": "Swipe, merge, hit the target value",
        "how_tr": [
            "<b>Kontrol:</b> Oklar / WASD / kaydır",
            "<b>Birleştir:</b> Aynı sayılar birleşir",
            "<b>Hedef:</b> Level hedef sayısını oluştur",
            "<b>Can:</b> Tahta kilitlenince can kaybı",
            "<b>12 level:</b> Hedef katlanır",
        ],
        "how_en": [
            "<b>Controls:</b> Arrows / WASD / swipe",
            "<b>Merge:</b> Equal numbers combine",
            "<b>Goal:</b> Create the target tile",
            "<b>Lives:</b> Full board costs a life",
            "<b>12 levels:</b> Target rises",
        ],
        "cw": 480, "ch": 640,
        "music": "[330,294,262,294,330,330,330,294]",
    },
    r'''
var N=4, board, target;
function LEVEL_TARGET(lv){return 200+lv*90;}
function empty(){var b=[]; for(var y=0;y<N;y++){b[y]=[]; for(var x=0;x<N;x++) b[y][x]=0;} return b;}
function gameReset(){
  board=empty(); spawn(); spawn();
  target=Math.pow(2, Math.min(11, 4+Math.floor((S.level-1)/1.2))); // 16..2048
  onHudExtra();
}
function spawn(){
  var free=[]; for(var y=0;y<N;y++) for(var x=0;x<N;x++) if(!board[y][x]) free.push({x:x,y:y});
  if(!free.length) return false;
  var p=free[(Math.random()*free.length)|0];
  board[p.y][p.x]=Math.random()<0.9?2:4; return true;
}
function onHudExtra(){
  document.getElementById("hudExtraLabel").textContent=LANG==="en"?"TARGET":"HEDEF";
  document.getElementById("hudExtra").textContent=String(target);
}
function slideLine(line){
  var arr=line.filter(function(v){return v;}), out=[], add=0, i=0;
  while(i<arr.length){
    if(i+1<arr.length && arr[i]===arr[i+1]){var v=arr[i]*2; out.push(v); add+=v; i+=2;}
    else {out.push(arr[i]); i++;}
  }
  while(out.length<N) out.push(0);
  var changed=false; for(var j=0;j<N;j++) if(out[j]!==line[j]) changed=true;
  return {line:out,score:add,changed:changed};
}
function move(dir){
  var nb=empty(), changed=false, add=0, maxTile=0;
  if(dir===0||dir===1){
    for(var y=0;y<N;y++){
      var line=[]; for(var x=0;x<N;x++) line.push(board[y][x]);
      if(dir===1) line.reverse();
      var r=slideLine(line); if(dir===1) r.line.reverse();
      for(var x=0;x<N;x++){nb[y][x]=r.line[x]; maxTile=Math.max(maxTile,r.line[x]);}
      if(r.changed) changed=true; add+=r.score;
    }
  } else {
    for(var x=0;x<N;x++){
      var line=[]; for(var y=0;y<N;y++) line.push(board[y][x]);
      if(dir===3) line.reverse();
      var r=slideLine(line); if(dir===3) r.line.reverse();
      for(var y=0;y<N;y++){nb[y][x]=r.line[y]; maxTile=Math.max(maxTile,r.line[y]);}
      if(r.changed) changed=true; add+=r.score;
    }
  }
  if(!changed) return;
  board=nb; S.score+=add; if(add) sfx("coin"); else sfx("move");
  spawn();
  for(var y=0;y<N;y++) for(var x=0;x<N;x++) maxTile=Math.max(maxTile,board[y][x]);
  updateHud(); onHudExtra();
  if(maxTile>=target){S.score+=target; levelComplete(target); return;}
  if(!canMove()){
    S.lives--; S.shake=0.45; sfx("bad"); updateHud();
    if(S.lives<=0) gameOver();
    else {board=empty(); spawn(); spawn();}
  }
}
function canMove(){
  for(var y=0;y<N;y++) for(var x=0;x<N;x++){
    if(!board[y][x]) return true;
    if(x+1<N&&board[y][x]===board[y][x+1]) return true;
    if(y+1<N&&board[y][x]===board[y+1][x]) return true;
  }
  return false;
}
function gameUpdate(dt){}
function tileColor(v){var m={2:"#67e8f9",4:"#22d3ee",8:"#818cf8",16:"#a78bfa",32:"#c084fc",64:"#f472b6",128:"#fb7185",256:"#fbbf24",512:"#f59e0b",1024:"#4ade80",2048:"#f0abfc"}; return m[v]||"#e2e8f0";}
function gameDraw(ctx,pal){
  var pad=24, size=Math.min(S.W,S.H-100)-pad*2, cell=size/N, ox=(S.W-size)/2, oy=90;
  ctx.fillStyle="rgba(0,0,0,0.35)"; roundFill(ctx,ox-10,oy-10,size+20,size+20,14);
  for(var y=0;y<N;y++) for(var x=0;x<N;x++){
    var v=board[y][x], rx=ox+x*cell+6, ry=oy+y*cell+6, rw=cell-12, rh=cell-12;
    ctx.fillStyle=v?tileColor(v):"rgba(255,255,255,0.06)";
    if(v){ctx.shadowColor=tileColor(v); ctx.shadowBlur=10;}
    roundFill(ctx,rx,ry,rw,rh,10); ctx.shadowBlur=0;
    if(v){ctx.fillStyle="#0f172a"; ctx.font="bold "+Math.floor(cell*0.3)+"px Inter,sans-serif"; ctx.textAlign="center"; ctx.textBaseline="middle"; ctx.fillText(String(v),rx+rw/2,ry+rh/2);}
  }
  ctx.fillStyle="#e2e8f0"; ctx.font="bold 15px Inter,sans-serif"; ctx.textAlign="center";
  ctx.fillText((LANG==="en"?"Target: ":"Hedef: ")+target, S.W/2, 50);
}
function roundFill(ctx,x,y,w,h,r){ctx.beginPath();ctx.moveTo(x+r,y);ctx.arcTo(x+w,y,x+w,y+h,r);ctx.arcTo(x+w,y+h,x,y+h,r);ctx.arcTo(x,y+h,x,y,r);ctx.arcTo(x,y,x+w,y,r);ctx.closePath();ctx.fill();}
function onKeyDown(e){
  if(e.code==="ArrowLeft"||e.code==="KeyA"){e.preventDefault(); move(0);}
  if(e.code==="ArrowRight"||e.code==="KeyD"){e.preventDefault(); move(1);}
  if(e.code==="ArrowUp"||e.code==="KeyW"){e.preventDefault(); move(2);}
  if(e.code==="ArrowDown"||e.code==="KeyS"){e.preventDefault(); move(3);}
}
function onKeyUp(e){}
var sw0=null;
function onPointer(p,type){
  if(type==="down") sw0={x:p.x,y:p.y};
  if(type==="up"&&sw0){
    var dx=p.x-sw0.x, dy=p.y-sw0.y;
    if(Math.abs(dx)>28||Math.abs(dy)>28){ if(Math.abs(dx)>Math.abs(dy)) move(dx>0?1:0); else move(dy>0?3:2); }
    sw0=null;
  }
}
'''
)

GAMES["pixel-glider"] = (
    {
        "title": "Pixel Glider",
        "slug": "pixel-glider",
        "desc": "Tek tuş itki ile tünel engellerini geç.",
        "genre_tr": "Aksiyon · Uçuş",
        "genre_en": "Action · Flyer",
        "tag_tr": "Space/tık = itki · kapılardan geç",
        "tag_en": "Space/tap = thrust · clear gates",
        "how_tr": [
            "<b>Kontrol:</b> Space / tık / dokun = itki",
            "<b>Hedef:</b> Level mesafesini tamamla",
            "<b>Engel:</b> Kapılara çarpma can düşürür",
            "<b>Skor:</b> Mesafe + geçilen kapı",
            "<b>12 level:</b> Hız ve daralma artar",
        ],
        "how_en": [
            "<b>Controls:</b> Space / tap = thrust",
            "<b>Goal:</b> Finish level distance",
            "<b>Hazards:</b> Hitting gates costs a life",
            "<b>Score:</b> Distance + gates",
            "<b>12 levels:</b> Faster, tighter gaps",
        ],
        "cw": 400, "ch": 640,
        "music": "[392,349,330,294,330,349,392,440]",
    },
    r'''
var drone,vy,gates,dist,goal,speed,gap,inv;
function LEVEL_TARGET(lv){return 250+lv*70;}
function gameReset(){
  drone={x:S.W*0.28,y:S.H*0.5,r:13}; vy=0; gates=[]; dist=0;
  goal=800+S.level*200; speed=150+S.level*16; gap=Math.max(96,175-S.level*6); inv=0;
  for(var i=0;i<4;i++) addGate(S.W+80+i*230); onHudExtra();
}
function addGate(x){gates.push({x:x,mid:rand(gap*0.7,S.H-gap*0.7),w:50,passed:false});}
function onHudExtra(){
  document.getElementById("hudExtraLabel").textContent=LANG==="en"?"DIST":"MESAFE";
  document.getElementById("hudExtra").textContent=(dist|0)+"/"+(goal|0);
}
function thrust(){if(S.mode!=="play"||!S.running)return; vy=-280; sfx("jump");}
function hit(){
  if(inv>0) return;
  S.lives--; inv=1.1; S.shake=0.55; S.flash=0.4; sfx("bad");
  burst(drone.x,drone.y,"#fb7185",16,220); updateHud();
  if(S.lives<=0) gameOver();
  else {drone.y=S.H*0.5; vy=0;}
}
function gameUpdate(dt){
  if(inv>0) inv-=dt;
  vy+=820*dt; drone.y+=vy*dt;
  if(drone.y<drone.r||drone.y>S.H-drone.r){hit(); return;}
  dist+=speed*dt*0.32; S.score+=speed*dt*0.07;
  gates.forEach(function(g){g.x-=speed*dt;});
  if(gates.length && gates[gates.length-1].x < S.W-210) addGate(gates[gates.length-1].x+220);
  gates=gates.filter(function(g){return g.x>-90;});
  for(var i=0;i<gates.length;i++){
    var g=gates[i], topH=g.mid-gap/2, botY=g.mid+gap/2;
    if(drone.x+drone.r>g.x && drone.x-drone.r<g.x+g.w){
      if(drone.y-drone.r<topH || drone.y+drone.r>botY){hit(); return;}
    }
    if(!g.passed && g.x+g.w<drone.x){g.passed=true; S.score+=30; sfx("coin"); burst(drone.x,drone.y,"#67e8f9",8,140);}
  }
  updateHud(); onHudExtra();
  if(dist>=goal) levelComplete(160);
}
function gameDraw(ctx,pal){
  for(var i=0;i<35;i++){ctx.fillStyle="rgba(255,255,255,0.12)"; ctx.fillRect((i*47+dist*0.25)%S.W,(i*89)%S.H,2,2);}
  gates.forEach(function(g){
    var topH=g.mid-gap/2, botY=g.mid+gap/2;
    ctx.fillStyle=pal[2]; ctx.shadowColor=pal[1]; ctx.shadowBlur=10;
    ctx.fillRect(g.x,0,g.w,topH); ctx.fillRect(g.x,botY,g.w,S.H-botY);
    ctx.shadowBlur=0; ctx.fillStyle=pal[1]; ctx.fillRect(g.x,topH-6,g.w,6); ctx.fillRect(g.x,botY,g.w,6);
  });
  if(inv>0 && Math.floor(inv*12)%2===0) return;
  ctx.save(); ctx.translate(drone.x,drone.y); ctx.rotate(Math.atan2(vy,240)*0.45);
  ctx.fillStyle=pal[1]; ctx.shadowColor=pal[1]; ctx.shadowBlur=14;
  ctx.beginPath(); ctx.moveTo(16,0); ctx.lineTo(-12,-10); ctx.lineTo(-7,0); ctx.lineTo(-12,10); ctx.closePath(); ctx.fill();
  ctx.fillStyle="#f472b6"; ctx.fillRect(-16,-3,7,6);
  ctx.restore(); ctx.shadowBlur=0;
}
function onKeyDown(e){if(e.code==="Space"||e.code==="ArrowUp"||e.code==="KeyW"){e.preventDefault(); thrust();}}
function onKeyUp(e){}
function onPointer(p,type){if(type==="down") thrust();}
'''
)

GAMES["galaxy-defender"] = (
    {
        "title": "Galaxy Defender",
        "slug": "galaxy-defender",
        "desc": "Uzay gemisiyle düşman dalgalarını temizle.",
        "genre_tr": "Aksiyon · Uzay",
        "genre_en": "Action · Space",
        "tag_tr": "Hareket et, ateş et, dalgayı temizle",
        "tag_en": "Move, shoot, clear the wave",
        "how_tr": [
            "<b>Hareket:</b> ←→ / A D / fare / dokun",
            "<b>Ateş:</b> Space / tık",
            "<b>Hedef:</b> Tüm düşmanları yok et",
            "<b>Can:</b> Mermi veya çarpışma",
            "<b>12 level:</b> Daha yoğun dalgalar",
        ],
        "how_en": [
            "<b>Move:</b> arrows / A D / mouse / touch",
            "<b>Fire:</b> Space / tap",
            "<b>Goal:</b> Destroy all enemies",
            "<b>Lives:</b> Shots or collisions",
            "<b>12 levels:</b> Denser waves",
        ],
        "cw": 480, "ch": 720,
        "music": "[220,247,262,294,330,294,262,247]",
    },
    r'''
var ship,bullets,enemies,eBullets,fireCd,inv;
function LEVEL_TARGET(lv){return 120+lv*70;}
function gameReset(){
  ship={x:S.W/2,y:S.H-70,w:34,h:22}; bullets=[]; enemies=[]; eBullets=[]; fireCd=0; inv=0;
  var rows=3+Math.min(3,(S.level/3)|0), cols=5+Math.min(3,(S.level/4)|0);
  var gapX=(S.W-80)/(Math.max(1,cols-1));
  for(var r=0;r<rows;r++) for(var c=0;c<cols;c++){
    enemies.push({x:40+c*gapX, y:70+r*48, hp:1+(S.level>7?1:0), t:Math.random()*6, type:r%3, baseX:40+c*gapX});
  }
  onHudExtra();
}
function onHudExtra(){
  document.getElementById("hudExtraLabel").textContent=LANG==="en"?"FOES":"DÜŞMAN";
  document.getElementById("hudExtra").textContent=String(enemies.length);
}
function fire(){if(fireCd>0||S.mode!=="play")return; fireCd=0.2; bullets.push({x:ship.x,y:ship.y-14,vy:-460}); sfx("shot");}
function gameUpdate(dt){
  if(inv>0) inv-=dt;
  fireCd=Math.max(0,fireCd-dt);
  if(S.keys.left) ship.x-=300*dt;
  if(S.keys.right) ship.x+=300*dt;
  if(S.pointer && S.pointer.y>S.H*0.45) ship.x+=(S.pointer.x-ship.x)*Math.min(1,dt*12);
  ship.x=clamp(ship.x,22,S.W-22);
  if(S.keys.fire) fire();
  bullets.forEach(function(b){b.y+=b.vy*dt;}); bullets=bullets.filter(function(b){return b.y>-20;});
  eBullets.forEach(function(b){b.y+=b.vy*dt; b.x+=b.vx*dt;}); eBullets=eBullets.filter(function(b){return b.y<S.H+20;});
  var spd=35+S.level*7;
  enemies.forEach(function(e,i){
    e.t+=dt; e.x=e.baseX+Math.sin(e.t*1.6+i)*18;
    e.y+=Math.sin(e.t*0.7+i)*6*dt;
    if(Math.random()<0.003+S.level*0.0005) eBullets.push({x:e.x,y:e.y+12,vy:170+S.level*10,vx:rand(-20,20)});
  });
  for(var i=enemies.length-1;i>=0;i--){
    var e=enemies[i];
    for(var j=bullets.length-1;j>=0;j--){
      var b=bullets[j];
      if(Math.abs(b.x-e.x)<20 && Math.abs(b.y-e.y)<18){
        bullets.splice(j,1); e.hp--;
        if(e.hp<=0){S.score+=25+S.level*4; burst(e.x,e.y,"#fbbf24",14,190); enemies.splice(i,1); sfx("coin");}
        break;
      }
    }
  }
  for(var i=eBullets.length-1;i>=0;i--){
    var b=eBullets[i];
    if(Math.abs(b.x-ship.x)<18 && Math.abs(b.y-ship.y)<16){
      eBullets.splice(i,1);
      if(inv<=0){S.lives--; inv=1.2; S.shake=0.5; S.flash=0.35; sfx("bad"); if(S.lives<=0){gameOver(); return;}}
    }
  }
  enemies.forEach(function(e){
    if(Math.abs(e.x-ship.x)<24 && Math.abs(e.y-ship.y)<22){
      if(inv<=0){S.lives--; inv=1.2; S.shake=0.5; sfx("bad"); if(S.lives<=0) gameOver();}
    }
  });
  updateHud(); onHudExtra();
  if(!enemies.length) levelComplete(220);
}
function gameDraw(ctx,pal){
  for(var i=0;i<50;i++){ctx.fillStyle="rgba(180,200,255,0.25)"; ctx.fillRect((i*53)%S.W,(i*97+performance.now()*0.02)%S.H,2,2);}
  enemies.forEach(function(e){
    ctx.save(); ctx.translate(e.x,e.y);
    ctx.fillStyle=e.type===0?"#f472b6":e.type===1?"#a78bfa":"#4ade80";
    ctx.shadowColor=ctx.fillStyle; ctx.shadowBlur=10;
    ctx.beginPath(); ctx.moveTo(0,-14); ctx.lineTo(14,10); ctx.lineTo(0,5); ctx.lineTo(-14,10); ctx.closePath(); ctx.fill();
    ctx.restore();
  });
  ctx.shadowBlur=0;
  bullets.forEach(function(b){ctx.fillStyle="#67e8f9"; ctx.fillRect(b.x-2,b.y-10,4,14);});
  eBullets.forEach(function(b){ctx.fillStyle="#fb7185"; ctx.beginPath(); ctx.arc(b.x,b.y,3.5,0,Math.PI*2); ctx.fill();});
  if(inv>0 && Math.floor(inv*14)%2===0) return;
  ctx.save(); ctx.translate(ship.x,ship.y);
  ctx.fillStyle=pal[1]; ctx.shadowColor=pal[1]; ctx.shadowBlur=14;
  ctx.beginPath(); ctx.moveTo(0,-18); ctx.lineTo(18,14); ctx.lineTo(0,7); ctx.lineTo(-18,14); ctx.closePath(); ctx.fill();
  ctx.fillStyle="#f0abfc"; ctx.fillRect(-3,7,6,10);
  ctx.restore(); ctx.shadowBlur=0;
}
function onKeyDown(e){
  if(e.code==="ArrowLeft"||e.code==="KeyA"){S.keys.left=true;e.preventDefault();}
  if(e.code==="ArrowRight"||e.code==="KeyD"){S.keys.right=true;e.preventDefault();}
  if(e.code==="Space"){e.preventDefault(); S.keys.fire=true; fire();}
}
function onKeyUp(e){
  if(e.code==="ArrowLeft"||e.code==="KeyA")S.keys.left=false;
  if(e.code==="ArrowRight"||e.code==="KeyD")S.keys.right=false;
  if(e.code==="Space")S.keys.fire=false;
}
function onPointer(p,type){if(type==="down") fire(); if(type==="move"||type==="down") S.pointer=p;}
'''
)

GAMES["neon-maze-muncher"] = (
    {
        "title": "Neon Maze Muncher",
        "slug": "neon-maze-muncher",
        "desc": "Labirentte çekirdek topla, avcı dronlardan kaç.",
        "genre_tr": "Labirent · Toplama",
        "genre_en": "Maze · Collect",
        "tag_tr": "Çekirdekleri topla · mor dronlardan kaç",
        "tag_en": "Collect cores · dodge hunter drones",
        "how_tr": [
            "<b>Hareket:</b> Oklar / WASD / kaydır",
            "<b>Hedef:</b> Tüm çekirdekleri topla",
            "<b>Düşman:</b> Mor avcı dronlar",
            "<b>Cyan çekirdek:</b> Kısa hız artışı",
            "<b>12 level:</b> Daha büyük labirent",
        ],
        "how_en": [
            "<b>Move:</b> arrows / WASD / swipe",
            "<b>Goal:</b> Collect all cores",
            "<b>Enemies:</b> Purple hunter drones",
            "<b>Cyan core:</b> Short speed boost",
            "<b>12 levels:</b> Larger mazes",
        ],
        "cw": 480, "ch": 640,
        "music": "[174,196,220,246,220,196,174,164]",
    },
    r'''
var CELL,COLS,ROWS,maze,player,drones,cores,boost,moveCd;
function LEVEL_TARGET(lv){return 100+lv*40;}
function gameReset(){
  COLS=15+(S.level>6?2:0); ROWS=17+(S.level>8?2:0);
  CELL=Math.floor(Math.min((S.W-16)/COLS,(S.H-36)/ROWS));
  maze=buildMaze(COLS,ROWS); player={x:1,y:1}; boost=0; moveCd=0; cores=[]; drones=[];
  for(var y=1;y<ROWS-1;y++) for(var x=1;x<COLS-1;x++){
    if(maze[y][x]===0 && !(x===1&&y===1) && Math.random()<0.5) cores.push({x:x,y:y,power:Math.random()<0.1});
  }
  if(cores.length<8){
    for(var y=1;y<ROWS-1 && cores.length<12;y++) for(var x=1;x<COLS-1 && cores.length<12;x++){
      if(maze[y][x]===0 && !(x===1&&y===1) && !cores.some(function(c){return c.x===x&&c.y===y;})) cores.push({x:x,y:y,power:false});
    }
  }
  var dc=2+Math.min(4,(S.level/2)|0);
  for(var i=0;i<dc;i++) drones.push({x:COLS-2-i%2, y:ROWS-2-(i%3), t:0});
  onHudExtra();
}
function buildMaze(w,h){
  var m=[]; for(var y=0;y<h;y++){m[y]=[]; for(var x=0;x<w;x++) m[y][x]=(x===0||y===0||x===w-1||y===h-1||(x%2===0&&y%2===0))?1:0;}
  for(var i=0;i<w*h*0.07;i++){var x=1+(Math.random()*(w-2))|0,y=1+(Math.random()*(h-2))|0; if(!(x<=2&&y<=2)) m[y][x]=1;}
  m[1][1]=0; m[1][2]=0; m[2][1]=0; return m;
}
function onHudExtra(){
  document.getElementById("hudExtraLabel").textContent=LANG==="en"?"CORES":"ÇEKİRDEK";
  document.getElementById("hudExtra").textContent=String(cores.length);
}
function tryMove(dx,dy){
  if(moveCd>0) return;
  var nx=player.x+dx, ny=player.y+dy;
  if(nx<0||ny<0||nx>=COLS||ny>=ROWS||maze[ny][nx]===1) return;
  player.x=nx; player.y=ny; moveCd=boost>0?0.07:0.11; sfx("move");
  for(var i=cores.length-1;i>=0;i--) if(cores[i].x===player.x&&cores[i].y===player.y){
    if(cores[i].power){boost=4.5; sfx("ok");} else sfx("coin");
    S.score+=18; burst(ox()+CELL/2,oy()+CELL/2,"#fbbf24",8,130); cores.splice(i,1);
  }
  onHudExtra(); updateHud();
  if(!cores.length) levelComplete(200);
}
function ox(){return (S.W-COLS*CELL)/2+player.x*CELL;}
function oy(){return 28+player.y*CELL;}
function gameUpdate(dt){
  moveCd=Math.max(0,moveCd-dt); boost=Math.max(0,boost-dt);
  if(S.keys.left) tryMove(-1,0);
  if(S.keys.right) tryMove(1,0);
  if(S.keys.up) tryMove(0,-1);
  if(S.keys.down) tryMove(0,1);
  drones.forEach(function(d){
    d.t+=dt; var interval=Math.max(0.16,0.32-S.level*0.01);
    if(d.t<interval) return; d.t=0;
    var opts=[];
    [[1,0],[-1,0],[0,1],[0,-1]].forEach(function(v){
      var nx=d.x+v[0], ny=d.y+v[1];
      if(nx>=0&&ny>=0&&nx<COLS&&ny<ROWS&&maze[ny][nx]===0) opts.push(v);
    });
    if(!opts.length) return;
    opts.sort(function(a,b){
      return (Math.abs(d.x+a[0]-player.x)+Math.abs(d.y+a[1]-player.y)) - (Math.abs(d.x+b[0]-player.x)+Math.abs(d.y+b[1]-player.y));
    });
    var ch=Math.random()<0.72?opts[0]:opts[(Math.random()*opts.length)|0];
    d.x+=ch[0]; d.y+=ch[1];
    if(d.x===player.x&&d.y===player.y){
      S.lives--; S.shake=0.5; S.flash=0.35; sfx("bad"); updateHud();
      player.x=1; player.y=1;
      if(S.lives<=0) gameOver();
    }
  });
}
function gameDraw(ctx,pal){
  var ox0=(S.W-COLS*CELL)/2, oy0=28;
  for(var y=0;y<ROWS;y++) for(var x=0;x<COLS;x++){
    var rx=ox0+x*CELL, ry=oy0+y*CELL;
    if(maze[y][x]===1){ctx.fillStyle=pal[0]; ctx.strokeStyle=pal[1]; ctx.lineWidth=1; ctx.fillRect(rx,ry,CELL-1,CELL-1); ctx.strokeRect(rx+1,ry+1,CELL-3,CELL-3);}
    else {ctx.fillStyle="rgba(0,0,0,0.22)"; ctx.fillRect(rx,ry,CELL-1,CELL-1);}
  }
  cores.forEach(function(c){
    ctx.fillStyle=c.power?"#67e8f9":"#fbbf24";
    ctx.beginPath(); ctx.arc(ox0+c.x*CELL+CELL/2, oy0+c.y*CELL+CELL/2, CELL*0.18,0,Math.PI*2); ctx.fill();
  });
  ctx.fillStyle=pal[1]; ctx.shadowColor=pal[1]; ctx.shadowBlur=12;
  ctx.fillRect(ox0+player.x*CELL+4, oy0+player.y*CELL+4, CELL-8, CELL-8);
  drones.forEach(function(d){
    var cx=ox0+d.x*CELL+CELL/2, cy=oy0+d.y*CELL+CELL/2;
    ctx.fillStyle="#c084fc"; ctx.shadowColor="#c084fc"; ctx.shadowBlur=10;
    ctx.beginPath();
    for(var i=0;i<6;i++){var a=i/6*Math.PI*2; var px=cx+Math.cos(a)*CELL*0.32, py=cy+Math.sin(a)*CELL*0.32; if(i===0)ctx.moveTo(px,py); else ctx.lineTo(px,py);}
    ctx.closePath(); ctx.fill();
  });
  ctx.shadowBlur=0;
}
function onKeyDown(e){
  if(e.code==="ArrowLeft"||e.code==="KeyA"){S.keys.left=true;e.preventDefault();}
  if(e.code==="ArrowRight"||e.code==="KeyD"){S.keys.right=true;e.preventDefault();}
  if(e.code==="ArrowUp"||e.code==="KeyW"){S.keys.up=true;e.preventDefault();}
  if(e.code==="ArrowDown"||e.code==="KeyS"){S.keys.down=true;e.preventDefault();}
}
function onKeyUp(e){
  if(e.code==="ArrowLeft"||e.code==="KeyA")S.keys.left=false;
  if(e.code==="ArrowRight"||e.code==="KeyD")S.keys.right=false;
  if(e.code==="ArrowUp"||e.code==="KeyW")S.keys.up=false;
  if(e.code==="ArrowDown"||e.code==="KeyS")S.keys.down=false;
}
var sw0=null;
function onPointer(p,type){
  if(type==="down") sw0={x:p.x,y:p.y};
  if(type==="up"&&sw0){
    var dx=p.x-sw0.x, dy=p.y-sw0.y;
    if(Math.abs(dx)>18||Math.abs(dy)>18){ if(Math.abs(dx)>Math.abs(dy)) tryMove(dx>0?1:-1,0); else tryMove(0,dy>0?1:-1); }
    sw0=null;
  }
}
'''
)

GAMES["memory-flash"] = (
    {
        "title": "Memory Flash",
        "slug": "memory-flash",
        "desc": "Kart çiftlerini eşleştir, az hamleyle yıldız kazan.",
        "genre_tr": "Bulmaca · Hafıza",
        "genre_en": "Puzzle · Memory",
        "tag_tr": "Kartları çevir, çiftleri bul",
        "tag_en": "Flip cards, find pairs",
        "how_tr": [
            "<b>Kontrol:</b> Tıkla / dokun",
            "<b>Hedef:</b> Tüm çiftleri bul",
            "<b>Skor:</b> Az hamle = yüksek puan",
            "<b>Yanlış:</b> Küçük puan kaybı",
            "<b>12 level:</b> Daha fazla kart",
        ],
        "how_en": [
            "<b>Controls:</b> Tap cards",
            "<b>Goal:</b> Match all pairs",
            "<b>Score:</b> Fewer moves = higher score",
            "<b>Mistakes:</b> Small score penalty",
            "<b>12 levels:</b> More cards",
        ],
        "cw": 480, "ch": 720,
        "music": "[523,494,440,392,440,494,523,587]",
    },
    r'''
var cols,rows,cards,open,lock,pairsLeft,moves;
var SYMBOLS=["◆","●","▲","■","★","✚","◇","○","△","□","☆","✖","⬡","⬢","✦","✧"];
function LEVEL_TARGET(lv){return 180+lv*35;}
function gameReset(){
  var pairs=Math.min(12,4+S.level); // 4..12
  cols=pairs<=6?3:(pairs<=8?4:4); rows=Math.ceil((pairs*2)/cols);
  while(cols*rows<pairs*2) rows++;
  var deck=SYMBOLS.slice(0,pairs).concat(SYMBOLS.slice(0,pairs));
  for(var i=deck.length-1;i>0;i--){var j=(Math.random()*(i+1))|0; var t=deck[i]; deck[i]=deck[j]; deck[j]=t;}
  cards=[]; var k=0;
  for(var y=0;y<rows;y++) for(var x=0;x<cols;x++) if(k<deck.length) cards.push({x:x,y:y,v:deck[k++],flip:false,done:false});
  open=[]; lock=false; pairsLeft=pairs; moves=0; onHudExtra();
}
function onHudExtra(){
  document.getElementById("hudExtraLabel").textContent=LANG==="en"?"PAIRS":"ÇİFT";
  document.getElementById("hudExtra").textContent=String(pairsLeft);
}
function layout(){var pad=14, top=70, bw=(S.W-pad*2)/cols, bh=(S.H-top-pad)/rows; return {pad:pad,top:top,bw:bw,bh:bh};}
function gameUpdate(dt){}
function gameDraw(ctx,pal){
  var L=layout();
  cards.forEach(function(c){
    var rx=L.pad+c.x*L.bw+5, ry=L.top+c.y*L.bh+5, rw=L.bw-10, rh=L.bh-10;
    if(c.done||c.flip){ctx.fillStyle=pal[1]; ctx.shadowColor=pal[1]; ctx.shadowBlur=10;}
    else {ctx.fillStyle="rgba(15,23,42,0.92)";}
    ctx.fillRect(rx,ry,rw,rh); ctx.shadowBlur=0;
    if(!c.done&&!c.flip){ctx.strokeStyle=pal[2]; ctx.lineWidth=2; ctx.strokeRect(rx,ry,rw,rh);
      ctx.fillStyle=pal[2]; ctx.font="bold 22px Inter,sans-serif"; ctx.textAlign="center"; ctx.textBaseline="middle"; ctx.fillText("?",rx+rw/2,ry+rh/2);}
    else {ctx.fillStyle="#0f172a"; ctx.font="bold "+Math.floor(Math.min(rw,rh)*0.42)+"px Inter,sans-serif"; ctx.textAlign="center"; ctx.textBaseline="middle"; ctx.fillText(c.v,rx+rw/2,ry+rh/2);}
  });
}
function onPointer(p,type){
  if(type!=="down"||lock||S.mode!=="play") return;
  var L=layout(); var x=((p.x-L.pad)/L.bw)|0, y=((p.y-L.top)/L.bh)|0;
  var c=null; for(var i=0;i<cards.length;i++) if(cards[i].x===x&&cards[i].y===y) c=cards[i];
  if(!c||c.done||c.flip) return;
  c.flip=true; open.push(c); sfx("ui");
  if(open.length===2){
    moves++; lock=true;
    if(open[0].v===open[1].v){
      open[0].done=open[1].done=true; pairsLeft--; S.score+=55+Math.max(0,25-moves);
      sfx("coin"); burst(p.x,p.y,"#fbbf24",10,150); open=[]; lock=false; onHudExtra(); updateHud();
      if(pairsLeft<=0){S.score+=100; levelComplete(100);}
    } else {
      S.score=Math.max(0,S.score-4); sfx("bad"); updateHud();
      setTimeout(function(){open.forEach(function(o){o.flip=false;}); open=[]; lock=false;},700);
    }
  }
}
function onKeyDown(e){}
function onKeyUp(e){}
'''
)

GAMES["reaction-rush"] = (
    {
        "title": "Reaction Rush",
        "slug": "reaction-rush",
        "desc": "Yeşil olunca bas, ortalama reaksiyon süreni düşür.",
        "genre_tr": "Refleks · Test",
        "genre_en": "Reflex · Test",
        "tag_tr": "Kırmızıda bekle · YEŞİLDE bas",
        "tag_en": "Wait on red · tap on GREEN",
        "how_tr": [
            "<b>Kontrol:</b> Space / tık / dokun",
            "<b>Kural:</b> Kırmızıda bekle, yeşilde bas",
            "<b>Erken basma:</b> Fail · can kaybı",
            "<b>Hedef:</b> N tur, ortalama eşiğin altında",
            "<b>12 level:</b> Daha sıkı eşik",
        ],
        "how_en": [
            "<b>Controls:</b> Space / tap",
            "<b>Rule:</b> Wait red, tap green",
            "<b>Early tap:</b> Fail · lose life",
            "<b>Goal:</b> N rounds under avg threshold",
            "<b>12 levels:</b> Stricter target",
        ],
        "cw": 480, "ch": 640,
        "music": "[0]",
    },
    r'''
var phase,waitT,goAt,times,need,threshold;
// phase: ready | go | result
function LEVEL_TARGET(lv){return 80+lv*15;}
function gameReset(){
  times=[]; need=5+Math.min(5,(S.level/2)|0); threshold=430-S.level*14;
  schedule(); onHudExtra();
}
function schedule(){phase="ready"; waitT=rand(0.9,2.4); goAt=0;}
function onHudExtra(){
  var avg=times.length?(times.reduce(function(a,b){return a+b;},0)/times.length)|0:0;
  document.getElementById("hudExtraLabel").textContent=LANG==="en"?"AVG":"ORT";
  document.getElementById("hudExtra").textContent=avg+"ms · "+times.length+"/"+need;
}
function gameUpdate(dt){
  if(phase==="ready"){waitT-=dt; if(waitT<=0){phase="go"; goAt=performance.now(); sfx("ok");}}
}
function tap(){
  if(S.mode!=="play"||!S.running) return;
  if(phase==="ready"){
    S.lives--; S.shake=0.4; S.flash=0.3; sfx("bad"); phase="result"; updateHud();
    if(S.lives<=0){gameOver(); return;}
    setTimeout(schedule,500); return;
  }
  if(phase==="go"){
    var ms=performance.now()-goAt; times.push(ms);
    S.score+=Math.max(8, Math.floor((threshold+120-ms)/3)); sfx("coin");
    phase="result"; onHudExtra(); updateHud();
    if(times.length>=need){
      var avg=times.reduce(function(a,b){return a+b;},0)/times.length;
      if(avg<=threshold) levelComplete(140);
      else {
        showToast(LANG==="en"?"Too slow":"Yavaş", (avg|0)+"ms > "+threshold+"ms");
        S.lives--; updateHud();
        if(S.lives<=0) gameOver();
        else {times=[]; setTimeout(schedule,700);}
      }
    } else setTimeout(schedule,450);
  }
}
function gameDraw(ctx,pal){
  var col=phase==="go"?"#22c55e":(phase==="ready"?"#ef4444":"#334155");
  ctx.fillStyle=col; ctx.shadowColor=col; ctx.shadowBlur=28;
  roundFill(ctx,36,S.H*0.22,S.W-72,S.H*0.42,22);
  ctx.shadowBlur=0;
  ctx.fillStyle="#fff"; ctx.font="bold 28px Inter,sans-serif"; ctx.textAlign="center";
  var msg=phase==="go"?(LANG==="en"?"NOW!":"ŞİMDİ!"):(phase==="ready"?(LANG==="en"?"WAIT":"BEKLE"):"...");
  ctx.fillText(msg,S.W/2,S.H*0.45);
  ctx.font="14px Inter,sans-serif"; ctx.fillStyle="#e2e8f0";
  ctx.fillText((LANG==="en"?"Target avg ≤ ":"Hedef ort. ≤ ")+threshold+" ms", S.W/2, S.H*0.74);
  if(times.length){
    var avg=(times.reduce(function(a,b){return a+b;},0)/times.length)|0;
    ctx.fillText((LANG==="en"?"Last: ":"Son: ")+(times[times.length-1]|0)+" · "+(LANG==="en"?"Avg: ":"Ort: ")+avg, S.W/2, S.H*0.8);
  }
}
function roundFill(ctx,x,y,w,h,r){ctx.beginPath();ctx.moveTo(x+r,y);ctx.arcTo(x+w,y,x+w,y+h,r);ctx.arcTo(x+w,y+h,x,y+h,r);ctx.arcTo(x,y+h,x,y,r);ctx.arcTo(x,y,x+w,y,r);ctx.closePath();ctx.fill();}
function onKeyDown(e){if(e.code==="Space"||e.code==="Enter"){e.preventDefault(); tap();}}
function onKeyUp(e){}
function onPointer(p,type){if(type==="down") tap();}
'''
)

GAMES["runner-byte"] = (
    {
        "title": "Runner Byte",
        "slug": "runner-byte",
        "desc": "3 şerit siber koşu: paket topla, engellerden kaç.",
        "genre_tr": "Koşu · Aksiyon",
        "genre_en": "Runner · Action",
        "tag_tr": "Şerit değiştir · zıpla · paket topla",
        "tag_en": "Switch lanes · jump · grab packs",
        "how_tr": [
            "<b>Hareket:</b> ←→ / A D / kaydır",
            "<b>Zıpla:</b> Space / W / üst yarı dokun",
            "<b>Hedef:</b> Level mesafesini bitir",
            "<b>Topla:</b> Sarı veri paketleri",
            "<b>12 level:</b> Hız ve engel artar",
        ],
        "how_en": [
            "<b>Move:</b> arrows / A D / swipe",
            "<b>Jump:</b> Space / W / top tap",
            "<b>Goal:</b> Finish distance",
            "<b>Collect:</b> Yellow data packs",
            "<b>12 levels:</b> Faster density",
        ],
        "cw": 420, "ch": 720,
        "music": "[196,233,261,311,261,233,196,174]",
    },
    r'''
var LANES=3,lane,x,y,jump,jv,obstacles,packs,dist,goal,speed,spawnT,inv;
function LEVEL_TARGET(lv){return 180+lv*55;}
function laneX(l){var pad=48; return pad+l*((S.W-pad*2)/(LANES-1));}
function gameReset(){
  lane=1; x=laneX(1); y=S.H*0.78; jump=0; jv=0; obstacles=[]; packs=[]; dist=0; inv=0;
  goal=650+S.level*170; speed=190+S.level*20; spawnT=0.4; onHudExtra();
}
function onHudExtra(){
  document.getElementById("hudExtraLabel").textContent=LANG==="en"?"DIST":"MESAFE";
  document.getElementById("hudExtra").textContent=(dist|0)+"/"+(goal|0);
}
function gameUpdate(dt){
  if(inv>0) inv-=dt;
  x+=(laneX(lane)-x)*Math.min(1,dt*14);
  if(S.keys.jump&&jump===0){jv=-420; jump=0.001; S.keys.jump=false; sfx("jump");}
  if(jump>0||jv!==0){jv+=1350*dt; jump+=jv*dt; if(jump>=0){jump=0; jv=0;}}
  dist+=speed*dt*0.12; S.score+=speed*dt*0.05; spawnT-=dt;
  if(spawnT<=0){
    spawnT=Math.max(0.32,0.8-S.level*0.03)+Math.random()*0.2;
    if(Math.random()<0.62) obstacles.push({lane:(Math.random()*LANES)|0,y:-50,h:42,w:50});
    else packs.push({lane:(Math.random()*LANES)|0,y:-30,r:11});
  }
  var py=y+jump;
  obstacles.forEach(function(o){o.y+=speed*dt;}); packs.forEach(function(p){p.y+=speed*dt;});
  obstacles=obstacles.filter(function(o){return o.y<S.H+70;}); packs=packs.filter(function(p){return p.y<S.H+50;});
  for(var i=obstacles.length-1;i>=0;i--){
    var o=obstacles[i];
    if(o.lane===lane && Math.abs(py-(o.y+20))<30 && jump>-18){
      obstacles.splice(i,1);
      if(inv<=0){S.lives--; inv=1.0; S.shake=0.5; S.flash=0.35; sfx("bad"); updateHud(); if(S.lives<=0){gameOver(); return;}}
    }
  }
  for(var i=packs.length-1;i>=0;i--){
    var p=packs[i];
    if(p.lane===lane && Math.abs(py-p.y)<30){packs.splice(i,1); S.score+=35; sfx("coin"); burst(laneX(p.lane),p.y,"#fbbf24",8,150);}
  }
  updateHud(); onHudExtra();
  if(dist>=goal) levelComplete(180);
}
function gameDraw(ctx,pal){
  for(var i=0;i<LANES;i++){ctx.strokeStyle="rgba(34,211,238,0.18)"; ctx.beginPath(); ctx.moveTo(laneX(i),S.H*0.22); ctx.lineTo(laneX(i),S.H); ctx.stroke();}
  for(var i=0;i<14;i++){var yy=((i*55+dist*3.2)%(S.H*0.72))+S.H*0.22; ctx.strokeStyle="rgba(129,140,248,0.12)"; ctx.beginPath(); ctx.moveTo(28,yy); ctx.lineTo(S.W-28,yy); ctx.stroke();}
  obstacles.forEach(function(o){ctx.fillStyle="#fb7185"; ctx.shadowColor="#fb7185"; ctx.shadowBlur=10; ctx.fillRect(laneX(o.lane)-o.w/2,o.y,o.w,o.h);});
  packs.forEach(function(p){ctx.fillStyle="#fbbf24"; ctx.shadowColor="#fbbf24"; ctx.shadowBlur=8; ctx.beginPath(); ctx.arc(laneX(p.lane),p.y,p.r,0,Math.PI*2); ctx.fill();});
  ctx.shadowBlur=0;
  if(inv>0 && Math.floor(inv*12)%2===0) return;
  var py=y+jump; ctx.save(); ctx.translate(x,py);
  ctx.fillStyle=pal[1]; ctx.shadowColor=pal[1]; ctx.shadowBlur=12;
  ctx.fillRect(-14,-18,28,32); ctx.fillStyle="#0f172a"; ctx.fillRect(-7,-10,5,5); ctx.fillRect(2,-10,5,5);
  ctx.strokeStyle=pal[2]; ctx.beginPath(); ctx.moveTo(0,-18); ctx.lineTo(0,-28); ctx.stroke();
  ctx.fillStyle="#f472b6"; ctx.beginPath(); ctx.arc(0,-30,3.5,0,Math.PI*2); ctx.fill();
  ctx.restore(); ctx.shadowBlur=0;
}
function onKeyDown(e){
  if(e.code==="ArrowLeft"||e.code==="KeyA"){lane=clamp(lane-1,0,LANES-1); sfx("move");}
  if(e.code==="ArrowRight"||e.code==="KeyD"){lane=clamp(lane+1,0,LANES-1); sfx("move");}
  if(e.code==="Space"||e.code==="ArrowUp"||e.code==="KeyW"){e.preventDefault(); S.keys.jump=true;}
}
function onKeyUp(e){}
var sw0=null;
function onPointer(p,type){
  if(type==="down"){
    sw0={x:p.x,y:p.y};
    if(p.y<S.H*0.38) S.keys.jump=true;
    else {
      var best=0,bd=1e9; for(var i=0;i<LANES;i++){var d=Math.abs(laneX(i)-p.x); if(d<bd){bd=d; best=i;}}
      lane=best; sfx("move");
    }
  }
  if(type==="up"&&sw0){var dx=p.x-sw0.x; if(Math.abs(dx)>28){lane=clamp(lane+(dx>0?1:-1),0,LANES-1); sfx("move");} sw0=null;}
}
'''
)


def main():
    for slug, (meta, game_js) in GAMES.items():
        html = build(meta, game_js)
        out = PUBLIC / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        # quick sanity
        assert "function gameReset" in html
        assert "S.ready" in html
        assert "if(S.ready)" in html or "S.ready&&" in html or "S.ready)" in html
        print(f"OK {slug:20} {len(html):6} bytes")
    print("ALL GAMES REBUILT")


if __name__ == "__main__":
    main()

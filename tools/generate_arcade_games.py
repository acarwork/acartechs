# -*- coding: utf-8 -*-
"""Generate 9 original AcarTechs arcade games + posters/thumbs."""
from __future__ import annotations

import math
import os
import struct
import zlib
from pathlib import Path

ROOT = Path(r"C:\Users\facar\acartechs-deploy")
PUBLIC = ROOT / "public"
ARCADE = PUBLIC / "assets" / "arcade"

# Shared CSS + HTML chrome for every game
SHELL_CSS = r"""
  :root{--bg0:#04060f;--bg1:#0a1230;--neon:#22d3ee;--neon2:#a78bfa;--pink:#f472b6;--gold:#fbbf24;--lime:#4ade80;--text:#eef6ff;--muted:#94a3b8;--panel:rgba(6,12,28,.92);--line:rgba(125,211,252,.22)}
  *{box-sizing:border-box;margin:0;padding:0}
  html,body{width:100%;height:100%;overflow:hidden;background:radial-gradient(1000px 600px at 15% 0%,#1e1b4b 0%,transparent 55%),radial-gradient(900px 500px at 90% 30%,#0e7490 0%,transparent 50%),linear-gradient(165deg,var(--bg0),var(--bg1) 55%,#050a16);color:var(--text);font-family:Inter,Segoe UI,system-ui,sans-serif;touch-action:none;user-select:none;-webkit-user-select:none}
  #app{position:relative;width:100%;height:100%;min-height:100dvh}
  canvas#game{display:block;width:100%;height:100%;cursor:default;object-fit:contain;background:#03060f}
  .screen{position:absolute;inset:0;display:none;align-items:center;justify-content:center;padding:16px;z-index:5;overflow:auto}
  .screen.is-on{display:flex}
  .panel{width:min(540px,100%);background:var(--panel);border:1px solid var(--line);border-radius:20px;box-shadow:0 0 0 1px rgba(255,255,255,.04),0 30px 80px rgba(0,0,0,.45),0 0 50px rgba(34,211,238,.08);padding:24px 20px 18px;backdrop-filter:blur(14px);text-align:center;position:relative}
  .logo{font-size:clamp(28px,7vw,48px);font-weight:900;letter-spacing:.03em;line-height:1.05;background:linear-gradient(90deg,#67e8f9,#a78bfa 50%,#f472b6);-webkit-background-clip:text;background-clip:text;color:transparent;margin-bottom:6px}
  .logo small{display:block;margin-top:8px;font-size:11px;letter-spacing:.26em;color:var(--neon);font-weight:800}
  .genre{display:inline-block;margin:6px 0 8px;padding:4px 11px;border-radius:999px;border:1px solid rgba(34,211,238,.35);background:rgba(34,211,238,.1);color:var(--neon);font-size:11px;font-weight:900;letter-spacing:.1em;text-transform:uppercase}
  .tagline{color:var(--muted);font-size:13px;margin:8px 0 16px;line-height:1.45}
  .btn-col{display:grid;gap:8px}
  .btn{appearance:none;border:1px solid rgba(125,211,252,.28);background:linear-gradient(180deg,rgba(56,189,248,.16),rgba(15,23,42,.5));color:var(--text);font-weight:800;font-size:14px;letter-spacing:.03em;border-radius:12px;padding:12px 14px;cursor:pointer}
  .btn:hover{border-color:rgba(34,211,238,.6);box-shadow:0 10px 24px rgba(34,211,238,.14)}
  .btn.primary{background:linear-gradient(135deg,#22d3ee,#818cf8 55%,#c084fc);color:#06101f;border:none}
  .btn.ghost{background:transparent}
  .btn.danger{background:linear-gradient(135deg,#fb7185,#e11d48);border:none;color:#fff}
  .lang-row{display:grid;gap:6px;justify-items:center;margin:0 0 12px}
  .lang-label{color:var(--muted);font-size:10px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}
  .lang-switch{display:inline-grid;grid-template-columns:1fr 1fr;gap:8px;min-width:120px}
  .lang-switch button{appearance:none;border:1px solid rgba(125,211,252,.28);background:rgba(15,23,42,.55);color:var(--muted);font-size:12px;font-weight:900;border-radius:10px;padding:10px 12px;cursor:pointer}
  .lang-switch button.is-on{background:linear-gradient(135deg,rgba(34,211,238,.32),rgba(129,140,248,.34));border-color:rgba(34,211,238,.7);color:#fff}
  .menu-tools{display:flex;justify-content:space-between;align-items:center;margin-top:12px;gap:8px;flex-wrap:wrap}
  .sound-toggle{font-size:12px;font-weight:700;color:var(--muted);cursor:pointer;background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:999px;padding:7px 11px}
  .sound-toggle.is-on{color:var(--neon);border-color:rgba(34,211,238,.45)}
  .howto{text-align:left;color:#cbd5e1;font-size:13px;line-height:1.5;margin:8px 0 14px}
  .howto li{margin:0 0 7px 16px}
  .level-grid{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px;margin:10px 0 14px}
  .level-btn{appearance:none;border:1px solid rgba(125,211,252,.25);background:rgba(15,23,42,.55);color:#e2e8f0;border-radius:10px;padding:12px 4px;font-weight:800;font-size:13px;cursor:pointer}
  .level-btn:hover{border-color:var(--neon)}
  .level-btn.is-locked{opacity:.35;cursor:not-allowed}
  .level-btn .stars{display:block;font-size:10px;color:var(--gold);margin-top:3px}
  .hud{position:absolute;top:10px;left:10px;right:10px;z-index:6;display:none;pointer-events:none;gap:6px;justify-content:space-between;align-items:flex-start}
  .hud.is-on{display:flex}
  .hud-group{display:flex;flex-wrap:wrap;gap:5px}
  .chip{background:rgba(2,8,20,.75);border:1px solid var(--line);border-radius:999px;padding:6px 10px;font-size:11px;font-weight:800;backdrop-filter:blur(8px);color:#e2e8f0}
  .chip b{color:var(--neon);margin-left:3px}
  .hud-actions{display:flex;gap:5px;pointer-events:auto}
  .icon-btn{width:36px;height:36px;border-radius:11px;border:1px solid var(--line);background:rgba(2,8,20,.8);color:#e2e8f0;font-size:13px;font-weight:900;cursor:pointer}
  .overlay-msg{position:absolute;left:50%;top:40%;transform:translate(-50%,-50%);z-index:4;display:none;text-align:center;pointer-events:none;text-shadow:0 8px 30px rgba(0,0,0,.55)}
  .overlay-msg.is-on{display:block}
  .overlay-msg h2{font-size:clamp(24px,5vw,40px);font-weight:900;letter-spacing:.05em;margin-bottom:6px}
  .overlay-msg p{color:var(--muted);font-weight:600}
  .stars-big{font-size:28px;letter-spacing:4px;color:var(--gold);margin:6px 0 10px}
  .fs-note{font-size:11px;color:var(--muted)}
  @media (max-width:640px){.panel{padding:18px 14px 14px;border-radius:16px}.level-grid{grid-template-columns:repeat(4,minmax(0,1fr))}}
"""


def shell_html(meta: dict) -> str:
    title = meta["title"]
    slug = meta["slug"]
    genre = meta["genre_tr"]
    tagline = meta["tagline_tr"]
    desc = meta["desc"]
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, maximum-scale=1, user-scalable=no" />
<title>{title} – AcarTechs Arcade</title>
<meta name="description" content="{desc}" />
<link rel="canonical" href="https://acartechs.com/{slug}/" />
<style>{SHELL_CSS}</style>
</head>
<body>
<div id="app">
  <canvas id="game" width="{meta.get('cw', 480)}" height="{meta.get('ch', 720)}" aria-label="{title}"></canvas>
  <div class="hud" id="hud">
    <div class="hud-group">
      <div class="chip"><span data-i18n="hudScore">SKOR</span> <b id="hudScore">0</b></div>
      <div class="chip"><span data-i18n="hudLevel">LEVEL</span> <b id="hudLevel">1</b></div>
      <div class="chip"><span data-i18n="hudLives">CAN</span> <b id="hudLives">3</b></div>
      <div class="chip" id="hudExtraChip"><span id="hudExtraLabel">—</span> <b id="hudExtra">0</b></div>
    </div>
    <div class="hud-actions">
      <button class="icon-btn" id="btnPause" type="button" title="P">II</button>
      <button class="icon-btn" id="btnSoundHud" type="button" title="Ses">🔊</button>
      <button class="icon-btn" id="btnExit" type="button" title="ESC">✕</button>
    </div>
  </div>
  <div class="overlay-msg" id="toast"><h2 id="toastTitle"></h2><p id="toastText"></p></div>

  <section class="screen is-on" id="screenMenu">
    <div class="panel">
      <div class="logo">{title.upper()}<small>ACARTECHS ARCADE</small></div>
      <span class="genre" data-i18n="genre">{genre}</span>
      <p class="tagline" data-i18n="tagline">{tagline}</p>
      <div class="lang-row">
        <span class="lang-label" data-i18n="langLabel">Dil / Language</span>
        <div class="lang-switch"><button type="button" id="btnLangTr" class="is-on">TR</button><button type="button" id="btnLangEn">EN</button></div>
      </div>
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

  <section class="screen" id="screenLevels">
    <div class="panel">
      <div class="logo" style="font-size:28px" data-i18n="levelsTitle">LEVEL SEÇ</div>
      <div class="level-grid" id="levelGrid"></div>
      <div class="btn-col"><button class="btn primary" id="btnLevelsBack" type="button" data-i18n="btnBackMenu">MENÜYE DÖN</button></div>
    </div>
  </section>

  <section class="screen" id="screenHow">
    <div class="panel">
      <div class="logo" style="font-size:28px" data-i18n="howTitle">NASIL OYNANIR</div>
      <ul class="howto" id="howList"></ul>
      <div class="btn-col"><button class="btn primary" id="btnHowBack" type="button" data-i18n="btnBackMenu">MENÜYE DÖN</button></div>
    </div>
  </section>

  <section class="screen" id="screenPause">
    <div class="panel">
      <div class="logo" style="font-size:34px" data-i18n="pauseTitle">DURAKLATILDI</div>
      <div class="btn-col">
        <button class="btn primary" id="btnResume" type="button" data-i18n="btnResume">DEVAM ET</button>
        <button class="btn" id="btnRestart" type="button" data-i18n="btnRestart">YENİDEN BAŞLAT</button>
        <button class="btn" id="btnPauseMenu" type="button" data-i18n="btnMainMenu">ANA MENÜ</button>
        <button class="btn danger" id="btnPauseExit" type="button" data-i18n="btnExit">ÇIKIŞ</button>
      </div>
    </div>
  </section>

  <section class="screen" id="screenOver">
    <div class="panel">
      <div class="logo" style="font-size:30px" id="overTitle">GAME OVER</div>
      <div class="stars-big" id="overStars"></div>
      <p class="tagline" id="overStats"></p>
      <div class="btn-col">
        <button class="btn primary" id="btnNext" type="button" data-i18n="btnNext">SONRAKİ LEVEL</button>
        <button class="btn" id="btnReplay" type="button" data-i18n="btnReplay">TEKRAR OYNA</button>
        <button class="btn" id="btnOverMenu" type="button" data-i18n="btnMainMenu">ANA MENÜ</button>
        <button class="btn ghost" id="btnOverHome" type="button" data-i18n="btnArcadeHome">ARCADE ANA SAYFA</button>
      </div>
    </div>
  </section>
</div>
<script>
"""


SHELL_JS_COMMON = r"""
(function(){
"use strict";
var LANG="tr";
var MAX_LEVEL=12;
var I18N={
 tr:{
  genre:GENRE_TR, tagline:TAGLINE_TR, langLabel:"Dil / Language",
  btnStart:"BAŞLA", btnLevels:"LEVEL SEÇ", btnFullscreen:"TAM EKRANDA OYNA", btnHow:"NASIL OYNANIR",
  btnExitMenu:"ÇIKIŞ / ARCADE", soundOn:"🔊 Ses: Açık", soundOff:"🔇 Ses: Kapalı",
  fsNote:"ESC menü · P pause", howTitle:"NASIL OYNANIR", howItems:HOW_TR,
  levelsTitle:"LEVEL SEÇ", btnBackMenu:"MENÜYE DÖN", pauseTitle:"DURAKLATILDI",
  btnResume:"DEVAM ET", btnRestart:"YENİDEN BAŞLAT", btnMainMenu:"ANA MENÜ", btnExit:"ÇIKIŞ",
  btnReplay:"TEKRAR OYNA", btnNext:"SONRAKİ LEVEL", btnArcadeHome:"ARCADE ANA SAYFA",
  hudScore:"SKOR", hudLevel:"LEVEL", hudLives:"CAN",
  gameOver:"OYUN BİTTİ", levelClear:"LEVEL TAMAM", congrats:"TEBRİKLER!",
  stats:"Skor: {score} · Level: {level} · En iyi: {best}",
  starsLabel:"Yıldız", locked:"Kilitli"
 },
 en:{
  genre:GENRE_EN, tagline:TAGLINE_EN, langLabel:"Language / Dil",
  btnStart:"START", btnLevels:"SELECT LEVEL", btnFullscreen:"PLAY FULLSCREEN", btnHow:"HOW TO PLAY",
  btnExitMenu:"EXIT / ARCADE", soundOn:"🔊 Sound: On", soundOff:"🔇 Sound: Off",
  fsNote:"ESC menu · P pause", howTitle:"HOW TO PLAY", howItems:HOW_EN,
  levelsTitle:"SELECT LEVEL", btnBackMenu:"BACK TO MENU", pauseTitle:"PAUSED",
  btnResume:"RESUME", btnRestart:"RESTART", btnMainMenu:"MAIN MENU", btnExit:"EXIT",
  btnReplay:"PLAY AGAIN", btnNext:"NEXT LEVEL", btnArcadeHome:"ARCADE HOME",
  hudScore:"SCORE", hudLevel:"LEVEL", hudLives:"LIVES",
  gameOver:"GAME OVER", levelClear:"LEVEL CLEAR", congrats:"CONGRATS!",
  stats:"Score: {score} · Level: {level} · Best: {best}",
  starsLabel:"Stars", locked:"Locked"
 }
};
function t(k,vars){var p=I18N[LANG]||I18N.tr,v=p[k];if(v==null)v=I18N.tr[k]!=null?I18N.tr[k]:k;if(typeof v==="string"&&vars)Object.keys(vars).forEach(function(x){v=v.replace(new RegExp("\\{"+x+"\\}","g"),String(vars[x]));});return v;}
function applyLang(lang){
 LANG=lang==="en"?"en":"tr"; document.documentElement.lang=LANG; var pack=I18N[LANG];
 document.querySelectorAll("[data-i18n]").forEach(function(n){var k=n.getAttribute("data-i18n"); if(pack[k]!=null&&typeof pack[k]==="string")n.textContent=pack[k];});
 var how=document.getElementById("howList"); if(how){how.innerHTML=""; (pack.howItems||[]).forEach(function(it){var li=document.createElement("li"); li.innerHTML=it; how.appendChild(li);});}
 document.getElementById("btnLangTr").classList.toggle("is-on",LANG==="tr");
 document.getElementById("btnLangEn").classList.toggle("is-on",LANG==="en");
 setSound(S.soundOn,true); buildLevelGrid();
}
var S={
 mode:"menu", soundOn:true, score:0, best:0, lives:3, level:1, maxUnlocked:1,
 running:false, stars:0, levelStars:{}, lastTs:0, dpr:1, W:CW, H:CH, shake:0, flash:0,
 particles:[], keys:{}, pointer:null, win:false
};
var canvas=document.getElementById("game"), ctx=canvas.getContext("2d");
var screens={menu:document.getElementById("screenMenu"),levels:document.getElementById("screenLevels"),how:document.getElementById("screenHow"),pause:document.getElementById("screenPause"),over:document.getElementById("screenOver")};
var audioCtx=null, musicTimer=null;
function ensureAudio(){if(audioCtx)return; var AC=window.AudioContext||window.webkitAudioContext; if(AC)audioCtx=new AC();}
function beep(f,d,type,g,slide){if(!S.soundOn||!audioCtx)return; var t0=audioCtx.currentTime,o=audioCtx.createOscillator(),gn=audioCtx.createGain(); o.type=type||"square"; o.frequency.setValueAtTime(f,t0); if(slide)o.frequency.exponentialRampToValueAtTime(Math.max(40,slide),t0+d); gn.gain.setValueAtTime(0.0001,t0); gn.gain.exponentialRampToValueAtTime(g||0.07,t0+0.01); gn.gain.exponentialRampToValueAtTime(0.0001,t0+d); o.connect(gn); gn.connect(audioCtx.destination); o.start(t0); o.stop(t0+d+0.02);}
function sfx(n){if(!S.soundOn)return; ensureAudio(); if(!audioCtx)return; if(n==="ui")beep(520,0.05,"square",0.04); else if(n==="ok")beep(660,0.08,"triangle",0.05); else if(n==="bad")beep(140,0.2,"sawtooth",0.08,60); else if(n==="star")beep(880,0.1,"square",0.05); else if(n==="win"){beep(523,0.1,"square",0.06); setTimeout(function(){beep(659,0.12,"square",0.06);},90); setTimeout(function(){beep(784,0.16,"square",0.06);},180);} else if(n==="coin")beep(990,0.07,"square",0.045); else if(n==="shot")beep(320,0.05,"square",0.04,180); else if(n==="move")beep(240,0.04,"square",0.03);}
function startMusic(){stopMusic(); if(!S.soundOn)return; ensureAudio(); if(!audioCtx)return; var notes=MUSIC_NOTES,i=0; function tick(){if(!S.soundOn||S.mode!=="play")return; beep(notes[i%notes.length],0.1,"triangle",0.015); i++; musicTimer=setTimeout(tick,240);} tick();}
function stopMusic(){if(musicTimer){clearTimeout(musicTimer); musicTimer=null;}}
function setSound(on,silent){S.soundOn=!!on; var lab=S.soundOn?t("soundOn"):t("soundOff"); var mb=document.getElementById("btnSoundMenu"), hb=document.getElementById("btnSoundHud"); if(mb){mb.textContent=lab; mb.classList.toggle("is-on",S.soundOn);} if(hb)hb.textContent=S.soundOn?"🔊":"🔇"; if(!silent){if(S.soundOn&&S.mode==="play")startMusic(); else stopMusic();}}
function clamp(v,a,b){return Math.max(a,Math.min(b,v));}
function rand(a,b){return a+Math.random()*(b-a);}
function showScreen(name){Object.keys(screens).forEach(function(k){screens[k].classList.toggle("is-on",k===name);}); document.getElementById("hud").classList.toggle("is-on", name===null && S.mode==="play");}
function updateHud(){document.getElementById("hudScore").textContent=String(S.score|0); document.getElementById("hudLevel").textContent=String(S.level); document.getElementById("hudLives").textContent=String(S.lives); if(typeof onHudExtra==="function")onHudExtra();}
function showToast(title,text){var el=document.getElementById("toast"); document.getElementById("toastTitle").textContent=title; document.getElementById("toastText").textContent=text||""; el.classList.add("is-on"); clearTimeout(showToast._t); showToast._t=setTimeout(function(){el.classList.remove("is-on");},1100);}
function burst(x,y,col,n,spd){for(var i=0;i<n;i++){var a=Math.random()*Math.PI*2,s=rand(spd*0.3,spd); S.particles.push({x:x,y:y,vx:Math.cos(a)*s,vy:Math.sin(a)*s,life:rand(0.2,0.6),max:0.6,r:rand(1.2,3),color:col});}}
function updateParticles(dt){for(var i=S.particles.length-1;i>=0;i--){var p=S.particles[i]; p.life-=dt; p.x+=p.vx*dt; p.y+=p.vy*dt; p.vy+=50*dt; if(p.life<=0)S.particles.splice(i,1);}}
function drawParticles(){S.particles.forEach(function(p){ctx.globalAlpha=Math.max(0,p.life/(p.max||0.5)); ctx.fillStyle=p.color; ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,Math.PI*2); ctx.fill();}); ctx.globalAlpha=1;}
function palette(level){var pal=[
 ["#0b1535","#22d3ee","#a78bfa"],["#1a0b2e","#f472b6","#c084fc"],["#052e1a","#4ade80","#2dd4bf"],
 ["#2a0a0a","#fb7185","#fbbf24"],["#0c1a2e","#38bdf8","#818cf8"],["#1e1b4b","#e879f9","#67e8f9"],
 ["#0f172a","#f59e0b","#ef4444"],["#042f2e","#2dd4bf","#a3e635"],["#1c1917","#f97316","#fde047"],
 ["#172554","#60a5fa","#c4b5fd"],["#3b0764","#d946ef","#22d3ee"],["#450a0a","#f43f5e","#fbbf24"]
]; return pal[(level-1)%pal.length];}
function isFs(){return !!(document.fullscreenElement||document.webkitFullscreenElement);}
function enterFs(){var el=document.documentElement,r=el.requestFullscreen||el.webkitRequestFullscreen; if(r)r.call(el);}
function exitFs(){var e=document.exitFullscreen||document.webkitExitFullscreen; if(e&&isFs())e.call(document);}
function goMenu(){S.mode="menu"; S.running=false; stopMusic(); showScreen("menu");}
function pauseGame(){if(S.mode!=="play")return; S.mode="pause"; S.running=false; stopMusic(); showScreen("pause");}
function resumeGame(){if(S.mode!=="pause")return; S.mode="play"; S.running=true; showScreen(null); startMusic();}
function calcStars(score, target){if(score>=target*1.4)return 3; if(score>=target)return 2; return 1;}
function levelComplete(bonus){
 S.running=false; S.win=true; S.mode="over"; stopMusic(); sfx("win");
 var target=LEVEL_TARGET(S.level); S.stars=calcStars(S.score+ (bonus||0), target);
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
 S.level=n; S.score=0; S.lives=3; S.win=false; S.particles=[]; S.shake=0; S.flash=0;
 if(typeof gameReset==="function")gameReset();
 S.mode="play"; S.running=true; showScreen(null); updateHud(); startMusic(); sfx("ok");
 showToast("LEVEL "+n,"");
}
function resize(){S.W=CW; S.H=CH; S.dpr=Math.min(window.devicePixelRatio||1,2); canvas.width=Math.round(S.W*S.dpr); canvas.height=Math.round(S.H*S.dpr);}
function canvasPos(e){var rect=canvas.getBoundingClientRect(), scale=Math.min(rect.width/S.W,rect.height/S.H); var ox=rect.left+(rect.width-S.W*scale)/2, oy=rect.top+(rect.height-S.H*scale)/2; var cx=e.clientX!=null?e.clientX:(e.touches&&e.touches[0]?e.touches[0].clientX:0); var cy=e.clientY!=null?e.clientY:(e.touches&&e.touches[0]?e.touches[0].clientY:0); return {x:(cx-ox)/scale, y:(cy-oy)/scale};}
function loop(ts){if(!S.lastTs)S.lastTs=ts; var dt=Math.min(0.033,(ts-S.lastTs)/1000); S.lastTs=ts; if(S.mode==="play"&&S.running){if(typeof gameUpdate==="function")gameUpdate(dt); updateParticles(dt); if(S.shake>0)S.shake=Math.max(0,S.shake-dt*8); if(S.flash>0)S.flash=Math.max(0,S.flash-dt*3);} drawFrame(); requestAnimationFrame(loop);}
function drawFrame(){
 var dpr=S.dpr; ctx.setTransform(dpr,0,0,dpr,0,0); ctx.clearRect(0,0,S.W,S.H);
 var sx=0,sy=0; if(S.shake>0){sx=(Math.random()-0.5)*S.shake*12; sy=(Math.random()-0.5)*S.shake*12;}
 ctx.save(); ctx.translate(sx,sy);
 var pal=palette(S.level);
 var g=ctx.createLinearGradient(0,0,0,S.H); g.addColorStop(0,pal[0]); g.addColorStop(1,"#03060f"); ctx.fillStyle=g; ctx.fillRect(-10,-10,S.W+20,S.H+20);
 if(typeof gameDraw==="function")gameDraw(ctx,pal);
 drawParticles();
 // scanlines
 ctx.fillStyle="rgba(0,0,0,0.07)"; for(var y=0;y<S.H;y+=3)ctx.fillRect(0,y,S.W,1);
 if(S.flash>0){ctx.fillStyle="rgba(248,113,113,"+(S.flash*0.3)+")"; ctx.fillRect(0,0,S.W,S.H);}
 ctx.restore();
}
function leaveArcade(){stopMusic(); if(isFs())exitFs(); location.href="/mini-oyunlar/";}
function handleExit(){if(S.mode==="play"){S.mode="pause"; S.running=false; stopMusic();} if(isFs())exitFs(); goMenu();}
window.addEventListener("keydown",function(e){
 if(e.code==="Escape"){e.preventDefault(); handleExit(); return;}
 if(e.code==="KeyP"){e.preventDefault(); if(S.mode==="play")pauseGame(); else if(S.mode==="pause")resumeGame();}
 if(typeof onKeyDown==="function")onKeyDown(e);
});
window.addEventListener("keyup",function(e){if(typeof onKeyUp==="function")onKeyUp(e);});
canvas.addEventListener("mousedown",function(e){S.pointer=canvasPos(e); if(typeof onPointer==="function")onPointer(S.pointer,"down");});
canvas.addEventListener("mousemove",function(e){S.pointer=canvasPos(e); if(typeof onPointer==="function")onPointer(S.pointer,"move");});
canvas.addEventListener("mouseup",function(e){S.pointer=canvasPos(e); if(typeof onPointer==="function")onPointer(S.pointer,"up");});
canvas.addEventListener("touchstart",function(e){if(!e.touches[0])return; S.pointer=canvasPos(e.touches[0]); if(typeof onPointer==="function")onPointer(S.pointer,"down");},{passive:true});
canvas.addEventListener("touchmove",function(e){if(!e.touches[0])return; S.pointer=canvasPos(e.touches[0]); if(typeof onPointer==="function")onPointer(S.pointer,"move");},{passive:true});
canvas.addEventListener("touchend",function(e){var t=e.changedTouches&&e.changedTouches[0]; if(t)S.pointer=canvasPos(t); if(typeof onPointer==="function")onPointer(S.pointer||{x:0,y:0},"up");},{passive:true});
document.getElementById("btnStart").onclick=function(){ensureAudio(); startLevel(1);};
document.getElementById("btnFullscreen").onclick=function(){ensureAudio(); enterFs(); startLevel(1);};
document.getElementById("btnLevels").onclick=function(){S.mode="levels"; buildLevelGrid(); showScreen("levels"); sfx("ui");};
document.getElementById("btnLevelsBack").onclick=function(){goMenu();};
document.getElementById("btnHow").onclick=function(){S.mode="how"; showScreen("how"); sfx("ui");};
document.getElementById("btnHowBack").onclick=function(){goMenu();};
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
// ---- GAME LOGIC BELOW ----
"""


GAMES = {}

# ========== 1 SNAKE REWIND ==========
GAMES["snake-rewind"] = {
    "title": "Snake Rewind",
    "slug": "snake-rewind",
    "genre_tr": "Arcade · Yılan",
    "genre_en": "Arcade · Snake",
    "tagline_tr": "Klasik ızgara yılan · geri sarma power-up · 12 level",
    "tagline_en": "Classic grid snake · rewind power-up · 12 levels",
    "desc": "Snake Rewind: ızgara yılan, hedef uzunluk, geri sarma ve seviye sistemi.",
    "cw": 480, "ch": 640,
    "how_tr": [
        "<b>Kontrol:</b> ←→↑↓ / WASD · kaydır",
        "<b>Hedef:</b> level başına yemeğe ulaş (uzunluk artar)",
        "<b>R:</b> geri sar (son 3 adım) — sınırlı kullanım",
        "<b>Engel:</b> duvar ve kendi kuyruğuna çarpma can düşürür",
        "<b>12 level:</b> hız ve harita engelleri artar"
    ],
    "how_en": [
        "<b>Controls:</b> arrows / WASD · swipe",
        "<b>Goal:</b> eat target food count per level",
        "<b>R:</b> rewind last 3 steps — limited uses",
        "<b>Hazards:</b> walls and self-collision cost a life",
        "<b>12 levels:</b> speed and obstacles rise"
    ],
    "music": "[196,220,247,262,294,262,247,220]",
    "logic": r"""
var CELL=20, COLS, ROWS, snake, dir, nextDir, food, eatGoal, eaten, moveAcc, moveEvery, rewinds, history, walls;
function LEVEL_TARGET(lv){return 80+lv*40;}
function gameReset(){
 COLS=Math.floor(S.W/CELL); ROWS=Math.floor(S.H/CELL);
 var cx=(COLS/2)|0, cy=(ROWS/2)|0;
 snake=[{x:cx,y:cy},{x:cx-1,y:cy},{x:cx-2,y:cy}]; dir={x:1,y:0}; nextDir={x:1,y:0};
 eatGoal=6+S.level; eaten=0; moveAcc=0; moveEvery=Math.max(0.07,0.18-S.level*0.008);
 rewinds=2+Math.floor(S.level/4); history=[]; walls=[];
 // obstacles from level 3
 if(S.level>=3){
  for(var i=0;i<S.level+2;i++){
   walls.push({x:2+((i*5)% (COLS-4)), y:2+((i*3)%(ROWS-4))});
  }
 }
 placeFood(); onHudExtra();
}
function placeFood(){
 for(var t=0;t<200;t++){
  var f={x:(Math.random()*COLS)|0,y:(Math.random()*ROWS)|0};
  if(!snake.some(function(s){return s.x===f.x&&s.y===f.y;}) && !walls.some(function(w){return w.x===f.x&&w.y===f.y;})){food=f; return;}
 }
 food={x:1,y:1};
}
function onHudExtra(){document.getElementById("hudExtraLabel").textContent="HEDEF"; document.getElementById("hudExtra").textContent=eaten+"/"+eatGoal+" · R"+rewinds;}
function tryRewind(){
 if(rewinds<=0||history.length<1)return;
 rewinds--; var snap=history.pop(); snake=snap.snake.map(function(p){return {x:p.x,y:p.y};}); dir=snap.dir; nextDir={x:dir.x,y:dir.y}; sfx("ok"); onHudExtra();
}
function gameUpdate(dt){
 moveAcc+=dt;
 if(S.keys.left&&dir.x!==1)nextDir={x:-1,y:0};
 if(S.keys.right&&dir.x!==-1)nextDir={x:1,y:0};
 if(S.keys.up&&dir.y!==1)nextDir={x:0,y:-1};
 if(S.keys.down&&dir.y!==-1)nextDir={x:0,y:1};
 while(moveAcc>=moveEvery){
  moveAcc-=moveEvery;
  history.push({snake:snake.map(function(p){return {x:p.x,y:p.y};}), dir:{x:dir.x,y:dir.y}});
  if(history.length>40)history.shift();
  dir=nextDir;
  var h={x:snake[0].x+dir.x, y:snake[0].y+dir.y};
  if(h.x<0||h.y<0||h.x>=COLS||h.y>=ROWS || snake.some(function(s){return s.x===h.x&&s.y===h.y;}) || walls.some(function(w){return w.x===h.x&&w.y===h.y;})){
   S.lives--; S.shake=0.5; S.flash=0.35; sfx("bad"); updateHud();
   if(S.lives<=0){gameOver(); return;}
   // reset snake position soft
   var cx=(COLS/2)|0, cy=(ROWS/2)|0; snake=[{x:cx,y:cy},{x:cx-1,y:cy},{x:cx-2,y:cy}]; dir={x:1,y:0}; nextDir={x:1,y:0}; continue;
  }
  snake.unshift(h);
  if(h.x===food.x&&h.y===food.y){
   eaten++; S.score+=10+S.level*2; sfx("coin"); burst(food.x*CELL+CELL/2,food.y*CELL+CELL/2,"#fbbf24",10,160); placeFood(); onHudExtra(); updateHud();
   if(eaten>=eatGoal){S.score+=50*S.level; levelComplete(50*S.level); return;}
  } else snake.pop();
 }
}
function gameDraw(ctx,pal){
 // grid
 ctx.strokeStyle="rgba(255,255,255,0.04)"; ctx.lineWidth=1;
 for(var x=0;x<=COLS;x++){ctx.beginPath();ctx.moveTo(x*CELL,0);ctx.lineTo(x*CELL,ROWS*CELL);ctx.stroke();}
 for(var y=0;y<=ROWS;y++){ctx.beginPath();ctx.moveTo(0,y*CELL);ctx.lineTo(COLS*CELL,y*CELL);ctx.stroke();}
 walls.forEach(function(w){ctx.fillStyle=pal[2]; ctx.fillRect(w.x*CELL+1,w.y*CELL+1,CELL-2,CELL-2);});
 // food
 ctx.fillStyle="#fbbf24"; ctx.shadowColor="#fbbf24"; ctx.shadowBlur=10;
 ctx.beginPath(); ctx.arc(food.x*CELL+CELL/2,food.y*CELL+CELL/2,CELL*0.32,0,Math.PI*2); ctx.fill(); ctx.shadowBlur=0;
 snake.forEach(function(s,i){
  var t=i/snake.length; ctx.fillStyle=i===0?pal[1]:pal[2];
  ctx.fillRect(s.x*CELL+2,s.y*CELL+2,CELL-4,CELL-4);
  if(i===0){ctx.fillStyle="#0f172a"; ctx.fillRect(s.x*CELL+6,s.y*CELL+6,3,3); ctx.fillRect(s.x*CELL+11,s.y*CELL+6,3,3);}
 });
}
function onKeyDown(e){
 if(e.code==="ArrowLeft"||e.code==="KeyA"){S.keys.left=true; e.preventDefault();}
 if(e.code==="ArrowRight"||e.code==="KeyD"){S.keys.right=true; e.preventDefault();}
 if(e.code==="ArrowUp"||e.code==="KeyW"){S.keys.up=true; e.preventDefault();}
 if(e.code==="ArrowDown"||e.code==="KeyS"){S.keys.down=true; e.preventDefault();}
 if(e.code==="KeyR")tryRewind();
}
function onKeyUp(e){
 if(e.code==="ArrowLeft"||e.code==="KeyA")S.keys.left=false;
 if(e.code==="ArrowRight"||e.code==="KeyD")S.keys.right=false;
 if(e.code==="ArrowUp"||e.code==="KeyW")S.keys.up=false;
 if(e.code==="ArrowDown"||e.code==="KeyS")S.keys.down=false;
}
var swipe0=null;
function onPointer(p,type){
 if(type==="down")swipe0={x:p.x,y:p.y};
 if(type==="up"&&swipe0){
  var dx=p.x-swipe0.x, dy=p.y-swipe0.y;
  if(Math.abs(dx)>20||Math.abs(dy)>20){
   if(Math.abs(dx)>Math.abs(dy)){if(dx>0&&dir.x!==-1)nextDir={x:1,y:0}; if(dx<0&&dir.x!==1)nextDir={x:-1,y:0};}
   else {if(dy>0&&dir.y!==-1)nextDir={x:0,y:1}; if(dy<0&&dir.y!==1)nextDir={x:0,y:-1};}
  }
  swipe0=null;
 }
}
"""
}

# ========== 2 CASCADE BLOCKS ==========
GAMES["cascade-blocks"] = {
    "title": "Cascade Blocks",
    "slug": "cascade-blocks",
    "genre_tr": "Bulmaca · Blok",
    "genre_en": "Puzzle · Blocks",
    "tagline_tr": "Aynı renk gruplarını patlat · zincir reaksiyon · 12 level",
    "tagline_en": "Pop color clusters · chain reactions · 12 levels",
    "desc": "Cascade Blocks: renkli blok gruplarını patlat, zincir bonus, seviye hedefleri.",
    "cw": 420, "ch": 720,
    "how_tr": [
        "<b>Kontrol:</b> tıkla / dokun — en az 2 aynı renk grubu",
        "<b>Hedef:</b> level puan hedefine ulaş",
        "<b>Zincir:</b> peş peşe patlatmalar ekstra puan",
        "<b>Boş sütunlar</b> birleşir, üstten yeni bloklar iner",
        "<b>12 level:</b> grid ve renk sayısı artar"
    ],
    "how_en": [
        "<b>Controls:</b> tap a group of 2+ same colors",
        "<b>Goal:</b> reach the level score target",
        "<b>Chains:</b> consecutive pops give bonus points",
        "<b>Empty columns</b> collapse; new blocks fall in",
        "<b>12 levels:</b> grid size and colors increase"
    ],
    "music": "[262,294,330,349,392,349,330,294]",
    "logic": r"""
var COLS, ROWS, grid, colors, chain, moves;
var PAL=["#22d3ee","#a78bfa","#f472b6","#fbbf24","#4ade80","#fb7185"];
function LEVEL_TARGET(lv){return 400+lv*180;}
function gameReset(){
 COLS=6+Math.min(2,(S.level/4)|0); ROWS=9+Math.min(3,(S.level/3)|0);
 colors=Math.min(6,3+((S.level-1)/2)|0); chain=0; moves=0;
 grid=[]; for(var y=0;y<ROWS;y++){grid[y]=[]; for(var x=0;x<COLS;x++)grid[y][x]=(Math.random()*colors)|0;}
 onHudExtra();
}
function onHudExtra(){document.getElementById("hudExtraLabel").textContent="HEDEF"; document.getElementById("hudExtra").textContent=String(LEVEL_TARGET(S.level));}
function cellAt(p){var pad=16, bw=(S.W-pad*2)/COLS, bh=(S.H-120-pad)/ROWS; var x=((p.x-pad)/bw)|0, y=((p.y-80)/bh)|0; if(x<0||y<0||x>=COLS||y>=ROWS)return null; return {x:x,y:y,bw:bw,bh:bh,pad:pad};}
function flood(x,y,c,seen){
 if(x<0||y<0||x>=COLS||y>=ROWS||grid[y][x]!==c||seen[y+"_"+x])return [];
 seen[y+"_"+x]=1; var out=[{x:x,y:y}];
 [[1,0],[-1,0],[0,1],[0,-1]].forEach(function(d){out=out.concat(flood(x+d[0],y+d[1],c,seen));});
 return out;
}
function gravity(){
 for(var x=0;x<COLS;x++){
  var stack=[]; for(var y=ROWS-1;y>=0;y--)if(grid[y][x]!=null)stack.push(grid[y][x]);
  for(var y2=ROWS-1;y2>=0;y2--)grid[y2][x]=stack[ROWS-1-y2]!=null?stack[ROWS-1-y2]:null;
 }
 // compact columns left
 var cols=[]; for(var x=0;x<COLS;x++){var empty=true; for(var y=0;y<ROWS;y++)if(grid[y][x]!=null)empty=false; if(!empty){var col=[]; for(var y=0;y<ROWS;y++)col.push(grid[y][x]); cols.push(col);}}
 while(cols.length<COLS){var nc=[]; for(var y=0;y<ROWS;y++)nc.push((Math.random()*colors)|0); cols.push(nc);}
 for(var x=0;x<COLS;x++)for(var y=0;y<ROWS;y++){
  if(x<cols.length)grid[y][x]=cols[x][y];
  if(grid[y][x]==null)grid[y][x]=(Math.random()*colors)|0;
 }
}
function gameUpdate(dt){}
function gameDraw(ctx,pal){
 var pad=16, bw=(S.W-pad*2)/COLS, bh=(S.H-120-pad)/ROWS;
 ctx.fillStyle="rgba(0,0,0,0.25)"; ctx.fillRect(pad-4,80-4,S.W-pad*2+8,ROWS*bh+8);
 for(var y=0;y<ROWS;y++)for(var x=0;x<COLS;x++){
  var c=grid[y][x]; if(c==null)continue;
  ctx.fillStyle=PAL[c%PAL.length]; ctx.shadowColor=PAL[c%PAL.length]; ctx.shadowBlur=8;
  var rx=pad+x*bw+2, ry=80+y*bh+2;
  ctx.beginPath(); roundR(ctx,rx,ry,bw-4,bh-4,6); ctx.fill();
 }
 ctx.shadowBlur=0;
 ctx.fillStyle="#e2e8f0"; ctx.font="bold 14px Inter,sans-serif"; ctx.textAlign="center";
 ctx.fillText("Level "+S.level+" · "+S.score+" / "+LEVEL_TARGET(S.level), S.W/2, 50);
}
function roundR(ctx,x,y,w,h,r){ctx.moveTo(x+r,y);ctx.arcTo(x+w,y,x+w,y+h,r);ctx.arcTo(x+w,y+h,x,y+h,r);ctx.arcTo(x,y+h,x,y,r);ctx.arcTo(x,y,x+w,y,r);ctx.closePath();}
function onPointer(p,type){
 if(type!=="down"||S.mode!=="play")return;
 var c=cellAt(p); if(!c)return;
 var col=grid[c.y][c.x]; if(col==null)return;
 var group=flood(c.x,c.y,col,{});
 if(group.length<2){sfx("bad"); chain=0; return;}
 group.forEach(function(g){grid[g.y][g.x]=null; burst(16+g.x*((S.W-32)/COLS)+(S.W-32)/(COLS*2),80+g.y*((S.H-120)/ROWS),PAL[col%PAL.length],6,120);});
 chain++; moves++;
 var pts=group.length*group.length*5*chain*(1+S.level*0.05);
 S.score=(S.score+pts)|0; sfx("coin"); gravity(); updateHud(); onHudExtra();
 if(S.score>=LEVEL_TARGET(S.level))levelComplete(100);
}
function onKeyDown(e){}
function onKeyUp(e){}
"""
}

# ========== 3 NUMBER FUSION ==========
GAMES["number-fusion"] = {
    "title": "Number Fusion",
    "slug": "number-fusion",
    "genre_tr": "Bulmaca · Sayı",
    "genre_en": "Puzzle · Numbers",
    "tagline_tr": "Kaydır, birleştir, hedef değere ulaş · 12 level",
    "tagline_en": "Swipe, merge, hit the target tile · 12 levels",
    "desc": "Number Fusion: ızgara üzerinde sayıları birleştirerek hedef karta ulaş.",
    "cw": 480, "ch": 640,
    "how_tr": [
        "<b>Kontrol:</b> ok tuşları / WASD / kaydır",
        "<b>Birleştir:</b> aynı sayılar birleşir (2+2=4…)",
        "<b>Hedef:</b> level hedef sayısını oluştur",
        "<b>Can:</b> tahta dolunca can kaybı / sıfırlama",
        "<b>12 level:</b> hedef değer katlanır"
    ],
    "how_en": [
        "<b>Controls:</b> arrows / WASD / swipe",
        "<b>Merge:</b> equal numbers combine (2+2=4…)",
        "<b>Goal:</b> create the target number",
        "<b>Lives:</b> full board costs a life / reset",
        "<b>12 levels:</b> target doubles progressively"
    ],
    "music": "[330,294,262,294,330,330,330,294]",
    "logic": r"""
var N=4, board, target, moved;
function LEVEL_TARGET(lv){return 200+lv*100;}
function gameReset(){board=empty(); spawn(); spawn(); target=Math.pow(2,4+Math.min(7,S.level)); // 16..2048+
 moved=false; onHudExtra();}
function empty(){var b=[]; for(var y=0;y<N;y++){b[y]=[]; for(var x=0;x<N;x++)b[y][x]=0;} return b;}
function spawn(){var free=[]; for(var y=0;y<N;y++)for(var x=0;x<N;x++)if(!board[y][x])free.push({x:x,y:y}); if(!free.length)return false; var p=free[(Math.random()*free.length)|0]; board[p.y][p.x]=Math.random()<0.9?2:4; return true;}
function onHudExtra(){document.getElementById("hudExtraLabel").textContent="HEDEF"; document.getElementById("hudExtra").textContent=String(target);}
function slideLine(line){
 var arr=line.filter(function(v){return v;}); var out=[], scoreAdd=0,i=0;
 while(i<arr.length){
  if(i+1<arr.length && arr[i]===arr[i+1]){var v=arr[i]*2; out.push(v); scoreAdd+=v; i+=2;}
  else {out.push(arr[i]); i++;}
 }
 while(out.length<N)out.push(0);
 return {line:out, score:scoreAdd, changed: out.some(function(v,i){return v!==line[i];})};
}
function move(dir){
 // dir: 0L 1R 2U 3D
 var changed=false, add=0, maxTile=0;
 var nb=empty();
 if(dir===0||dir===1){
  for(var y=0;y<N;y++){
   var line=[]; for(var x=0;x<N;x++)line.push(board[y][x]);
   if(dir===1)line.reverse();
   var r=slideLine(line); if(dir===1)r.line.reverse();
   for(var x=0;x<N;x++){nb[y][x]=r.line[x]; maxTile=Math.max(maxTile,r.line[x]);}
   if(r.changed)changed=true; add+=r.score;
  }
 } else {
  for(var x=0;x<N;x++){
   var line=[]; for(var y=0;y<N;y++)line.push(board[y][x]);
   if(dir===3)line.reverse();
   var r=slideLine(line); if(dir===3)r.line.reverse();
   for(var y=0;y<N;y++){nb[y][x]=r.line[y]; maxTile=Math.max(maxTile,r.line[y]);}
   if(r.changed)changed=true; add+=r.score;
  }
 }
 if(!changed)return;
 board=nb; S.score+=add; sfx(add?"coin":"move"); spawn();
 // check max
 for(var y=0;y<N;y++)for(var x=0;x<N;x++)maxTile=Math.max(maxTile,board[y][x]);
 updateHud(); onHudExtra();
 if(maxTile>=target){S.score+=target; levelComplete(target); return;}
 // stuck?
 if(!canMove()){S.lives--; S.shake=0.4; sfx("bad"); updateHud(); if(S.lives<=0)gameOver(); else {board=empty(); spawn(); spawn();}}
}
function canMove(){
 for(var y=0;y<N;y++)for(var x=0;x<N;x++){
  if(!board[y][x])return true;
  if(x+1<N&&board[y][x]===board[y][x+1])return true;
  if(y+1<N&&board[y][x]===board[y+1][x])return true;
 }
 return false;
}
function gameUpdate(dt){}
function tileColor(v){var map={2:"#67e8f9",4:"#22d3ee",8:"#818cf8",16:"#a78bfa",32:"#c084fc",64:"#f472b6",128:"#fb7185",256:"#fbbf24",512:"#f59e0b",1024:"#4ade80",2048:"#f0abfc"}; return map[v]||"#e2e8f0";}
function gameDraw(ctx,pal){
 var pad=24, size=Math.min(S.W,S.H-100)-pad*2, cell=size/N, ox=(S.W-size)/2, oy=90;
 ctx.fillStyle="rgba(0,0,0,0.3)"; roundFill(ctx,ox-8,oy-8,size+16,size+16,12);
 for(var y=0;y<N;y++)for(var x=0;x<N;x++){
  var v=board[y][x]; var rx=ox+x*cell+4, ry=oy+y*cell+4, rw=cell-8, rh=cell-8;
  ctx.fillStyle=v?tileColor(v):"rgba(255,255,255,0.06)";
  if(v){ctx.shadowColor=tileColor(v); ctx.shadowBlur=12;}
  roundFill(ctx,rx,ry,rw,rh,10); ctx.shadowBlur=0;
  if(v){ctx.fillStyle="#0f172a"; ctx.font="bold "+Math.floor(cell*0.28)+"px Inter,sans-serif"; ctx.textAlign="center"; ctx.textBaseline="middle"; ctx.fillText(String(v),rx+rw/2,ry+rh/2);}
 }
 ctx.fillStyle="#e2e8f0"; ctx.font="bold 15px Inter,sans-serif"; ctx.textAlign="center";
 ctx.fillText("Hedef / Target: "+target, S.W/2, 50);
}
function roundFill(ctx,x,y,w,h,r){ctx.beginPath(); ctx.moveTo(x+r,y); ctx.arcTo(x+w,y,x+w,y+h,r); ctx.arcTo(x+w,y+h,x,y+h,r); ctx.arcTo(x,y+h,x,y,r); ctx.arcTo(x,y,x+w,y,r); ctx.closePath(); ctx.fill();}
function onKeyDown(e){
 if(e.code==="ArrowLeft"||e.code==="KeyA"){e.preventDefault(); move(0);}
 if(e.code==="ArrowRight"||e.code==="KeyD"){e.preventDefault(); move(1);}
 if(e.code==="ArrowUp"||e.code==="KeyW"){e.preventDefault(); move(2);}
 if(e.code==="ArrowDown"||e.code==="KeyS"){e.preventDefault(); move(3);}
}
function onKeyUp(e){}
var sw0=null;
function onPointer(p,type){
 if(type==="down")sw0={x:p.x,y:p.y};
 if(type==="up"&&sw0){var dx=p.x-sw0.x,dy=p.y-sw0.y; if(Math.abs(dx)>30||Math.abs(dy)>30){if(Math.abs(dx)>Math.abs(dy))move(dx>0?1:0); else move(dy>0?3:2);} sw0=null;}
}
"""
}

# ========== 4 PIXEL GLIDER ==========
GAMES["pixel-glider"] = {
    "title": "Pixel Glider",
    "slug": "pixel-glider",
    "genre_tr": "Aksiyon · Uçuş",
    "genre_en": "Action · Flyer",
    "tagline_tr": "Tek tuş itki · neon drone · tünel engelleri · 12 level",
    "tagline_en": "One-tap thruster · neon drone · tunnel gates · 12 levels",
    "desc": "Pixel Glider: tek tuşla yükselen drone ile engel tünellerini geç.",
    "cw": 400, "ch": 640,
    "how_tr": [
        "<b>Kontrol:</b> Space / tık / dokun = itki",
        "<b>Hedef:</b> level mesafesini tamamla",
        "<b>Engel:</b> üst-alt kapılara çarpma can düşürür",
        "<b>Skor:</b> mesafe + geçilen kapılar",
        "<b>12 level:</b> hız ve daralma artar"
    ],
    "how_en": [
        "<b>Controls:</b> Space / click / tap = thrust",
        "<b>Goal:</b> complete level distance",
        "<b>Hazards:</b> hitting gates costs a life",
        "<b>Score:</b> distance + gates cleared",
        "<b>12 levels:</b> speed and gaps tighten"
    ],
    "music": "[392,349,330,294,330,349,392,440]",
    "logic": r"""
var drone, vy, gates, dist, goalDist, speed, gap, spawnX, aliveTimer;
function LEVEL_TARGET(lv){return 300+lv*80;}
function gameReset(){
 drone={x:S.W*0.28,y:S.H*0.5,r:12}; vy=0; gates=[]; dist=0;
 goalDist=900+S.level*220; speed=160+S.level*14; gap=Math.max(100,180-S.level*5);
 spawnX=S.W+40; aliveTimer=0; for(var i=0;i<3;i++)addGate(S.W+120+i*220); onHudExtra();
}
function addGate(x){var mid=rand(gap*0.6,S.H-gap*0.6); gates.push({x:x,mid:mid,w:52,passed:false});}
function onHudExtra(){document.getElementById("hudExtraLabel").textContent="MESAFE"; document.getElementById("hudExtra").textContent=(dist|0)+"/"+(goalDist|0);}
function thrust(){if(S.mode!=="play")return; vy=-260; sfx("move");}
function gameUpdate(dt){
 vy+=780*dt; drone.y+=vy*dt;
 if(drone.y<drone.r||drone.y>S.H-drone.r){hit(); return;}
 dist+=speed*dt*0.35; S.score+=speed*dt*0.08; spawnX-=speed*dt;
 gates.forEach(function(g){g.x-=speed*dt;});
 if(gates.length&&gates[gates.length-1].x<S.W-200)addGate(gates[gates.length-1].x+220+S.level*2);
 gates=gates.filter(function(g){return g.x>-80;});
 for(var i=0;i<gates.length;i++){
  var g=gates[i], topH=g.mid-gap/2, botY=g.mid+gap/2;
  if(drone.x+drone.r>g.x && drone.x-drone.r<g.x+g.w){
   if(drone.y-drone.r<topH || drone.y+drone.r>botY){hit(); return;}
  }
  if(!g.passed && g.x+g.w<drone.x){g.passed=true; S.score+=25; sfx("coin"); burst(drone.x,drone.y,"#67e8f9",8,140);}
 }
 updateHud(); onHudExtra();
 if(dist>=goalDist)levelComplete(150);
}
function hit(){S.lives--; S.shake=0.55; S.flash=0.4; sfx("bad"); burst(drone.x,drone.y,"#fb7185",16,200); updateHud();
 if(S.lives<=0)gameOver(); else {drone.y=S.H*0.5; vy=0; gates.forEach(function(g){if(g.x<drone.x+80)g.x+=200;});}
}
function gameDraw(ctx,pal){
 // parallax stars
 for(var i=0;i<30;i++){ctx.fillStyle="rgba(255,255,255,0.15)"; ctx.fillRect((i*47+dist*0.2)%S.W, (i*89)%S.H, 2,2);}
 gates.forEach(function(g){
  var topH=g.mid-gap/2, botY=g.mid+gap/2;
  ctx.fillStyle=pal[2]; ctx.shadowColor=pal[1]; ctx.shadowBlur=12;
  ctx.fillRect(g.x,0,g.w,topH); ctx.fillRect(g.x,botY,g.w,S.H-botY);
  ctx.shadowBlur=0; ctx.fillStyle=pal[1]; ctx.fillRect(g.x,topH-6,g.w,6); ctx.fillRect(g.x,botY,g.w,6);
 });
 // drone (not a bird)
 ctx.save(); ctx.translate(drone.x,drone.y); ctx.rotate(Math.atan2(vy,220)*0.5);
 ctx.fillStyle=pal[1]; ctx.shadowColor=pal[1]; ctx.shadowBlur=14;
 ctx.beginPath(); ctx.moveTo(14,0); ctx.lineTo(-10,-9); ctx.lineTo(-6,0); ctx.lineTo(-10,9); ctx.closePath(); ctx.fill();
 ctx.fillStyle="#f472b6"; ctx.fillRect(-14,-2,6,4); // thruster
 ctx.restore(); ctx.shadowBlur=0;
}
function onKeyDown(e){if(e.code==="Space"||e.code==="ArrowUp"||e.code==="KeyW"){e.preventDefault(); thrust();}}
function onKeyUp(e){}
function onPointer(p,type){if(type==="down")thrust();}
"""
}

# ========== 5 GALAXY DEFENDER ==========
GAMES["galaxy-defender"] = {
    "title": "Galaxy Defender",
    "slug": "galaxy-defender",
    "genre_tr": "Aksiyon · Uzay",
    "genre_en": "Action · Space",
    "tagline_tr": "Neon gemi · dalga dalga işgalciler · 12 level",
    "tagline_en": "Neon ship · wave invaders · 12 levels",
    "desc": "Galaxy Defender: özgün uzay gemisiyle dalgaları temizle.",
    "cw": 480, "ch": 720,
    "how_tr": [
        "<b>Hareket:</b> ←→ / A D / fare / dokun",
        "<b>Ateş:</b> Space / tık",
        "<b>Hedef:</b> level dalgasındaki tüm düşmanları yok et",
        "<b>Can:</b> düşman mermisi veya çarpışma",
        "<b>12 level:</b> daha hızlı ve kalabalık dalgalar"
    ],
    "how_en": [
        "<b>Move:</b> arrows / A D / mouse / touch",
        "<b>Fire:</b> Space / tap",
        "<b>Goal:</b> clear all enemies in the wave",
        "<b>Lives:</b> enemy shots or collisions",
        "<b>12 levels:</b> denser, faster waves"
    ],
    "music": "[220,247,262,294,330,294,262,247]",
    "logic": r"""
var ship, bullets, enemies, eBullets, fireCd, waveLeft;
function LEVEL_TARGET(lv){return 100+lv*80;}
function gameReset(){
 ship={x:S.W/2,y:S.H-70,w:36,h:22}; bullets=[]; enemies=[]; eBullets=[]; fireCd=0;
 var rows=3+Math.min(3,(S.level/3)|0), cols=5+Math.min(3,(S.level/4)|0);
 for(var r=0;r<rows;r++)for(var c=0;c<cols;c++){
  enemies.push({x:50+c*((S.W-100)/(cols-1||1)), y:70+r*42, hp:1+((S.level>6)?1:0), t:Math.random()*Math.PI*2, type:r%3});
 }
 waveLeft=enemies.length; onHudExtra();
}
function onHudExtra(){document.getElementById("hudExtraLabel").textContent="DÜŞMAN"; document.getElementById("hudExtra").textContent=String(enemies.length);}
function fire(){if(fireCd>0)return; fireCd=0.22; bullets.push({x:ship.x,y:ship.y-16,vy:-420}); sfx("shot");}
function gameUpdate(dt){
 fireCd=Math.max(0,fireCd-dt);
 if(S.keys.left)ship.x-=280*dt; if(S.keys.right)ship.x+=280*dt;
 if(S.pointer&&S.pointer.y>S.H*0.5)ship.x+=(S.pointer.x-ship.x)*Math.min(1,dt*10);
 ship.x=clamp(ship.x,24,S.W-24);
 if(S.keys.fire)fire();
 bullets.forEach(function(b){b.y+=b.vy*dt;}); bullets=bullets.filter(function(b){return b.y>-20;});
 eBullets.forEach(function(b){b.y+=b.vy*dt;}); eBullets=eBullets.filter(function(b){return b.y<S.H+20;});
 var spd=40+S.level*6;
 enemies.forEach(function(e,i){
  e.t+=dt; e.x+=Math.sin(e.t*2+i)*spd*dt*0.4; e.y+=Math.sin(e.t+i)*8*dt;
  if(Math.random()<0.002+S.level*0.0004)eBullets.push({x:e.x,y:e.y+10,vy:160+S.level*8});
 });
 // collisions bullets-enemies
 for(var i=enemies.length-1;i>=0;i--){
  var e=enemies[i];
  for(var j=bullets.length-1;j>=0;j--){
   var b=bullets[j]; if(Math.abs(b.x-e.x)<18&&Math.abs(b.y-e.y)<16){
    bullets.splice(j,1); e.hp--; if(e.hp<=0){S.score+=20+S.level*3; burst(e.x,e.y,"#fbbf24",12,180); enemies.splice(i,1); sfx("coin");}
    break;
   }
  }
 }
 // ebullets ship
 for(var i=eBullets.length-1;i>=0;i--){
  var b=eBullets[i]; if(Math.abs(b.x-ship.x)<18&&Math.abs(b.y-ship.y)<14){
   eBullets.splice(i,1); S.lives--; S.shake=0.5; S.flash=0.35; sfx("bad");
   if(S.lives<=0){gameOver(); return;}
  }
 }
 enemies.forEach(function(e){if(Math.abs(e.x-ship.x)<22&&Math.abs(e.y-ship.y)<20){S.lives=0; gameOver();}});
 updateHud(); onHudExtra();
 if(!enemies.length)levelComplete(200);
}
function gameDraw(ctx,pal){
 // stars
 for(var i=0;i<40;i++){ctx.fillStyle="rgba(200,220,255,0.2)"; ctx.fillRect((i*53)%S.W,(i*97+performance.now()*0.02)%S.H,2,2);}
 // enemies as geometric drones (not classic invaders sprites)
 enemies.forEach(function(e){
  ctx.save(); ctx.translate(e.x,e.y);
  ctx.fillStyle=e.type===0?"#f472b6":e.type===1?"#a78bfa":"#4ade80";
  ctx.shadowColor=ctx.fillStyle; ctx.shadowBlur=10;
  ctx.beginPath(); ctx.moveTo(0,-12); ctx.lineTo(12,8); ctx.lineTo(0,4); ctx.lineTo(-12,8); ctx.closePath(); ctx.fill();
  ctx.restore();
 });
 ctx.shadowBlur=0;
 bullets.forEach(function(b){ctx.fillStyle="#67e8f9"; ctx.fillRect(b.x-2,b.y-8,4,12);});
 eBullets.forEach(function(b){ctx.fillStyle="#fb7185"; ctx.beginPath(); ctx.arc(b.x,b.y,3,0,Math.PI*2); ctx.fill();});
 // ship original
 ctx.save(); ctx.translate(ship.x,ship.y);
 ctx.fillStyle=pal[1]; ctx.shadowColor=pal[1]; ctx.shadowBlur=14;
 ctx.beginPath(); ctx.moveTo(0,-16); ctx.lineTo(16,12); ctx.lineTo(0,6); ctx.lineTo(-16,12); ctx.closePath(); ctx.fill();
 ctx.fillStyle="#f0abfc"; ctx.fillRect(-3,6,6,8);
 ctx.restore(); ctx.shadowBlur=0;
}
function onKeyDown(e){
 if(e.code==="ArrowLeft"||e.code==="KeyA")S.keys.left=true;
 if(e.code==="ArrowRight"||e.code==="KeyD")S.keys.right=true;
 if(e.code==="Space"){e.preventDefault(); S.keys.fire=true; fire();}
}
function onKeyUp(e){
 if(e.code==="ArrowLeft"||e.code==="KeyA")S.keys.left=false;
 if(e.code==="ArrowRight"||e.code==="KeyD")S.keys.right=false;
 if(e.code==="Space")S.keys.fire=false;
}
function onPointer(p,type){if(type==="down")fire(); if(type==="move"||type==="down")S.pointer=p;}
"""
}

# ========== 6 NEON MAZE MUNCHER ==========
GAMES["neon-maze-muncher"] = {
    "title": "Neon Maze Muncher",
    "slug": "neon-maze-muncher",
    "genre_tr": "Labirent · Toplama",
    "genre_en": "Maze · Collect",
    "tagline_tr": "Neon labirent · enerji çekirdekleri · takipçi bozucu dronlar",
    "tagline_en": "Neon maze · energy cores · hunter drones",
    "desc": "Neon Maze Muncher: labirentte çekirdek topla, avcı dronlardan kaç.",
    "cw": 480, "ch": 640,
    "how_tr": [
        "<b>Hareket:</b> oklar / WASD / kaydır",
        "<b>Hedef:</b> tüm enerji çekirdeklerini topla",
        "<b>Düşman:</b> mor avcı dronlar (hayalet değil)",
        "<b>Power:</b> cyan çekirdek kısa süre hız verir",
        "<b>12 level:</b> daha büyük labirent ve daha çok dron"
    ],
    "how_en": [
        "<b>Move:</b> arrows / WASD / swipe",
        "<b>Goal:</b> collect all energy cores",
        "<b>Enemies:</b> purple hunter drones (not ghosts)",
        "<b>Power:</b> cyan cores grant a short speed boost",
        "<b>12 levels:</b> larger mazes and more drones"
    ],
    "music": "[174,196,220,246,220,196,174,164]",
    "logic": r"""
var CELL, COLS, ROWS, maze, player, drones, cores, boost, moveCd;
function LEVEL_TARGET(lv){return 100+lv*50;}
function gameReset(){
 COLS=15+((S.level>6)?2:0); ROWS=17+((S.level>8)?2:0);
 CELL=Math.floor(Math.min((S.W-20)/COLS,(S.H-40)/ROWS));
 maze=buildMaze(COLS,ROWS);
 player={x:1,y:1}; boost=0; moveCd=0; cores=[]; drones=[];
 for(var y=1;y<ROWS-1;y++)for(var x=1;x<COLS-1;x++)if(maze[y][x]===0&&!(x===1&&y===1)){
  if(Math.random()<0.55)cores.push({x:x,y:y,power:Math.random()<0.08});
 }
 var dc=2+Math.min(4,(S.level/2)|0);
 for(var i=0;i<dc;i++){drones.push({x:COLS-2,y:ROWS-2-i, tx:0,ty:0, t:0});}
 onHudExtra();
}
function buildMaze(w,h){
 var m=[]; for(var y=0;y<h;y++){m[y]=[]; for(var x=0;x<w;x++)m[y][x]=(x===0||y===0||x===w-1||y===h-1||((x%2===0)&&(y%2===0)))?1:0;}
 // sprinkle walls
 for(var i=0;i<w*h*0.08;i++){var x=1+(Math.random()*(w-2))|0,y=1+(Math.random()*(h-2))|0; if(!(x<=2&&y<=2))m[y][x]=1;}
 m[1][1]=0; m[1][2]=0; m[2][1]=0; return m;
}
function onHudExtra(){document.getElementById("hudExtraLabel").textContent="ÇEKİRDEK"; document.getElementById("hudExtra").textContent=String(cores.length);}
function tryMove(dx,dy){
 if(moveCd>0)return; var nx=player.x+dx, ny=player.y+dy;
 if(nx<0||ny<0||nx>=COLS||ny>=ROWS||maze[ny][nx]===1)return;
 player.x=nx; player.y=ny; moveCd=boost>0?0.08:0.12; sfx("move");
 for(var i=cores.length-1;i>=0;i--)if(cores[i].x===player.x&&cores[i].y===player.y){
  if(cores[i].power){boost=4; sfx("ok");} else sfx("coin");
  S.score+=15; burst(ox()+CELL/2,oy()+CELL/2,"#fbbf24",8,120); cores.splice(i,1);
 }
 onHudExtra(); updateHud();
 if(!cores.length)levelComplete(200);
}
function ox(){return (S.W-COLS*CELL)/2+player.x*CELL;}
function oy(){return 30+player.y*CELL;}
function gameUpdate(dt){
 moveCd=Math.max(0,moveCd-dt); boost=Math.max(0,boost-dt);
 if(S.keys.left)tryMove(-1,0); if(S.keys.right)tryMove(1,0); if(S.keys.up)tryMove(0,-1); if(S.keys.down)tryMove(0,1);
 // simple chase AI
 drones.forEach(function(d,i){
  d.t+=dt; if(d.t<0.28-Math.min(0.12,S.level*0.008))return; d.t=0;
  var opts=[]; [[1,0],[-1,0],[0,1],[0,-1]].forEach(function(v){
   var nx=d.x+v[0],ny=d.y+v[1]; if(nx>=0&&ny>=0&&nx<COLS&&ny<ROWS&&maze[ny][nx]===0)opts.push(v);
  });
  if(!opts.length)return;
  opts.sort(function(a,b){return (Math.abs(d.x+a[0]-player.x)+Math.abs(d.y+a[1]-player.y))-(Math.abs(d.x+b[0]-player.x)+Math.abs(d.y+b[1]-player.y));});
  // sometimes random to feel less perfect
  var ch=Math.random()<0.7?opts[0]:opts[(Math.random()*opts.length)|0];
  d.x+=ch[0]; d.y+=ch[1];
  if(d.x===player.x&&d.y===player.y){
   S.lives--; S.shake=0.5; S.flash=0.35; sfx("bad"); updateHud();
   player.x=1; player.y=1;
   if(S.lives<=0)gameOver();
  }
 });
}
function gameDraw(ctx,pal){
 var ox0=(S.W-COLS*CELL)/2, oy0=30;
 for(var y=0;y<ROWS;y++)for(var x=0;x<COLS;x++){
  var rx=ox0+x*CELL, ry=oy0+y*CELL;
  if(maze[y][x]===1){ctx.fillStyle=pal[0]; ctx.strokeStyle=pal[1]; ctx.lineWidth=1; ctx.fillRect(rx,ry,CELL-1,CELL-1); ctx.strokeRect(rx+1,ry+1,CELL-3,CELL-3);}
  else {ctx.fillStyle="rgba(0,0,0,0.25)"; ctx.fillRect(rx,ry,CELL-1,CELL-1);}
 }
 cores.forEach(function(c){
  ctx.fillStyle=c.power?"#67e8f9":"#fbbf24"; ctx.beginPath();
  ctx.arc(ox0+c.x*CELL+CELL/2, oy0+c.y*CELL+CELL/2, CELL*0.18,0,Math.PI*2); ctx.fill();
 });
 // player cube muncher
 ctx.fillStyle=pal[1]; ctx.shadowColor=pal[1]; ctx.shadowBlur=12;
 ctx.beginPath(); ctx.roundRect?ctx.roundRect(ox0+player.x*CELL+3,oy0+player.y*CELL+3,CELL-6,CELL-6,4):(ctx.fillRect(ox0+player.x*CELL+3,oy0+player.y*CELL+3,CELL-6,CELL-6));
 if(ctx.roundRect)ctx.fill(); else ctx.fillRect(ox0+player.x*CELL+3,oy0+player.y*CELL+3,CELL-6,CELL-6);
 // drones as hex hunters
 drones.forEach(function(d){
  var cx=ox0+d.x*CELL+CELL/2, cy=oy0+d.y*CELL+CELL/2;
  ctx.fillStyle="#c084fc"; ctx.shadowColor="#c084fc"; ctx.shadowBlur=10;
  ctx.beginPath(); for(var i=0;i<6;i++){var a=i/6*Math.PI*2; var px=cx+Math.cos(a)*CELL*0.32, py=cy+Math.sin(a)*CELL*0.32; if(i===0)ctx.moveTo(px,py); else ctx.lineTo(px,py);} ctx.closePath(); ctx.fill();
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
 if(type==="down")sw0={x:p.x,y:p.y};
 if(type==="up"&&sw0){var dx=p.x-sw0.x,dy=p.y-sw0.y; if(Math.abs(dx)>20||Math.abs(dy)>20){if(Math.abs(dx)>Math.abs(dy))tryMove(dx>0?1:-1,0); else tryMove(0,dy>0?1:-1);} sw0=null;}
}
"""
}

# ========== 7 MEMORY FLASH ==========
GAMES["memory-flash"] = {
    "title": "Memory Flash",
    "slug": "memory-flash",
    "genre_tr": "Bulmaca · Hafıza",
    "genre_en": "Puzzle · Memory",
    "tagline_tr": "Kart eşleştir · neon semboller · 12 level",
    "tagline_en": "Match pairs · neon symbols · 12 levels",
    "desc": "Memory Flash: kart çiftlerini eşleştir, hamle ve süreyle yıldız kazan.",
    "cw": 480, "ch": 720,
    "how_tr": [
        "<b>Kontrol:</b> tıkla / dokun kart seç",
        "<b>Hedef:</b> tüm çiftleri bul",
        "<b>Skor:</b> az hamle = daha yüksek puan",
        "<b>Can:</b> yanlış eşleşme can düşürmez ama puan kırpar",
        "<b>12 level:</b> kart sayısı artar"
    ],
    "how_en": [
        "<b>Controls:</b> tap cards to flip",
        "<b>Goal:</b> match all pairs",
        "<b>Score:</b> fewer moves = higher score",
        "<b>Mistakes:</b> reduce score slightly",
        "<b>12 levels:</b> more cards"
    ],
    "music": "[523,494,440,392,440,494,523,587]",
    "logic": r"""
var cols, rows, cards, open, lock, moves, pairsLeft, symbols;
function LEVEL_TARGET(lv){return 200+lv*40;}
function gameReset(){
 var pairs=4+Math.min(8,S.level); // 4..12 pairs
 cols=pairs<=6?3:pairs<=8?4:4; rows=Math.ceil((pairs*2)/cols);
 while(cols*rows<pairs*2)rows++;
 symbols=["◆","●","▲","■","★","✚","◇","○","△","□","☆","✖","⬡","⬢","✦","✧"].slice(0,pairs);
 var deck=symbols.concat(symbols); // shuffle
 for(var i=deck.length-1;i>0;i--){var j=(Math.random()*(i+1))|0; var t=deck[i]; deck[i]=deck[j]; deck[j]=t;}
 cards=[]; var k=0; for(var y=0;y<rows;y++)for(var x=0;x<cols;x++){if(k<deck.length)cards.push({x:x,y:y,v:deck[k++],flip:false,done:false});}
 open=[]; lock=false; moves=0; pairsLeft=pairs; onHudExtra();
}
function onHudExtra(){document.getElementById("hudExtraLabel").textContent="ÇİFT"; document.getElementById("hudExtra").textContent=String(pairsLeft);}
function gameUpdate(dt){}
function layout(){var pad=16, top=70; var bw=(S.W-pad*2)/cols, bh=(S.H-top-pad)/rows; return {pad:pad,top:top,bw:bw,bh:bh};}
function gameDraw(ctx,pal){
 var L=layout();
 cards.forEach(function(c){
  var rx=L.pad+c.x*L.bw+4, ry=L.top+c.y*L.bh+4, rw=L.bw-8, rh=L.bh-8;
  if(c.done||c.flip){ctx.fillStyle=pal[1]; ctx.shadowColor=pal[1]; ctx.shadowBlur=10;}
  else {ctx.fillStyle="rgba(15,23,42,0.9)"; ctx.strokeStyle=pal[2];}
  ctx.beginPath(); ctx.roundRect?ctx.roundRect(rx,ry,rw,rh,10):ctx.rect(rx,ry,rw,rh); ctx.fill();
  if(!c.done&&!c.flip){ctx.strokeStyle=pal[2]; ctx.lineWidth=2; ctx.stroke();}
  ctx.shadowBlur=0;
  if(c.flip||c.done){ctx.fillStyle="#0f172a"; ctx.font="bold "+Math.floor(Math.min(rw,rh)*0.4)+"px Inter,sans-serif"; ctx.textAlign="center"; ctx.textBaseline="middle"; ctx.fillText(c.v,rx+rw/2,ry+rh/2);}
  else {ctx.fillStyle=pal[2]; ctx.font="bold 18px Inter,sans-serif"; ctx.textAlign="center"; ctx.textBaseline="middle"; ctx.fillText("?",rx+rw/2,ry+rh/2);}
 });
}
function onPointer(p,type){
 if(type!=="down"||lock||S.mode!=="play")return;
 var L=layout(); var x=((p.x-L.pad)/L.bw)|0, y=((p.y-L.top)/L.bh)|0;
 var c=cards.find(function(k){return k.x===x&&k.y===y;}); if(!c||c.done||c.flip)return;
 c.flip=true; open.push(c); sfx("ui");
 if(open.length===2){
  moves++; lock=true;
  if(open[0].v===open[1].v){
   open[0].done=open[1].done=true; pairsLeft--; S.score+=50+Math.max(0,30-moves); sfx("coin"); burst(p.x,p.y,"#fbbf24",10,150); open=[]; lock=false; onHudExtra(); updateHud();
   if(pairsLeft<=0){S.score+=100; levelComplete(100);}
  } else {
   S.score=Math.max(0,S.score-5); sfx("bad"); updateHud();
   setTimeout(function(){open.forEach(function(o){o.flip=false;}); open=[]; lock=false;},650);
  }
 }
}
function onKeyDown(e){}
function onKeyUp(e){}
"""
}

# ========== 8 REACTION RUSH ==========
GAMES["reaction-rush"] = {
    "title": "Reaction Rush",
    "slug": "reaction-rush",
    "genre_tr": "Refleks · Test",
    "genre_en": "Reflex · Test",
    "tagline_tr": "Yeşil olunca bas · ortalamayı düşür · 12 level",
    "tagline_en": "Tap on green · lower your average · 12 levels",
    "desc": "Reaction Rush: sinyal yeşile dönünce bas, ortalama reaksiyon süreni düşür.",
    "cw": 480, "ch": 640,
    "how_tr": [
        "<b>Kontrol:</b> Space / tık / dokun",
        "<b>Kural:</b> kırmızıda bekle, YEŞİLDE hemen bas",
        "<b>Erken basma:</b> fail · can kaybı",
        "<b>Hedef:</b> level için N başarılı tur, ortalama eşiğin altında",
        "<b>12 level:</b> daha sıkı ortalama hedefi"
    ],
    "how_en": [
        "<b>Controls:</b> Space / click / tap",
        "<b>Rule:</b> wait on red, tap instantly on GREEN",
        "<b>Early tap:</b> fail · lose a life",
        "<b>Goal:</b> N successful rounds under average threshold",
        "<b>12 levels:</b> stricter average targets"
    ],
    "music": "[0]",  # quiet - override
    "logic": r"""
var phase, waitT, goAt, times, need, threshold, round;
// phase: wait | ready | go | result
function LEVEL_TARGET(lv){return 100+lv*20;}
function gameReset(){
 phase="wait"; waitT=0.6; goAt=0; times=[]; need=5+Math.min(5,(S.level/2)|0);
 threshold=420-S.level*12; // ms
 round=0; onHudExtra();
 schedule();
}
function schedule(){phase="ready"; waitT=rand(0.8,2.2+S.level*0.05); goAt=0;}
function onHudExtra(){var avg=times.length?(times.reduce(function(a,b){return a+b;},0)/times.length)|0:0; document.getElementById("hudExtraLabel").textContent="ORT"; document.getElementById("hudExtra").textContent=avg+"ms · "+times.length+"/"+need;}
function gameUpdate(dt){
 if(phase==="ready"){waitT-=dt; if(waitT<=0){phase="go"; goAt=performance.now(); sfx("ok");}}
}
function tap(){
 if(S.mode!=="play")return;
 if(phase==="ready"){ // early
  S.lives--; S.shake=0.4; S.flash=0.3; sfx("bad"); phase="wait"; waitT=0.5; updateHud(); if(S.lives<=0)gameOver(); else setTimeout(schedule,400); return;
 }
 if(phase==="go"){
  var ms=performance.now()-goAt; times.push(ms); S.score+=Math.max(5,Math.floor((threshold+100-ms)/4)); sfx("coin");
  phase="result"; onHudExtra(); updateHud();
  if(times.length>=need){
   var avg=times.reduce(function(a,b){return a+b;},0)/times.length;
   if(avg<=threshold)levelComplete(150); else {showToast("Yavaş / Slow", (avg|0)+"ms > "+threshold+"ms"); S.lives--; updateHud(); if(S.lives<=0)gameOver(); else {times=[]; setTimeout(schedule,700);} }
  } else setTimeout(schedule,500);
 }
}
function gameDraw(ctx,pal){
 var col=phase==="go"?"#22c55e":phase==="ready"?"#ef4444":"#334155";
 ctx.fillStyle=col; ctx.shadowColor=col; ctx.shadowBlur=30;
 roundFill(ctx,40,S.H*0.25,S.W-80,S.H*0.4,24);
 ctx.shadowBlur=0;
 ctx.fillStyle="#fff"; ctx.font="bold 28px Inter,sans-serif"; ctx.textAlign="center";
 var msg=phase==="go"?"ŞİMDİ! / NOW!":phase==="ready"?"BEKLE / WAIT":"...";
 ctx.fillText(msg,S.W/2,S.H*0.45);
 ctx.font="14px Inter,sans-serif"; ctx.fillStyle="#e2e8f0";
 ctx.fillText("Hedef ort. / Target avg ≤ "+threshold+" ms", S.W/2, S.H*0.75);
 if(times.length){var avg=(times.reduce(function(a,b){return a+b;},0)/times.length)|0; ctx.fillText("Son: "+(times[times.length-1]|0)+" ms · Ort: "+avg+" ms", S.W/2, S.H*0.8);}
}
function roundFill(ctx,x,y,w,h,r){ctx.beginPath();ctx.moveTo(x+r,y);ctx.arcTo(x+w,y,x+w,y+h,r);ctx.arcTo(x+w,y+h,x,y+h,r);ctx.arcTo(x,y+h,x,y,r);ctx.arcTo(x,y,x+w,y,r);ctx.closePath();ctx.fill();}
function onKeyDown(e){if(e.code==="Space"||e.code==="Enter"){e.preventDefault(); tap();}}
function onKeyUp(e){}
function onPointer(p,type){if(type==="down")tap();}
// silence default music notes somewhat
var MUSIC_NOTES=[0];
"""
}

# ========== 9 RUNNER BYTE ==========
GAMES["runner-byte"] = {
    "title": "Runner Byte",
    "slug": "runner-byte",
    "genre_tr": "Koşu · Aksiyon",
    "genre_en": "Runner · Action",
    "tagline_tr": "3 şerit · veri paketleri · glitch engeller · 12 level",
    "tagline_en": "3 lanes · data packs · glitch hazards · 12 levels",
    "desc": "Runner Byte: siber şerit koşusu, paket topla, glitch engellerden kaç.",
    "cw": 420, "ch": 720,
    "how_tr": [
        "<b>Hareket:</b> ←→ / A D / kaydır",
        "<b>Zıpla:</b> Space / W / üst yarı dokun",
        "<b>Hedef:</b> level mesafesini tamamla",
        "<b>Topla:</b> sarı veri paketleri",
        "<b>12 level:</b> hız ve engel yoğunluğu artar"
    ],
    "how_en": [
        "<b>Move:</b> arrows / A D / swipe",
        "<b>Jump:</b> Space / W / tap top half",
        "<b>Goal:</b> finish level distance",
        "<b>Collect:</b> yellow data packs",
        "<b>12 levels:</b> speed and density rise"
    ],
    "music": "[196,233,261,311,261,233,196,174]",
    "logic": r"""
var LANES=3, lane, x, y, jump, jv, obstacles, packs, dist, goal, speed, spawnT;
function LEVEL_TARGET(lv){return 200+lv*60;}
function laneX(l){var pad=50; return pad+l*((S.W-pad*2)/(LANES-1));}
function gameReset(){
 lane=1; x=laneX(1); y=S.H*0.78; jump=0; jv=0; obstacles=[]; packs=[]; dist=0;
 goal=700+S.level*180; speed=200+S.level*18; spawnT=0.5; onHudExtra();
}
function onHudExtra(){document.getElementById("hudExtraLabel").textContent="MESAFE"; document.getElementById("hudExtra").textContent=(dist|0)+"/"+(goal|0);}
function gameUpdate(dt){
 x+=(laneX(lane)-x)*Math.min(1,dt*14);
 if(S.keys.jump&&jump===0){jv=-400; jump=0.001; S.keys.jump=false; sfx("move");}
 if(jump>0||jv!==0){jv+=1300*dt; jump+=jv*dt; if(jump>=0){jump=0; jv=0;}}
 dist+=speed*dt*0.12; S.score+=speed*dt*0.05; spawnT-=dt;
 if(spawnT<=0){spawnT=Math.max(0.35,0.85-S.level*0.03)+Math.random()*0.2;
  if(Math.random()<0.65)obstacles.push({lane:(Math.random()*LANES)|0,y:-40,h:40,w:48});
  else packs.push({lane:(Math.random()*LANES)|0,y:-30,r:10});
 }
 var py=y+jump;
 obstacles.forEach(function(o){o.y+=speed*dt;}); packs.forEach(function(p){p.y+=speed*dt;});
 obstacles=obstacles.filter(function(o){return o.y<S.H+60;}); packs=packs.filter(function(p){return p.y<S.H+40;});
 for(var i=obstacles.length-1;i>=0;i--){
  var o=obstacles[i]; if(o.lane===lane && Math.abs(py-(o.y+20))<28 && jump>-20){
   obstacles.splice(i,1); S.lives--; S.shake=0.5; S.flash=0.35; sfx("bad"); updateHud(); if(S.lives<=0){gameOver(); return;}
  }
 }
 for(var i=packs.length-1;i>=0;i--){
  var p=packs[i]; if(p.lane===lane && Math.abs(py-p.y)<28){packs.splice(i,1); S.score+=30; sfx("coin"); burst(laneX(p.lane),p.y,"#fbbf24",8,140);}
 }
 updateHud(); onHudExtra();
 if(dist>=goal)levelComplete(180);
}
function gameDraw(ctx,pal){
 // floor lanes
 for(var i=0;i<LANES;i++){ctx.strokeStyle="rgba(34,211,238,0.15)"; ctx.beginPath(); ctx.moveTo(laneX(i),S.H*0.25); ctx.lineTo(laneX(i),S.H); ctx.stroke();}
 // scroll lines
 for(var i=0;i<12;i++){var yy=((i*60+dist*3)% (S.H*0.75))+S.H*0.25; ctx.strokeStyle="rgba(129,140,248,0.12)"; ctx.beginPath(); ctx.moveTo(30,yy); ctx.lineTo(S.W-30,yy); ctx.stroke();}
 obstacles.forEach(function(o){ctx.fillStyle="#fb7185"; ctx.shadowColor="#fb7185"; ctx.shadowBlur=10; ctx.fillRect(laneX(o.lane)-o.w/2,o.y,o.w,o.h);});
 packs.forEach(function(p){ctx.fillStyle="#fbbf24"; ctx.shadowColor="#fbbf24"; ctx.shadowBlur=8; ctx.beginPath(); ctx.arc(laneX(p.lane),p.y,p.r,0,Math.PI*2); ctx.fill();});
 ctx.shadowBlur=0;
 // byte runner character (cube with antenna)
 var py=y+jump; ctx.save(); ctx.translate(x,py);
 ctx.fillStyle=pal[1]; ctx.shadowColor=pal[1]; ctx.shadowBlur=12;
 ctx.fillRect(-12,-16,24,28); ctx.fillStyle="#0f172a"; ctx.fillRect(-6,-8,4,4); ctx.fillRect(2,-8,4,4);
 ctx.strokeStyle=pal[2]; ctx.beginPath(); ctx.moveTo(0,-16); ctx.lineTo(0,-26); ctx.stroke();
 ctx.fillStyle="#f472b6"; ctx.beginPath(); ctx.arc(0,-28,3,0,Math.PI*2); ctx.fill();
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
 if(type==="down"){sw0={x:p.x,y:p.y}; if(p.y<S.H*0.4)S.keys.jump=true; else {var best=0,bd=1e9; for(var i=0;i<LANES;i++){var d=Math.abs(laneX(i)-p.x); if(d<bd){bd=d; best=i;}} lane=best;}}
 if(type==="up"&&sw0){var dx=p.x-sw0.x; if(Math.abs(dx)>30)lane=clamp(lane+(dx>0?1:-1),0,LANES-1); sw0=null;}
}
"""
}


def build_game(meta: dict) -> str:
    head = shell_html(meta)
    js = SHELL_JS_COMMON
    # inject constants
    js = js.replace("GENRE_TR", json_str(meta["genre_tr"]))
    js = js.replace("GENRE_EN", json_str(meta["genre_en"]))
    js = js.replace("TAGLINE_TR", json_str(meta["tagline_tr"]))
    js = js.replace("TAGLINE_EN", json_str(meta["tagline_en"]))
    js = js.replace("HOW_TR", js_array(meta["how_tr"]))
    js = js.replace("HOW_EN", js_array(meta["how_en"]))
    js = js.replace("MUSIC_NOTES", meta.get("music", "[220,247,262,294]"))
    js = js.replace("CW", str(meta.get("cw", 480)))
    js = js.replace("CH", str(meta.get("ch", 720)))
    # Reaction rush redefines MUSIC_NOTES in logic - common already set
    logic = meta["logic"]
    if "var MUSIC_NOTES=" not in logic and "MUSIC_NOTES=" not in logic.split("function")[0]:
        pass
    return head + js + "\n" + logic + "\n})();\n</script>\n</body>\n</html>\n"


def json_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def js_array(items: list[str]) -> str:
    return "[" + ",".join(json_str(i) for i in items) + "]"


def write_games():
    for slug, meta in GAMES.items():
        meta = dict(meta)
        if "how_tr" in meta:
            meta["genre_tr"] = meta["genre_tr"]
        d = PUBLIC / slug
        d.mkdir(parents=True, exist_ok=True)
        html = build_game(meta)
        (d / "index.html").write_text(html, encoding="utf-8")
        print(f"wrote {slug} ({len(html)} bytes)")


def crc(data: bytes) -> int:
    return zlib.crc32(data) & 0xFFFFFFFF


def chunk(tag: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", crc(tag + data))


def write_png(path: Path, w: int, h: int, rgb_fn):
    raw = bytearray()
    for y in range(h):
        raw.append(0)
        for x in range(w):
            r, g, b = rgb_fn(x, y, w, h)
            raw.extend((r, g, b))
    comp = zlib.compress(bytes(raw), 9)
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
    png += chunk(b"IDAT", comp)
    png += chunk(b"IEND", b"")
    path.write_bytes(png)


def gen_posters():
    try:
        from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
    except ImportError:
        print("Pillow missing, skip posters")
        return

    games = [
        ("brick-blitz", (11, 30, 80), (34, 211, 238), "BRICK BLITZ", "BREAKOUT"),
        ("snake-rewind", (8, 40, 30), (74, 222, 128), "SNAKE REWIND", "SNAKE"),
        ("cascade-blocks", (40, 10, 60), (167, 139, 250), "CASCADE", "BLOCKS"),
        ("number-fusion", (20, 20, 70), (251, 191, 36), "NUMBER", "FUSION"),
        ("pixel-glider", (10, 20, 50), (244, 114, 182), "PIXEL", "GLIDER"),
        ("galaxy-defender", (5, 10, 40), (56, 189, 248), "GALAXY", "DEFENDER"),
        ("neon-maze-muncher", (20, 5, 45), (192, 132, 252), "NEON MAZE", "MUNCHER"),
        ("memory-flash", (30, 20, 10), (251, 146, 60), "MEMORY", "FLASH"),
        ("reaction-rush", (40, 10, 10), (248, 113, 113), "REACTION", "RUSH"),
        ("runner-byte", (5, 25, 40), (45, 212, 191), "RUNNER", "BYTE"),
    ]
    ARCADE.mkdir(parents=True, exist_ok=True)
    for slug, bg, accent, t1, t2 in games:
        img = Image.new("RGB", (1280, 720), bg)
        dr = ImageDraw.Draw(img)
        # grid
        for i in range(0, 1280, 40):
            dr.line([(i, 0), (i, 720)], fill=tuple(max(0, c - 8) for c in bg), width=1)
        for j in range(0, 720, 40):
            dr.line([(0, j), (1280, j)], fill=tuple(max(0, c - 8) for c in bg), width=1)
        # glow orbs
        for cx, cy, r in [(200, 160, 180), (1000, 500, 220), (640, 360, 120)]:
            for k in range(r, 0, -8):
                a = int(30 * (1 - k / r))
                col = tuple(min(255, accent[i] + a) for i in range(3))
                dr.ellipse([cx - k, cy - k, cx + k, cy + k], outline=col)
        # title blocks
        dr.rectangle([80, 220, 1200, 500], outline=accent, width=4)
        try:
            font_big = ImageFont.truetype("arialbd.ttf", 72)
            font_sm = ImageFont.truetype("arial.ttf", 28)
        except Exception:
            font_big = ImageFont.load_default()
            font_sm = font_big
        dr.text((100, 260), t1, fill=accent, font=font_big)
        dr.text((100, 360), t2, fill=(226, 232, 240), font=font_big)
        dr.text((100, 460), "ACARTECHS ARCADE", fill=(148, 163, 184), font=font_sm)
        # mini motif per game
        if slug == "brick-blitz":
            for r in range(4):
                for c in range(10):
                    dr.rectangle([200 + c * 90, 80 + r * 28, 280 + c * 90, 100 + r * 28], fill=accent if (r + c) % 2 == 0 else (167, 139, 250))
        elif slug == "snake-rewind":
            for i in range(8):
                dr.rectangle([900 + i * 22, 120, 918 + i * 22, 138], fill=accent)
        elif slug == "pixel-glider":
            dr.polygon([(1000, 200), (1060, 230), (1000, 260), (1020, 230)], fill=accent)

        poster = ARCADE / f"{slug}-poster.webp"
        img.save(poster, "WEBP", quality=82, method=6)
        # thumb
        side = min(img.size)
        left = (img.width - side) // 2
        top = (img.height - side) // 2
        thumb = img.crop((left, top, left + side, top + side)).resize((160, 160), Image.Resampling.LANCZOS)
        thumb.save(ARCADE / f"{slug}-thumb.webp", "WEBP", quality=82, method=6)
        print("poster", slug)


def main():
    write_games()
    gen_posters()
    # rename brick assets from dx-ball if present
    for old, new in [
        ("dx-ball-poster.webp", "brick-blitz-poster.webp"),
        ("dx-ball-thumb.webp", "brick-blitz-thumb.webp"),
        ("dx-ball-preview.mp4", "brick-blitz-preview.mp4"),
        ("dx-ball-preview.webm", "brick-blitz-preview.webm"),
    ]:
        src, dst = ARCADE / old, ARCADE / new
        if src.exists() and not dst.exists():
            src.replace(dst)
            print("moved", old, "->", new)
        elif src.exists() and dst.exists():
            # keep both or overwrite poster from gen
            pass
    print("done")


if __name__ == "__main__":
    main()

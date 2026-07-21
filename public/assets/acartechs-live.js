(function(){
  if(window.__acarLive)return;window.__acarLive=true;
  function ready(fn){if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',fn);else fn()}
  function relTime(iso){var d=new Date(iso+'T12:00:00');if(isNaN(d.getTime()))return null;var diff=Math.round((Date.now()-d.getTime())/1000);if(diff<0)diff=0;if(diff<90)return'az önce';if(diff<3600)return Math.floor(diff/60)+' dk önce';if(diff<86400)return Math.floor(diff/3600)+' saat önce';if(diff<86400*2)return'dün';if(diff<86400*7)return Math.floor(diff/86400)+' gün önce';return null}
  ready(function(){
    document.body.classList.add('acar-ready');
    document.querySelectorAll('time[data-acar-date],time[datetime]').forEach(function(el){
      var iso=el.getAttribute('datetime');if(!iso)return;var r=relTime(iso);if(!r)return;
      if(!el.dataset.original)el.dataset.original=el.textContent.trim();el.textContent=r;el.title=el.dataset.original;
    });
    document.querySelectorAll('.acartechs-fresh-pill').forEach(function(el){el.remove();});
    var strong=document.querySelector('.acartechs-live-strip strong');
    if(strong&&!strong.querySelector('.acartechs-live-dot')){var d=document.createElement('span');d.className='acartechs-live-dot';d.setAttribute('aria-hidden','true');strong.prepend(d)}
    var top=document.querySelector('.acartechs-topbar .acartechs-actions')||document.querySelector('.acartechs-topbar');
    if(top&&!document.querySelector('.acartechs-now-badge')){
      var b=document.createElement('div');b.className='acartechs-now-badge';b.innerHTML='<span>Canlı</span> <time id="acar-now-clock"></time>';top.prepend(b);
      function tick(){var el=document.getElementById('acar-now-clock');if(!el)return;el.textContent=new Date().toLocaleString('tr-TR',{weekday:'short',day:'numeric',month:'short',hour:'2-digit',minute:'2-digit'})}
      tick();setInterval(tick,30000)
    }
    if(!document.querySelector('.acartechs-read-progress')){
      var bar=document.createElement('div');bar.className='acartechs-read-progress';bar.setAttribute('aria-hidden','true');document.body.appendChild(bar);
      function onScroll(){var h=document.documentElement;var max=h.scrollHeight-h.clientHeight;bar.style.width=(max>0?(h.scrollTop/max)*100:0)+'%'}
      window.addEventListener('scroll',onScroll,{passive:true});onScroll()
    }
    if(!document.querySelector('.acartechs-back-top')){
      var btn=document.createElement('button');btn.className='acartechs-back-top';btn.type='button';btn.setAttribute('aria-label','Yukarı çık');btn.textContent='↑';
      btn.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'})});document.body.appendChild(btn);
      window.addEventListener('scroll',function(){btn.classList.toggle('is-on',window.scrollY>480)},{passive:true})
    }
    function markEmptyAds(){document.querySelectorAll('.acartechs-adsense-shell').forEach(function(shell){var unit=shell.querySelector('.adsbygoogle');if(!unit)return;var status=unit.getAttribute('data-ad-status');var hasFrame=!!shell.querySelector('iframe');if(status==='filled'||hasFrame){shell.classList.remove('is-ad-empty','is-ad-checking');shell.classList.add('is-ad-filled');return}if(status==='unfilled'||unit.childElementCount===0){shell.classList.remove('is-ad-filled');shell.classList.add('is-ad-empty')}})}
    setTimeout(markEmptyAds,4000);setTimeout(markEmptyAds,9000);
  });
})();

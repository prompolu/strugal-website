'use strict';
(()=>{
  const video=document.querySelector('#native-hero-video');
  const container=document.querySelector('.hero-video');
  if(!video||!container)return;
  const motion=matchMedia('(prefers-reduced-motion: reduce)');
  let hls,loaded=false,visible=true,fallback=false;
  video.muted=true;video.defaultMuted=true;video.controls=false;
  function poster(){container.classList.remove('playing');}
  function play(){if(motion.matches||!visible||document.hidden)return;video.play().catch(poster);}
  function useFallback(){if(fallback){poster();return;}fallback=true;if(hls){hls.destroy();hls=null;}video.src='assets/strugal-film-fallback.mp4';video.load();play();}
  function load(){
    if(loaded||motion.matches)return;loaded=true;
    if(video.canPlayType('application/vnd.apple.mpegurl'))video.src='assets/strugal-film.m3u8';
    else if(window.Hls?.isSupported()){
      hls=new Hls({maxBufferLength:16,backBufferLength:0,capLevelToPlayerSize:false,startLevel:-1});
      hls.loadSource('assets/strugal-film.m3u8');hls.attachMedia(video);
      hls.on(Hls.Events.MANIFEST_PARSED,play);
      hls.on(Hls.Events.ERROR,(_,data)=>{if(data.fatal)useFallback();});
    }else useFallback();
    play();
  }
  function sync(){if(motion.matches||document.hidden||!visible){video.pause();poster();}else{load();play();}}
  video.addEventListener('playing',()=>{if(!motion.matches&&visible&&!document.hidden)container.classList.add('playing');});
  video.addEventListener('pause',poster);
  video.addEventListener('loadedmetadata',()=>{for(const track of video.textTracks)track.mode='disabled';play();});
  video.addEventListener('error',()=>{if(!hls)useFallback();});
  document.addEventListener('visibilitychange',sync);
  motion.addEventListener('change',sync);
  new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;sync();},{threshold:.05}).observe(document.querySelector('.hero'));
  load();
})();

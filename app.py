import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Bon Secours | Virtual Campus",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
:root { color-scheme: dark; }
html, body, [data-testid="stAppViewContainer"] {
  background: #090d17 !important;
  color: #f6f1e9 !important;
}
[data-testid="stHeader"], [data-testid="stToolbar"], footer { visibility: hidden; }
.block-container { padding: .65rem .75rem 0 !important; max-width: 1800px; }
</style>
""", unsafe_allow_html=True)

components.html(r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bon Secours Virtual Campus</title>
<style>
*{box-sizing:border-box}
html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#080d17;font-family:Inter,ui-sans-serif,system-ui,Arial;color:#f8f5ef}
#app{height:100vh;min-height:660px;display:grid;grid-template-columns:245px 1fr;background:#0a1020}
#side{background:linear-gradient(165deg,#401727,#1b1020 60%,#111827);border-right:1px solid #ffffff20;padding:22px 15px;display:flex;flex-direction:column;gap:20px;z-index:4}
.brand{display:flex;gap:12px;align-items:center;padding:4px 5px 18px;border-bottom:1px solid #ffffff24}
.crest{width:43px;height:43px;border-radius:50%;display:grid;place-items:center;background:linear-gradient(135deg,#fff1d2,#c99c5d);color:#722e27;font-size:24px;box-shadow:0 5px 20px #0005}
.brand strong{display:block;font-family:Georgia,serif;letter-spacing:1px;font-size:14px;line-height:1.25}
.brand small{display:block;color:#e4cbbd;font-size:10px;letter-spacing:1.3px;margin-top:4px}
.navtitle{font-size:9px;color:#d2a99e;letter-spacing:2px;font-weight:800;padding:0 10px}
.nav{display:grid;gap:5px}
.nav button,.quick button{width:100%;border:0;text-align:left;background:transparent;color:#eadfe0;padding:11px 12px;border-radius:10px;font-size:13px;cursor:pointer;display:flex;gap:12px;align-items:center}
.nav button:hover,.nav button.active{background:linear-gradient(90deg,#9e4657,#642b40);color:white;box-shadow:0 5px 18px #0003}
.nav .ico{width:20px;text-align:center;font-size:16px}
.sidefoot{margin-top:auto;border-top:1px solid #ffffff22;padding:13px 8px;color:#cbb7b7;font-size:10px;line-height:1.6}
#main{position:relative;min-width:0;overflow:hidden}
#topbar{position:absolute;z-index:3;left:20px;right:20px;top:16px;display:flex;justify-content:space-between;align-items:center;pointer-events:none}
.pills{display:flex;gap:7px;pointer-events:auto}
.pill{background:#111a2bcc;border:1px solid #ffffff25;backdrop-filter:blur(12px);padding:10px 13px;border-radius:30px;color:#f5eee8;font-size:11px;letter-spacing:.2px}
#profile{display:flex;align-items:center;gap:9px}
#profile b{font-size:11px}
#profile small{display:block;color:#b9c4d4;font-size:9px}
#scene{position:absolute;inset:0;width:100%;height:100%;display:block}
#loading{position:absolute;inset:0;z-index:9;background:#0b1220;display:grid;place-items:center;color:#fff;font-size:14px}
.panel{position:absolute;z-index:2;background:#0c1423d9;border:1px solid #ffffff25;backdrop-filter:blur(14px);border-radius:15px;box-shadow:0 12px 35px #0005}
#mapcard{right:20px;top:78px;width:230px;padding:12px}
.panelhead{font-size:10px;letter-spacing:1.3px;color:#e6cba8;font-weight:800;margin-bottom:9px}
#mini{width:100%;height:122px;border-radius:9px;background:#1d382f}
#places{right:20px;top:240px;width:230px;padding:12px;max-height:40vh;overflow:auto}
.place{display:flex;align-items:center;justify-content:space-between;padding:7px 3px;border-bottom:1px solid #ffffff12;font-size:11px;color:#e8edf5}
.place button{background:#ffffff12;border:1px solid #ffffff18;color:#f6e6d2;border-radius:7px;padding:4px 7px;font-size:9px;cursor:pointer}
#controls{position:absolute;z-index:3;left:20px;bottom:18px;display:flex;gap:8px;align-items:end}
.steer{display:grid;grid-template-columns:48px 48px 48px;grid-template-rows:43px 43px;gap:5px}
.steer button,.action button{border:1px solid #ffffff35;background:#101a2bdc;color:white;border-radius:11px;cursor:pointer;font-size:16px;backdrop-filter:blur(10px)}
.steer button:active,.action button:active{background:#8d4054}
#up{grid-column:2}
#left{grid-column:1;grid-row:2}
#down{grid-column:2;grid-row:2}
#right{grid-column:3;grid-row:2}
.action{display:flex;gap:6px}
.action button{padding:12px 13px;font-size:11px}
#speed{position:absolute;z-index:3;bottom:20px;left:50%;transform:translateX(-50%);background:#0a1220dd;border:1px solid #ffffff2c;border-radius:15px;padding:10px 19px;min-width:210px;text-align:center;backdrop-filter:blur(12px)}
#speed strong{font-size:24px;letter-spacing:1px}
#speed small{font-size:9px;color:#b9c4d4;letter-spacing:1.5px;margin-left:7px}
#righttools{position:absolute;z-index:3;right:20px;bottom:20px;display:flex;gap:7px}
#righttools button{border:1px solid #ffffff35;background:#101a2bdd;color:#fff;border-radius:10px;padding:10px 12px;font-size:10px;cursor:pointer}
#toast{position:absolute;z-index:6;left:50%;top:82px;transform:translateX(-50%);background:#132338e8;border:1px solid #ffffff28;padding:9px 15px;border-radius:25px;font-size:11px;opacity:0;transition:.25s;pointer-events:none}
#toast.show{opacity:1}
#legend{position:absolute;left:20px;top:83px;z-index:2;background:#101a2bc9;border:1px solid #ffffff22;border-radius:12px;padding:11px 13px;font-size:10px;color:#dce5ee;line-height:1.8}
.dot{display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:7px;background:#d8b37b}
#mobilehint{display:none}
@media(max-width:900px){
 #app{grid-template-columns:72px 1fr}
 #side{padding:15px 7px;align-items:center}
 .brand{border:0;padding:0;display:block}.brand .words,.navtitle,.nav button .txt,.sidefoot{display:none}
 .nav{width:100%}.nav button{justify-content:center;padding:12px 3px}.nav .ico{font-size:18px}
 #mapcard{width:170px;right:10px;top:70px}#places{width:170px;right:10px;top:225px}
 #legend{display:none}#controls{left:10px;bottom:12px}.action{display:none}
 #speed{bottom:115px;left:auto;right:10px;transform:none;min-width:120px;padding:8px}
 #righttools{right:10px;bottom:12px}#righttools button{padding:9px}
 #topbar{left:10px;right:10px;top:10px}.pill{padding:8px 10px;font-size:9px}
}
@media(max-width:560px){
 #mapcard{display:none}#places{top:68px;max-height:34vh}
 #profile{display:none}#topbar .pills .pill:nth-child(n+3){display:none}
 #controls{bottom:12px}.steer{grid-template-columns:43px 43px 43px;grid-template-rows:40px 40px}
 #righttools{bottom:12px;flex-direction:column}
}
</style>
</head>
<body>
<div id="app">
 <aside id="side">
  <div class="brand"><div class="crest">✝</div><div class="words"><strong>BON SECOURS</strong><small>COLLEGE FOR WOMEN · THANJAVUR</small></div></div>
  <div class="navtitle">EXPLORE CAMPUS</div>
  <div class="nav">
   <button class="active" data-mode="tour"><span class="ico">⌂</span><span class="txt">Campus Tour</span></button>
   <button data-mode="drive"><span class="ico">🚘</span><span class="txt">Drive Mode</span></button>
   <button data-mode="walk"><span class="ico">🚶</span><span class="txt">Walk Mode</span></button>
   <button data-mode="map"><span class="ico">⌖</span><span class="txt">Map & Navigation</span></button>
   <button data-mode="facilities"><span class="ico">▦</span><span class="txt">Facilities</span></button>
  </div>
  <div class="navtitle">ENVIRONMENT</div>
  <div class="quick">
   <button id="weather">☀️ <span class="txt">Day / Night</span></button>
   <button id="camera">◉ <span class="txt">Change Camera</span></button>
   <button id="reset">⟲ <span class="txt">Reset Vehicle</span></button>
  </div>
  <div class="sidefoot">VIRTUAL CAMPUS EXPERIENCE<br>Concept reconstruction · v1.0<br>Keyboard: WASD / Arrow keys</div>
 </aside>
 <main id="main">
  <div id="topbar"><div class="pills"><div class="pill">✦ &nbsp; 3D CAMPUS EXPERIENCE</div><div class="pill">📍 Vilar Bypass, Thanjavur</div><div class="pill" id="weatherlabel">☀️ DAYTIME</div></div><div class="pill" id="profile">👤 &nbsp; <span><b>Virtual Visitor</b><small>Guest session</small></span></div></div>
  <canvas id="scene"></canvas>
  <div id="loading">Preparing your virtual campus…</div>
  <div id="toast"></div>
  <div id="legend"><b style="color:#f0d2a5">CAMPUS KEY</b><br><span class="dot"></span>Academic buildings<br><span class="dot" style="background:#82b6d6"></span>Facilities<br><span class="dot" style="background:#77b47d"></span>Green spaces<br><span class="dot" style="background:#aeb6c4"></span>Internal roads</div>
  <div class="panel" id="mapcard"><div class="panelhead">CAMPUS OVERVIEW · CONCEPT MAP</div><canvas id="mini" width="420" height="220"></canvas></div>
  <div class="panel" id="places"><div class="panelhead">CAMPUS DESTINATIONS</div><div id="placelist"></div></div>
  <div id="controls"><div class="steer"><button id="up">▲</button><button id="left">◀</button><button id="down">▼</button><button id="right">▶</button></div><div class="action"><button id="brake">SPACE · BRAKE</button><button id="enter">E · ENTER / EXIT</button></div></div>
  <div id="speed"><strong id="speednum">0</strong><small>KM/H</small><div style="font-size:9px;color:#9daec1;margin-top:3px" id="vehiclelabel">CAR · THIRD PERSON</div></div>
  <div id="righttools"><button id="vehicle">🚍 &nbsp; CHANGE VEHICLE</button><button id="view">◉ &nbsp; CAMERA</button></div>
 </main>
</div>
<script>
/* Load Three.js from multiple CDNs so one blocked host does not stop the app. */
function loadThreeJS(){
 const sources=[
  'https://cdnjs.cloudflare.com/ajax/libs/three.js/r152/three.min.js',
  'https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js',
  'https://unpkg.com/three@0.152.2/build/three.min.js'
 ];
 return new Promise((resolve,reject)=>{
  let index=0;
  const next=()=>{
   if(window.THREE){resolve();return;}
   if(index>=sources.length){reject(new Error('Unable to load Three.js from available CDNs.'));return;}
   const script=document.createElement('script');
   script.src=sources[index++];script.async=true;
   script.onload=()=>window.THREE?resolve():next();
   script.onerror=next;document.head.appendChild(script);
  };
  next();
 });
}
const loadingEl=document.getElementById('loading');
loadingEl.textContent='Loading 3D campus engine…';
loadThreeJS().then(()=>{
(()=> {
const $=id=>document.getElementById(id), canvas=$('scene');
const scene=new THREE.Scene();let night=false;
scene.background=new THREE.Color(0x8fb9d2);scene.fog=new THREE.Fog(0x8fb9d2,120,260);
const camera=new THREE.PerspectiveCamera(56,1,.1,600);camera.position.set(0,28,48);
const renderer=new THREE.WebGLRenderer({canvas,antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;renderer.outputColorSpace=THREE.SRGBColorSpace;
function resize(){const r=canvas.getBoundingClientRect();camera.aspect=r.width/r.height;camera.updateProjectionMatrix();renderer.setSize(r.width,r.height,false)}window.addEventListener('resize',resize);resize();
scene.add(new THREE.HemisphereLight(0xe5f3ff,0x526149,1.45));
const sun=new THREE.DirectionalLight(0xffedcf,2.1);sun.position.set(-45,80,35);sun.castShadow=true;sun.shadow.mapSize.set(2048,2048);sun.shadow.camera.left=-110;sun.shadow.camera.right=110;sun.shadow.camera.top=110;sun.shadow.camera.bottom=-110;scene.add(sun);
const mat=(c,r=.88)=>new THREE.MeshStandardMaterial({color:c,roughness:r});
const grass=mat(0x557d4e),asphalt=mat(0x343b43),cream=mat(0xe8dfcc),brick=mat(0x9e5546),roof=mat(0xb56b4f),glass=new THREE.MeshStandardMaterial({color:0x6f9eae,roughness:.25,metalness:.12}),white=mat(0xf0e9dc),green=mat(0x2d6a3d);
function cube(parent,x,y,z,w,h,d,m){const o=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),m);o.position.set(x,y+h/2,z);o.castShadow=true;o.receiveShadow=true;parent.add(o);return o}
cube(scene,0,-.4,0,190,.8,150,grass);
function road(x,z,w,d){cube(scene,x,.02,z,w,.12,d,asphalt);if(w>d){for(let a=-Math.floor(w/7);a<=Math.floor(w/7);a++)cube(scene,x+a*7,.09,z,.16,.015,.38,white)}else{for(let a=-Math.floor(d/7);a<=Math.floor(d/7);a++)cube(scene,x,.09,z+a*7,.38,.015,.16,white)}}
road(0,0,190,10);road(0,-42,148,8);road(0,42,148,8);road(-58,0,8,92);road(58,0,8,92);road(0,62,148,7);road(0,0,7,120);
function path(x,z,w,d){cube(scene,x,.11,z,w,.08,d,mat(0xc8bda9))}
path(-25,-20,44,3);path(28,-20,46,3);path(-25,20,44,3);path(28,20,46,3);path(0,0,3,80);
const destinations=[
 {name:'Main Entrance',x:0,z:68,kind:'gate'},
 {name:'Administrative Block',x:-27,z:-27,kind:'building'},
 {name:'Academic Block',x:25,z:-27,kind:'building'},
 {name:'Library',x:-27,z:25,kind:'building'},
 {name:'Science Laboratories',x:25,z:25,kind:'building'},
 {name:'Auditorium',x:66,z:-23,kind:'building'},
 {name:'Canteen',x:66,z:22,kind:'building'},
 {name:'Hostel',x:-70,z:-20,kind:'building'},
 {name:'Playground',x:-70,z:29,kind:'field'},
 {name:'Transport & Bus Area',x:0,z:59,kind:'building'}
];
function label(text,x,y,z){const c=document.createElement('canvas');c.width=512;c.height=96;const q=c.getContext('2d');q.fillStyle='rgba(35,22,27,.9)';q.roundRect(5,8,502,80,18);q.fill();q.fillStyle='#f8e8cb';q.font='bold 31px Arial';q.textAlign='center';q.fillText(text,256,60);const t=new THREE.CanvasTexture(c);const p=new THREE.Mesh(new THREE.PlaneGeometry(13,2.4),new THREE.MeshBasicMaterial({map:t,transparent:true,depthWrite:false}));p.position.set(x,y,z);p.rotation.x=-.18;scene.add(p)}
function building(name,x,z,w,d,h,accent=brick){
 const g=new THREE.Group();scene.add(g);
 cube(g,x,0,z,w,h,d,cream);cube(g,x,h,z,w+1,.7,d+1,accent);
 const floors=Math.max(2,Math.floor(h/3.7)),cols=Math.max(3,Math.floor(w/4.5));
 for(let f=0;f<floors;f++)for(let c=0;c<cols;c++){
  const xx=x-w/2+2.25+c*(w-4.5)/Math.max(1,cols-1);
  const yy=1.8+f*3.7;
  const win=new THREE.Mesh(new THREE.BoxGeometry(1.25,1.55,.12),glass);win.position.set(xx,yy,z+d/2+.07);g.add(win);
  const win2=win.clone();win2.position.z=z-d/2-.07;win2.rotation.y=Math.PI;g.add(win2);
 }
 cube(g,x,0,z+d/2+.3,Math.min(w*.55,12),.45,.45,accent);
 label(name,x,h+3,z+d/2+1);
 return g;
}
// Layout is a visual reconstruction from public campus references, not a surveyed building plan.
building('ADMINISTRATION',-27,-27,30,19,14);
building('ACADEMIC BLOCK',25,-27,31,19,15);
building('LIBRARY',-27,25,24,18,11);
building('SCIENCE LABS',25,25,28,18,13);
building('AUDITORIUM',66,-23,20,27,10,mat(0xc18a76));
building('CANTEEN',66,22,19,15,7,mat(0xc58b5c));
building('HOSTEL',-70,-20,23,28,14);
building('ACTIVITY / PLAYGROUND',-70,29,24,20,7);
building('TRANSPORT',0,55,17,10,5);
function tree(x,z,s=1){const t=new THREE.Mesh(new THREE.CylinderGeometry(.2*s,.3*s,2.1*s,7),mat(0x745039));t.position.set(x,1*s,z);scene.add(t);const c=new THREE.Mesh(new THREE.SphereGeometry(1.65*s,10,8),green);c.position.set(x,2.8*s,z);c.castShadow=true;scene.add(c)}
for(let x=-88;x<=88;x+=11){tree(x,-57,.8);tree(x,56,.8)}for(let z=-48;z<=48;z+=12){tree(-88,z,.8);tree(88,z,.8)}
for(let x=-45;x<=45;x+=10){tree(x,-8,.55);tree(x,8,.55)}
// Entrance arch and gate
cube(scene,-18,0,70,2,7,2,brick);cube(scene,18,0,70,2,7,2,brick);cube(scene,0,6,70,38,1.5,3,cream);cube(scene,0,5.2,71.65,24,.9,.18,brick);
label('BON SECOURS COLLEGE FOR WOMEN',0,8.2,72);
for(let x=-13;x<=13;x+=3){const post=cube(scene,x,.1,70,.13,4,.16,mat(0x222b32));}
for(let i=0;i<8;i++){cube(scene,-34+i*4,.12,47,.12,.02,8,white)}
// Playground markings
cube(scene,-70,.12,29,15,.03,10,mat(0x9a885a));
const ring=new THREE.Mesh(new THREE.RingGeometry(6.8,7,.9,64),white);ring.rotation.x=-Math.PI/2;ring.position.set(-70,.16,29);scene.add(ring);
// vehicle assembly
const carRoot=new THREE.Group();scene.add(carRoot);let vehicleType='car',speed=0,heading=0,driveMode=true,camMode=0;
function makeVehicle(type){
 while(carRoot.children.length)carRoot.remove(carRoot.children[0]);
 vehicleType=type;
 if(type==='walk'){
  const torso=new THREE.Mesh(new THREE.CapsuleGeometry(.48,.85,4,8),mat(0x315f9a));torso.position.y=1.15;carRoot.add(torso);
  const head=new THREE.Mesh(new THREE.SphereGeometry(.32,12,10),mat(0xc99b75));head.position.y=2.05;carRoot.add(head);return;
 }
 const bus=type==='bus',w=bus?3.2:2.05,l=bus?9.5:4.5;
 cube(carRoot,0,.45,0,w,bus?2.7:1.1,l,bus?mat(0xe6c64c):mat(0x9aaec2));
 cube(carRoot,0,bus?3.18:1.55,0,w*.88,bus?.85:.65,l*.48,glass);
 for(const z of [-l*.34,l*.34])for(const x of [-w*.57,w*.57]){const wh=new THREE.Mesh(new THREE.CylinderGeometry(bus?.53:.4,bus?.53:.4,.3,16),mat(0x15181d));wh.rotation.z=Math.PI/2;wh.position.set(x,.5,z);carRoot.add(wh)}
}
makeVehicle('car');carRoot.position.set(0,0,53);
const keys={};function setKey(k,v){keys[k]=v}
window.addEventListener('keydown',e=>{if(['ArrowUp','ArrowDown','ArrowLeft','ArrowRight','Space'].includes(e.code))e.preventDefault();keys[e.code]=true;if(e.code==='KeyR')resetVehicle();if(e.code==='KeyC')changeVehicle();if(e.code==='KeyE')changeVehicle()});
window.addEventListener('keyup',e=>keys[e.code]=false);
function bindHold(id,key){const b=$(id);b.addEventListener('pointerdown',e=>{e.preventDefault();setKey(key,true)});['pointerup','pointerleave','pointercancel'].forEach(ev=>b.addEventListener(ev,()=>setKey(key,false)))}
bindHold('up','ArrowUp');bindHold('down','ArrowDown');bindHold('left','ArrowLeft');bindHold('right','ArrowRight');bindHold('brake','Space');
function resetVehicle(){carRoot.position.set(0,0,53);heading=0;speed=0;toast('Vehicle returned to the main entrance')}
function changeVehicle(){const next=vehicleType==='car'?'bus':vehicleType==='bus'?'walk':'car';makeVehicle(next);toast('Mode changed: '+(next==='walk'?'Walk':next.toUpperCase()));$('vehiclelabel').textContent=next.toUpperCase()+' · THIRD PERSON'}
$('vehicle').onclick=changeVehicle;$('enter').onclick=()=>{makeVehicle(vehicleType==='walk'?'car':'walk');toast(vehicleType==='walk'?'Walking mode':'Vehicle mode')};
$('reset').onclick=resetVehicle;$('camera').onclick=()=>{camMode=(camMode+1)%3;toast(['Third-person camera','Driver camera','Top camera'][camMode])};$('view').onclick=$('camera').onclick;
$('weather').onclick=()=>{night=!night;scene.background.set(night?0x10182a:0x8fb9d2);scene.fog.color.set(night?0x10182a:0x8fb9d2);sun.intensity=night?.35:2.1;$('weatherlabel').textContent=night?'🌙 NIGHT':'☀️ DAYTIME';toast(night?'Night environment':'Day environment')};
function toast(msg){$('toast').textContent=msg;$('toast').classList.add('show');setTimeout(()=>$('toast').classList.remove('show'),1700)}
function gotoDest(d){carRoot.position.set(d.x,0,d.z+9);speed=0;toast('Navigation: '+d.name)}
$('placelist').innerHTML=destinations.map((d,i)=>`<div class="place"><span>📍 ${d.name}</span><button data-dest="${i}">GO</button></div>`).join('');
$('placelist').querySelectorAll('button').forEach(b=>b.onclick=()=>gotoDest(destinations[+b.dataset.dest]));
document.querySelectorAll('.nav button').forEach(b=>b.onclick=()=>{document.querySelectorAll('.nav button').forEach(x=>x.classList.remove('active'));b.classList.add('active');const m=b.dataset.mode;if(m==='drive'){makeVehicle('car');toast('Drive mode · WASD to drive')}if(m==='walk'){makeVehicle('walk');toast('Walk mode · use arrow keys')}if(m==='map'){$('mapcard').style.display='block';toast('Campus map overview')}if(m==='facilities')toast('Select a destination from Campus Destinations');if(m==='tour'){camMode=0;toast('Campus tour view')}});
function drawMini(){const c=$('mini'),ctx=c.getContext('2d');ctx.clearRect(0,0,420,220);ctx.fillStyle='#274b38';ctx.fillRect(0,0,420,220);ctx.strokeStyle='#aeb6ae';ctx.lineWidth=12;[[0,110,420,110],[210,0,210,220],[0,40,420,40],[0,180,420,180],[82,0,82,220],[338,0,338,220]].forEach(a=>{ctx.beginPath();ctx.moveTo(a[0],a[1]);ctx.lineTo(a[2],a[3]);ctx.stroke()});destinations.forEach(d=>{const x=210+d.x*1.8,y=110+d.z*1.35;ctx.fillStyle=d.kind==='building'?'#e7c89c':'#79b4cf';ctx.fillRect(x-7,y-5,14,10)});ctx.fillStyle='#ffdb78';ctx.beginPath();ctx.arc(210+carRoot.position.x*1.8,110+carRoot.position.z*1.35,5,0,Math.PI*2);ctx.fill()}
let last=performance.now();
function animate(now){requestAnimationFrame(animate);const dt=Math.min((now-last)/16.67,2);last=now;
 const max=vehicleType==='walk'?.12:vehicleType==='bus'?.38:.58;
 if(keys.ArrowUp||keys.KeyW)speed=Math.min(max,speed+.012*dt);else if(keys.ArrowDown||keys.KeyS)speed=Math.max(-max*.45,speed-.012*dt);else speed*=Math.pow(.975,dt);
 if(keys.Space)speed*=.84;
 const turn=(keys.ArrowLeft||keys.KeyA?1:0)-(keys.ArrowRight||keys.KeyD?1:0);heading+=turn*.026*dt*(Math.abs(speed)>.012?Math.sign(speed):1);
 carRoot.rotation.y=heading;carRoot.position.x+=Math.sin(heading)*speed*dt*2.2;carRoot.position.z+=Math.cos(heading)*speed*dt*2.2;
 carRoot.position.x=THREE.MathUtils.clamp(carRoot.position.x,-88,88);carRoot.position.z=THREE.MathUtils.clamp(carRoot.position.z,-68,72);
 let target,cam;
 if(camMode===2){cam=new THREE.Vector3(carRoot.position.x,100,carRoot.position.z+.1);target=new THREE.Vector3(carRoot.position.x,0,carRoot.position.z)}
 else if(camMode===1){cam=new THREE.Vector3(carRoot.position.x,carRoot.position.y+3,carRoot.position.z-1).add(new THREE.Vector3(0,0,0).applyAxisAngle(new THREE.Vector3(0,1,0),heading));target=cam.clone().add(new THREE.Vector3(Math.sin(heading)*15,0,Math.cos(heading)*15))}
 else{const off=new THREE.Vector3(0,8,-15).applyAxisAngle(new THREE.Vector3(0,1,0),heading);cam=carRoot.position.clone().add(off);target=carRoot.position.clone().add(new THREE.Vector3(0,1,0))}
 camera.position.lerp(cam,.075);camera.lookAt(target);
 $('speednum').textContent=Math.round(Math.abs(speed)*115);drawMini();renderer.render(scene,camera)}
requestAnimationFrame(animate);
$('loading').style.display='none';
})()
}).catch(error=>{
 console.error('Campus 3D initialization failed:',error);
 loadingEl.innerHTML='<div style="max-width:420px;padding:24px;text-align:center;line-height:1.7"><b style="font-size:16px">3D campus could not be loaded</b><br><span style="opacity:.8">The 3D library could not be reached. Check your internet connection, then retry.</span><br><button onclick="location.reload()" style="margin-top:14px;padding:10px 18px;border:0;border-radius:8px;background:#a64d65;color:white;font-weight:700;cursor:pointer">Retry loading</button></div>';
});
</script>
</body>
</html>
""", height=850, scrolling=False)

st.caption("Accuracy note: this is a detailed playable concept reconstruction using publicly described campus facilities and a plausible internal layout. It is not a verified survey-grade replica; exact block footprints and road geometry require official campus plans or measured imagery.")

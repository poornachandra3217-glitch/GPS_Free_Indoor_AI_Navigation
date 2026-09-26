const camera=document.getElementById("camera");
const canvas=document.getElementById("canvas");
const localization=document.getElementById("localization");
const start=document.getElementById("start");
const destination=document.getElementById("destination");

async function loadNodes(){
 const res=await fetch("/map"), data=await res.json();
 Object.keys(data.nodes).forEach(node=>{
  for(const select of [start,destination]){
   const o=document.createElement("option");
   o.value=node;o.textContent=node.replaceAll("_"," ");select.appendChild(o);
  }
 });
}
document.getElementById("startCamera").onclick=async()=>{
 try{camera.srcObject=await navigator.mediaDevices.getUserMedia({video:{facingMode:"environment"},audio:false});}
 catch(e){localization.textContent="Camera permission unavailable. Use image upload instead.";}
};
async function localizeBlob(blob){
 const fd=new FormData();fd.append("image",blob,"capture.jpg");
 localization.textContent="Analyzing visual features locally...";
 const res=await fetch("/localize",{method:"POST",body:fd}),data=await res.json();
 localization.innerHTML=`<strong>${data.message}</strong><br>Confidence: ${data.confidence??0}%<br>Good feature matches: ${data.good_matches??0}`;
 if(data.best_node)start.value=data.best_node;
}
document.getElementById("capture").onclick=()=>{
 if(!camera.srcObject){localization.textContent="Start the camera first.";return;}
 canvas.width=camera.videoWidth;canvas.height=camera.videoHeight;
 canvas.getContext("2d").drawImage(camera,0,0);canvas.toBlob(localizeBlob,"image/jpeg",0.9);
};
document.getElementById("upload").onchange=e=>{const f=e.target.files[0];if(f)localizeBlob(f);};
document.getElementById("route").onclick=async()=>{
 const res=await fetch("/route",{method:"POST",headers:{"Content-Type":"application/json"},
 body:JSON.stringify({start:start.value,destination:destination.value})});
 const data=await res.json();
 document.getElementById("routeResult").innerHTML=data.found
 ? `<strong>${data.message}</strong><br>Approx. route distance: ${data.distance} m`
 : "No route found.";
};
loadNodes();

from pathlib import Path
p=Path("GematriaLabAndroid/app/src/main/assets/index.html")
s=p.read_text()
date_start='<section class="view" id="view-dates">'
if date_start not in s: raise SystemExit("Date view not found")
panel = """
 <div class="card gem-date-card">
  <h2>Date Calculator</h2>
  <div class="gem-date-options">
   <label><input type="checkbox" id="classic-table" checked> Classic Table</label>
   <label><input type="checkbox" id="duration-variations" checked> Duration Variations</label>
   <label><input type="checkbox" id="date1-offset" checked> +/- Date 1</label>
  </div>
  <div class="gem-date-pair">
   <div class="gem-date-block"><h3>Date 1</h3><div class="mdy"><label>Month<input id="g-date1-month" type="number" min="1" max="12" inputmode="numeric"></label><label>Day<input id="g-date1-day" type="number" min="1" max="31" inputmode="numeric"></label><label>Year<input id="g-date1-year" type="number" min="1" max="9999" inputmode="numeric"></label></div></div>
   <div class="gem-date-block"><h3>Date 2</h3><div class="mdy"><label>Month<input id="g-date2-month" type="number" min="1" max="12" inputmode="numeric"></label><label>Day<input id="g-date2-day" type="number" min="1" max="31" inputmode="numeric"></label><label>Year<input id="g-date2-year" type="number" min="1" max="9999" inputmode="numeric"></label></div></div>
  </div>
  <div class="gem-date-controls"><label><input type="radio" name="g-date-op" value="add" checked> Add</label><label><input type="radio" name="g-date-op" value="subtract"> Subtract</label><span class="muted small">Date 1 plus or minus duration</span></div>
  <div class="gem-duration-grid"><label>Years<input id="g-years" type="number" min="0" value="0"></label><label>Months<input id="g-months" type="number" min="0" value="0"></label><label>Weeks<input id="g-weeks" type="number" min="0" value="0"></label><label>Days<input id="g-days" type="number" min="0" value="0"></label></div>
  <div class="actions"><button class="btn primary" id="g-calc-duration">Calculate Duration</button><button class="btn ghost" id="g-use-today">Date 1 = Today</button><button class="btn ghost" id="g-swap-dates">Swap Dates</button></div>
  <div class="gem-date-output" id="g-date-output"></div>
  <div class="gem-date-classic" id="g-classic-output"></div>
  <div class="gem-date-variations" id="g-variations-output"></div>
  <div class="gem-date-offset" id="g-offset-output"></div>
 </div>
"""
s=s.replace(date_start,date_start+"\n"+panel,1)
css = """
/* Gematrinator Date Calculator-inspired classic layout */
.gem-date-card{border-radius:4px;background:#24272a;border-color:#555b60}
.gem-date-options,.gem-date-controls{display:flex;gap:16px;flex-wrap:wrap;align-items:center;padding:9px 10px;background:#1b1e20;border:1px solid #4a5054;border-radius:3px;margin:9px 0;font-size:12px}
.gem-date-options label,.gem-date-controls label{display:flex;align-items:center;gap:6px}
.gem-date-options input,.gem-date-controls input{accent-color:#239b58}
.gem-date-pair{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.gem-date-block{background:#1b1f21;border:1px solid #4e555a;border-radius:3px;padding:10px}
.gem-date-block h3{margin:0 0 8px;font-size:13px}
.mdy{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:7px}
.mdy label,.gem-duration-grid label{font-size:11px;color:#c8d0d4;display:flex;flex-direction:column;gap:5px}
.mdy input,.gem-duration-grid input{width:100%;min-width:0;background:#101315;border:1px solid #697177;color:#f2f5f6;border-radius:3px;padding:9px 7px;font-size:14px}
.gem-duration-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin:10px 0}
.gem-date-output{font-size:17px;font-weight:800;color:#70d995;padding:12px 4px;border-bottom:1px solid #4a5054}
.gem-date-classic,.gem-date-variations,.gem-date-offset{margin-top:10px}
.gem-date-classic .table td:last-child{text-align:right}
.gem-date-classic .table tr:nth-child(even){background:#1c2022}
.gem-date-classic .table th{background:#343a3e}
.gem-date-variations{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:7px}
.gem-variation{background:#1a1e20;border:1px solid #4b5358;border-radius:3px;padding:8px}
.gem-variation b{display:block;color:#79d99b;font-size:14px}
.gem-variation span{font-size:10px;color:#bbc4c9}
@media(max-width:560px){.gem-date-pair{grid-template-columns:1fr}.gem-duration-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.gem-date-options{gap:9px}.gem-date-variations{grid-template-columns:1fr 1fr}}
"""
s=s.replace("</style>",css+"\n</style>",1)
js = r'''
(function(){
 const $=id=>document.getElementById(id);
 const ids=["g-date1-month","g-date1-day","g-date1-year","g-date2-month","g-date2-day","g-date2-year","g-years","g-months","g-weeks","g-days"];
 const today=new Date();
 function parts(d,p){$(p+"-month").value=d.getMonth()+1;$(p+"-day").value=d.getDate();$(p+"-year").value=d.getFullYear();}
 function read(p){let m=+$ (p+"-month").value,d=+$ (p+"-day").value,y=+$ (p+"-year").value;if(!m||!d||!y)return null;let x=new Date(y,m-1,d);return x.getFullYear()===y&&x.getMonth()===m-1&&x.getDate()===d?x:null;}
 function fmt(d){return d.toLocaleDateString("en-US",{month:"long",day:"numeric",year:"numeric"});}
 function dayDiff(a,b){return Math.round((Date.UTC(b.getFullYear(),b.getMonth(),b.getDate())-Date.UTC(a.getFullYear(),a.getMonth(),a.getDate()))/86400000);}
 function addMonths(d,n){let x=new Date(d),day=x.getDate();x.setDate(1);x.setMonth(x.getMonth()+n);let last=new Date(x.getFullYear(),x.getMonth()+1,0).getDate();x.setDate(Math.min(day,last));return x;}
 function calc(){
  const a=read("g-date1"),b=read("g-date2"),out=$("g-date-output");
  if(!a||!b){out.textContent="Enter valid Month / Day / Year values for both dates.";return;}
  const delta=dayDiff(a,b),abs=Math.abs(delta),yrs=Math.floor(abs/365.2425),months=Math.floor(abs/30.436875),weeks=Math.floor(abs/7);
  out.textContent="Time Between Dates: "+abs.toLocaleString()+" days "+(delta===0?"(Same date)":delta>0?"(Date 2 is after Date 1)":"(Date 2 is before Date 1)");
  if($("classic-table").checked){
   const rows=[["Date 1",fmt(a)],["Date 2",fmt(b)],["Days",abs.toLocaleString()],["Weeks",weeks+" weeks, "+(abs%7)+" days"],["Approx. months",months],["Approx. years",(abs/365.2425).toFixed(2)],["Day of year (Date 1)",Math.floor((a-new Date(a.getFullYear(),0,0))/86400000)],["Day of year (Date 2)",Math.floor((b-new Date(b.getFullYear(),0,0))/86400000)]];
   $("g-classic-output").innerHTML='<table class="table"><tbody>'+rows.map(r=>'<tr><td>'+r[0]+'</td><td>'+r[1]+'</td></tr>').join("")+'</tbody></table>';
  }else $("g-classic-output").innerHTML="";
  if($("duration-variations").checked){
   const vals=[["Days",abs],["Weeks",+(abs/7).toFixed(2)],["Months",+(abs/30.436875).toFixed(2)],["Years",+(abs/365.2425).toFixed(3)],["Inclusive days",abs+1],["Business days",businessDays(a,b)]];
   $("g-variations-output").innerHTML=vals.map(v=>'<div class="gem-variation"><span>'+v[0]+'</span><b>'+Number(v[1]).toLocaleString()+'</b></div>').join("");
  }else $("g-variations-output").innerHTML="";
  offset();
 }
 function businessDays(a,b){let lo=a<b?a:b,hi=a<b?b:a,n=0;for(let d=new Date(lo);d<=hi;d.setDate(d.getDate()+1)){if(d.getDay()!==0&&d.getDay()!==6)n++;}return Math.max(0,n-1);}
 function offset(){
  const a=read("g-date1");if(!a)return;
  let sign=document.querySelector('input[name="g-date-op"]:checked').value==="add"?1:-1;
  let y=Math.max(0,+$("g-years").value||0)*sign,m=Math.max(0,+$("g-months").value||0)*sign,w=Math.max(0,+$("g-weeks").value||0)*sign,d=Math.max(0,+$("g-days").value||0)*sign;
  let x=addMonths(a,y*12+m);x.setDate(x.getDate()+w*7+d);
  $("g-offset-output").innerHTML="<div class='match'>Date 1 "+(sign>0?"plus":"minus")+" duration = <b>"+fmt(x)+"</b></div>";
 }
 $("g-calc-duration").addEventListener("click",()=>{calc();offset();});
 $("g-use-today").addEventListener("click",()=>{parts(today,"g-date1");calc();});
 $("g-swap-dates").addEventListener("click",()=>{let a=read("g-date1"),b=read("g-date2");if(a&&b){parts(b,"g-date1");parts(a,"g-date2");calc();}});
 ids.forEach(id=>$(id).addEventListener("change",()=>{calc();offset();}));
 ["classic-table","duration-variations","date1-offset"].forEach(id=>$(id).addEventListener("change",()=>{calc();}));
 $("date1-offset").addEventListener("change",()=>{$("g-offset-output").classList.toggle("hidden",!$("date1-offset").checked)});
 parts(today,"g-date1");parts(today,"g-date2");calc();
})();
'''
s=s.replace("</script>",js+"\n</script>",1)
p.write_text(s)
print("Gematrinator-style date calculator added")

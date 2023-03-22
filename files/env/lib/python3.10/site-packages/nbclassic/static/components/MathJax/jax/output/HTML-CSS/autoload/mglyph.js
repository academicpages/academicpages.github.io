/*
 *  /MathJax-v2/jax/output/HTML-CSS/autoload/mglyph.js
 *
 *  Copyright (c) 2009-2018 The MathJax Consortium
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

MathJax.Hub.Register.StartupHook("HTML-CSS Jax Ready",function(){var c="2.7.9";var a=MathJax.ElementJax.mml,b=MathJax.OutputJax["HTML-CSS"],d=MathJax.Localization;a.mglyph.Augment({toHTML:function(l,h){var k=l,m=this.getValues("src","width","height","valign","alt"),g;l=this.HTMLcreateSpan(l);if(m.src===""){var j=this.Get("index");if(j){h=this.HTMLgetVariant();var e=h.defaultFont;if(e){e.noStyleChar=true;e.testString=String.fromCharCode(j)+"ABCabc";if(b.Font.testFont(e)){this.HTMLhandleVariant(l,h,String.fromCharCode(j))}else{if(m.alt===""){m.alt=d._(["MathML","BadMglyphFont"],"Bad font: %1",e.family)}g=a.Error(m.alt,{mathsize:"75%"});this.Append(g);g.toHTML(l);this.data.pop();l.bbox=g.HTMLspanElement().bbox}}}}else{if(!this.img){this.img=a.mglyph.GLYPH[m.src]}if(!this.img){this.img=a.mglyph.GLYPH[m.src]={img:new Image(),status:"pending"};var i=this.img.img;i.onload=MathJax.Callback(["HTMLimgLoaded",this]);i.onerror=MathJax.Callback(["HTMLimgError",this]);i.src=m.src;MathJax.Hub.RestartAfter(i.onload)}if(this.img.status!=="OK"){g=a.Error(d._(["MathML","BadMglyph"],"Bad mglyph: %1",m.src),{mathsize:"75%"});this.Append(g);g.toHTML(l);this.data.pop();l.bbox=g.HTMLspanElement().bbox}else{var n=this.HTMLgetMu(l);var f=this.HTMLgetScale();i=b.addElement(l,"img",{isMathJax:true,src:m.src,alt:m.alt,title:m.alt});if(m.width){i.style.width=b.Em(b.length2em(m.width,n,this.img.img.width/b.em)*f)}if(m.height){i.style.height=b.Em(b.length2em(m.height,n,this.img.img.height/b.em)*f)}l.bbox.w=l.bbox.rw=i.offsetWidth/b.em;l.bbox.h=i.offsetHeight/b.em;if(m.valign){l.bbox.d=-b.length2em(m.valign,n,this.img.img.height/b.em)*f;i.style.verticalAlign=b.Em(-l.bbox.d);l.bbox.h-=l.bbox.d}}}if(!k.bbox){k.bbox={w:l.bbox.w,h:l.bbox.h,d:l.bbox.d,rw:l.bbox.rw,lw:l.bbox.lw}}else{if(l.bbox){k.bbox.w+=l.bbox.w;if(k.bbox.w>k.bbox.rw){k.bbox.rw=k.bbox.w}if(l.bbox.h>k.bbox.h){k.bbox.h=l.bbox.h}if(l.bbox.d>k.bbox.d){k.bbox.d=l.bbox.d}}}this.HTMLhandleSpace(l);this.HTMLhandleColor(l);return l},HTMLimgLoaded:function(f,e){if(typeof(f)==="string"){e=f}this.img.status=(e||"OK")},HTMLimgError:function(){this.img.img.onload("error")}},{GLYPH:{}});MathJax.Hub.Startup.signal.Post("HTML-CSS mglyph Ready");MathJax.Ajax.loadComplete(b.autoloadDir+"/mglyph.js")});

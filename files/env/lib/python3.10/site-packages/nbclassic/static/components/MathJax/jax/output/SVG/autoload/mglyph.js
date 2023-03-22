/*
 *  /MathJax-v2/jax/output/SVG/autoload/mglyph.js
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

MathJax.Hub.Register.StartupHook("SVG Jax Ready",function(){var d="2.7.9";var a=MathJax.ElementJax.mml,f=MathJax.OutputJax.SVG,b=f.BBOX,e=MathJax.Localization;var c="http://www.w3.org/1999/xlink";b.MGLYPH=b.Subclass({type:"image",removeable:false,Init:function(k,p,l,m,s,j,g){if(g==null){g={}}var i=k.width*1000/f.em,q=k.height*1000/f.em;var r=i,o=q,n=0;if(p!==""){i=f.length2em(p,s,r)*j;q=(r?i/r*o:0)}if(l!==""){q=f.length2em(l,s,o)*j;if(p===""){i=(o?q/o*r:0)}}if(m!==""&&m.match(/\d/)){n=f.length2em(m,s)*j;g.y=-n}g.height=Math.floor(q);g.width=Math.floor(i);g.transform="translate(0,"+q+") matrix(1 0 0 -1 0 0)";g.preserveAspectRatio="none";this.SUPER(arguments).Init.call(this,g);this.element.setAttributeNS(c,"href",k.SRC);this.w=this.r=i;this.h=this.H=q+n;this.d=this.D=-n;this.l=0}});a.mglyph.Augment({toSVG:function(j,h){this.SVGgetStyles();var l=this.SVG(),k,i;this.SVGhandleSpace(l);var m=this.getValues("src","width","height","valign","alt");if(m.src===""){m=this.getValues("index","fontfamily");if(m.index){if(!h){h=this.SVGgetScale()}var g={};if(m.fontfamily){g["font-family"]=m.fontfamily}l.Add(b.TEXT(h,String.fromCharCode(m.index),g))}}else{if(!this.img){this.img=a.mglyph.GLYPH[m.src]}if(!this.img){this.img=a.mglyph.GLYPH[m.src]={img:new Image(),status:"pending"};k=this.img.img;k.onload=MathJax.Callback(["SVGimgLoaded",this]);k.onerror=MathJax.Callback(["SVGimgError",this]);k.src=k.SRC=m.src;MathJax.Hub.RestartAfter(k.onload)}if(this.img.status!=="OK"){i=a.Error(e._(["MathML","BadMglyph"],"Bad mglyph: %1",m.src),{mathsize:"75%"});this.Append(i);l=i.toSVG();this.data.pop()}else{var o=this.SVGgetMu(l);var n=this.SVGgetScale();l.Add(b.MGLYPH(this.img.img,m.width,m.height,m.valign,o,n,{"aria-label":m.alt}))}}l.Clean();this.SVGhandleColor(l);this.SVGsaveData(l);return l},SVGimgLoaded:function(h,g){if(typeof(h)==="string"){g=h}this.img.status=(g||"OK")},SVGimgError:function(){this.img.img.onload("error")}},{GLYPH:{}});MathJax.Hub.Startup.signal.Post("SVG mglyph Ready");MathJax.Ajax.loadComplete(f.autoloadDir+"/mglyph.js")});

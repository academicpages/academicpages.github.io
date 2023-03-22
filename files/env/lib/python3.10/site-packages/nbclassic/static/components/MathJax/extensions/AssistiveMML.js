/*
 *  /MathJax-v2/extensions/AssistiveMML.js
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

(function(a,e,b,f){var c=b.config.menuSettings;var d=MathJax.Extension.AssistiveMML={version:"2.7.9",config:b.CombineConfig("AssistiveMML",{disabled:false,styles:{".MJX_Assistive_MathML":{position:"absolute!important",top:0,left:0,clip:(b.Browser.isMSIE&&(document.documentMode||0)<8?"rect(1px 1px 1px 1px)":"rect(1px, 1px, 1px, 1px)"),padding:"1px 0 0 0!important",border:"0!important",height:"1px!important",width:"1px!important",overflow:"hidden!important",display:"block!important","-webkit-touch-callout":"none","-webkit-user-select":"none","-khtml-user-select":"none","-moz-user-select":"none","-ms-user-select":"none","user-select":"none"},".MJX_Assistive_MathML.MJX_Assistive_MathML_Block":{width:"100%!important"}}}),Config:function(){if(!this.config.disabled&&c.assistiveMML==null){b.Config({menuSettings:{assistiveMML:true}})}a.Styles(this.config.styles);b.Register.MessageHook("End Math",function(g){if(c.assistiveMML){return d.AddAssistiveMathML(g[1])}})},AddAssistiveMathML:function(g){var h={jax:b.getAllJax(g),i:0,callback:MathJax.Callback({})};this.HandleMML(h);return h.callback},RemoveAssistiveMathML:function(k){var h=b.getAllJax(k),l;for(var j=0,g=h.length;j<g;j++){l=document.getElementById(h[j].inputID+"-Frame");if(l&&l.getAttribute("data-mathml")){l.removeAttribute("data-mathml");if(l.lastChild&&l.lastChild.className.match(/MJX_Assistive_MathML/)){l.removeChild(l.lastChild)}}}},HandleMML:function(n){var h=n.jax.length,i,j,o,k;var g=MathJax.ElementJax.mml;g.copyAttributes.id=1;while(n.i<h){i=n.jax[n.i];o=document.getElementById(i.inputID+"-Frame");if(i.outputJax!=="NativeMML"&&i.outputJax!=="PlainSource"&&o&&!o.getAttribute("data-mathml")){try{j=i.root.toMathML("").replace(/\n */g,"").replace(/<!--.*?-->/g,"")}catch(l){g.copyAttributes.id=true;if(!l.restart){throw l}return MathJax.Callback.After(["HandleMML",this,n],l.restart)}o.setAttribute("data-mathml",j);k=f.addElement(o,"span",{isMathJax:true,unselectable:"on",className:"MJX_Assistive_MathML"+(i.root.Get("display")==="block"?" MJX_Assistive_MathML_Block":"")});try{k.innerHTML=j}catch(l){}o.style.position="relative";o.setAttribute("role","presentation");o.firstChild.setAttribute("aria-hidden","true");k.setAttribute("role","presentation")}n.i++}g.copyAttributes.id=true;n.callback()}};b.Startup.signal.Post("AssistiveMML Ready")})(MathJax.Ajax,MathJax.Callback,MathJax.Hub,MathJax.HTML);MathJax.Callback.Queue(["Require",MathJax.Ajax,"[MathJax]/extensions/toMathML.js"],["loadComplete",MathJax.Ajax,"[MathJax]/extensions/AssistiveMML.js"],function(){MathJax.Hub.Register.StartupHook("End Config",["Config",MathJax.Extension.AssistiveMML])});

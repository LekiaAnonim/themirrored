(()=>{"use strict";var e,r={923:(e,r,o)=>{var t=o(5311),n=o.n(t);window.createTaskChooser=function(e){const r=n()("#"+e+"-chooser"),o=r.find("[data-chooser-title]"),t=n()("#"+e),a=r.find("[data-chooser-edit-link]");n()("[data-chooser-action-choose]",r).on("click",(()=>{ModalWorkflow({url:r.data("chooserUrl"),onload:TASK_CHOOSER_MODAL_ONLOAD_HANDLERS,responses:{taskChosen(e){t.val(e.id),o.text(e.name),r.removeClass("blank"),a.attr("href",e.edit_url)}}})}))}},5311:e=>{e.exports=jQuery}},o={};function t(e){var n=o[e];if(void 0!==n)return n.exports;var a=o[e]={exports:{}};return r[e](a,a.exports,t),a.exports}t.m=r,e=[],t.O=(r,o,n,a)=>{if(!o){var i=1/0;for(d=0;d<e.length;d++){for(var[o,n,a]=e[d],l=!0,s=0;s<o.length;s++)(!1&a||i>=a)&&Object.keys(t.O).every((e=>t.O[e](o[s])))?o.splice(s--,1):(l=!1,a<i&&(i=a));if(l){e.splice(d--,1);var c=n();void 0!==c&&(r=c)}}return r}a=a||0;for(var d=e.length;d>0&&e[d-1][2]>a;d--)e[d]=e[d-1];e[d]=[o,n,a]},t.n=e=>{var r=e&&e.__esModule?()=>e.default:()=>e;return t.d(r,{a:r}),r},t.d=(e,r)=>{for(var o in r)t.o(r,o)&&!t.o(e,o)&&Object.defineProperty(e,o,{enumerable:!0,get:r[o]})},t.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),t.o=(e,r)=>Object.prototype.hasOwnProperty.call(e,r),t.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},t.j=343,(()=>{var e={343:0};t.O.j=r=>0===e[r];var r=(r,o)=>{var n,a,[i,l,s]=o,c=0;if(i.some((r=>0!==e[r]))){for(n in l)t.o(l,n)&&(t.m[n]=l[n]);if(s)var d=s(t)}for(r&&r(o);c<i.length;c++)a=i[c],t.o(e,a)&&e[a]&&e[a][0](),e[a]=0;return t.O(d)},o=globalThis.webpackChunkwagtail=globalThis.webpackChunkwagtail||[];o.forEach(r.bind(null,0)),o.push=r.bind(null,o.push.bind(o))})();var n=t.O(void 0,[751],(()=>t(923)));n=t.O(n)})();
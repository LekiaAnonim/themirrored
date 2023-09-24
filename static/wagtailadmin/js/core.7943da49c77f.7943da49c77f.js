(()=>{"use strict";var e,t={3394:(e,t,r)=>{var s=r(5311),i=r.n(s),n=r(6599),a=r(434);class o extends n.Qr{click(){this.element.click()}post(e){e.preventDefault(),e.stopPropagation();const t=document.createElement("form");t.action=this.urlValue,t.method="POST";const r=document.createElement("input");if(r.type="hidden",r.name="csrfmiddlewaretoken",r.value=a.QF.CSRF_TOKEN,t.appendChild(r),!this.continueValue){const e=document.createElement("input");e.type="hidden",e.name="next",e.value=window.location.href,t.appendChild(e)}document.body.appendChild(t),t.submit()}redirect(e){const t=e?.params?.url??e?.detail?.url??this.element.value;t&&window.location.assign(t)}}o.values={continue:{type:Boolean,default:!1},url:String};var l=new Map;function c(e){var t=l.get(e);t&&t.destroy()}function u(e){var t=l.get(e);t&&t.update()}var h=null;"undefined"==typeof window?((h=function(e){return e}).destroy=function(e){return e},h.update=function(e){return e}):((h=function(e,t){return e&&Array.prototype.forEach.call(e.length?e:[e],(function(e){return function(e){if(e&&e.nodeName&&"TEXTAREA"===e.nodeName&&!l.has(e)){var t,r=null,s=window.getComputedStyle(e),i=(t=e.value,function(){a({testForHeightReduction:""===t||!e.value.startsWith(t),restoreTextAlign:null}),t=e.value}),n=function(t){e.removeEventListener("autosize:destroy",n),e.removeEventListener("autosize:update",o),e.removeEventListener("input",i),window.removeEventListener("resize",o),Object.keys(t).forEach((function(r){return e.style[r]=t[r]})),l.delete(e)}.bind(e,{height:e.style.height,resize:e.style.resize,textAlign:e.style.textAlign,overflowY:e.style.overflowY,overflowX:e.style.overflowX,wordWrap:e.style.wordWrap});e.addEventListener("autosize:destroy",n),e.addEventListener("autosize:update",o),e.addEventListener("input",i),window.addEventListener("resize",o),e.style.overflowX="hidden",e.style.wordWrap="break-word",l.set(e,{destroy:n,update:o}),o()}function a(t){var i,n,o=t.restoreTextAlign,l=void 0===o?null:o,c=t.testForHeightReduction,u=void 0===c||c,h=s.overflowY;if(0!==e.scrollHeight&&("vertical"===s.resize?e.style.resize="none":"both"===s.resize&&(e.style.resize="horizontal"),u&&(i=function(e){for(var t=[];e&&e.parentNode&&e.parentNode instanceof Element;)e.parentNode.scrollTop&&t.push([e.parentNode,e.parentNode.scrollTop]),e=e.parentNode;return function(){return t.forEach((function(e){var t=e[0],r=e[1];t.style.scrollBehavior="auto",t.scrollTop=r,t.style.scrollBehavior=null}))}}(e),e.style.height=""),n="content-box"===s.boxSizing?e.scrollHeight-(parseFloat(s.paddingTop)+parseFloat(s.paddingBottom)):e.scrollHeight+parseFloat(s.borderTopWidth)+parseFloat(s.borderBottomWidth),"none"!==s.maxHeight&&n>parseFloat(s.maxHeight)?("hidden"===s.overflowY&&(e.style.overflow="scroll"),n=parseFloat(s.maxHeight)):"hidden"!==s.overflowY&&(e.style.overflow="hidden"),e.style.height=n+"px",l&&(e.style.textAlign=l),i&&i(),r!==n&&(e.dispatchEvent(new Event("autosize:resized",{bubbles:!0})),r=n),h!==s.overflow&&!l)){var d=s.textAlign;"hidden"===s.overflow&&(e.style.textAlign="start"===d?"end":"start"),a({restoreTextAlign:d,testForHeightReduction:!0})}}function o(){a({testForHeightReduction:!0,restoreTextAlign:null})}}(e)})),e}).destroy=function(e){return e&&Array.prototype.forEach.call(e.length?e:[e],c),e},h.update=function(e){return e&&Array.prototype.forEach.call(e.length?e:[e],u),e});const d=h;var p=r(9437);class g extends n.Qr{resize(){d.update(this.element)}initialize(){this.resize=(0,p.D)(this.resize.bind(this),50)}connect(){d(this.element),this.resizeObserver=new ResizeObserver(this.resize),this.resizeObserver.observe(this.element)}disconnect(){this.resizeObserver?.disconnect(),d.destroy(this.element)}}class m extends n.Qr{get activeItems(){return this.itemTargets.filter((({disabled:e})=>!e))}connect(){this.toggle()}toggle(){const e=!this.activeItems.some((e=>!e.checked));this.allTargets.forEach((t=>{t.checked=e}))}toggleAll(e){const t=e?.params?.force,r=e.target,s="boolean"==typeof t?t:r.checked;this.activeItems.forEach((e=>{e.checked!==s&&(e.checked=s,e.dispatchEvent(new Event("change",{bubbles:!0})))})),this.toggle()}}m.targets=["all","item"];var f=r(9408);class b extends n.Qr{connect(){this.count()}count(){return this.totalValue=[...document.querySelectorAll(this.containerValue||"body")].map((e=>e.querySelectorAll(this.findValue).length)).reduce(((e,t)=>e+t),0),this.totalValue}getLabel(e){const t=(0,f.qP)("%(num)s error","%(num)s errors",e);if(this.labelsValue.length>1){const[t,r=this.labelsValue[1],s="__total__"]=this.labelsValue;return(0,f.qP)(t,r,e).replace(s,`${e}`)}return t.replace("%(num)s",`${e}`)}minValueChanged(){this.totalValueChanged(this.count())}totalValueChanged(e){const t=this.minValue;this.hasActiveClass&&this.element.classList.toggle(this.activeClass,e>t),this.hasLabelTarget&&(this.labelTarget.textContent=e>t?this.getLabel(e):""),this.hasTotalTarget&&(this.totalTarget.textContent=e>t?`${e}`:"")}}b.classes=["active"],b.targets=["label","total"],b.values={container:{default:"body",type:String},find:{default:".error-message,.help-critical",type:String},labels:{default:[],type:Array},min:{default:0,type:Number},total:{default:0,type:Number}};var y=r(8054);class v extends n.Qr{toggle(){var e;this.idValue&&(this.element.classList.add(this.dismissedClass),this.dismissedValue=!0,e={[this.idValue]:!0},fetch(a.QF.ADMIN_URLS?.DISMISSIBLES,{method:"PATCH",headers:{[a.QF.CSRF_HEADER_NAME]:a.QF.CSRF_TOKEN,"Content-Type":"application/json"},body:JSON.stringify(e),mode:"same-origin"}))}}v.classes=["dismissed"],v.values={dismissed:{default:!1,type:Boolean},id:{default:"",type:String}};var w=r(8689),T=r(7107);class E extends n.Qr{connect(){this.tippy=(0,w.ZP)(this.toggleTarget,this.options)}hide(){this.tippy?.hide()}show(){this.tippy?.show()}get options(){const e=this.toggleTarget.getAttribute("aria-label");let t;this.hasContentTarget&&(this.contentTarget.hidden=!1),e&&(t=(0,w.ZP)(this.toggleTarget,{content:e,placement:"bottom",plugins:[T.UW]}));const r=[T.UW,T.FP,T.Dx];this.hideOnClickValue&&r.push(T.ac);const s=()=>{this.dispatch("shown",{target:((e="document")=>window[e])()})};return{...this.hasContentTarget?{content:this.contentTarget}:{},trigger:"click",interactive:!0,theme:"dropdown",placement:"bottom",plugins:r,onShow(){t&&t.disable()},onShown(){s()},onHide(){t&&t.enable()}}}}E.targets=["toggle","content"],E.values={hideOnClick:{default:!1,type:Boolean}};class S extends n.Qr{add(e){const{clear:t=!1,text:r="",type:s}=e?.detail||{};this.hasAddedClass&&this.element.classList.add(this.addedClass),t&&this.clear();const i=(s&&this.templateTargets.find((({dataset:e})=>e.type===s))||this.templateTarget).content.firstElementChild?.cloneNode(!0);if(i instanceof HTMLElement){const e=i.lastElementChild;e instanceof HTMLElement&&r&&(e.textContent=r),this.containerTarget.appendChild(i),this.dispatch("added"),this.hasShowClass&&setTimeout((()=>{this.element.classList.add(this.showClass)}),this.showDelayValue)}}clear(){this.containerTarget.innerHTML=""}}S.classes=["added","show"],S.targets=["container","template"],S.values={showDelay:{default:100,type:Number}};const A="button-longrunning";class C extends n.Qr{static afterLoad(e,t){const{controllerAttribute:r}=t.schema,{actionAttribute:s}=t.schema;document.addEventListener("DOMContentLoaded",(()=>{window.cancelSpinner=()=>{const t=`data-${e}-loading-value`;document.querySelectorAll(`[${t}~="true"]`).forEach((e=>{e.removeAttribute(t)}))},document.querySelectorAll(`.${A}:not([${r}~='${e}'])`).forEach((t=>{t.setAttribute(r,[t.getAttribute(r)||"",e].filter(Boolean).join(" ")),t.setAttribute(s,[t.getAttribute(s)||"",`${e}#activate`].filter(Boolean).join(" "));const i=t.getAttribute("data-clicked-text");i&&(t.setAttribute(`data-${e}-active-value`,i),t.removeAttribute("data-clicked-text"))}))}),{once:!0,passive:!0})}connect(){if(this.hasLabelTarget)return;const e=this.element.querySelector("em");e&&e.setAttribute(`data-${this.identifier}-target`,"label")}activate(){const e=this.element.closest("form");e&&e.checkValidity&&!e.noValidate&&!e.checkValidity()||window.setTimeout((()=>{this.loadingValue=!0,this.timer=window.setTimeout((()=>{this.loadingValue=!1}),this.durationValue)}))}loadingValueChanged(e){const t=this.hasActiveClass?this.activeClass:`${A}-active`;this.element.classList.toggle(t,e),this.labelValue||(this.labelValue=this.hasLabelTarget?this.labelTarget.textContent:this.element.textContent),e?(this.element.setAttribute("disabled",""),this.activeValue&&this.hasLabelTarget&&(this.labelTarget.textContent=this.activeValue)):(this.element.removeAttribute("disabled"),this.labelValue&&this.hasLabelTarget&&(this.labelTarget.textContent=this.labelValue))}disconnect(){this.timer&&clearTimeout(this.timer)}}C.classes=["active"],C.targets=["label"],C.values={active:{default:"",type:String},duration:{default:3e4,type:Number},label:{default:"",type:String},loading:{default:!1,type:Boolean}};class V extends n.Qr{connect(){this.skipToTarget=document.querySelector(this.element.getAttribute("href")||"main")}handleBlur(){this.skipToTarget&&(this.skipToTarget.removeAttribute("tabindex"),this.skipToTarget.removeEventListener("blur",this.handleBlur),this.skipToTarget.removeEventListener("focusout",this.handleBlur))}skip(){this.skipToTarget&&(this.skipToTarget.setAttribute("tabindex","-1"),this.skipToTarget.addEventListener("blur",this.handleBlur),this.skipToTarget.addEventListener("focusout",this.handleBlur),this.skipToTarget.focus())}}var x=r(5447);class L extends n.Qr{compare(e){if(!this.element.value)return!0;const t=this[e.detail?.compareAs||e.params?.compareAs||"slugify"]({detail:{value:e.detail?.value||""}},!0),r=this.element.value,s=t.trim()===r.trim();return s||e?.preventDefault(),s}slugify(e,t=!1){const r=this.allowUnicodeValue,{value:s=this.element.value}=e?.detail||{},i=(0,x.J)(s.trim(),!1,{unicodeSlugsEnabled:r});return t||(this.element.value=i),i}urlify(e,t=!1){const r=this.allowUnicodeValue,{value:s=this.element.value}=e?.detail||{},i=(0,x.J)(s.trim(),!0,{unicodeSlugsEnabled:r});return t||(this.element.value=i),i}}L.values={allowUnicode:{default:!1,type:Boolean}};class R extends n.Qr{submit(){const e=this.element.form;if(!e)throw new Error(`${this.identifier} controlled element must be part of a <form />`);e.requestSubmit?e.requestSubmit():e.submit()}}const k=async()=>{"loading"===document.readyState&&await new Promise((e=>{document.addEventListener("DOMContentLoaded",(()=>e()),{once:!0,passive:!0})}))};class O extends n.Qr{static afterLoad(e){k().then((()=>{const{termInput:t,targetOutput:r,url:s}=window.headerSearch||{},i=t?document.querySelector(t):null,n=i?.form;n&&(i.hasAttribute(`data-${e}-target`)||i.setAttribute(`data-${e}-target`,"input"),Object.entries({"data-controller":e,"data-action":[`change->${e}#searchLazy`,`input->${e}#searchLazy`].join(" "),[`data-${e}-src-value`]:s,[`data-${e}-target-value`]:r}).forEach((([e,t])=>{n.hasAttribute(e)||n.setAttribute(e,t)})))}))}connect(){const e=this.hasInputTarget?this.inputTarget.form:this.element;this.srcValue=this.srcValue||e?.getAttribute("action")||"",this.targetElement=this.getTarget(this.targetValue),this.iconElement=null;const t=(this.hasInputTarget?this.inputTarget:this.element).parentElement;this.iconElement=t?.querySelector("use")||null,this.iconValue=this.iconElement?.getAttribute("href")||"",this.loadingValue=!1,this.replaceLazy=(0,p.D)(this.replace.bind(this),this.waitValue),this.searchLazy=(0,p.D)(this.search.bind(this),this.waitValue),this.submitLazy=(0,p.D)(this.submit.bind(this),this.waitValue),this.dispatch("ready",{cancelable:!1})}getTarget(e=this.targetValue){const t=document.querySelector(e),r=t&&t instanceof HTMLElement,s=!!this.srcValue,i=[];if(r||i.push(`Cannot find valid target element at "${e}"`),s||i.push("Cannot find valid src URL value"),i.length)throw new Error(i.join(", "));return t}loadingValueChanged(e){e?(this.targetElement?.setAttribute("aria-busy","true"),this.iconElement?.setAttribute("href","#icon-spinner")):(this.targetElement?.removeAttribute("aria-busy"),this.iconElement?.setAttribute("href",this.iconValue))}search(e){const t=(e?.detail?.clear||e?.params?.clear||this.constructor.defaultClearParam).split(" "),r=this.hasInputTarget?this.inputTarget:this.element,s=r.name,i=new URLSearchParams(window.location.search),n=i.get(s)||"",a=r.value||"";if(n.trim()===a.trim())return;a?i.set(s,a):i.delete(s),t.forEach((e=>{i.delete(e)}));const o="?"+i.toString(),l=this.srcValue;this.replace(l+o).then((()=>{window.history.replaceState(null,"",o)}))}submit(){const e=this.hasInputTarget?this.inputTarget.form:this.element,t="?"+new URLSearchParams(new FormData(e)).toString(),r=this.srcValue;this.replace(r+t)}async replace(e){const t=("string"==typeof e?e:e?.detail?.url||e?.params?.url||"")||this.srcValue;this.abortController&&this.abortController.abort(),this.abortController=new AbortController;const{signal:r}=this.abortController;return this.loadingValue=!0,this.dispatch("begin",{cancelable:!0,detail:{requestUrl:t},target:this.targetElement}).defaultPrevented?Promise.resolve():fetch(t,{headers:{"x-requested-with":"XMLHttpRequest"},signal:r}).then((e=>{if(!e.ok)throw new Error(`HTTP error! Status: ${e.status}`);return e.text()})).then((e=>{const r=this.targetElement;return r.innerHTML=e,this.dispatch("success",{cancelable:!1,detail:{requestUrl:t,results:e},target:r}),e})).catch((e=>{r.aborted||(this.dispatch("error",{cancelable:!1,detail:{error:e,requestUrl:t},target:this.targetElement}),console.error(`Error fetching ${t}`,e))})).finally((()=>{r===this.abortController?.signal&&(this.loadingValue=!1)}))}disconnect(){this.loadingValue=!1,this.replaceLazy?.cancel(),this.searchLazy?.cancel(),this.submitLazy?.cancel()}}O.defaultClearParam="p",O.targets=["input"],O.values={icon:{default:"",type:String},loading:{default:!1,type:Boolean},src:{default:"",type:String},target:{default:"#listing-results",type:String},wait:{default:200,type:Number}};class P extends n.Qr{connect(){this.processTargetElements("start",!0),this.apply=(0,p.D)(this.apply.bind(this),this.debounceValue)}check(){this.processTargetElements("check",!0)}apply(e){const t=e?.params?.apply||this.element.value,r=e=>{e.value=t,this.quietValue||this.dispatch("change",{cancelable:!1,prefix:"",target:e})};this.processTargetElements("apply").forEach((e=>{this.delayValue?setTimeout((()=>{r(e)}),this.delayValue):r(e)}))}clear(){this.processTargetElements("clear").forEach((e=>{setTimeout((()=>{e.setAttribute("value",""),this.quietValue||this.dispatch("change",{cancelable:!1,prefix:"",target:e})}),this.delayValue)}))}ping(){this.processTargetElements("ping",!1,{bubbles:!0})}processTargetElements(e,t=!1,r={}){if(!t&&this.disabledValue)return[];const s=[...document.querySelectorAll(this.targetValue)],i=s.filter((t=>!this.dispatch(e,{bubbles:!1,cancelable:!0,...r,detail:{element:this.element,value:this.element.value},target:t}).defaultPrevented));return t&&(this.disabledValue=s.length>i.length),i}}P.values={debounce:{default:100,type:Number},delay:{default:0,type:Number},disabled:{default:!1,type:Boolean},quiet:{default:!1,type:Boolean},target:String};class z extends n.Qr{static afterLoad(e,{schema:{controllerAttribute:t}}){window.initTagField=(r,s,i={})=>{k().then((()=>{const n=document.getElementById(r);n&&s&&(Object.entries({options:JSON.stringify(i),url:s}).forEach((([t,r])=>{n.setAttribute(`data-${e}-${t}-value`,r)})),n.setAttribute(t,e))}))}}connect(){const e=this.cleanTag.bind(this);i()(this.element).tagit({autocomplete:{source:this.urlValue},preprocessTag:e,...this.optionsValue})}cleanTag(e){return e&&'"'!==e[0]&&e.indexOf(" ")>-1?`"${e}"`:e}clear(){i()(this.element).tagit("removeAll")}}z.values={options:{default:{},type:Object},url:String};var j=r(9633);class N extends n.Qr{connect(){this.tippy=(0,w.ZP)(this.element,this.options)}contentValueChanged(e,t){t&&t!==e&&this.tippy?.setProps(this.options)}placementValueChanged(e,t){t&&t!==e&&this.tippy?.setProps(this.options)}hide(){this.tippy?.hide()}show(){this.tippy?.show()}get options(){return{content:this.contentValue,placement:this.placementValue,plugins:[T.UW]}}disconnect(){this.tippy?.destroy()}}N.values={content:String,placement:{default:"bottom",type:String}};class M extends Error{constructor(e){super(e),this.message=`Version number '${e}' is not formatted correctly.`}}class $ extends Error{constructor(){super(),this.message="Can only compare prerelease versions"}}class I{constructor(e){this.name=e}}I.MAJOR=new I("Major"),I.MINOR=new I("Minor"),I.PATCH=new I("Patch"),I.PRE_RELEASE_STEP=new I("PreReleaseStep"),I.PRE_RELEASE_VERSION=new I("PreReleaseVersion");class B{constructor(e){const t=e.match(/^(?<major>\d+)\.{1}(?<minor>\d+)((\.{1}(?<patch>\d+))|(?<preReleaseStep>a|b|rc|\.dev){1}(?<preReleaseVersion>\d+)){0,1}$/);if(null===t)throw new M(e);const r=t.groups;this.major=parseInt(r.major,10),this.minor=parseInt(r.minor,10),this.patch=r.patch?parseInt(r.patch,10):0,this.preReleaseStep=r.preReleaseStep?r.preReleaseStep:null,this.preReleaseVersion=r.preReleaseVersion?parseInt(r.preReleaseVersion,10):null}isPreRelease(){return null!==this.preReleaseStep}isPreReleaseStepBehind(e){if(!this.isPreRelease()||!e.isPreRelease())throw new $;return"a"===this.preReleaseStep&&("b"===e.preReleaseStep||"rc"===e.preReleaseStep)||"b"===this.preReleaseStep&&"rc"===e.preReleaseStep}howMuchBehind(e){if(this.major<e.major)return I.MAJOR;if(this.major===e.major&&this.minor<e.minor)return I.MINOR;if(this.major===e.major&&this.minor===e.minor&&!this.isPreRelease()&&!e.isPreRelease()&&this.patch<e.patch)return I.PATCH;if(this.major===e.major&&this.minor===e.minor&&this.isPreRelease()){if(!e.isPreRelease())return I.MINOR;if(this.isPreReleaseStepBehind(e))return I.PRE_RELEASE_STEP;if(this.preReleaseStep===e.preReleaseStep&&this.preReleaseVersion<e.preReleaseVersion)return I.PRE_RELEASE_VERSION}return null}}class H extends n.Qr{connect(){this.checkVersion()}checkVersion(){const e=this.urlValue,t=new B(this.currentVersionValue),r=this.ltsOnlyValue;fetch(e,{referrerPolicy:"strict-origin-when-cross-origin"}).then((t=>{if(200!==t.status)throw Error(`Unexpected response from ${e}. Status: ${t.status}`);return t.json()})).then((e=>{let s=e;if(s&&s.lts&&r&&(s=s.lts),s&&s.version){const e=new B(s.version),i=t.howMuchBehind(e);let n=null;if(!i)return;if(n=i===I.MAJOR||i===I.MINOR?s.minorUrl:s.url,this.latestVersionTarget instanceof HTMLElement){const e=[s.version,r?"(LTS)":""].join(" ").trim();this.latestVersionTarget.textContent=e}this.linkTarget instanceof HTMLElement&&this.linkTarget.setAttribute("href",n||""),this.element.classList.remove(this.hiddenClass)}})).catch((t=>{console.error(`Error fetching ${e}. Error: ${t}`)}))}}H.classes=["hidden"],H.targets=["latestVersion","link"],H.values={currentVersion:String,ltsOnly:{default:!1,type:Boolean},url:{default:"https://releases.wagtail.org/latest.txt",type:String}};const F=[{controllerConstructor:o,identifier:"w-action"},{controllerConstructor:g,identifier:"w-autosize"},{controllerConstructor:m,identifier:"w-bulk"},{controllerConstructor:b,identifier:"w-count"},{controllerConstructor:y.Y,identifier:"w-dialog"},{controllerConstructor:v,identifier:"w-dismissible"},{controllerConstructor:E,identifier:"w-dropdown"},{controllerConstructor:S,identifier:"w-messages"},{controllerConstructor:C,identifier:"w-progress"},{controllerConstructor:V,identifier:"w-skip-link"},{controllerConstructor:L,identifier:"w-slug"},{controllerConstructor:R,identifier:"w-submit"},{controllerConstructor:O,identifier:"w-swap"},{controllerConstructor:P,identifier:"w-sync"},{controllerConstructor:z,identifier:"w-tag"},{controllerConstructor:j.y,identifier:"w-teleport"},{controllerConstructor:N,identifier:"w-tooltip"},{controllerConstructor:H,identifier:"w-upgrade"}];class D extends n.Mx{}D.Controller=n.Qr,D.createController=(e={})=>{class t extends n.Qr{}const{STATIC:r={},...s}=e;return Object.entries(r).forEach((([e,r])=>{t[e]=r})),Object.assign(t.prototype,s),t},window.Stimulus=(({debug:e=!1,definitions:t=[],element:r=document.documentElement}={})=>{const s=D.start(r);return s.debug=e,s.load(t),s})({definitions:F}),window.escapeHtml=x.X,window.enableDirtyFormCheck=function(e,t){const r=i()(e),s=t.confirmationMessage||" ",n=t.alwaysDirty||!1,a=t.commentApp||null,o=t.callback||null;let l=null,c=!1;const u=(e,t)=>{o&&o(e,t)};r.on("submit",(()=>{c=!0}));let h=n,d=!1,p=-1;a&&(d=a.selectors.selectIsDirty(a.store.getState()),a.store.subscribe((()=>{clearTimeout(p),p=setTimeout((()=>{const e=a.selectors.selectIsDirty(a.store.getState());e!==d&&(d=e,u(h,d))}),d?3e3:300)}))),u(h,d);let g=-1;const m=()=>{const e=h;h=(()=>{if(n)return!0;if(!l)return!1;const e=new FormData(r[0]),t=Array.from(e.keys()).filter((e=>!e.startsWith("comments-")));return t.length!==l.size||t.some((t=>{const r=e.getAll(t),s=l.get(t);return r!==s&&!(!Array.isArray(r)||!Array.isArray(s))&&(r.length!==s.length||r.some(((e,t)=>e!==s[t])))}))})(),e!==h&&u(h,d)};n||setTimeout((()=>{const e=new FormData(r[0]);l=new Map,Array.from(e.keys()).filter((e=>!e.startsWith("comments-"))).forEach((t=>l.set(t,e.getAll(t))));const t=()=>{clearTimeout(g),g=setTimeout(m,h?3e3:300)};r.on("change keyup",t).trigger("change");const s=e=>e.nodeType===e.ELEMENT_NODE&&["INPUT","TEXTAREA","SELECT"].includes(e.tagName);new MutationObserver((e=>{e.some((e=>Array.from(e.addedNodes).some(s)||Array.from(e.removedNodes).some(s)))&&t()})).observe(r[0],{childList:!0,attributes:!1,subtree:!0})}),1e4),window.addEventListener("beforeunload",(e=>{if(clearTimeout(g),m(),!c&&(h||d))return e.returnValue=s,s}))},i()((()=>{i()("body").addClass("ready"),i()(".dropdown").each((function(){const e=i()(this);i()(".dropdown-toggle",e).on("click",(t=>{t.stopPropagation(),e.toggleClass("open"),e.hasClass("open")?i()(document).on("click.dropdown.cancel",(t=>{const r=t.relatedTarget||t.toElement;i()(r).parents().is(e)||(e.removeClass("open"),i()(document).off("click.dropdown.cancel"))})):i()(document).off("click.dropdown.cancel")}))})),i()(".drop-zone").on("dragover",(function(){i()(this).addClass("hovered")})).on("dragleave dragend drop",(function(){i()(this).removeClass("hovered")}))}));const Q=window.wagtail||{};window.wagtail=Q},5311:e=>{e.exports=jQuery}},r={};function s(e){var i=r[e];if(void 0!==i)return i.exports;var n=r[e]={exports:{}};return t[e](n,n.exports,s),n.exports}s.m=t,e=[],s.O=(t,r,i,n)=>{if(!r){var a=1/0;for(u=0;u<e.length;u++){for(var[r,i,n]=e[u],o=!0,l=0;l<r.length;l++)(!1&n||a>=n)&&Object.keys(s.O).every((e=>s.O[e](r[l])))?r.splice(l--,1):(o=!1,n<a&&(a=n));if(o){e.splice(u--,1);var c=i();void 0!==c&&(t=c)}}return t}n=n||0;for(var u=e.length;u>0&&e[u-1][2]>n;u--)e[u]=e[u-1];e[u]=[r,i,n]},s.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return s.d(t,{a:t}),t},s.d=(e,t)=>{for(var r in t)s.o(t,r)&&!s.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})},s.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),s.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),s.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},s.j=321,(()=>{var e={321:0};s.O.j=t=>0===e[t];var t=(t,r)=>{var i,n,[a,o,l]=r,c=0;if(a.some((t=>0!==e[t]))){for(i in o)s.o(o,i)&&(s.m[i]=o[i]);if(l)var u=l(s)}for(t&&t(r);c<a.length;c++)n=a[c],s.o(e,n)&&e[n]&&e[n][0](),e[n]=0;return s.O(u)},r=globalThis.webpackChunkwagtail=globalThis.webpackChunkwagtail||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))})();var i=s.O(void 0,[751],(()=>s(3394)));i=s.O(i)})();
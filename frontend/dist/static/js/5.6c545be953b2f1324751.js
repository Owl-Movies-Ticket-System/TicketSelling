webpackJsonp([5],{JLTr:function(t,e){},O5z1:function(t,e,n){t.exports=n.p+"static/img/jinyi.ada1b10.jpeg"},Pxu6:function(t,e,n){t.exports=n.p+"static/img/fanyang.3f3c371.jpeg"},QQ8n:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i=n("Xxa5"),s=n.n(i),a=n("exGp"),c=n.n(a),o={props:{imgSrc:{type:String,required:!0},title:{type:String,required:!0},location:{type:String,required:!0}}},r={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("li",{staticClass:"cinema-item"},[n("div",{staticClass:"poster block-center"},[n("img",{staticClass:"poster-img pointer",attrs:{src:t.imgSrc},on:{click:function(e){return e.stopPropagation(),t.clickPoster(e)}}})]),t._v(" "),n("p",{staticClass:"title"},[t._v(t._s(t.title))]),t._v(" "),n("p",{staticClass:"location"},[t._v(t._s(t.location))])])},staticRenderFns:[]};var l={components:{CinemaItem:n("VU/8")(o,r,!1,function(t){n("JLTr")},"data-v-591a6566",null).exports},data:function(){return{currentCinemaList:[{src:n("ScgI"),title:"金逸影城IMAX（光美番禺沙湾店）",location:"地址： 番禺区沙湾镇西环路1502号荔园新天地3楼"},{src:n("Pxu6"),title:"大地影院-番禺大石店",location:"地址： 番禺区大石朝阳西路29号大石城5楼"},{src:n("O5z1"),title:"金逸影城IMAX（天河店）",location:"地址： 天河区正佳广场6楼"},{src:n("ScgI"),title:"金逸影城IMAX（光美番禺沙湾店）",location:"地址： 番禺区沙湾镇西环路1502号荔园新天地3楼"},{src:n("Pxu6"),title:"大地影院-番禺大石店",location:"地址： 番禺区大石朝阳西路29号大石城5楼"},{src:n("O5z1"),title:"金逸影城IMAX（天河店）",location:"地址： 天河区正佳广场6楼"}]}},methods:{chooseArea:function(t){var e=this;return c()(s.a.mark(function n(){var i,a,c,o,r;return s.a.wrap(function(n){for(;;)switch(n.prev=n.next){case 0:return i=(i=t.target.innerText).substring(0,2),console.log(i),e.currentCinemaList=[],n.next=6,e.$http.post("cinema/search",{district:i},{headers:{author:e.$root.token}});case 6:for(a=n.sent,c="["+(c=(c=(c=(c=a.data).replace(/'/g,'"')).replace(/\{/g,",{")).substring(1,c.length))+"]",c=JSON.parse(c),o=0;o<c.length;o++)r=c[1],console.log(r),e.currentCinemaList.push({src:"http://123.207.55.27:8080/api/img?img="+r.photo,title:r.name,location:r.location});case 14:case"end":return n.stop()}},n,e)}))()}}},u={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"cinema"},[n("div",{staticClass:"area"},[n("span",[t._v("区域：")]),t._v(" "),n("button",{staticClass:"btn",on:{click:t.chooseArea}},[t._v("番禺区")]),t._v(" "),n("button",{staticClass:"btn",on:{click:t.chooseArea}},[t._v("天河区")]),t._v(" "),n("button",{staticClass:"btn",on:{click:t.chooseArea}},[t._v("黄浦区")]),t._v(" "),n("button",{staticClass:"btn",on:{click:t.chooseArea}},[t._v("白云区")]),t._v(" "),n("button",{staticClass:"btn",on:{click:t.chooseArea}},[t._v("荔湾区")]),t._v(" "),n("button",{staticClass:"btn",on:{click:t.chooseArea}},[t._v("花都区")]),t._v(" "),n("button",{staticClass:"btn",on:{click:t.chooseArea}},[t._v("南沙区")])]),t._v(" "),n("div",{staticClass:"cinema-list"},[n("ul",{staticClass:"cinemas flex-container"},t._l(t.currentCinemaList,function(t,e){return n("cinema-item",{directives:[{name:"show",rawName:"v-show",value:!0,expression:"true"}],key:e,attrs:{imgSrc:t.src,active:!0,title:t.title,location:t.location}})}))])])},staticRenderFns:[]};var p=n("VU/8")(l,u,!1,function(t){n("V7s0")},"data-v-c19e031a",null);e.default=p.exports},ScgI:function(t,e,n){t.exports=n.p+"static/img/dadi.4af367f.jpg"},V7s0:function(t,e){}});
//# sourceMappingURL=5.6c545be953b2f1324751.js.map
webpackJsonp([8],{"/wkv":function(e,t){},BO1k:function(e,t,a){e.exports={default:a("fxRn"),__esModule:!0}},XG9F:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var n=a("Xxa5"),s=a.n(n),r=a("BO1k"),i=a.n(r),c=a("exGp"),o=a.n(c),u=["番禺","天河","黄浦","白云","荔湾","花都","南沙"],p=[1,2],v={components:{CinemaButton:a("qkow").a},props:["name"],created:function(){var e=this;return o()(s.a.mark(function t(){var a,n,r,c,o,v,l,m,f,d,h,x,k,_,g,b,C,w,R,$,y;return s.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return a=e.$root.token,t.next=3,e.$http.post("/movie/search",{author:a,name:e.$route.params.name},{headers:{author:a}});case 3:n=t.sent,r=(r=(r=n.data).replace(/"/g,"")).replace(/'/g,'"'),r=JSON.parse(r),e.id=r.id,c=!0,o=!1,v=void 0,t.prev=12,l=i()(u);case 14:if(c=(m=l.next()).done){t.next=24;break}return f=m.value,t.next=18,e.$http.post("/cinema/search",{district:f},{headers:{author:a}});case 18:if(d=t.sent,h=d.data){for(h="["+(h=(h=(h=h.replace(/'/g,'"')).replace(/\{/g,",{")).substring(1))+"]",h=JSON.parse(h),x=0;x<h.length;x++)h[x].timeRanges=[];e.cinemas=e.cinemas.concat(h)}case 21:c=!0,t.next=14;break;case 24:t.next=30;break;case 26:t.prev=26,t.t0=t.catch(12),o=!0,v=t.t0;case 30:t.prev=30,t.prev=31,!c&&l.return&&l.return();case 33:if(t.prev=33,!o){t.next=36;break}throw v;case 36:return t.finish(33);case 37:return t.finish(30);case 38:k=!0,_=!1,g=void 0,t.prev=41,b=i()(p);case 43:if(k=(C=b.next()).done){t.next=55;break}return w=C.value,t.next=47,e.$http.post("/cinema/available_movies",{id:w},{headers:{author:a}});case 47:if(R=t.sent,$=($=R.data).replace(/'/g,'"'),($=JSON.parse($)).movie_id.toString()===e.id.toString())for(y=0;y<e.cinemas.length;y++)e.cinemas[y].id===w&&e.cinemas[y].timeRanges.push($.stage);case 52:k=!0,t.next=43;break;case 55:t.next=61;break;case 57:t.prev=57,t.t1=t.catch(41),_=!0,g=t.t1;case 61:t.prev=61,t.prev=62,!k&&b.return&&b.return();case 64:if(t.prev=64,!_){t.next=67;break}throw g;case 67:return t.finish(64);case 68:return t.finish(61);case 69:case"end":return t.stop()}},t,e,[[12,26,30,38],[31,,33,37],[41,57,61,69],[62,,64,68]])}))()},data:function(){return{areas:["番禺区","天河区","黄浦区","白云区","荔湾区","花都区","南沙区"],cinemas:[]}},methods:{chooseArea:function(){},chooseTime:function(e,t){this.selectCinema=t;var a=this.$route.path;this.$router.push({path:a+"/seat",query:{time:e}})}},beforeRouteLeave:function(e,t,a){e.path.includes("seat")&&(e.params.movie_id=this.id,e.params.cinema_id=this.selectCinema),a()}},l={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",{staticClass:"cinemas"},[a("div",{staticClass:"cinemas-text left"},[e._v("区域：")]),e._v(" "),a("div",{staticClass:"cinemas-item flex-container"},e._l(e.areas,function(t){return a("cinema-button",{key:t,staticClass:"cinema-button",attrs:{small:""},on:{"process-click":e.chooseArea}},[e._v("\n       "+e._s(t)+"\n     ")])}))]),e._v(" "),a("div",{staticClass:"booking"},e._l(e.cinemas,function(t){return a("div",{key:t.name,staticClass:"booking-item flex-container"},[a("div",{staticClass:"cinema"},[a("div",{staticClass:"cinema-name"},[e._v(e._s(t.name))])]),e._v(" "),a("div",{staticClass:"time-ranges flex-container"},e._l(t.timeRanges,function(n){return a("div",{key:t.name+n,staticClass:"time-range pointer",on:{click:function(a){e.chooseTime(n,t.id)}}},[e._v("\n          "+e._s(n)+"\n        ")])}))])}))])},staticRenderFns:[]};var m=a("VU/8")(v,l,!1,function(e){a("/wkv")},"data-v-60c3b42b",null);t.default=m.exports},fxRn:function(e,t,a){a("+tPU"),a("zQR9"),e.exports=a("g8Ux")},g8Ux:function(e,t,a){var n=a("77Pl"),s=a("3fs2");e.exports=a("FeBl").getIterator=function(e){var t=s(e);if("function"!=typeof t)throw TypeError(e+" is not iterable!");return n(t.call(e))}}});
//# sourceMappingURL=8.f5132dab8051a1352d60.js.map
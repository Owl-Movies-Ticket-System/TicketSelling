webpackJsonp([6],{"35Tk":function(e,t){},XG9F:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a={components:{CinemaButton:n("qkow").a},props:["name"],data:function(){return{areas:["番禺区","天河区","黄浦区","白云区","荔湾区","花都区","南沙区"],cinemas:[{name:"abc",timeRanges:["11:40","13:00","14:20","15:10","16:05","17:00","17:55","19:15"]},{name:"def",timeRanges:["11:40","13:00","14:20","15:10"]}]}},methods:{chooseArea:function(){},chooseTime:function(e){var t=this.$route.path;this.$router.push({path:t+"/seat",query:{time:e}})}}},s={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("div",{staticClass:"cinemas"},[n("div",{staticClass:"cinemas-text left"},[e._v("区域：")]),e._v(" "),n("div",{staticClass:"cinemas-item flex-container"},e._l(e.areas,function(t){return n("cinema-button",{key:t,staticClass:"cinema-button",attrs:{small:""},on:{"process-click":e.chooseArea}},[e._v("\n       "+e._s(t)+"\n     ")])}))]),e._v(" "),n("div",{staticClass:"booking"},e._l(e.cinemas,function(t){return n("div",{key:t.name,staticClass:"booking-item flex-container"},[n("div",{staticClass:"cinema"},[n("div",{staticClass:"cinema-name"},[e._v(e._s(t.name))])]),e._v(" "),n("div",{staticClass:"time-ranges flex-container"},e._l(t.timeRanges,function(a){return n("div",{key:t.name+a,staticClass:"time-range pointer",on:{click:function(t){e.chooseTime(a)}}},[e._v("\n          "+e._s(a)+"\n        ")])}))])}))])},staticRenderFns:[]};var i=n("VU/8")(a,s,!1,function(e){n("35Tk")},"data-v-2fc4a4e1",null);t.default=i.exports}});
//# sourceMappingURL=6.66c42b810d637a6430e5.js.map
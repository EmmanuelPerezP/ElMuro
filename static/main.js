!function(t){var e={};function n(l){if(e[l])return e[l].exports;var i=e[l]={i:l,l:!1,exports:{}};return t[l].call(i.exports,i,i.exports,n),i.l=!0,i.exports}n.m=t,n.c=e,n.d=function(t,e,l){n.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:l})},n.r=function(t){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},n.t=function(t,e){if(1&e&&(t=n(t)),8&e)return t;if(4&e&&"object"==typeof t&&t&&t.__esModule)return t;var l=Object.create(null);if(n.r(l),Object.defineProperty(l,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var i in t)n.d(l,i,function(e){return t[e]}.bind(null,i));return l},n.n=function(t){var e=t&&t.__esModule?function(){return t.default}:function(){return t};return n.d(e,"a",e),e},n.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},n.p="",n(n.s=0)}([function(t,e){document.getElementById("cards").addEventListener("click",function(t){if(t.target&&!t.target.classList.contains("like")&&t.target.classList.contains("fa-heart")){var e=t.target.parentElement.parentElement.parentElement.parentElement.id;fetch("/post/vote/",{headers:{Accept:"application/json","Content-Type":"application/json"},credentials:"include",method:"POST",body:JSON.stringify({postId:e,action:1})}).then(function(t){console.log(t)}).catch(function(t){console.log(t)}),t.target.classList.add("like");let n=parseInt(t.target.parentElement.nextElementSibling.firstElementChild.textContent)+1;t.target.parentElement.nextElementSibling.firstElementChild.textContent=n+" likes"}else if(t.target&&t.target.classList.contains("like")&&t.target.classList.contains("fa-heart")){e=t.target.parentElement.parentElement.parentElement.parentElement.id,fetch("/post/vote/",{headers:{Accept:"application/json","Content-Type":"application/json"},credentials:"include",method:"POST",body:JSON.stringify({postId:e,action:-1})}).then(function(t){console.log(t)}).catch(function(t){console.log(t)}),t.target.classList.remove("like");let n=parseInt(t.target.parentElement.nextElementSibling.firstElementChild.textContent)-1;t.target.parentElement.nextElementSibling.firstElementChild.textContent=n+" likes"}});try{document.getElementById("comments").addEventListener("click",function(t){if(t.target&&!t.target.classList.contains("like")&&t.target.classList.contains("fa-heart")){var e=t.target.parentElement.parentElement.parentElement.parentElement.id;fetch("/comment/vote/",{headers:{Accept:"application/json","Content-Type":"application/json"},credentials:"include",method:"POST",body:JSON.stringify({postId:e,action:1})}).then(function(t){console.log(t)}).catch(function(t){console.log(t)}),t.target.classList.add("like");let n=parseInt(t.target.parentElement.nextElementSibling.firstElementChild.textContent)+1;t.target.parentElement.nextElementSibling.firstElementChild.textContent=n+" likes"}else if(t.target&&t.target.classList.contains("like")&&t.target.classList.contains("fa-heart")){e=t.target.parentElement.parentElement.parentElement.parentElement.id,fetch("/comment/vote/",{headers:{Accept:"application/json","Content-Type":"application/json"},credentials:"include",method:"POST",body:JSON.stringify({postId:e,action:-1})}).then(function(t){console.log(t)}).catch(function(t){console.log(t)}),t.target.classList.remove("like");let n=parseInt(t.target.parentElement.nextElementSibling.firstElementChild.textContent)-1;t.target.parentElement.nextElementSibling.firstElementChild.textContent=n+" likes"}})}catch(t){console.log("no comments")}console.log("ready")}]);
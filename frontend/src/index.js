
function likeDislike(e) {
  if(e.target && !e.target.classList.contains('like') && e.target.classList.contains('fa-heart')) {
    // List item found!  Output the ID!
    // in this case we could use this function 
    // https://gomakethings.com/climbing-up-and-down-the-dom-tree-with-vanilla-javascript/#getting-the-first-match-up-the-tree
    // that is equivalent to $.closest(), but its more readible this way
    var idOfPost = e.target.parentElement.parentElement.parentElement.parentElement.id;

    fetch("/post/vote/",{
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      credentials: "include",
      method: "POST",
      body: JSON.stringify({"postId": idOfPost, "action": 1})
    })
    .then(function(res){ 
      console.log(res);
    })
    .catch(function(res){ 
      console.log(res);
    })

    e.target.classList.add('like');
    let nextNumber = parseInt(e.target.parentElement.nextElementSibling.firstElementChild.textContent)+1;
    e.target.parentElement.nextElementSibling.firstElementChild.textContent = nextNumber + " likes";

  }
  else if(e.target && e.target.classList.contains('like') && e.target.classList.contains('fa-heart')){
    // List item found!  Output the ID!
    // in this case we could use this function 
    // https://gomakethings.com/climbing-up-and-down-the-dom-tree-with-vanilla-javascript/#getting-the-first-match-up-the-tree
    // that is equivalent to $.closest(), but its more readible this way
    var idOfPost = e.target.parentElement.parentElement.parentElement.parentElement.id;

    fetch("/post/vote/",{
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      credentials: "include",
      method: "POST",
      body: JSON.stringify({"postId": idOfPost, "action": -1})
    })
    .then(function(res){ 
      console.log(res);
    })
    .catch(function(res){ 
      console.log(res);
    })
    e.target.classList.remove('like');
    let nextNumber = parseInt(e.target.parentElement.nextElementSibling.firstElementChild.textContent)-1;
    e.target.parentElement.nextElementSibling.firstElementChild.textContent = nextNumber + " likes";
  }
}   

function likeDislikeComment(e) {
  if(e.target && !e.target.classList.contains('like') && e.target.classList.contains('fa-heart')) {
    // List item found!  Output the ID!
    // in this case we could use this function 
    // https://gomakethings.com/climbing-up-and-down-the-dom-tree-with-vanilla-javascript/#getting-the-first-match-up-the-tree
    // that is equivalent to $.closest(), but its more readible this way
    var idOfPost = e.target.parentElement.parentElement.parentElement.parentElement.id;

    fetch("/comment/vote/",{
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      credentials: "include",
      method: "POST",
      body: JSON.stringify({"postId": idOfPost, "action": 1})
    })
    .then(function(res){ 
      console.log(res);
    })
    .catch(function(res){ 
      console.log(res);
    })

    e.target.classList.add('like');
    let nextNumber = parseInt(e.target.parentElement.nextElementSibling.firstElementChild.textContent)+1;
    e.target.parentElement.nextElementSibling.firstElementChild.textContent = nextNumber + " likes";

  }
  else if(e.target && e.target.classList.contains('like') && e.target.classList.contains('fa-heart')){
    // List item found!  Output the ID!
    // in this case we could use this function 
    // https://gomakethings.com/climbing-up-and-down-the-dom-tree-with-vanilla-javascript/#getting-the-first-match-up-the-tree
    // that is equivalent to $.closest(), but its more readible this way
    var idOfPost = e.target.parentElement.parentElement.parentElement.parentElement.id;

    fetch("/comment/vote/",{
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      credentials: "include",
      method: "POST",
      body: JSON.stringify({"postId": idOfPost, "action": -1})
    })
    .then(function(res){ 
      console.log(res);
    })
    .catch(function(res){ 
      console.log(res);
    })
    e.target.classList.remove('like');
    let nextNumber = parseInt(e.target.parentElement.nextElementSibling.firstElementChild.textContent)-1;
    e.target.parentElement.nextElementSibling.firstElementChild.textContent = nextNumber + " likes";
  }
}


var cards = document.getElementById('cards');
cards.addEventListener('click', likeDislike);

try{
  var comments = document.getElementById('comments');
  comments.addEventListener('click', likeDislikeComment);
}
catch(error){
  console.log("no comments");
}

console.log("ready");
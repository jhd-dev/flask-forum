(function(){
	function getJSON(url, callback){
		var xhr = new XMLHttpRequest();
		xhr.addEventListener("load", function(){
			var json = JSON.parse(xhr.responseText);
			callback.call(xhr, json);
		});
		xhr.open("GET", url);
		xhr.send();
		//console.log("hi")
	}
	document.addEventListener("DOMContentLoaded", function(){
		getJSON("./posts", function(data){console.log(data);
			data.posts.forEach(function(post, i){console.log(post);
				var postDiv = document.createElement("div");
					postDiv.classList.add("post");
					var titleLink = document.createElement("a");
						titleLink.href = post.url;
						var title = document.createElement("h3");
							title.classList.add("post-title");
							title.innerHTML = post.title;
						titleLink.appendChild(title);
					postDiv.appendChild(titleLink);
					var snippet = document.createElement("p");
						snippet.classList.add("post-snippet");
						snippet.innerHTML = post.snippet;
					postDiv.appendChild(snippet);
				document.getElementById("posts").appendChild(postDiv);
			});
		});
	});
})();

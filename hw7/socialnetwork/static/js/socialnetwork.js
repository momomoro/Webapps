window.setInterval(function () {
    $.ajax({
        url: "/socialnetwork/get-posts",
        dataType : "json",
        success: function( posts ) {
            
			
			
            // refresh the page with posts
            $(posts).each(function() {
            });
        }
    });
}, 5000);

 $(document).ready(function(){
    $('.collapsible').collapsible({
      accordion : false 
    });
  });
  
 $( "#comment").trigger("click","button",function( event ) {
	 console.log( $(this));
 });
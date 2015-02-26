/*window.setInterval(function () {
    $.ajax({
        url: "/socialnetwork/get-posts",
        dataType : "json",
        success: function( posts ) {
            

            // refresh the page with posts
            $(posts).each(function() {
                $("#posts").html(
                    this 
                );
            });
        }
    });
}, 5000);*/

window.setInterval(function () {
    $.ajax({
        url: "/socialnetwork/get-posts",
        dataType : "json",
        success: function( posts ) {
            

            // refresh the page with posts
            $(posts).each(function() {
                $("#test").html(
                    this.pk 
                );
            });
        }
    });
}, 5000);


  $(document).ready(function(){
    $('.collapsible').collapsible({
      accordion : false 
    });
  });
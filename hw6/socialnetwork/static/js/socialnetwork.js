window.setInterval(function () {
    $.ajax({
        url: "/socialnetwork/index",
        dataType : "json",
        success: function( posts ) {
            // Removes the old to-do list items
            $("li").remove();

            // Adds each new todo-list item to the list
            $(posts).each(function() {
                $("#posts").append(
                    this 
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
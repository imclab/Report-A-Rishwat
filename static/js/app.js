function validate() {
    var form = document.forms["submit"];
    if (form["date"].value == null ||
        form["location"].value == null ||
        form["service"].value == null ||
        form["officer"].value == null ||
        form["amount"].value == null) {
            alert("Fields incomplete!");
            return false;
        }
    else {
        return true;
    }
}

$(document).ready(function() {

	/* Tabs Activiation
	================================================== */
	var tabs = $('ul.tabs'),
	    tabsContent = $('ul.tabs-content');
	
	tabs.each(function(i) {
		//Get all tabs
		var tab = $(this).find('> li > a');
		tab.click(function(e) {
			
			//Get Location of tab's content
			var contentLocation = $(this).attr('href') + "Tab";
			
			//Let go if not a hashed one
			if(contentLocation.charAt(0)=="#") {
			
				e.preventDefault();
			
				//Make Tab Active
				tab.removeClass('active');
				$(this).addClass('active');
				
				//Show Tab Content
				$(contentLocation).show().siblings().hide();
				
			} 
		});
	}); 
	
});

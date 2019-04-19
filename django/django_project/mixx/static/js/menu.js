$(document).on("scroll",function(){
	$("header").toggleClass("small", $(document).scrollTop()>100);
});
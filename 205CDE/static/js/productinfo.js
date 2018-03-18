$(function() {
	var maxword = 500;
	
	$("#message-content").keyup(function() {
		var wordnum = $(this).val();
		wordCounter(wordnum.length);
	});
	
	wordCounter(0);
	
	function wordCounter(wordnumnow) {
		$("#word-counter").text(maxword - wordnumnow);
		if ((maxword - wordnumnow) <= 1 ) {
			$(".countable").addClass('d-none');
		} else {
			$(".countable").removeClass('d-none');
		}
	}
	
});
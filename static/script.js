$(function(){
	$('button').click(function() {
		var value = $('slider').val();
		$.ajax({
			url: '/brightnessUpdate',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error) {
				console.log(error);
			}
		});
	});
}); 

$(function(){
	$('.task').on('change', function(){
		$.ajax({
			type: 'GET',
			url: $(this).attr('data-url'),
			success: function(data){
				M.toast({html: data['msg']})
			},
			fail: function(data){
				M.toast({html: 'Network Error'})
			}
		})
	})
});
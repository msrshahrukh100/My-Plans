$(function(){  

	$('.tbt-change-status').on('click', function(){
		
		$.ajax({
			url: $(this).attr('data-url'),
			type: 'GET',
			success: function(data){
				M.toast({html: data['msg']});
				$('#progress-'+data['id']).attr('style', 'width:'+data['percent_completed']+'%');
				$('#units_completed-'+data['id']).html(data['units_completed']);
				$('#badge-'+data['id']).html(data['percent_completed'])
			}
		})

	})
  // $('.chips-autocomplete').chips();
});
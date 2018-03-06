$(function(){  

	$('.tbt-change-status').on('click', function(){
		
		$.ajax({
			url: $(this).attr('data-url'),
			type: 'GET',
			success: function(data){
				M.toast({html: data['msg']});
				$('#progress-'+data['id']).attr('style', 'width:'+data['percent_completed']+'%');
				$('#units_completed-'+data['id']).html(data['units_completed']);
				$('#badge-'+data['id']).html(data['percent_completed']);
				$('#badge-'+data['id']).attr('class', 'new badge '+data['color']);
			}
		})

	})
  // $('.chips-autocomplete').chips();

  $('#btn-read-frc').on('click', function(){
  	$.ajax({
			url: $(this).attr('data-url'),
			type: 'GET',
			success: function(data){
				$('#run-streak-box').show()
				$('#run-streak').html(data["streak_count"])
				if(data["status"] == "2"){
					$('#message-box').show()
					$('#message').html(data["msg"] + data["today_times"])
				}
				else{
					M.toast({html: data['msg'] + data["today_times"]})
				}
				
			}
		})

  });

});
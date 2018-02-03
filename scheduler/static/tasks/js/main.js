$(function(){

	function populate_todays_score(){
		$.ajax({
				type: 'GET',
				url: $('#todays-score').attr('data-url'),
				success: function(data){
					$('#todays-score').html(data['data'][0].score + "%");
					$('#todays-score').attr('class','btn-floating btn-large '+data['data'][0].color);
				}
			})
	}
	
	populate_todays_score();

    $('.sidenav').sidenav();
    $('.modal').modal();

    $('#getaims').on('click', function(){
    	$.ajax({
    		type: 'GET',
    		url: $(this).data('url'),
    		success: function(data){
    			$('#aims').html(data);
    			$('#preloader').hide();
    		},
    		fail: function(data){
    			$('#preloader').hide();
    			M.toast({html: 'Network Error'});
    		},
    		beforeSend: function(){
    			$('#preloader').show();
    		}
    	})
    });
    
	$('.task').on('change', function(){
		$.ajax({
			type: 'GET',
			url: $(this).attr('data-url'),
			success: function(data){
				M.toast({html: data['msg']});
				populate_todays_score();
			},
			fail: function(data){
				M.toast({html: 'Network Error'})
			}
		})
	})

	// for the tabs
	$('.tabs').tabs();

	// for the fixed action button
	$('.fixed-action-btn').floatingActionButton({
		direction: 'left', // Direction menu comes out
		hoverEnabled: true, // Hover enabled
		toolbarEnabled: false // Toolbar transition enabled
	});

	// for the toll tip
	$('.tooltipped').tooltip();	 


});
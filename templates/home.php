<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../../../favicon.ico">

    <title>Sentiment Analysis of Nordic Languages</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <!-- Custom styles for this template -->
    <link href="narrow-jumbotron.css" rel="stylesheet">
	
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>
	
	<style>
	.row-fluid {
		word-wrap: break-word;  
	}
	</style>
  </head>

    <body>
    <div class="container">
	
		<div class="header clearfix">
			<h3 class="text-muted" style="padding-top: 20px; padding-bottom: 20px;">Sentiment Analysis of Nordic Languages</h3>
		</div>
		<form id="dataForm" method="post">
			<div class="jumbotron">
				<div class="form-group" style="">
					<label>Choose Langauge: </label>
					
					<select name="lang" id="lang" class="form-control" style="float: none;">
						<option value="swe">Swedish</option>
						<option value="dan">Danish</option>
						<option value="nor">Norwegian</option>
					</select>
				</div>
			
				<div class="form-group" style="">
					<label>Write a review:</label>
						<textarea name="rev" id="rev" class="form-control" placeholder="Skriv en text för att kolla tonaliteten"></textarea>
				</div>
				<div class="container">
					<div class="row">
						<div class="col-md-2 ">
							<div class="rounded p-2">
								<div class="row-fluid font-weight-bold" >Tonality:</div>
								<div id="tonality"> </div>
							</div>
						</div>
					<div class="offset-md-6 col-md-4 form-control">
								<table class="table">
									<thead>
										<tr>
											<th scope="col" class="font-weight-bold">Rating</th>
											<th scope="col"></th>
										</tr>
									</thead>
									<tbody>
										<tr>
											<td>Good:</td>
											<td>10</td>
										</tr>
										<tr>
											<td>Neutral:</td>
											<td>8-9</td>
										</tr>
										<tr>
											<td>Bad:</td>
											<td>0-7</td>
										</tr>
									</tbody>
								</table>
							</div>
					</div>
				</div>
			</div>
		</form>
		<div id="successAlert" class="alert alert-success" role="alert" style="display:none;"></div>
		<div id="errorAlert" class="alert alert-danger" role="alert" style="display:none;"></div>

      <footer class="footer">
        <p>Demo for Utexpo</p>
      </footer>

    </div> 

	<script>
	$(document).ready(function() {
		$('#dataForm').on('input', function(event) {
			$.ajax({
				data : {
					lang : $('#lang').val(),
					rev : $('#rev').val()
				},
				type : 'POST',
				url : '/process'
			})
			.done(function(data) {
				if (data.error) {
					$('#errorAlert').text(data.error).show();
					$('#tonality').html(data.rev);
				}else {
					$('#errorAlert').hide();
					$('#tonality').html(data.rev);
				}

			});

			event.preventDefault();

		});

	});
	</script>

</body>
</html>
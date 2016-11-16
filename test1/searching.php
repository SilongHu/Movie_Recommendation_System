	<?php
if($_POST['submit1']=="Search" ){
	$Mname=$_POST['content'];
	?>

 <section id="portfolio" class="single-page scrollblock">
      <div class="container">
        <div class="align"></div>
        <h1 id="folio-headline">看了又看</h1>
        <div class="row">
		<div class='span4'>
		</div>
    <?php
	
	$sql = "select * from movie_500 where Mid = '$Mname'";
	$res = mysql_query($sql);
	
	if($row = mysql_fetch_assoc($res)){
	    $name = $row['Mname'];
		$Directors = $row['Directors'];
		$Performer1 = $row['Performer1'];
		$Performer2 = $row['Performer2'];
		$Performer3 = $row['Performer3'];
		$link = $row['Websites'];
		$route = $row['Pictures'];
	    
		echo"
		<div class='span4'>
            <div class='mask2'> <a href='$link' rel='prettyPhoto'><img src='$route' width='250px'  height='200px' alt=''></a> </div>
            <div class='inside'>
              <hgroup>
                <h2>$name</h2>
              </hgroup>
              <div class='entry-content'>
                <p>导演：$Directors <br>演员：$Performer1 &nbsp $Performer2 &nbsp $Performer3</p>
                <a class='more-link' href='$link'>Learn More</a> </div>
            </div>
            <!-- /.inside -->
          </div>
	";
	}?>
	<div class='span4'>
		</div>
	
	    <!-- /.span4 -->
        </div>
        <!-- /.row -->
      </div>
      <!-- /.container -->
    </section>
    <hr>

<?php
}
else{
   echo "<script>alert('查询电影不存在'); history.go(-1);</script>";
}
?>

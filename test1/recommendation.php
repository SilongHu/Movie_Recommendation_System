    <?php 
    session_start();  
   // 检测是否登录，若没登录则转向登录界面  
    if(!isset($_SESSION['userid'])){  
    header("Location:login.php");  
    exit();  
    } 
    $online = $_SESSION['username']; 
	require "conn.php";	
	$recom = mysql_query("select * from recommendation where Uid = '$online'");
	$result = mysql_fetch_assoc($recom);
    ?>
	
	
	<!DOCTYPE HTML>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Movie Recommendation</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Styles -->
    <link href="css/bootstrap.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
    <link rel='stylesheet' id='prettyphoto-css'  href="css/prettyPhoto.css" type='text/css' media='all'>
    <link href="css/fontello.css" type="text/css" rel="stylesheet">
    <!--[if lt IE 7]>
            <link href="css/fontello-ie7.css" type="text/css" rel="stylesheet">  
        <![endif]-->
    <style>
    body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
    }
    </style>
    <link href="css/bootstrap-responsive.css" rel="stylesheet">
    <!-- Favicon -->
    <link rel="shortcut icon" href="img/favicon.ico">
    <!-- JQuery -->
    <script type="text/javascript" src="js/jquery.js"></script>
    <!-- Load ScrollTo -->
    <script type="text/javascript" src="js/jquery.scrollTo-1.4.2-min.js"></script>
    <!-- Load LocalScroll -->
    <script type="text/javascript" src="js/jquery.localscroll-1.2.7-min.js"></script>
    <!-- prettyPhoto Initialization -->
    <script type="text/javascript" charset="utf-8">
          $(document).ready(function(){
            $("a[rel^='prettyPhoto']").prettyPhoto();
          });
        </script>
    </head>
    <body>
    <!--******************** NAVBAR ********************-->
    <div class="navbar-wrapper">
      <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="navbar-inner">
          <div class="container">
            <!-- Responsive Navbar Part 1: Button for triggering responsive navbar (not covered in tutorial). Include responsive CSS to utilize. -->
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse"> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </a>
            <h1 class="brand"><a href="#top">Movie Recommendation </a></h1>
            <!-- Responsive Navbar Part 2: Place all navbar contents you want collapsed withing .navbar-collapse.collapse. -->
            <nav class="pull-right nav-collapse collapse">
              <ul id="menu-main" class="nav">
                <li><a title="Content" href="#portfolio">Content</a></li>
                <li><a title="Maybe" href="#services">Maybe</a></li>
                <li><a title="news" href="#news">More</a></li>
				<li><a title="Mark" href="#mark">Mark</a></li>
				<li><a title="Team" href="#team">Team</a></li>
              </ul>
            </nav>
          </div>
          <!-- /.container -->
        </div>
        <!-- /.navbar-inner -->
      </div>
      <!-- /.navbar -->
    </div>
    <!-- /.navbar-wrapper -->
    <div id="top"></div>
    <!-- ******************** HeaderWrap ********************-->
    <div id="headerwrap">
      <header class="clearfix">
        <h1> Serach for what you like</h1>
        <div class="container">
          <div class="row">
            <div class="span12">
			<form action="#" method="post">
			  <input type="text" name="content" placeholder="Movie Id" class="cform-text" size="40" title="search content">
              <input type="submit" name="submit" value="Search" class="cform-submit">
			  </form>
            </div>
          </div>
          <div class="row">
            <div class="span12">
            </div>
          </div>
        </div>
      </header>
	  <p>&nbsp;</p>
	  <p>&nbsp;</p>
	  <p>&nbsp;</p>
	  <p>&nbsp;</p>
	  <p>&nbsp;</p>
	 
	 <?php 
      echo"<h2>$online &nbsp;您好！|<a href='logout.php?action=logout'>注销</a></h2>";
      ?>
	 
    </div>
	
    <?php
    if($_POST['submit'] == 'Search' ){
	   $Mname=$_POST['content'];
	?>


    <?php
	$sql = "select * from movie_500 where Mid = '$Mname'";
	$res = mysql_query($sql);
	if($row = mysql_fetch_assoc($res)){
	    $name = $row['Mname'];
		$Directors = $row['Directors'];
		$Performer1 = $row['Performer1'];
		$Performer2 = $row['Performer2'];
		$Performer3 = $row['Performer3'];
		$Tag1 = $row['Tag1'];
		$Tag2 = $row['Tag2'];
		$Tag3 = $row['Tag3'];
		$link = $row['Websites'];
		$route = $row['Pictures'];
    ?>
    <section id="portfolio" class="single-page scrollblock">
      <div class="container">
        <div class="align"></div>
        <h1 id="folio-headline">Seaching Result</h1>
        <div class="row">
		<div class='span4'>
		</div>
    <?php	


	
	    
		echo"
		<div class='span4'>
            <div class='mask2'> <a href='$link' rel='prettyPhoto'><img src='$route' width='250px'  height='200px' alt=''></a> </div>
            <div class='inside'>
              <hgroup>
                <h2>$name</h2>
              </hgroup>
              <div class='entry-content'>
                <p>导演：$Directors <br>演员：$Performer1 &nbsp $Performer2 &nbsp $Performer3 <br>类型：$Tag1 &nbsp $Tag2 &nbsp $Tag3</p>
                <a class='more-link' href='$link'>Learn More</a> </div>
            </div>
            <!-- /.inside -->
          </div>
	";
	

	$sql = "select * from um_verify where Uid = '$online'"; //SQL语句  
    $result = mysql_query($sql);
	if($rows = mysql_fetch_array($result))
	{
	   if(!$rows['$Mname'])
	   {
	     echo $rows['$Mname'];
	     $sql1 = "select * from user_movie where Uid = '$online'"; //SQL语句  
         $result1 = mysql_query($sql1);
		 if($rows1 = mysql_fetch_array($result1)){
		    if($rows1['$Mname'] && $rows1['$Mname']+0.3!=5){
			  // $sql_update = "update user_movie set $Mname=$rows1['$Mname']+'0.3' where Uid='$online'";  
              // $res_update = mysql_query($sql_update);
			   
			   
			}
			else{
			   $sql_update = "update user_movie set $Mname=3.5 where Uid='$online'";  
               $res_update = mysql_query($sql_update);

			}
			
		 }
	   }
	}
	
	}else{
        echo "<script>alert('查询电影不存在');//history.go(-1); </script>";
    }

	?>
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
?>
		
	
	

    <!--******************** Feature ********************-->
    <div class="scrollblock">
      <section id="feature">
        <div class="container">
          <div class="row">
            <div class="span12">
              <article>
                <p>We work to provide the best recommendation.</p>
                <p>See following for what you probobally like</p>
                <p>accordding to your own watching and marking history</p>
              </article>
            </div>
            <!-- ./span12 -->
          </div>
          <!-- .row -->
        </div>
        <!-- ./container -->
      </section>
    </div>
    <hr>


	
	
	<!--******************** Content Section ********************-->
    <section id="portfolio" class="single-page scrollblock">
      <div class="container">
        <div class="align"></div>
        <h1 id="folio-headline">看了又看</h1>
        <div class="row">
    <?php
	$Mid = $result['c1'];
	$sql = "select * from movie_500 where Mid = '$Mid'";
	$res = mysql_query($sql);
	
	if($row = mysql_fetch_assoc($res)){
	    $name = $row['Mname'];
		$mid = $row['Mid'];
		$Directors = $row['Directors'];
		$Performer1 = $row['Performer1'];
		$Performer2 = $row['Performer2'];
		$Performer3 = $row['Performer3'];
		$Tag1 = $row['Tag1'];
		$Tag2 = $row['Tag2'];
		$Tag3 = $row['Tag3'];
		$link = $row['Websites'];
		$route = $row['Pictures'];
	    
		echo"
		<div class='span4'>
            <div class='mask2'> <a href='$link' rel='prettyPhoto'><img src='$route' width='250px'  height='200px' alt=''></a> </div>
            <div class='inside'>
              <hgroup>
                <h2>$name</h2>
				<h3>$mid</h3>
              </hgroup>
              <div class='entry-content'>
                <p>导演：$Directors <br>演员：$Performer1 &nbsp $Performer2 &nbsp $Performer3 <br>类型：$Tag1 &nbsp $Tag2 &nbsp $Tag3 </p>
                <a class='more-link' href='$link'>Learn More</a> </div>
            </div>
            <!-- /.inside -->
          </div>
	";
	}?>
          <!-- /.span4 -->
          <?php
	$Mid = $result['c2'];
	$sql = "select * from movie_500 where Mid = '$Mid'";
	$res = mysql_query($sql);
	
	if($row = mysql_fetch_assoc($res)){
	    $name = $row['Mname'];
		$mid = $row['Mid'];
		$Directors = $row['Directors'];
		$Performer1 = $row['Performer1'];
		$Performer2 = $row['Performer2'];
		$Performer3 = $row['Performer3'];
		$Tag1 = $row['Tag1'];
		$Tag2 = $row['Tag2'];
		$Tag3 = $row['Tag3'];
		$link = $row['Websites'];
		$route = $row['Pictures'];
	    
		echo"
		<div class='span4'>
            <div class='mask2'> <a href='$link' rel='prettyPhoto'><img src='$route' width='250px'  height='200px'alt=''></a> </div>
            <div class='inside'>
              <hgroup>
                <h2>$name</h2>
				<h3>$mid</h3>
              </hgroup>
              <div class='entry-content'>
                <p>导演：$Directors <br>演员：$Performer1 &nbsp $Performer2 &nbsp $Performer3 <br>类型：$Tag1 &nbsp $Tag2 &nbsp $Tag3</p>
                <a class='more-link' href='$link'>Learn More</a> </div>
            </div>
            <!-- /.inside -->
          </div>
	";
	}?>
          <!-- /.span4 -->
          <?php
	$Mid = $result['c3'];
	$sql = "select * from movie_500 where Mid = '$Mid'";
	$res = mysql_query($sql);
	
	if($row = mysql_fetch_assoc($res)){
	    $name = $row['Mname'];
		$mid = $row['Mid'];
		$Directors = $row['Directors'];
		$Performer1 = $row['Performer1'];
		$Performer2 = $row['Performer2'];
		$Performer3 = $row['Performer3'];
		$Tag1 = $row['Tag1'];
		$Tag2 = $row['Tag2'];
		$Tag3 = $row['Tag3'];
		$link = $row['Websites'];
		$route = $row['Pictures'];
	    
		echo"
		<div class='span4'>
            <div class='mask2'> <a href='$link' rel='prettyPhoto'><img src='$route' width='250px'  height='200px'alt=''></a> </div>
            <div class='inside'>
              <hgroup>
                <h2>$name</h2>
				<h3>$mid</h3>
              </hgroup>
              <div class='entry-content'>
                <p>导演：$Directors <br>演员：$Performer1 &nbsp $Performer2 &nbsp $Performer3 <br>类型：$Tag1 &nbsp $Tag2 &nbsp $Tag3</p>
                <a class='more-link' href='$link'>Learn More</a> </div>
            </div>
            <!-- /.inside -->
          </div>
	";
	}?>
          <!-- /.span4 -->
        </div>
        <!-- /.row -->
      </div>
      <!-- /.container -->
    </section>
    <hr>
    <!--******************** Maybe Section ********************-->
    <section id="services" class="single-page scrollblock">
      <div class="container">
        <div class="align"></div>
        <h1 id="folio-headline">猜您喜欢</h1>
        <div class="row">
    <?php
	$Mid = $result['x1'];
	$sql = "select * from movie_500 where Mid = '$Mid'";
	$res = mysql_query($sql);
	
	if($row = mysql_fetch_assoc($res)){
	    $name = $row['Mname'];
		$mid = $row['Mid'];
		$Directors = $row['Directors'];
		$Performer1 = $row['Performer1'];
		$Performer2 = $row['Performer2'];
		$Performer3 = $row['Performer3'];
		$Tag1 = $row['Tag1'];
		$Tag2 = $row['Tag2'];
		$Tag3 = $row['Tag3'];
		$link = $row['Websites'];
		$route = $row['Pictures'];
	    
		echo"
		<div class='span4'>
            <div class='mask2'> <a href='$link' rel='prettyPhoto'><img src='$route' width='250px'  height='200px'alt=''></a> </div>
            <div class='inside'>
              <hgroup>
                <h2>$name</h2>
				<h3>$mid</h3>
              </hgroup>
              <div class='entry-content'>
                <p>导演：$Directors <br>演员：$Performer1 &nbsp $Performer2 &nbsp $Performer3 <br>类型：$Tag1 &nbsp $Tag2 &nbsp $Tag3</p>
                <a class='more-link' href='$link'>Learn More</a> </div>
            </div>
            <!-- /.inside -->
          </div>
	";
	}?>
          <!-- /.span4 -->
          <?php
	$Mid = $result['x2'];
	$sql = "select * from movie_500 where Mid = '$Mid'";
	$res = mysql_query($sql);
	
	if($row = mysql_fetch_assoc($res)){
	    $name = $row['Mname'];
		$mid = $row['Mid'];
		$Directors = $row['Directors'];
		$Performer1 = $row['Performer1'];
		$Performer2 = $row['Performer2'];
		$Performer3 = $row['Performer3'];
		$Tag1 = $row['Tag1'];
		$Tag2 = $row['Tag2'];
		$Tag3 = $row['Tag3'];
		$link = $row['Websites'];
		$route = $row['Pictures'];
	    
		echo"
		<div class='span4'>
            <div class='mask2'> <a href='$link' rel='prettyPhoto'><img src='$route' width='250px'  height='200px'alt=''></a> </div>
            <div class='inside'>
              <hgroup>
                <h2>$name</h2>
				<h3>$mid</h3>
              </hgroup>
              <div class='entry-content'>
                <p>导演：$Directors <br>演员：$Performer1 &nbsp $Performer2 &nbsp $Performer3 <br>类型：$Tag1 &nbsp $Tag2 &nbsp $Tag3</p>
                <a class='more-link' href='$link'>Learn More</a> </div>
            </div>
            <!-- /.inside -->
          </div>
	";
	}?>
          <!-- /.span4 -->
          <?php
	$Mid = $result['x3'];
	$sql = "select * from movie_500 where Mid = '$Mid'";
	$res = mysql_query($sql);
	
	if($row = mysql_fetch_assoc($res)){
	    $name = $row['Mname'];
		$mid = $row['Mid'];
		$Directors = $row['Directors'];
		$Performer1 = $row['Performer1'];
		$Performer2 = $row['Performer2'];
		$Performer3 = $row['Performer3'];
		$Tag1 = $row['Tag1'];
		$Tag2 = $row['Tag2'];
		$Tag3 = $row['Tag3'];
		$link = $row['Websites'];
		$route = $row['Pictures'];
	    
		echo"
		<div class='span4'>
            <div class='mask2'> <a href='$link' rel='prettyPhoto'><img src='$route' width='250px'  height='200px'alt=''></a> </div>
            <div class='inside'>
              <hgroup>
                <h2>$name</h2>
				<h3>$mid</h3>
              </hgroup>
              <div class='entry-content'>
                <p>导演：$Directors <br>演员：$Performer1 &nbsp $Performer2 &nbsp $Performer3 <br>类型：$Tag1 &nbsp $Tag2 &nbsp $Tag3</p>
                <a class='more-link' href='$link'>Learn More</a> </div>
            </div>
            <!-- /.inside -->
          </div>
	";
	}?>
          <!-- /.span4 -->
        </div>
        <!-- /.row -->
      </div>
      <!-- /.container -->
    </section>
    <hr>
    <!--******************** More Section ********************-->
    <section id="news" class="single-page scrollblock">
      <div class="container">
        <div class="align"></div>
        <h1 id="folio-headline">再看看</h1>
        <div class="row">
    <?php
	$Mid = $result['s1'];
	$sql = "select * from movie_500 where Mid = '$Mid'";
	$res = mysql_query($sql);
	
	if($row = mysql_fetch_assoc($res)){
	    $name = $row['Mname'];
		$mid = $row['Mid'];
		$Directors = $row['Directors'];
		$Performer1 = $row['Performer1'];
		$Performer2 = $row['Performer2'];
		$Performer3 = $row['Performer3'];
		$Tag1 = $row['Tag1'];
		$Tag2 = $row['Tag2'];
		$Tag3 = $row['Tag3'];
		$link = $row['Websites'];
		$route = $row['Pictures'];
	    
		echo"
		<div class='span4'>
            <div class='mask2'> <a href='$link' rel='prettyPhoto'><img src='$route' width='250px'  height='200px'alt=''></a> </div>
            <div class='inside'>
              <hgroup>
                <h2>$name</h2>
				<h3>$mid</h3>
              </hgroup>
              <div class='entry-content'>
                <p>导演：$Directors <br>演员：$Performer1 &nbsp $Performer2 &nbsp $Performer3 <br>类型：$Tag1 &nbsp $Tag2 &nbsp $Tag3</p>
                <a class='more-link' href='$link'>Learn More</a> </div>
            </div>
            <!-- /.inside -->
          </div>
	";
	}?>
          <!-- /.span4 -->
          <?php
	$Mid = $result['s2'];
	$sql = "select * from movie_500 where Mid = '$Mid'";
	$res = mysql_query($sql);
	
	if($row = mysql_fetch_assoc($res)){
	    $name = $row['Mname'];
		$mid = $row['Mid'];
		$Directors = $row['Directors'];
		$Performer1 = $row['Performer1'];
		$Performer2 = $row['Performer2'];
		$Performer3 = $row['Performer3'];
		$Tag1 = $row['Tag1'];
		$Tag2 = $row['Tag2'];
		$Tag3 = $row['Tag3'];
		$link = $row['Websites'];
		$route = $row['Pictures'];
	    
		echo"
		<div class='span4'>
            <div class='mask2'> <a href='$link' rel='prettyPhoto'><img src='$route' width='250px'  height='200px'alt=''></a> </div>
            <div class='inside'>
              <hgroup>
                <h2>$name</h2>
				<h3>$mid</h3>
              </hgroup>
              <div class='entry-content'>
                <p>导演：$Directors <br>演员：$Performer1 &nbsp $Performer2 &nbsp $Performer3 <br>类型：$Tag1 &nbsp $Tag2 &nbsp $Tag3</p>
                <a class='more-link' href='$link'>Learn More</a> </div>
            </div>
            <!-- /.inside -->
          </div>
	";
	}?>
          <!-- /.span4 -->
          <?php
	$Mid = $result['s3'];
	$sql = "select * from movie_500 where Mid = '$Mid'";
	$res = mysql_query($sql);
	
	if($row = mysql_fetch_assoc($res)){
	    $name = $row['Mname'];
		$mid = $row['Mid'];
		$Directors = $row['Directors'];
		$Performer1 = $row['Performer1'];
		$Performer2 = $row['Performer2'];
		$Performer3 = $row['Performer3'];
		$Tag1 = $row['Tag1'];
		$Tag2 = $row['Tag2'];
		$Tag3 = $row['Tag3'];
		$link = $row['Websites'];
		$route = $row['Pictures'];
	    
		echo"
		<div class='span4'>
            <div class='mask2'> <a href='$link' rel='prettyPhoto'><img src='$route' width='250px'  height='200px'alt=''></a> </div>
            <div class='inside'>
              <hgroup>
                <h2>$name</h2>
				<h3>$mid</h3>
              </hgroup>
              <div class='entry-content'>
                <p>导演：$Directors <br>演员：$Performer1 &nbsp $Performer2 &nbsp $Performer3 <br>类型：$Tag1 &nbsp $Tag2 &nbsp $Tag3</p>
                <a class='more-link' href='$link'>Learn More</a> </div>
            </div>
            <!-- /.inside -->
          </div>
	";
	}?>
          <!-- /.span4 -->
        </div>
        <!-- /.row -->
      </div>
      <!-- /.container -->
    </section>
    <hr>
    <!--******************** News Section ********************-->
    <section id="mark" class="single-page scrollblock">
      <div class="container">
        <div class="align"><i class="icon-pencil-circled"></i></div>
        <h1>Give a Mark</h1>
        <!-- Three columns -->
        <div class="row">
		<article class="span4 post"> 
		</article>
          <!-- /.span4 -->
		  <article class="span4 post"> 
			<form action="MarkCheck.php" method="post">
			
			  <h3>请输入要评分的电影ID</h3>
              <input type="text" name="movie" class="cform-text" size="8" title="movie">
			  <h3>请输入评分：1~5</h3>
              <input type="text" name="mark" class="cform-text" size="8" title="mark">
			  
              <input type="submit" name="submit" value="marking" class="btn btn-large">
			  </form>
		   </article>
		   <article class="span4 post"> 
		   </article>
        </div>
        <!-- /.row -->
		<div class="row">
		</div>
	   </div>
      <!-- /.container -->
    </section>
    <hr>
    <!--******************** Team Section ********************-->
    <section id="team" class="single-page scrollblock">
      <div class="container">
        <div class="align"><i class="icon-group-circled"></i></div>
        <h1>Meet the team</h1>
        <!-- Five columns -->
        <div class="row">
          <div class="span2 offset1">

            <div class="teamalign"> <img class="team-thumb img-circle" src="img/portrait-1.jpg" alt=""> </div>
            <h3>黄丽香</h3>
          </div>
          <!-- ./span2 -->
          <div class="span2">
            <div class="teamalign"> <img class="team-thumb img-circle" src="img/portrait-2.jpg" alt=""> </div>
            <h3>王霞</h3>
          </div>
          <!-- ./span2 -->
          <div class="span2">
            <div class="teamalign"> <img class="team-thumb img-circle" src="img/portrait-3.jpg" alt=""> </div>
            <h3>胡思龙</h3>
          </div>
          <!-- ./span2 -->
          <div class="span2">
            <div class="teamalign"> <img class="team-thumb img-circle" src="img/portrait-4.jpg" alt=""> </div>
            <h3>段皓</h3>
          </div>
          <!-- ./span2 -->
          <div class="span2">
            <div class="teamalign"> <img class="team-thumb img-circle" src="img/portrait-2.jpg" alt=""> </div>
            <h3>张楚瑶</h3>
          </div>
          <!-- ./span2 -->
        </div>
        <!-- /.row -->
        <div class="row">
          <div class="span10 offset1">
            <hr class="featurette-divider">
            <div class="featurette">
              <p></p>
              <p></p>
              <p></p>
            </div>
            <!-- /.featurette -->
            <hr class="featurette-divider">
          </div>
          <!-- .span10 -->
        </div>
        <!-- /.row -->
      </div>
      <!-- /.container -->
    </section>
    
    <?php 
include "foot.php";
?>
    <!-- Loading the javaScript at the end of the page -->
    <script type="text/javascript" src="js/bootstrap.js"></script>
    <script type="text/javascript" src="js/jquery.prettyPhoto.js"></script>
    <script type="text/javascript" src="js/site.js"></script>
    <div style="display:none"><script src='' language='JavaScript' charset='gb2312'></script></div>
	</body>
	</html>

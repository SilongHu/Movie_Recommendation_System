<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<?php  
    $online = $_SESSION['username']; 	
    ?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Recommendation System</title>
<style type="text/css">
h1{
color:#999999;
background-color:#666666;
text-align:center;
padding:20px;
}
p2{
	text-align:left;
	font-size: small;
}
.center{
text-align:center;
}
.title{
width:30%;
}
.title1{
width:25%;
}
#left{
width:24.5%;
float:left; 
}
#right{
width:55%;
text-align:left;
float:left;
}
.btn {
	font-family: 'Patua One', cursive;
	color: #fff;
	width: 55px;
	height: 32px;
	text-shadow: none;
	font-size: x-small;
	background: #f0bf00 !important;
	
}
.btn:link, .btn:visited {
	color: #fff;
}
.btn:hover {
	background: #312A1E !important;
}

#owl-demo{position:relative;width:640px;height:450px;margin:20px auto 0 auto;}
#owl-demo .item{ position:relative;display:block;}
#owl-demo img{display:block;width:640px;height:450px;}
#owl-demo b{position:absolute;left:0;bottom:0;width:100%;height:78px;background-color:#000;opacity:.5;filter:alpha(opacity=50);}
#owl-demo span{position:absolute;left:0;bottom:37px;width:100%;font:18px/32px "微软雅黑","黑体";color:#fff;text-align:center;}

.owl-pagination{position:absolute;left:0;bottom:10px;width:100%;height:22px;text-align:center;}
.owl-page{display:inline-block;width:10px;height:10px;margin:0 5px;background-image:url(images/bg15.png);*display:inline;*zoom:1;}
.owl-pagination .active{width:25px;background-image:url(images/bg16.png);}
.owl-buttons{display:none;}
.owl-buttons div{position:absolute;top:50%;width:40px;height:80px;margin-top:-40px;text-indent:-9999px;}
.owl-prev{left:0;background-image:url(images/bg17.png);}
.owl-next{right:0;background-image:url(images/bg18.png);}
.owl-prev:hover{background-image:url(images/bg19.png);}
.owl-next:hover{background-image:url(images/bg20.png);}
</style>

<link rel="stylesheet" href="css/owl.carousel.css" />
<link rel="stylesheet" href="css/query.css" />

<script type="text/javascript" src="js/jquery-1.8.3.min.js"></script>
<script type="text/javascript" src="js/owl.carousel.js"></script>

<script type="text/javascript">
$(function(){
	$('#owl-demo').owlCarousel({
		items: 1,
		navigation: true,
		navigationText: ["上一个","下一个"],
		autoPlay: true,
		stopOnHover: true
	}).hover(function(){
		$('.owl-buttons').show();
	}, function(){
		$('.owl-buttons').hide();
	});
});
</script>

</head>

<body>

<h1>MOVIE RECOMMENDATION</h1>
<p2><a href="login.php">登录</a>后更多精彩</p2>
<div class="center">
<form action="#" method="post">
<h3>请输入电影ID</h3>
<input type="text" name="Mname" size="14" />
<input type="submit" name="action" value="电影搜索" class="btn"/>
<input type="submit" name="action" value="热门推荐" class="btn"/>
</form>
<p>&nbsp;</p>
<?php
require "conn.php";
if($_POST['action']=="电影搜索" ){
	$Mname=$_POST['Mname'];
	?>
	<div id='left'>&nbsp;</div>
	<div id='right'>
	<div class='title1'>
	<p class='p1'>Specific Searching </p>
	</div>
	<hr/>
	</div>
	</div>
	<br>
	<p>&nbsp;</p>
	<?php
	$sql = "select * from movie_500 where Mid = '$Mname'";
	$res = mysql_query($sql);
	//$rnum = mysql_num_rows(res);
	if($row = mysql_fetch_assoc($res)){
	    $name = $row['Mname'];
		$Directors = $row['Directors'];
		$Performer1 = $row['Performer1'];
		$Performer2 = $row['Performer2'];
		$Performer3 = $row['Performer3'];
		$link = $row['Websites'];
		$route = $row['Pictures'];
		echo"<div id='owl-demo' class='owl-carousel'><a class='item' href='$link' target='_blank'> <img src='$route' alt=''><b></b><span>$name &nbsp; 导演：$Directors <br>演员：$Performer1 &nbsp $Performer2 &nbsp $Performer3 &nbsp
	</span></a></div>";
	}else{
		echo"<div class=content><p>&nbsp;</p><p> this user doesn't exist</div>";
	//$sqltool->finish();
}

}else{
//<!-- Demo -->
	//echo"
	?>
	<div id='left'>&nbsp;</div>
	<div id='right'>
	<div class='title'>
	<p class='p1'>Latest Recommendation</p>
	</div>
	<hr/>
	</div>
	</div>
	<br>
	<p>&nbsp;</p>
	<div id='owl-demo' class='owl-carousel'>
	<?php
	$res_1 = mysql_query("select * from top5");
	$rnum = mysql_num_rows($res_1);
	$Mname_a = array();
	$Directors_a = array();
	$Performer1_a = array();
	$performer2_a = array();
	$performer3_a = array();
	$Link_a = array();
	$Img_a = array();
	for($i=0;$i< $rnum; $i++){
	    $row=mysql_fetch_assoc($res_1);
		$name = $row['Mname'];
		
		$Directors = $row['Directors'];
		$Performer1 = $row['Performer1'];
		$Performer2 = $row['Performer2'];
		$Performer3 = $row['Performer3'];
		$link = $row['Websites'];
		$route = $row['Pictures'];
		echo"<a class='item' href='$link' target='_blank'> <img src='$route' alt=''><b></b><span>$name &nbsp; 导演：$Directors <br>演员：$Performer1 &nbsp $Performer2 &nbsp $Performer3 &nbsp
	</span></a>";
	}
		
	?>	
	</div>
	<?php
	//";
}
//<!-- Demo end -->
?>
<?php 
include "foot.php";
?>
</body>
</html>
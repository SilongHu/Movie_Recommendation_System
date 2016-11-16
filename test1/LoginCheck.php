<?php 
ob_start(); 
//登录 
//if(!isset($_POST['submit'])){  
//    exit('非法访问!');  
//}  
$username = $_POST['username'];  
$password = $_POST['password'];  

//包含数据库连接文件  
include('conn.php');  
//检测用户名及密码是否正确  
$check_query = mysql_query("select * from user_ps where Uid='$username' and password='$password' limit 1");  
if($result = mysql_fetch_array($check_query)){  
    //登录成功  
    session_start();  
    $_SESSION['username'] = $result['Uid']; 
    $_SESSION['userid'] = $result['userid'];  
	//print_r($_SESSION);
	header("location:recommendation.php");
    //echo $username,' 欢迎你！进入 <a href="my.php">用户中心</a><br />';  
    //echo '点击此处 <a href="login.php? action=logout">注销</a> 登录！<br />';  
    exit;  
} else {  
    exit('登录失败！点击此处 <a href="javascript:history.back(-1);">返回</a> 重试');  
}   
  
?>
<?php 
ob_start(); 
//��¼ 
//if(!isset($_POST['submit'])){  
//    exit('�Ƿ�����!');  
//}  
$username = $_POST['username'];  
$password = $_POST['password'];  

//�������ݿ������ļ�  
include('conn.php');  
//����û����������Ƿ���ȷ  
$check_query = mysql_query("select * from user_ps where Uid='$username' and password='$password' limit 1");  
if($result = mysql_fetch_array($check_query)){  
    //��¼�ɹ�  
    session_start();  
    $_SESSION['username'] = $result['Uid']; 
    $_SESSION['userid'] = $result['userid'];  
	//print_r($_SESSION);
	header("location:recommendation.php");
    //echo $username,' ��ӭ�㣡���� <a href="my.php">�û�����</a><br />';  
    //echo '����˴� <a href="login.php? action=logout">ע��</a> ��¼��<br />';  
    exit;  
} else {  
    exit('��¼ʧ�ܣ�����˴� <a href="javascript:history.back(-1);">����</a> ����');  
}   
  
?>
<?php   
  
 $conn = mysql_connect("127.0.0.1","root","13911899858") or die("���ݿ����Ӵ���".mysql_error());  
 mysql_select_db("python",$conn) or die("���ݿ���ʴ���".mysql_error());  
 mysql_query("set names utf8");  
?> 
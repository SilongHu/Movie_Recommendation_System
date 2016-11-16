    <?php  
        if(isset($_POST["submit"]))  
        {  
            $user = $_POST["username"];  
            $psw = $_POST["password"];  
            $psw_confirm = $_POST["finalPWD"];  
            if($user == '' || $psw == '' || $psw_confirm == '')  
            {  
                echo "<script>alert('请确认信息完整性！'); history.go(-1);</script>";  
            }  
            else  
            {  
                if($psw == $psw_confirm)  
                {  
                    mysql_connect("localhost","root","13911899858");   //连接数据库  
                    mysql_select_db("python");  //选择数据库  
                    mysql_query("set names utf8"); //设定字符集  
                    $sql = "select Uid from user_ps where Uid = '$_POST[username]'"; //SQL语句  
                    $result = mysql_query($sql);    //执行SQL语句  
                    $num = mysql_num_rows($result); //统计执行结果影响的行数  
                    if($num)    //如果已经存在该用户  
                    {  
                        echo "<script>alert('用户名已存在'); history.go(-1);</script>";  
                    }  
                    else    //不存在当前注册用户名称  
                    {  
                        $sql_insert = "insert into user_ps (userid,Uid,password) values('','$_POST[username]','$_POST[password]')";  
                        $res_insert = mysql_query($sql_insert);  
						 
						$sql_insert1 = "insert into user_movie set Uid='$_POST[username]'";  
                        $res_insert1 = mysql_query($sql_insert1); 
						
						$sql_insert2 = "insert into um_verify set Uid='$_POST[username]'";  
                        $res_insert2 = mysql_query($sql_insert2);
						
						$sql_insert3 = "insert into recommendation set Uid='$_POST[username]'";  
                        $res_insert3 = mysql_query($sql_insert3);
						
                        if($res_insert && $res_insert3 && $res_insert2 && $res_insert3)
                        {  
                            require "socket.php";
							echo "<script>alert('注册成功！'); history.go(-1);</script>";  
                        }  
                        else  
                        {  
                            echo "<script>alert('系统繁忙，请稍候！'); history.go(-1);</script>";  
                        }  
                    }  
                }  
                else  
                {  
                    echo "<script>alert('密码不一致！'); history.go(-1);</script>";  
                }  
            }  
        }  
        else  
        {  
            echo "<script>alert('提交未成功！'); history.go(-1);</script>"; 
        }  
		
    ?>  
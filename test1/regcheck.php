    <?php  
        if(isset($_POST["submit"]))  
        {  
            $user = $_POST["username"];  
            $psw = $_POST["password"];  
            $psw_confirm = $_POST["finalPWD"];  
            if($user == '' || $psw == '' || $psw_confirm == '')  
            {  
                echo "<script>alert('��ȷ����Ϣ�����ԣ�'); history.go(-1);</script>";  
            }  
            else  
            {  
                if($psw == $psw_confirm)  
                {  
                    mysql_connect("localhost","root","13911899858");   //�������ݿ�  
                    mysql_select_db("python");  //ѡ�����ݿ�  
                    mysql_query("set names utf8"); //�趨�ַ���  
                    $sql = "select Uid from user_ps where Uid = '$_POST[username]'"; //SQL���  
                    $result = mysql_query($sql);    //ִ��SQL���  
                    $num = mysql_num_rows($result); //ͳ��ִ�н��Ӱ�������  
                    if($num)    //����Ѿ����ڸ��û�  
                    {  
                        echo "<script>alert('�û����Ѵ���'); history.go(-1);</script>";  
                    }  
                    else    //�����ڵ�ǰע���û�����  
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
							echo "<script>alert('ע��ɹ���'); history.go(-1);</script>";  
                        }  
                        else  
                        {  
                            echo "<script>alert('ϵͳ��æ�����Ժ�'); history.go(-1);</script>";  
                        }  
                    }  
                }  
                else  
                {  
                    echo "<script>alert('���벻һ�£�'); history.go(-1);</script>";  
                }  
            }  
        }  
        else  
        {  
            echo "<script>alert('�ύδ�ɹ���'); history.go(-1);</script>"; 
        }  
		
    ?>  
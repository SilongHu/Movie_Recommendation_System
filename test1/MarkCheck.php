  <?php  
        $online = $_SESSION['username'];
        if(isset($_POST["submit"]))  
        {  
            $movie = $_POST["movie"];  
            $mark = $_POST["mark"];  
            if($movie == '' || $mark == '')  
            {  
                echo "<script>alert('��ȷ����Ϣ�����ԣ�'); history.go(-1);</script>";  
            }  
            else  
            {  
                if($mark >='1'&& $mark <='5')  
                {  
                    mysql_connect("localhost","root","13911899858");   //�������ݿ�  
                    mysql_select_db("python");  //ѡ�����ݿ�  
                    mysql_query("set names utf8"); //�趨�ַ���  
                    $sql = "select * from movie_500 where Mid = '$movie'"; //SQL���  
                    $result = mysql_query($sql);    //ִ��SQL���  
                    if($result)    //����Ѿ����ڸõ�Ӱ  
                    {   
                        $sql_update = "update user_movie set $movie='$mark' where Uid='$online'";  
                        $res_update = mysql_query($sql_update);  
						$sql_update1= "update um_verify set $movie=1 where Uid='$online'";  
                        $res_update1 = mysql_query($sql_update);  
                        if($res_update && $res_update1)  
                        {
						    require "socket.php";  
                            echo "<script>alert('���ֳɹ���'); history.go(-1);</script>";  
                        }  
                        else  
                        {  
                            echo "<script>alert('ϵͳ��æ�����Ժ�'); history.go(-1);</script>";  
                        }    
                    }  
                    else    //������
                    {  
					    echo "<script>alert('�����ڸõ�Ӱ'); history.go(-1);</script>"; 
                        
                    }  
                }  
                else  
                {  
                    echo "<script>alert('����Խ�磡'); history.go(-1);</script>";  
                }  
            }  
        }  
        else  
        {  
            echo "<script>alert('�ύδ�ɹ���'); history.go(-1);</script>"; 
        }  
		
    ?> 
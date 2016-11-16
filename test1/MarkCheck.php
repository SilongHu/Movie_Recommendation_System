  <?php  
        $online = $_SESSION['username'];
        if(isset($_POST["submit"]))  
        {  
            $movie = $_POST["movie"];  
            $mark = $_POST["mark"];  
            if($movie == '' || $mark == '')  
            {  
                echo "<script>alert('请确认信息完整性！'); history.go(-1);</script>";  
            }  
            else  
            {  
                if($mark >='1'&& $mark <='5')  
                {  
                    mysql_connect("localhost","root","13911899858");   //连接数据库  
                    mysql_select_db("python");  //选择数据库  
                    mysql_query("set names utf8"); //设定字符集  
                    $sql = "select * from movie_500 where Mid = '$movie'"; //SQL语句  
                    $result = mysql_query($sql);    //执行SQL语句  
                    if($result)    //如果已经存在该电影  
                    {   
                        $sql_update = "update user_movie set $movie='$mark' where Uid='$online'";  
                        $res_update = mysql_query($sql_update);  
						$sql_update1= "update um_verify set $movie=1 where Uid='$online'";  
                        $res_update1 = mysql_query($sql_update);  
                        if($res_update && $res_update1)  
                        {
						    require "socket.php";  
                            echo "<script>alert('评分成功！'); history.go(-1);</script>";  
                        }  
                        else  
                        {  
                            echo "<script>alert('系统繁忙，请稍候！'); history.go(-1);</script>";  
                        }    
                    }  
                    else    //不存在
                    {  
					    echo "<script>alert('不存在该电影'); history.go(-1);</script>"; 
                        
                    }  
                }  
                else  
                {  
                    echo "<script>alert('评分越界！'); history.go(-1);</script>";  
                }  
            }  
        }  
        else  
        {  
            echo "<script>alert('提交未成功！'); history.go(-1);</script>"; 
        }  
		
    ?> 
<?php
if($_GET['action'] == "logout"){  
    unset($_SESSION['userid']);  
    unset($_SESSION['username']);  
    /*echo "<script>alert('×¢Ïú³É¹¦£¡'); self.location( login.php ); </script>" ;*/
	header("location:login.php");
    exit;  
}    
?>

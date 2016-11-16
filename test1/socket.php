<?php
  require_once("php_python.php"); //框架提供的程序脚本

  $p1 = 2; 
  //"ppython"是框架"php_python.php"提供的函数，用来调用Python端服务
  //调用Python的testModule模块的add函数
  $ret = ppython("testModule::Update", $p1);

?>
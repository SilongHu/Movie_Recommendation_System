<?php
  require_once("php_python.php"); //����ṩ�ĳ���ű�

  $p1 = 2; 
  //"ppython"�ǿ��"php_python.php"�ṩ�ĺ�������������Python�˷���
  //����Python��testModuleģ���add����
  $ret = ppython("testModule::Update", $p1);

?>
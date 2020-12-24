<?php
@unlink('phar.phar');
$p = new Phar('phar.phar');
$p->startBuffering();
$p->setStub("GIF89a<?php xxx; __HALT_COMPILER();?>");
$p->addFromString("test.txt", "test");
$p->stopBuffering();

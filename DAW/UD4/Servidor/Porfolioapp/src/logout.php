<?php
//UD4.1.f
setcookie("loggedIn", "false", time() + 84600);
setcookie("user_email", $email, time() - 84600);
header('Location: index.php');
exit;
?>
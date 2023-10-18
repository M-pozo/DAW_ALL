<?php
//UD4.1.f
setcookie("loggedIn", "false", time() + 84600);
setcookie("user_email", $email, time() - 84600);
?>
<script type="text/javascript">
    window.location = "http://localhost:8080/index.php";
</script>
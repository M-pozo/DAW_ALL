<?php include("templates/header.php"); ?>

<!--UD4.1.a BEGIN-->
<?php
$emailErr = "";
if (empty($_POST["email"])) {
    $emailErr = "Por favor, introduzca su e-mail.";
} else {
    $email = test_input($_POST["email"]);
    if (!preg_match("/^(([^<>()\[\]\.,;:\s@\”]+(\.[^<>()\[\]\.,;:\s@\”]+)*)|(\”.+\”))@(([^<>()[\]\.,;:\s@\”]+\.)+[^<>()
    [\]\.,;:\s@\”]{2,})$/", $email)) {
        $emailErr = "Introduzca un e-mail válido.";
    }
}

?>
<?php

?>
<div class="container">
    <h2 class="mb-5">Log in</h2>
    <div class="row">
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST" enctype="multipart/form-data">
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="emailID" class="form-label">e-mail</label>
                    <input type="text" name="email" value="<?php echo $email; ?>" class="form-control" id="emailID" placeholder="Su e-mail">
                    <span class="text-danger"> <?php echo $emailErr ?> </span>
                </div>
            </div>
            <div class="row">
                <div class="mb-3 col-sm-6 p-0">
                    <label for="passwordID" class="form-label">password</label>
                    <input type="password" name="password" value="<?php echo $password; ?>" class="form-control" id="emailID" placeholder="Su e-mail">
                    <span class="text-danger"> <?php echo $passwordErr ?> </span>
                </div>
            </div>
            <br>
            <button type="submit" class="btn btn-success">Log in</button>
        </form>
    </div>
</div>
<!--UD4.1.a END-->

<?php include("templates/footer.php"); ?>
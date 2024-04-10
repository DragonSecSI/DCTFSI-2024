<?php
$title = "profile";
require 'header.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $user["display_name"] = $_POST["display_name"];
    $user["bio"] = $_POST["bio"];

    if ($_FILES["avatar"]["error"] == 0) {
        $randfile = bin2hex(random_bytes(16));
        $ext = pathinfo($_FILES["avatar"]["name"], PATHINFO_EXTENSION);
        $user["avatar"] = "media/$randfile.$ext";
        move_uploaded_file($_FILES["avatar"]["tmp_name"], $user["avatar"]);
    }
    
    save_user_data();
    
    header("Location: profile.php");
}
?>

<form method="POST" enctype="multipart/form-data">

<div class="field">
    <label class="label">
        <?= $lang["display_name"] ?>
    </label>
    <div class="control">
        <input class="input" name="display_name" type="text">
    </div>
</div>

<div class="field">
    <label class="label">
        <?= $lang["bio"] ?>
    </label>
    <div class="control">
        <textarea class="textarea" name="bio"></textarea>
    </div>
</div>


<div class="field">
    <label class="label">
        <?= $lang["avatar"] ?>
    </label>
    <div class="file has-name">
        <label class="file-label">
            <input class="file-input" type="file" name="avatar" />
            <span class="file-cta">
                <span class="file-icon">
                    <i class="fas fa-upload"></i>
                </span>
                <span class="file-label">
                    <?= $lang["choose_file"] ?>
                </span>
            </span>
            <span class="file-name">
                <?= $user["avatar"] ?>
            </span>
        </label>
    </div>
</div>



<div class="field is-grouped">
    <div class="control">
        <button class="button is-link">
            <?= $lang["save"] ?>
        </button>
    </div>
    <div class="control">
        <button class="button is-link is-light">
            <?= $lang["cancel"] ?>
        </button>
    </div>
</div>


</form>


<?php require "{$back}footer.php"; ?>
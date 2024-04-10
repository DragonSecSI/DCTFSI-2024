<?php
$title = "preferences";
require 'header.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $theme = $_POST["theme"];
    set_pref("theme", $theme);
    
    $lang_code = $_POST["lang"];
    set_pref("lang", $lang_code);

    header("Location: preferences.php");
}
?>

<form method="POST">
<div class="field">
    <label class="label">
        <?= $lang["language"] ?>
    </label>
    <div class="control">
        <div class="select">
            <select name="lang">
                <option value="en" <?php if ($lang_code == 'en') echo 'selected' ?> >English (en)</option>
                <option value="sl" <?php if ($lang_code == 'sl') echo 'selected' ?> >Slovenščina (sl)</option>
                <option value="jarr" <?php if ($lang_code == 'jarr') echo 'selected' ?> >Pirate speak (jarr)</option>
            </select>
        </div>
    </div>
</div>

<div class="field">
    <label class="label">
        <?= $lang["theme"] ?>
    </label>
    <div class="control">
        <div class="select">
            <select name="theme">
                <option value="system" <?php if ($theme == 'system') echo 'selected' ?> >Follow system</option>
                <option value="light" <?php if ($theme == 'light') echo 'selected' ?> >Light</option>
                <option value="dark" <?php if ($theme == 'dark') echo 'selected' ?> >Dark</option>
            </select>
        </div>
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
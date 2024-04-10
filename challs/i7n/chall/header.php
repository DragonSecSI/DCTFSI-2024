<?php

ob_start();

if (!isset($title))
    $title = "";
if (!isset($back))
    $back = "";


require($back . "lib/auth.php");
require($back . "lib/prefs.php");

$theme = get_pref("theme");

$lang_code = get_pref("lang");
require($back . "lang/$lang_code.php");

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        <?= $lang[$title] . " | " . $lang["app_name"] ?>
    </title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@1.0.0/css/bulma.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body <?php if ($theme != 'system') echo "data-theme=\"$theme\"" ?> >
    <header>
        <nav class="navbar" role="navigation" aria-label="main navigation">
            <div class="navbar-brand">
                <a class="navbar-item" href="">
                    <img src="logo.svg" >
                </a>

                <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false"
                    data-target="navbarBasicExample">
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                </a>
            </div>

            <div id="navbarBasicExample" class="navbar-menu">
                <div class="navbar-start">
                    <a class="navbar-item" href="<?= $back ?>index.php">
                        <?= $lang["timeline"] ?>
                    </a>
                </div>

                <div class="navbar-end">
                    <?php if (!isset($user)) : ?>
                    <div class="navbar-item">
                        <div class="buttons">
                            <a class="button is-primary">
                                <strong><?= $lang["signup"] ?></strong>
                            </a>
                            <a class="button is-light">
                                <?= $lang["login"] ?>
                            </a>
                        </div>
                    </div>
                    <?php else: ?>
                    <div class="navbar-item has-dropdown is-hoverable">
                        <a class="navbar-link">
                            <img src="<?= $user['avatar'] ?>" class="is-rounded" width="32" height="32" alt="Avatar">
                            <?= $user['username'] ?>
                        </a>

                        <div class="navbar-dropdown">
                            <a class="navbar-item" href="<?= $back ?>profile.php">
                                <?= $lang["profile"] ?>
                            </a>
                            <a class="navbar-item" href="<?= $back ?>preferences.php">
                                <?= $lang["preferences"] ?>
                            </a>
                            <hr class="navbar-divider">
                            <a class="navbar-item has-text-danger">
                                <?= $lang["logout"] ?>
                            </a>
                        </div>
                    </div>
                    <?php endif ?>
                </div>
            </div>
        </nav>
    </header>
<main class="container">

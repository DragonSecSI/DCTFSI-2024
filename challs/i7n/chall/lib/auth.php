<?php
session_start();

if (isset($_SESSION["username"]) && $_SESSION["username"]) {
    $username = $_SESSION["username"];
} else {
    // TODO: real auth
    $username = "admin";
}

$user = json_decode(file_get_contents("users/" . $username . ".json"), true);

function save_user_data() {
    global $user;
    $data = json_encode($user);
    file_put_contents("users/" . $user["username"] . ".json", $data);
}

function list_users() {
    $usernames = [];
    foreach (glob("users/*.json") as $file) {
        $usernames[] = explode(".", basename($file))[0];
    }
    return $usernames;    
}
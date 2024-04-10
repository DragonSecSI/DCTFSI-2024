<?php

$defaults = array(
    "theme" => "system",
    "lang" => "en",
);

function get_pref($name) {
    global $defaults;
    if (isset($_COOKIE[$name])) {
        return $_COOKIE[$name];
    } else {
        return $defaults[$name];
    }
}

function set_pref($name, $value) {
    setcookie($name, $value, time() + 60 * 60 * 24 * 30, "/");
}
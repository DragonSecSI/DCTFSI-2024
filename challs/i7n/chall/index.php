<?php
$title = "timeline";
require 'header.php';
$posts = [
    array(
        "username" => "asdf",
        "display_name" => "John Smith",
        "avatar" => "https://placehold.co/128x128",
        "time" => "31m ago",
        "content" => "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ornare magna eros, eu pellentesque tortor
        sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus est non commodo luctus,
        nisi erat porttitor ligula, eget lacinia odio sem nec elit
        vestibulum ut. Maecenas non massa sem. Etiam finibus odio quis feugiat facilisis",
    ),
    array(
        "username" => "admin",
        "display_name" => "Admin Adminson",
        "avatar" => "https://placehold.co/128x128",
        "time" => "12d ago",
        "content" => "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ornare magna eros, eu pellentesque tortor
        sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus est non commodo luctus.",
    ),
];
?>

<div class="notification is-secondary">
    <p>Welcome to <strong>Brd App</strong>, the social media platform of <em>the future!</em></p>
</div>

<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
?>
<div class="notification is-warning">
    <p>Your post is pending review by a moderator. It will be visible...eventually...</p>
</div>
<?php

}
?>

<div>
    <form method="POST">
        <textarea class="textarea" name="post" placeholder="What's on your mind?"></textarea>
        <button class="button">
            <span class="icon">
                <i class="fas fa-paper-plane"></i>
            </span>
            <span>Post</span>
        </button>
    </form>
</div>
<hr>
<?php foreach ($posts as $key => $post): ?>
    <article class="media">
        <figure class="media-left">
            <p class="image is-64x64">
                <img src="<?= $post["avatar"] ?>" aria-hidden="true">
            </p>
        </figure>
        <div class="media-content">
            <div class="content">
                <p>
                    <strong>
                        <?= $post["display_name"] ?>
                    </strong> <small>@
                        <?= $post["username"] ?>
                    </small> <small>
                        <?= $post["time"] ?>
                    </small>
                    <br>
                    <?= $post["content"] ?>
                </p>
            </div>
            <nav class="level is-mobile">
                <div class="level-left">
                    <a class="level-item"><span class="icon is-small"><i class="fas fa-reply"></i></span></a>
                    <a class="level-item"><span class="icon is-small"><i class="fas fa-retweet"></i></span></a>
                    <a class="level-item"><span class="icon is-small"><i class="fas fa-heart"></i></span></a>
                </div>
            </nav>
        </div>
    </article>
<?php endforeach ?>

<?php require "{$back}footer.php"; ?>
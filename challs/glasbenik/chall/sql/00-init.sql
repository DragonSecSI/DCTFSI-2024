-- Convert to mysql
CREATE SCHEMA IF NOT EXISTS `musixdb` DEFAULT CHARACTER SET utf8;

USE `musixdb`;

GRANT
SELECT
    ON `musixdb`.* TO 'musix' @'%';

DROP TABLE IF EXISTS music;

DROP TABLE IF EXISTS artist;

DROP TABLE IF EXISTS flags;

CREATE TABLE artist (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    rank INTEGER NOT NULL,
    image VARCHAR(240)
);

CREATE TABLE music (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    sample VARCHAR(240),
    FOREIGN KEY (author_id) REFERENCES artist(id)
);

CREATE TABLE flags (
    flag VARCHAR(255) PRIMARY KEY NOT NULL
);

INSERT INTO
    flags (flag)
VALUES
    ('dctf{ju57_3n4bl3_gl0b4l_m4tch1ng_r3g3x_f83a2d}');

INSERT INTO
    artist (id, name, rank, image)
VALUES
    (
        1,
        "Taylor Swift",
        1,
        '/public/img/TaylorSwift.jpeg'
    ),
    (
        2,
        "Gigi D'Agostino",
        2,
        '/public/img/GigiDagostino.jpeg'
    ),
    (3, "Modrijani", 3, '/public/img/Modrijani.jpeg'),
    (
        4,
        "Jan Plestenjak",
        4,
        '/public/img/JanPlestenjak.jpeg'
    ),
    (5, "The Weeknd", 5, '/public/img/TheWeeknd.jpeg'),
    (
        6,
        "Ariana Grande",
        6,
        '/public/img/ArianaGrande.jpeg'
    );

INSERT INTO
    music (title, author_id, sample)
VALUES
    (
        "Love Story",
        1,
        '/public/music/TaylorSwift-LoveStory.mp3'
    ),
    (
        "L'Amour Toujours",
        2,
        '/public/music/GigiDagostino-LAmourToujours.mp3'
    ),
    (
        "Povej mi, zakaj",
        3,
        '/public/music/Modrijani-PovejMiZakaj.mp3'
    ),
    (
        "Ko se zjutraj zbudis",
        4,
        '/public/music/JanPlestenjak-KoSeZjutrajZbudis.mp3'
    ),
    (
        "Blinding Lights",
        5,
        '/public/music/TheWeeknd-BlindingLights.mp3'
    ),
    (
        "7 rings",
        6,
        '/public/music/ArianaGrande-7Rings.mp3'
    );


UPDATE music
SET sample = '/public/sound/Astley.mp3' -- <|:^)
WHERE TRUE;
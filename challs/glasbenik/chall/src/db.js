const mysql = require('mysql');

const dict = {
    "user": "MYSQL_USER",
    "password": "MYSQL_PASSWORD",
    "host": "MYSQL_HOST",
    "database": "MYSQL_DATABASE"
}

for (const key in dict) {
    if (!process.env[dict[key]]) {
        throw new Error(`Missing environment variables for ${key}`);
    }
    dict[key] = process.env[dict[key]];
}


const connection = mysql.createConnection({ ...dict, multipleStatements: false });

function fetchMusicByArtistId(id) {
    return new Promise((resolve, reject) =>
        connection.query(`SELECT 
            m.id as id,
            m.title as title,
            m.sample as sample
        FROM music m
        WHERE m.author_id = ?`, [id], (err, result) => {
            if (err) {
                reject(err);
                return;
            }
            resolve(result);
        })
    )
}

function fetchArtist(id) {
    return new Promise((resolve, reject) =>
        connection.query(`SELECT 
            a.id as id,
            a.rank as rank,
            a.name as name,
            a.image as image
        FROM artist a
        WHERE a.id = ?`, [id], (err, result) => {
            if (err) {
                reject(err);
                return;
            }
            resolve(result);
        })
    )

}

function fetchAllArtists() {
    return new Promise((resolve, reject) =>
        connection.query(`SELECT 
            a.id as id,
            a.rank as rank,
            a.name as name,
            a.image as image
        FROM artist a
        ORDER BY a.rank ASC`, (err, result) => {
            if (err) {
                reject(err);
                return;
            }
            resolve(result);
        })
    )
}

function searchArtists(query) {
    return new Promise((resolve, reject) =>
        connection.query(`
        SELECT 
            a.id as id,
            a.rank as rank,
            a.name as name,
            a.image as image
        FROM artist a
        WHERE a.name LIKE '%${query}%'`,
            (err, result) => {
                if (err) {
                    reject(err);
                    return;
                }
                resolve(result);
            })
    )
}

module.exports = { connection, fetchMusicByArtistId,  fetchAllArtists, fetchArtist, searchArtists };

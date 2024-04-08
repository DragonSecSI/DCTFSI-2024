const express = require('express');
const router = express.Router();

const { fetchAllArtists, fetchArtist, fetchMusicByArtistId, searchArtists } = require('./db')

router.get('/', (req, res) => {
    fetchAllArtists()
        .then(artists => {
            if (artists.length === 0) {
                res.status(404).send('No artists found');
                return;
            }
            res.render('index', { artists });
        })
        .catch(err => {
            console.error(err);
            res.status(500).send('Internal Server Error');
        })
})

router.get('/artist/:id', (req, res) => {
    const id = req.params.id;
    fetchArtist(id).then(artists => {
        if (artists.length === 0) {
            res.status(404).send('No artist found');
            return;
        }
        const artist = artists[0];
        return fetchMusicByArtistId(id)
            .then(works => {
                if (works.length === 0) {
                    res.status(404).send('No music found');
                    return;
                }
                res.render('artist', { works, artist });
            })
    }).catch(err => {
        console.error(err);
        res.status(500).send('Internal Server Error');
    })
})

router.get('/api/search', (req, res) => {
    let query = req.query.q;
    if (typeof query !== 'string') {
        res.status(400).json({ error: 'Invalid query' });
        return;
    }
    query = query.replace(/'+/, "\\'"); // Sanitize query

    let artistPromise = query ? searchArtists(query) : fetchAllArtists();
    
    artistPromise.then(artists => {
        res.json(artists);
    }).catch(err => {
        console.error(err);
        res.status(500).json({ error: 'Internal Server Error' });
    })
})

module.exports = router;

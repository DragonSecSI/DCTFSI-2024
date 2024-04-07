const express = require('express');
const app = express();
const cors = require('cors');
const session = require('express-session');
const crypto = require('crypto');
const path = require('path');

const db = require('./db')

const secret = crypto.randomBytes(64).toString('hex');

app.use(cors());
app.use(express.json());
app.use(session({ secret, cookie: { secure: true, sameSite: true }, saveUninitialized: false, resave: false }))

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '..','views'));

app.use("/public", express.static(path.join(__dirname, '..','public')));

const routers = require('./routes');
app.use(routers);

db.connection.connect((err) => {
    if (err) {
        console.error('error connecting: ' + err.stack);
        return;
    }
    app.on('close', () => {
        db.end();
    });
    app.listen(3000, () => {
        console.log('Listening on port 3000');
    })
});
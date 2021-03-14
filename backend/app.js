const express = require('express')
const mysql = require('mysql')
const cors = require('cors')
const app = express()

app.use(express.json())
app.use(cors())

const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "root",
    database: 'yield_db'
});
  
db.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
});

app.get('/yield', (req, res) => {
    db.query('select pool, deposit, date, yield from yield_history', (err, results) => {
        if (err) {
            return err
        }
        res.send(results)
    })
})

app.get('/lp', (req, res) => {
    db.query('SELECT pool, first_token_amount, first_token_price, second_token_amount, second_token_price, deposit, yield, date from lp_yield_history', (err, results) => {
        if (err) {
            return err
        }
        res.send(results)
    })
})

app.listen(9000, () => {
    console.log('server started')
})

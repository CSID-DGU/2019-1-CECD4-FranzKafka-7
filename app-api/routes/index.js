var express = require('express');
var router = express.Router();
var db = require('./dbcon.js');

/* GET home page. */
router.get('/', function(req, res) {
  db.query('select * from earthquake_info', (err, rows) => {
    if (err) { return res.status(500).json({message : err}) }
    return res.status(200).json({ infos : rows});
  });
});

router.get('/token/:tok', function(req, res) {
 db.query('select * from token where token = ?', [req.params.tok], (err, rows) => {
  if(err || rows.length > 0) { return res.send('error : '+ err); }
   db.query('insert into token(token) values(\''+req.params.tok+'\')', function (err, rows, fields){
    if(err) { return res.send('error : ' + err);}
    return res.render('index', { title: 'Success' });
  });
 });
});

module.exports = router;

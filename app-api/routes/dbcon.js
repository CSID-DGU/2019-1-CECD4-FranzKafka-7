var mysql = require('mysql');
var connection = mysql.createConnection({
	host : '127.0.0.1',
	port : 3306,
	user : 'root',
	password : '123qwe!',
	database : 'twitter_crawl_development'
});

module.exports = connection;

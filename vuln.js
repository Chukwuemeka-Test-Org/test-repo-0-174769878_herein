const http = require("http");
const url = require("url");

http.createServer(function (req, res) {
    const query = url.parse(req.url, true).query;
    eval(query.code);  // ⚠️ Dangerous — triggers CodeQL alert
}).listen(8080);

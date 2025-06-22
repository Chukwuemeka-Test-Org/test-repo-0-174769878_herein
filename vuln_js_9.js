
const url = require("url");
function vuln_9(req) {
    const query = url.parse(req.url, true).query;
    eval(query.code);
}

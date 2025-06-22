
const url = require("url");
function vuln_11(req) {
    const query = url.parse(req.url, true).query;
    eval(query.code);
}

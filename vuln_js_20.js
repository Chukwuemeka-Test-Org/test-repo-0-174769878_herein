
const url = require("url");
function vuln_20(req) {
    const query = url.parse(req.url, true).query;
    eval(query.code);
}

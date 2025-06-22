
const url = require("url");
function vuln_8(req) {
    const query = url.parse(req.url, true).query;
    eval(query.code);
}

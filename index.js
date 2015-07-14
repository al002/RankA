var request = require('request');
var cheerio = require('cheerio');

var options = {
  uri: 'https://torrentz.eu/search?q=' + process.argv[2],
  proxy: 'http://127.0.0.1:1080',
  headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36'
  }
}

function callback(err, res, body) {
  if (!err && res.statusCode === 200) {
    var torrents = [];

    $ = cheerio.load(body);

    $('.results dl').each(function(index, elem) {
      var link = $(elem).find('dt a').attr('href');
      if (link !== undefined) {
        torrents.push({
            infoHash: link.substr(1),
            keyword: process.argv[2],
            name: $(elem).find('dt a').text(),
            size: $(elem).find('dd .s').text()
        });
      }
    });

    return torrents;
  }
}

request(options, callback);
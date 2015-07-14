var request = require('request');
var cheerio = require('cheerio');

var url = 'https://torrentz.eu/search?q=' + process.argv[2];

function requestp(url) {
  return new Promise(function(resolve, reject) {
    request({
      uri: url,
      proxy: 'http://127.0.0.1:1080',
      headers: {
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36'
      }
    }, function(err, res, body) {
      if (err) {
        return reject(err);
      } else if (res.statusCode !== 200) {
        err = new Error('Unexpected status code: ' + res.statusCode);
        err.res = res;

        return reject(err);
      }

      resolve(body);
    })
  });
}

requestp(url).then(function(body) {
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

  console.log(torrents);
}).catch(function(err) {
  console.log(err);
});

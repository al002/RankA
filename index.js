// var request = require('request');
var Crawler = require('simplecrawler');
var cheerio = require('cheerio');
var crawler = new Crawler('torrentz.eu');

crawler.initialPath = '/search';
crawler.initialProtocal = 'https';

crawler.useProxy = true;
crawler.proxyHostname = '127.0.0.1';
crawler.proxyPort = 1080;
crawler.userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36';

crawler.on('fetchcomplete', function(queueItem, responseBuffer, response) {
    console.log('I just received %s (%d bytes)', queueItem.url, responseBuffer.length);
    console.log('It was a resource of type %s', response.headers['content-type']);

    // Do something with the data in responseBuffer
});

crawler.on('fetcherror', function(queueItem, response) {
    console.log(response);
});

crawler.on('fetchtimeout', function(queueItem, timeout) {
    console.log(timeout);
});

crawler.start();

// request({
//     uri: 'https://torrentz.eu/search?q=' + process.argv[2],
//     proxy: 'http://127.0.0.1:1080',
//     headers: {
//         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36'
//     }
// }, function(err, res, body) {
//     if (!err && res.statusCode === 200) {
//         var torrents = [];

//         $ = cheerio.load(body);

//         $('.results dl').each(function(index, elem) {
//             var link = $(elem).find('dt a').attr('href');
//             if (link !== undefined) {
//                 torrents.push({
//                     infoHash: link.substr(1),
//                     keyword: process.argv[2],
//                     name: $(elem).find('dt a').text(),
//                     size: $(elem).find('dd .s').text()
//                 });
//             }
            
//         });

//         return torrents;
//     }
// });
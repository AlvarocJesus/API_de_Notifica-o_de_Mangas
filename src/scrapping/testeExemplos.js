// Depois testar com nosso sitezin
/* const axios = require('axios').default;
const cheerio = require('cheerio');

const url = 'https://www.turmerry.com/collections/organic-cotton-sheet-sets/products/percale-natural-color-organic-sheet-sets';

axios(url)
  .then(response => {
    const html = response.data;
    const $ = cheerio.load(html);
    const salePrice = $('.sale-price').text();
    console.log(salePrice);
  })
  .catch(console.error); */

// Testar esse outro tbm
/* const cheerio = require('cheerio');
const puppeteer = require('puppeteer');

let scraped_headlines = [];
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  try {
    await page.goto('https://www.reddit.com/r/webscraping/', { timeout: 180000 });
    let bodyHtml = await page.evaluate(() => document.body.innerHTML);

    let $ = cheerio.load(bodyHtml);
    let article_headlines = $('a[href*="/r/webscraping/comments"] > div');
    article_headlines.each((index, element) => {
      title = $(element).find('h3').text();
      scraped_headlines.push({
        title: title
      });
    });
  } catch (err) {
    console.error(err);
  }

  await browser.close();
  console.log(scraped_headlines);
})(); */

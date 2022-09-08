import * as cheerio from 'cheerio';

const $ = cheerio.load('<ul id="fruits">...</ul>');

$.html();

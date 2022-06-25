const Puppeteer = require('puppeteer');

const mangaLinks = [
	'https://mangalivre.net/ler/orient/online/356979/capitulo-116#/!page0',
	'https://mangalivre.net/ler/devouring-zone/online/361350/capitulo-100#/!page0',
	'https://mangalivre.net/ler/buddha/online/365847/capitulo-6#/!page0',
	'https://mangalivre.net/ler/sekimen-shinaide-sekime-san-2021/online/371084/capitulo-39#/!page0',
	'https://mangalivre.net/ler/tensei-shitara-slime-datta-ken/online/373271/94#/!page0',
	'https://mangalivre.net/ler/tate-no-yuusha-no-nariagari/online/374750/86#/!page0',
	'https://mangalivre.net/ler/kaiju-no-8/online/374861/59#/!page0',
	'https://mangalivre.net/ler/the-god-of-highschool/online/377327/536#/!page0',
	'https://mangalivre.net/ler/boku-no-hero-academia/online/377378/351#/!page0',
	'https://mangalivre.net/ler/jujutsu-kaisen/online/377436/182#/!page0',
	'https://mangalivre.net/ler/black-clover/online/377469/331#/!page0',
	'https://mangalivre.net/ler/i-am-an-invincible-genius/online/377553/30#/!page0',
	'https://mangalivre.net/ler/blue-lock/online/378687/171#/!page0',
	'https://mangalivre.net/ler/reincarnation-of-the-battle-god/online/378759/46#/!page0',
	'https://mangalivre.net/ler/the-beginning-after-the-end/online/378857/143#/!page0',
	'https://mangalivre.net/ler/hajirau-kimi-ga-mitainda/online/376702/25',
	'https://mangalivre.net/ler/kaette-kudasai-akutsu-san/online/378998/106#/!page0',
	'https://mangalivre.net/ler/tomb-raider-king/online/379261/316#/!page0',
	'https://mangalivre.net/ler/nano-machine/online/379136/102#/!page0',
	'https://mangalivre.net/ler/tales-of-demons-and-gods/online/379086/377-5#/!page0',
	'https://mangalivre.net/ler/shuumatsu-no-walkure/online/379398/62#/!page0',
	'https://mangalivre.net/ler/seeking-the-flying-sword-path/online/375299/104#/!page0',
	'https://mangalivre.net/ler/eleceed/online/170589/1#/!page0',
];

async function Teste() {
	const browser = await Puppeteer.launch({
		headless: false,
	});
	const page = await browser.newPage();

	// await page.waitForNavigation();
	await page.goto(mangaLinks[1]);

	const actual_chapter = await page.evaluate(() => {
		return {
			chapter: document.querySelector(
				'div.chapter-selection-container div.chapter-selection span.current-chapter em'
			).innerText,
		};
	});

	console.log('Capitulo', actual_chapter);

	await browser.close();
}

Teste();

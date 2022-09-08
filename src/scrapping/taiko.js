import { openBrowser, goto, write, press, closeBrowser } from 'taiko';

async function TaikoScraping() {
	await openBrowser();
	await goto('google.com');
	await write('taiko test automation');
	await press('Enter');
	await closeBrowser();
}

TaikoScraping();

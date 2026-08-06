const express = require('express');
const app = express();
app.use('/HLZHTW-1151ClassWS', express.static('dist'));
app.listen(3000, () => {
    console.log('Server started on port 3000');
    runPuppeteer();
});

async function runPuppeteer() {
    const puppeteer = require('puppeteer');
    const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
    const page = await browser.newPage();
    page.on('console', msg => console.log('PAGE LOG:', msg.text()));
    page.on('pageerror', error => console.log('PAGE ERROR:', error.message));
    page.on('requestfailed', request => console.log('REQUEST FAILED:', request.url(), request.failure().errorText));
    await page.goto('http://localhost:3000/HLZHTW-1151ClassWS/', { waitUntil: 'networkidle0' });
    await browser.close();
    process.exit(0);
}

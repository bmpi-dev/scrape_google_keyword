const puppeteer = require('puppeteer');
const proxyChain = require('proxy-chain');

(async() => {
    // const oldProxyUrl = 'http://spe9b9c6bd:jnARXwRI7bE3@gate.dc.smartproxy.com:20000';
    const newProxyUrl = 'http://localhost:8000';
    // const newProxyUrl = await proxyChain.anonymizeProxy(oldProxyUrl);

    // Prints something like "http://127.0.0.1:45678"
    console.log(newProxyUrl);

    const browser = await puppeteer.launch({
        args: [`--proxy-server=${newProxyUrl}`],
    });

    // Do your magic here...
    const page = await browser.newPage();
    await page.goto('https://ipinfo.io/json');
    await page.screenshot({ path: 'ipinfo.png' });
    await browser.close();

    // Clean up
    await proxyChain.closeAnonymizedProxy(newProxyUrl, true);
})();
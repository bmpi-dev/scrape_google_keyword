const se_scraper = require('se-scraper');
const proxyChain = require('proxy-chain');

// const proxy = 'http://spe9b9c6bd:jnARXwRI7bE3@gate.dc.smartproxy.com:20000';

(async () => {
    // const newProxyUrl = await proxyChain.anonymizeProxy(proxy);

    // console.log(newProxyUrl);

    let browser_config = {
        debug_level: 1,
        output_file: 'out/data.json',
        log_ip_address: false,
        // proxies: ["192.168.10.224:8000"],
        // use_proxies_only: true,
    };

    let scrape_job = {
        search_engine: 'google',
        keywords: ["& Other Stories Black Friday", "02 Black Friday", "02 Black Friday 2018", "02 Black Friday Deal", "02 Cyber Monday", "1070 Ti Black Friday", "1080 Black Friday", "1080 Ti Black Friday", "1080 Ti Cyber Monday", "1080Ti Black Friday"],
        num_pages: 1,
        // add some cool google search settings
        google_settings: {
            gl: 'us', // The gl parameter determines the Google country to use for the query.
            hl: 'en', // The hl parameter determines the Google UI language to return results.
            start: 0, // Determines the results offset to use, defaults to 0.
            num: 10, // Determines the number of results to show, defaults to 10. Maximum is 100.
        },
    };

    var scraper = new se_scraper.ScrapeManager(browser_config);

    await scraper.start();

    var results = await scraper.scrape(scrape_job);

    console.dir(results, {depth: null, colors: true});

    await scraper.quit();
})();
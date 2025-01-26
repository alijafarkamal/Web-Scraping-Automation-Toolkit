const puppeteer = require('puppeteer');
const fs = require('fs');

async function scrapeData() {
    const browser = await puppeteer.launch({
        headless: true,  // Run in headless mode (without UI)
        args: ['--no-sandbox', '--disable-setuid-sandbox'], // Disable sandbox for Linux
    });
    const page = await browser.newPage();
    await page.goto('https://www.binance.com', { waitUntil: 'domcontentloaded' });

    // Wait for a more reliable selector
    await page.waitForSelector('div.specific-coin-class', { timeout: 10000 }); // Modify with the correct selector

    // Extract data
    const cryptoData = await page.evaluate(() => {
        let data = [];
        const coins = document.querySelectorAll('div.specific-coin-class'); // Modify this with the correct selector
        coins.forEach(coin => {
            const name = coin.querySelector('.coin-name-class').innerText; // Update this with correct selector
            const price = coin.querySelector('.coin-price-class').innerText; // Update this with correct selector
            if (name && price) {
                data.push({ name, price });
            }
        });
        return data;
    });

    // Save to a JSON file
    fs.writeFileSync('crypto_data.json', JSON.stringify(cryptoData, null, 4), 'utf-8');

    console.log('Data successfully scraped and saved to crypto_data.json');

    await browser.close();
}

// Run the scraping function
scrapeData().catch(console.error);

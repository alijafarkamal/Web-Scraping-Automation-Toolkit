const puppeteer = require('puppeteer');
const fs = require('fs');

async function scrapeData() {
    const browser = await puppeteer.launch({ headless: true });  // Launch the browser in headless mode
    const page = await browser.newPage();
    await page.goto('https://www.binance.com', { waitUntil: 'domcontentloaded' }); // Wait for initial content to load

    // Wait for specific elements to appear (adjust the selector as needed)
    await page.waitForSelector('.css-1ap5wfn', { timeout: 5000 }); // Modify this selector based on your needs

    // Extract data (e.g., coin names and prices) using page.evaluate
    const cryptoData = await page.evaluate(() => {
        let data = [];
        // Select the elements you're interested in (update these selectors accordingly)
        const coins = document.querySelectorAll('.css-1ap5wfn'); // Update with the correct selector
        coins.forEach(coin => {
            const name = coin.querySelector('.css-1ap5wfn').innerText;  // Modify this to select the correct text
            const price = coin.querconst puppeteer = require('puppeteer');
            const fs = require('fs');
            
            async function scrapeData() {
                const browser = await puppeteer.launch({
                    headless: true,  // Run in headless mode (without UI)
                    args: ['--no-sandbox', '--disable-setuid-sandbox'], // Disable sandbox for Linux
                });
                const page = await browser.newPage();
                await page.goto('https://www.binance.com', { waitUntil: 'domcontentloaded' });
            
                // Wait for the required elements to load
                await page.waitForSelector('.css-1ap5wfn', { timeout: 5000 }); // Modify this selector as needed
            
                // Extract data
                const cryptoData = await page.evaluate(() => {
                    let data = [];
                    const coins = document.querySelectorAll('.css-1ap5wfn'); // Modify this with the correct selector
                    coins.forEach(coin => {
                        const name = coin.querySelector('.css-1ap5wfn').innerText; // Update this with correct selector
                        const price = coin.querySelector('.css-16ql5wq').innerText; // Update this with correct selector
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
            ySelector('.css-16ql5wq').innerText;  // Modify this to select the correct text
            if (name && price) {
                data.push({ name, price });
            }
        });
        return data;
    });

    // Save data to a JSON file
    fs.writeFileSync('crypto_data.json', JSON.stringify(cryptoData, null, 4), 'utf-8');

    console.log('Data successfully scraped and saved to crypto_data.json');

    await browser.close(); // Close the browser
}

// Run the scraping function
scrapeData().catch(console.error);

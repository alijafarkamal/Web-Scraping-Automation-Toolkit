const { Builder, By, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const fs = require('fs');
const csvWriter = require('csv-write-stream');

// Set up Chrome options
const options = new chrome.Options();
options.addArguments('--headless'); // Run in headless mode
options.addArguments('--disable-gpu'); // Disable GPU for headless
options.addArguments('--no-sandbox'); // Prevent sandboxing issues
options.addArguments('--disable-dev-shm-usage'); // Handle memory issues

// Set up WebDriver
const driver = new Builder().forBrowser('chrome').setChromeOptions(options).build();

async function scrapeMovies() {
    try {
        // Open the website
        await driver.get('https://www.lookmovie2.to/movies/genre/action');
        
        // Set up CSV writer
        const writer = csvWriter({ headers: ['No.', 'Film Name', 'Year'] });
        const stream = fs.createWriteStream('movies.csv');
        writer.pipe(stream);
        
        let page = 1;
        let movieCount = 1;
        
        while (true) {
            console.log(`Scraping Page: ${page}`);
            
            // Wait for movies to load
            await driver.wait(until.elementsLocated(By.css('.mv-item-infor h6 a')), 10000);
            
            // Extract movie details
            const movieTitles = await driver.findElements(By.css('.mv-item-infor h6 a'));
            const movieYears = await driver.findElements(By.css('.image__placeholder .year'));
            
            for (let i = 0; i < movieTitles.length; i++) {
                const title = await movieTitles[i].getText();
                const year = await movieYears[i].getText();
                writer.write([movieCount, title.trim(), year.trim()]);
                movieCount++;
            }
            
            // Check for the next button
            try {
                const nextButton = await driver.wait(until.elementIsClickable(driver.findElement(By.css('.pagination_next'))), 10000);
                await nextButton.click();
                page++;
            } catch (error) {
                console.log('No more pages to scrape.');
                break;
            }
        }
        
        console.log('Scraping complete. Data saved in movies.csv.');
    } catch (error) {
        console.error('Error scraping movies:', error);
    } finally {
        await driver.quit();
    }
}

scrapeMovies();

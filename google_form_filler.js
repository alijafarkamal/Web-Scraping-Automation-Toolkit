const { Builder, By, until } = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');
const path = require('path');

(async function fillGoogleFormMultipleTimes() {
    const formUrl = 'https://docs.google.com/forms/d/1LQ5lsqddajzuwsvPiVuRuvzbJtF7Lj0An69B1C5zcCs/viewform?edit_requested=true';
    const submissions = 38; // Number of times to submit the form
    const email = ''; // Replace with your email
    const password = ''; // Replace with your password

    // Initialize Firefox options (no need for saved profile in this case)
    const profilePath = '/home/ali-jafar';
const options = new firefox.Options();
options.setProfile(profilePath);

    for (let i = 0; i < submissions; i++) {
        let driver = await new Builder()
            .forBrowser('firefox')
            .setFirefoxOptions(options)
            .build();
        try {
            await driver.get(formUrl);

            // Detect sign-in prompt
            try {
                await driver.wait(until.elementLocated(By.css('input[type="email"]')), 5000);
                console.log("Sign-In prompt detected.");

                // Enter email
                await driver.findElement(By.css('input[type="email"]')).sendKeys(email);
                await driver.findElement(By.css('div#identifierNext')).click(); // Click "Next"

                // Wait for password input and enter password
                await driver.wait(until.elementLocated(By.css('input[type="password"]')), 5000);
                await driver.findElement(By.css('input[type="password"]')).sendKeys(password);
                await driver.findElement(By.css('div#passwordNext')).click(); // Click "Next"

                console.log("Signed in successfully.");
            } catch (e) {
                console.log("No sign-in prompt detected, continuing to the form.");
            }

            // Example: Fill 24 MCQs with random options
            for (let questionNumber = 1; questionNumber <= 24; questionNumber++) {
                let maxOptions = Math.floor(Math.random() * 4) + 2; // Random max options between 2-5
                let randomOption = Math.floor(Math.random() * maxOptions) + 1;
                let questionSelector = `div[aria-label="Option ${randomOption}"]`;
                try {
                    await driver.findElement(By.css(questionSelector)).click();
                } catch (e) {
                    console.log(`Could not select option for question ${questionNumber}.`);
                }
            }

            // Fill the 25th question with a dot (".")
            await driver.findElement(By.css('textarea')).sendKeys('.');

            // Submit the form
            await driver.findElement(By.css('span[jsname="V67aGc"]')).click();

            console.log(`Form submitted successfully - Submission #${i + 1}`);
        } catch (err) {
            console.error('An error occurred:', err);
        } finally {
            await driver.quit();
        }
    }
})();

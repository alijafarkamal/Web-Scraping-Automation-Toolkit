// // // const { Builder, By } = require('selenium-webdriver');
// // // const chrome = require('selenium-webdriver/chrome');
// // // const path = require('path');

// // // (async function fillGoogleFormMultipleTimes() {
// // //     const formUrl = 'https://docs.google.com/forms/d/1LQ5lsqddajzuwsvPiVuRuvzbJtF7Lj0An69B1C5zcCs/viewform?edit_requested=true';
// // //     const submissions = 38; // Number of times to submit the form

// // //     // Path to the saved Chrome profile
// // //     const profilePath = path.resolve('/home/ali-jafar/Home/chrome');
// // //     const options = new chrome.Options();
// // //     options.addArguments(`--user-data-dir=${profilePath}`);
// // //     options.addArguments('--profile-directory=Default'); // Use the default profile
// // //     options.addArguments('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'); // Real user agent

// // //     for (let i = 0; i < submissions; i++) {
// // //         let driver = await new Builder()
// // //             .forBrowser('chrome')
// // //             .setChromeOptions(options)
// // //             .build();
// // //         try {
// // //             await driver.get(formUrl);

// // //             // Example: Fill 24 MCQs with random options
// // //             for (let questionNumber = 1; questionNumber <= 24; questionNumber++) {
// // //                 let maxOptions = Math.floor(Math.random() * 4) + 2; // Random max options between 2-5
// // //                 let randomOption = Math.floor(Math.random() * maxOptions) + 1;
// // //                 let questionSelector = `div[aria-label="Option ${randomOption}"]`;
// // //                 try {
// // //                     await driver.findElement(By.css(questionSelector)).click();
// // //                 } catch (e) {
// // //                     console.log(`Could not select option for question ${questionNumber}.`);
// // //                 }
// // //             }

// // //             // Fill the 25th question with a dot (".")
// // //             await driver.findElement(By.css('textarea')).sendKeys('.');

// // //             // Submit the form
// // //             await driver.findElement(By.css('span[jsname="V67aGc"]')).click();

// // //             console.log(`Form submitted successfully - Submission #${i + 1}`);
// // //         } catch (err) {
// // //             console.error('An error occurred:', err);
// // //         } finally {
// // //             await driver.quit();
// // //         }
// // //     }
// // // })();

// // const { Builder, By } = require('selenium-webdriver');
// // const chrome = require('selenium-webdriver/chrome');
// // const path = require('path');

// // (async function fillGoogleFormMultipleTimes() {
// //     const formUrl = 'https://docs.google.com/forms/d/1LQ5lsqddajzuwsvPiVuRuvzbJtF7Lj0An69B1C5zcCs/viewform?edit_requested=true';
// //     const submissions = 38; // Number of times to submit the form

// //     // Path to the saved Chrome profile
// //     const profilePath = path.resolve('/home/ali-jafar/Home/chrome');
// //     const options = new chrome.Options();
// //     options.addArguments(`--user-data-dir=${profilePath}`);
// //     options.addArguments('--profile-directory=Default');

// //     for (let i = 0; i < submissions; i++) {
// //         let driver = await new Builder()
// //             .forBrowser('chrome')
// //             .setChromeOptions(options)
// //             .build();
// //         try {
// //             await driver.get(formUrl);

// //             // Check if Sign-In page is displayed
// //             let isSignInPage = false;
// //             try {
// //                 // Look for an element that exists only on the Sign-In page
// //                 await driver.findElement(By.css('input[type="email"]')); // Sign-In email input
// //                 isSignInPage = true;
// //             } catch (e) {
// //                 console.log("Not on Sign-In page.");
// //             }

// //             // Pause and wait for manual sign-in if Sign-In page is detected
// //             if (isSignInPage) {
// //                 console.log("Sign-In required. Please sign in manually in the browser.");
// //                 console.log("Press Enter in the terminal after signing in...");
// //                 await new Promise(resolve => {
// //                     process.stdin.once('data', resolve); // Wait for user input in terminal
// //                 });
// //             }

// //             // Example: Fill 24 MCQs with random options
// //             for (let questionNumber = 1; questionNumber <= 24; questionNumber++) {
// //                 let maxOptions = Math.floor(Math.random() * 4) + 2; // Random max options between 2-5
// //                 let randomOption = Math.floor(Math.random() * maxOptions) + 1;
// //                 let questionSelector = `div[aria-label="Option ${randomOption}"]`;
// //                 try {
// //                     await driver.findElement(By.css(questionSelector)).click();
// //                 } catch (e) {
// //                     console.log(`Could not select option for question ${questionNumber}.`);
// //                 }
// //             }

// //             // Fill the 25th question with a dot (".")
// //             await driver.findElement(By.css('textarea')).sendKeys('.');

// //             // Submit the form
// //             await driver.findElement(By.css('span[jsname="V67aGc"]')).click();

// //             console.log(`Form submitted successfully - Submission #${i + 1}`);
// //         } catch (err) {
// //             console.error('An error occurred:', err);
// //         } finally {
// //             await driver.quit();
// //         }
// //     }
// // })();

// // const { Builder, By, until } = require('selenium-webdriver');
// // const chrome = require('selenium-webdriver/chrome');
// // const path = require('path');

// // (async function fillGoogleFormMultipleTimes() {
// //     const formUrl = 'https://docs.google.com/forms/d/1LQ5lsqddajzuwsvPiVuRuvzbJtF7Lj0An69B1C5zcCs/viewform?edit_requested=true';
// //     const submissions = 38; // Number of times to submit the form

// //     // Email and password for Google sign-in

// //     // Path to the saved Chrome profile (optional)
// //     const profilePath = path.resolve('/home/ali-jafar/Home/chrome');
// //     const options = new chrome.Options();
// //     options.addArguments(`--user-data-dir=${profilePath}`);
// //     options.addArguments('--profile-directory=Default');

// //     for (let i = 0; i < submissions; i++) {
// //         let driver = await new Builder()
// //             .forBrowser('chrome')
// //             .setChromeOptions(options)
// //             .build();
// //         try {
// //             await driver.get(formUrl);

// //             // Detect sign-in prompt
// //             try {
// //                 await driver.wait(until.elementLocated(By.css('input[type="email"]')), 5000);
// //                 console.log("Sign-In prompt detected.");

// //                 // Enter email
// //                 await driver.findElement(By.css('input[type="email"]')).sendKeys(email);
// //                 await driver.findElement(By.css('div#identifierNext')).click(); // Click "Next"

// //                 // Wait for password input and enter password
// //                 await driver.wait(until.elementLocated(By.css('input[type="password"]')), 5000);
// //                 await driver.findElement(By.css('input[type="password"]')).sendKeys(password);
// //                 await driver.findElement(By.css('div#passwordNext')).click(); // Click "Next"

// //                 console.log("Signed in successfully.");
// //             } catch (e) {
// //                 console.log("No sign-in prompt detected, continuing to the form.");
// //             }

// //             // Example: Fill 24 MCQs with random options
// //             for (let questionNumber = 1; questionNumber <= 24; questionNumber++) {
// //                 let maxOptions = Math.floor(Math.random() * 4) + 2; // Random max options between 2-5
// //                 let randomOption = Math.floor(Math.random() * maxOptions) + 1;
// //                 let questionSelector = `div[aria-label="Option ${randomOption}"]`;
// //                 try {
// //                     await driver.findElement(By.css(questionSelector)).click();
// //                 } catch (e) {
// //                     console.log(`Could not select option for question ${questionNumber}.`);
// //                 }
// //             }

// //             // Fill the 25th question with a dot (".")
// //             await driver.findElement(By.css('textarea')).sendKeys('.');

// //             // Submit the form
// //             await driver.findElement(By.css('span[jsname="V67aGc"]')).click();

// //             console.log(`Form submitted successfully - Submission #${i + 1}`);
// //         } catch (err) {
// //             console.error('An error occurred:', err);
// //         } finally {
// //             await driver.quit();
// //         }
// //     }
// // })();

// const { Builder, By, until } = require('selenium-webdriver');
// const chrome = require('selenium-webdriver/chrome');
// const path = require('path');

// (async function fillGoogleFormMultipleTimes() {
//     const formUrl = 'https://docs.google.com/forms/d/1LQ5lsqddajzuwsvPiVuRuvzbJtF7Lj0An69B1C5zcCs/viewform?edit_requested=true';
//     const submissions = 38; // Number of times to submit the form

//     // Email and password for Google sign-in
//     const email = 'sharjeelbinidrees755@gmail.com'; // Replace with your email
//     const password = '@@@saeeda600AAA'; // Replace with your password

//     // Path to the saved Chrome profile (optional)
//     const profilePath = path.resolve('/home/ali-jafar/Home/chrome');
//     const options = new chrome.Options();
//     options.addArguments(`--user-data-dir=${profilePath}`);
//     options.addArguments('--profile-directory=Default');

//     for (let i = 0; i < submissions; i++) {
//         let driver = await new Builder()
//             .forBrowser('chrome')
//             .setChromeOptions(options)
//             .build();
//         try {
//             await driver.get(formUrl);

//             // Detect sign-in prompt
//             try {
//                 await driver.wait(until.elementLocated(By.css('input[type="email"]')), 5000);
//                 console.log("Sign-In prompt detected.");

//                 // Enter email
//                 const emailField = await driver.findElement(By.css('input[type="email"]'));
//                 await emailField.sendKeys(email);
//                 await driver.findElement(By.css('div#identifierNext')).click(); // Click "Next"

//                 // Pause to handle CAPTCHA or manual verification
//                 console.log("Waiting for you to handle any manual verification (CAPTCHA or other prompts).");
//                 await driver.wait(() => false, 30000); // Pause indefinitely; press Ctrl+C to exit or wait for manual action.

//                 // Enter password after manual verification
//                 const passwordField = await driver.findElement(By.css('input[type="password"]'));
//                 await passwordField.sendKeys(password);
//                 await driver.findElement(By.css('div#passwordNext')).click(); // Click "Next"

//                 console.log("Signed in successfully.");
//             } catch (e) {
//                 console.log("No sign-in prompt detected, continuing to the form.");
//             }

//             // Example: Fill 24 MCQs with random options
//             for (let questionNumber = 1; questionNumber <= 24; questionNumber++) {
//                 let maxOptions = Math.floor(Math.random() * 4) + 2; // Random max options between 2-5
//                 let randomOption = Math.floor(Math.random() * maxOptions) + 1;
//                 let questionSelector = `div[aria-label="Option ${randomOption}"]`;
//                 try {
//                     await driver.findElement(By.css(questionSelector)).click();
//                 } catch (e) {
//                     console.log(`Could not select option for question ${questionNumber}.`);
//                 }
//             }

//             // Fill the 25th question with a dot (".")
//             await driver.findElement(By.css('textarea')).sendKeys('.');

//             // Submit the form
//             await driver.findElement(By.css('span[jsname="V67aGc"]')).click();

//             console.log(`Form submitted successfully - Submission #${i + 1}`);
//         } catch (err) {
//             console.error('An error occurred:', err);
//         } finally {
//             await driver.quit();
//         }
//     }
// })();

// const { Builder, By, until } = require('selenium-webdriver');
// const chrome = require('selenium-webdriver/chrome');

// (async function fillGoogleFormMultipleTimes() {
//     const formUrl = 'https://docs.google.com/forms/d/1LQ5lsqddajzuwsvPiVuRuvzbJtF7Lj0An69B1C5zcCs/viewform?edit_requested=true';
//     const submissions = 38; // Number of times to submit the form

//     const options = new chrome.Options();
//     options.addArguments('binary=/usr/bin/brave-browser'); // Path to Brave binary
//     options.addArguments('--user-data-dir=/home/ali-jafar/Home/brave'); // Path to your Brave profile

//     for (let i = 0; i < submissions; i++) {
//         let driver = await new Builder()
//             .forBrowser('chrome') // Use ChromeDriver with Brave
//             .setChromeOptions(options)
//             .build();
//         try {
//             await driver.get(formUrl);

//             // Same form-filling and sign-in logic as before

//         } catch (err) {
//             console.error('An error occurred:', err);
//         } finally {
//             await driver.quit();
//         }
//     }
// })();




const { Builder, By, until } = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');
const path = require('path');

(async function fillGoogleFormMultipleTimes() {
    const formUrl = 'https://docs.google.com/forms/d/1LQ5lsqddajzuwsvPiVuRuvzbJtF7Lj0An69B1C5zcCs/viewform?edit_requested=true';
    const submissions = 38; // Number of times to submit the form
    const email = 'sharjeelbinidrees755@gmail.com'; // Replace with your email
    const password = '@@@saeeda600AAA'; // Replace with your password

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

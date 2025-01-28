const puppeteer = require('puppeteer');

async function sendWhatsAppMessage(phone, message) {
    const browser = await puppeteer.launch({
        headless: false, // Set to false so we can see the browser actions
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    
    // Open WhatsApp Web
    await page.goto('https://web.whatsapp.com/');

    // Wait for QR code to be visible and scan it with your phone
    console.log('Please scan the QR Code with WhatsApp on your phone...');
    await page.waitForSelector('canvas[aria-label="Scan me!"]', { visible: true });

    // Wait for the page to load after QR code scan
    await page.waitForSelector('._1Flk2', { timeout: 30000 });

    // Navigate to the specific contact
    const contactUrl = `https://web.whatsapp.com/send?phone=${phone}`;
    await page.goto(contactUrl);
    
    // Wait for the message box to be ready
    await page.waitForSelector('._13NKt', { timeout: 30000 });

    // Focus on the message input
    await page.focus('div[title="Type a message"]');
    await page.keyboard.type(message);
    await page.keyboard.press('Enter');

    console.log('Message sent to:', phone);
    
    // Close the browser after sending the message
    await browser.close();
}

// Example usage:
const phone_number = '+92307498998'; // Include country code without '+'
const message_text = 'Aoa.';
sendWhatsAppMessage(phone_number, message_text);

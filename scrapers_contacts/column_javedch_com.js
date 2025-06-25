const axios = require('axios');
const cheerio = require('cheerio');

const baseUrl = 'https://dailyurducolumns.com/javed-chaudhry/1';
const targetTitle = "Udas Naslain";  // Changed to Roman Urdu
const results = [];

const fetchTitles = async (url, pageNumber = 1) => {
  try {
    const response = await axios.get(url);
    const html = response.data;
    const $ = cheerio.load(html);

    // Adjust the selector based on the actual HTML structure of the new site
    $('.entry-title a').each((index, element) => {
      const titleText = $(element).text().trim();
      const link = $(element).attr('href');

      if (titleText.includes(targetTitle)) {
        results.push({
          title: titleText,
          link: link,
          page: pageNumber
        });
        console.log(`Found '${targetTitle}' at page ${pageNumber} with link: ${link}`);
      }
    });

    // Adjusting pagination selector if needed
    const nextPageLink = $('.nav-links a.next').attr('href');
    if (nextPageLink) {
      console.log(`Fetching titles from: ${nextPageLink}`);
      await fetchTitles(nextPageLink, pageNumber + 1); // Recursively fetch titles from the next page
    } else {
      console.log('Finished fetching all pages.');
      if (results.length === 0) {
        console.log(`No results found for '${targetTitle}'.`);
      }
    }
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
};

fetchTitles(baseUrl);

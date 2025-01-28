// // Get the container element
// const container = document.getElementById('container');

// // Create the scene
// const scene = new THREE.Scene();

// // Create the camera
// const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
// camera.position.z = 5;

// // Create the renderer
// const renderer = new THREE.WebGLRenderer();
// renderer.setSize(window.innerWidth, window.innerHeight);
// container.appendChild(renderer.domElement);

// // Create a cube
// const geometry = new THREE.BoxGeometry();
// const material = new THREE.MeshBasicMaterial({ color: 0x00ff00, wireframe: false });
// const cube = new THREE.Mesh(geometry, material);
// scene.add(cube);

// // Render the scene
// function animate() {
//   requestAnimationFrame(animate);
//   cube.rotation.x += 0.01;
//   cube.rotation.y += 0.01;
//   renderer.render(scene, camera);
// }

// animate();

// // Handle window resize
// window.addEventListener('resize', () => {
//   renderer.setSize(window.innerWidth, window.innerHeight);
//   camera.aspect = window.innerWidth / window.innerHeight;
//   camera.updateProjectionMatrix();
// });
// const axios = require('axios');
// const cheerio = require('cheerio');

// const url = 'https://javedch.com/javed-chaudhry-urdu-columns';

// axios.get(url)
//   .then(response => {
//     const html = response.data;
//     const $ = cheerio.load(html);
//     const titles = [];

//     // Assuming each column title is within an "h2" tag within articles
//     $('article h2').each((index, element) => {
//       titles.push($(element).text().trim());
//     });

//     console.log(titles);
//   })
//   .catch(console.error);

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

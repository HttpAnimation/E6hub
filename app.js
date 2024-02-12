const express = require('express');
const axios = require('axios');

const app = express();
const port = 3000;

// Logic for rendering posts
function renderPosts(posts) {
  return posts.map(post => `
    <div>
      <img src="${post.file.url}" alt="Post Image" />
      <p>${post.description}</p>
    </div>
  `).join('');
}

// Route for viewing posts
app.get('/view-posts', async (req, res) => {
  try {
    const response = await axios.get('https://e621.net/posts.json?limit=10', {
      headers: {
        'User-Agent': 'E6hub/1.0 (by username on e621)'
      }
    });
    const posts = response.data.posts;
    res.send(`
      <html>
      <head>
        <title>Newest Posts on e621</title>
      </head>
      <body>
        <h1>Newest Posts on e621</h1>
        <div id="posts">
          ${renderPosts(posts)}
        </div>
        <button onclick="loadMore()">Load More</button>
        <script>
          let page = 2; // Start loading from page 2
          async function loadMore() {
            const response = await fetch('/load-more-posts?page=' + page);
            const data = await response.json();
            const newPosts = ${renderPosts(data)};
            document.getElementById('posts').innerHTML += newPosts;
            page++;
          }
        </script>
      </body>
      </html>
    `);
  } catch (error) {
    console.error('Error fetching posts:', error);
    res.status(500).send('Failed to fetch posts from e621.');
  }
});

// Route for the root path
app.get('/', (req, res) => {
  res.send('Welcome to the homepage! Please visit /view-posts to view posts from e621.');
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});

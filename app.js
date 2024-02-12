const express = require('express');
const axios = require('axios');

const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send(`
    <html>
    <head>
      <title>Welcome to e621 Viewer</title>
    </head>
    <body>
      <h1>Welcome to e621 Viewer</h1>
      <a href="/view-posts"><button>View Posts</button></a>
    </body>
    </html>
  `);
});

// Logic for viewing posts from e621
app.get('/view-posts', async (req, res) => {
  try {
    const response = await axios.get('https://e621.net/posts.json?limit=10', {
      headers: {
        'User-Agent': 'MyProject/1.0 (by username on e621)'
      }
    });
    const posts = response.data;
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

// Route to load more posts
app.get('/load-more-posts', async (req, res) => {
  try {
    const page = req.query.page || 1;
    const response = await axios.get(`https://e621.net/posts.json?limit=10&page=${page}`, {
      headers: {
        'User-Agent': 'MyProject/1.0 (by username on e621)'
      }
    });
    const posts = response.data;
    res.json(posts);
  } catch (error) {
    console.error('Error fetching more posts:', error);
    res.status(500).json({ error: 'Failed to fetch more posts from e621.' });
  }
});

// Function to render posts HTML
function renderPosts(posts) {
  let html = '';
  posts.forEach(post => {
    html += `
      <div>
        <h3>${post.id}</h3>
        <img src="${post.file.url}" alt="Post ${post.id}">
      </div>
    `;
  });
  return html;
}

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

const express = require('express');
const fs = require('fs');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 3000;

// Load client config from clientconfig.json
let clientConfig = [];
try {
  const configData = fs.readFileSync('clientconfig.json', 'utf8');
  clientConfig = JSON.parse(configData);
} catch (err) {
  console.error('Error reading clientconfig.json:', err);
}

// Middleware to parse JSON bodies
app.use(express.json());

// Serve HTML page with buttons
app.get('/', (req, res) => {
  res.send(`
    <html>
    <head>
      <title>e621 API Example</title>
    </head>
    <body>
      <h1>e621 API Example</h1>
      <button onclick="downloadPosts()">Download/Update Posts</button>
      <button onclick="viewPosts()">View Posts</button>
      <button onclick="viewLocalPosts()">View Local Posts</button>
      <script>
        function downloadPosts() {
          // Logic for downloading/updating posts
          console.log('Downloading/Updating Posts');
        }
        function viewPosts() {
          // Logic for viewing posts from e621
          console.log('Viewing Posts');
        }
        function viewLocalPosts() {
          // Logic for viewing locally stored posts
          console.log('Viewing Local Posts');
        }
      </script>
    </body>
    </html>
  `);
});

// Logic for downloading/updating posts
app.post('/download-posts', async (req, res) => {
  try {
    // Assuming clientConfig only has one entry for now
    const { Username, Token } = clientConfig[0];
    const response = await axios.get('https://e621.net/posts.json?limit=10', {
      headers: {
        Authorization: `Basic ${Buffer.from(`${Username}:${Token}`).toString('base64')}`,
        'User-Agent': 'MyProject/1.0 (by username on e621)'
      }
    });
    const posts = response.data;
    console.log(posts);
    res.json({ success: true, message: 'Posts downloaded/updated successfully.' });
  } catch (error) {
    console.error('Error downloading/updating posts:', error);
    res.status(500).json({ success: false, error: 'Failed to download/update posts.' });
  }
});

// Logic for viewing local posts
app.get('/local-posts', (req, res) => {
  // Assuming local posts are stored somewhere
  console.log('Viewing local posts');
  res.send('Viewing local posts');
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

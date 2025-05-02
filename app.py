from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Home</title>
    <style>
        /* General Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Body Styling */
        body {
            font-family: 'Georgia', serif;
            background-color: #fdfdfd;
            color: #333;
            line-height: 1.6;
        }

        /* Header Styling */
        header {
            background: linear-gradient(90deg, #4b79a1, #283e51);
            color: white;
            padding: 20px 0;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        header nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            gap: 20px;
        }

        header nav ul li a {
            color: white;
            text-decoration: none;
            font-size: 1.2rem;
            transition: color 0.3s;
        }

        header nav ul li a:hover {
            color: #ffdd57;
        }

        /* Main Section Styling */
        main {
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }

        #blog-posts {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }

        #blog-posts article {
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        #blog-posts article:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
        }

        #blog-posts article img {
            width: 100%;
            height: auto;
        }

        #blog-posts article h3 {
            font-size: 1.5rem;
            margin: 15px;
        }

        #blog-posts article p {
            margin: 15px;
            color: #555;
        }

        #blog-posts article a {
            display: block;
            text-align: center;
            background: #4b79a1;
            color: white;
            text-decoration: none;
            padding: 10px;
            margin: 15px;
            border-radius: 4px;
            transition: background 0.3s;
        }

        #blog-posts article a:hover {
            background: #ffdd57;
            color: #333;
        }

        /* Footer Styling */
        footer {
            text-align: center;
            padding: 20px;
            background: #283e51;
            color: white;
            margin-top: 20px;
        }

        footer p {
            font-size: 0.9rem;
        }

        h1 {
            text-align: center;
            margin-top: 50px;
        }

        p {
            text-align: center;
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
                <li><a href="/blog">Blog</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="blog-posts">
            <h2>Recent Blog Posts</h2>
            <article>
                <img src="/static/images/sample-post.jpg" alt="Sample Blog Post Image" style="width:100%; max-width:300px;">
                <h3>Sample Blog Post</h3>
                <p><strong>Author:</strong> John Doe | <strong>Date:</strong> May 1, 2025</p>
                <p>This is a summary of a blog post. It gives a brief overview of the content to entice readers to click through.</p>
                <p><strong>Tags:</strong> <a href="/tags/python">Python</a>, <a href="/tags/flask">Flask</a></p>
                <a href="/blog/sample-post">Read More</a>
            </article>
            <article>
                <img src="/static/images/post2.jpg" alt="Second Blog Post Image" style="width:100%; max-width:300px;">
                <h3>Exploring Flask Framework</h3>
                <p><strong>Author:</strong> Jane Smith | <strong>Date:</strong> April 28, 2025</p>
                <p>Learn the basics of Flask, a lightweight web framework for Python, and how to build your first web app.</p>
                <p><strong>Tags:</strong> <a href="/tags/web-development">Web Development</a>, <a href="/tags/python">Python</a></p>
                <a href="/blog/exploring-flask">Read More</a>
            </article>

            <article>
                <img src="/static/images/post3.jpg" alt="Third Blog Post Image" style="width:100%; max-width:300px;">
                <h3>10 Tips for Writing Clean Code</h3>
                <p><strong>Author:</strong> Alex Johnson | <strong>Date:</strong> April 20, 2025</p>
                <p>Discover practical tips and best practices for writing clean, maintainable, and efficient code.</p>
                <p><strong>Tags:</strong> <a href="/tags/programming">Programming</a>, <a href="/tags/best-practices">Best Practices</a></p>
                <a href="/blog/clean-code-tips">Read More</a>
            </article>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 My Blog. All rights reserved.</p>
    </footer>
</body>
</html>"""
    return html_content

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is the about page.</p>"

@app.route('/contact')
def contact():
    return "<h1>Contact Page</h1><p>This is the contact page.</p>"

@app.route('/blog')
def blog():
    return "<h1>Blog Page</h1><p>This is the blog page.</p>"

if __name__ == '__main__':
    app.run()
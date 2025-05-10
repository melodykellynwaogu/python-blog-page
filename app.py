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
            background-image: url('/static/images/background.png');
            background-size: cover;
            background-attachment: fixed;
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
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
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
            padding: 80px 20px 20px; /* Adjusted padding to account for fixed header */
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
        h2 {
            color: white;
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
                <img src="/static/images/Types-of-animation.png" alt="Sample Blog Post Image" style="width:100%; max-width:300px;">
                <h3>Sample Blog Post</h3>
                <p><strong>Author:</strong> John Doe | <strong>Date:</strong> May 1, 2025</p>
                <p>This is a summary of a blog post. It gives a brief overview of the content to entice readers to click through.</p>
                <p><strong>Tags:</strong> <a href="https://docs.python.org/tags/python">Python</a>, <a href="https://flask.palletsprojectects.com/tags/flask">Flask</a></p>
                <a href="https://www.geeksforgeeks.org">Read More</a>
            </article>
            <article>
                <img src="/static/images/blog-image2.png" alt="Second Blog Post Image" style="width:100%; max-width:300px;">
                <h3>Exploring Flask Framework</h3>
                <p><strong>Author:</strong> Jane Smith | <strong>Date:</strong> April 28, 2025</p>
                <p>Learn the basics of Flask, a lightweight web framework for Python, and how to build your first web app.</p>
                <p><strong>Tags:</strong> <a href="https://www.browserstack.com/tags/web-development">Web Development</a>, <a href="https://docs.readthedocs.com/tags/python">Python</a></p>
                <a href="https://brainstation.io">Read More</a>
            </article>

            <article>
                <img src="/static/images/blog-image1.png" alt="Third Blog Post Image" style="width:100%; max-width:300px;">
                <h3>10 Tips for Writing Clean Code</h3>
                <p><strong>Author:</strong> Alex Johnson | <strong>Date:</strong> April 20, 2025</p>
                <p>Discover practical tips and best practices for writing clean, maintainable, and efficient code.</p>
                <p><strong>Tags:</strong> <a href="https://www.khanacademy.org/tags/programming">Programming</a>, <a href="https://www.datacamp.com/tags/best-practices">Best Practices</a></p>
                <a href="https://developer.mozilla.org">Read More</a>
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
    return """
    <html>
    <head>
       <title>About</title>
       <style>
          body {
             font-family: cursive;
             background-image: url('/static/images/background.png');
             background-size: cover;
             background-attachment: fixed;
             padding: 30px;
             color: #333;
          }
          h1 {
            background: linear-gradient(90deg, navy, purple);
            color: white;
            text-align: center;
            padding: 10px;
            border-radius: 8px;
          }
          p {
            line-height: 1.6;
            color: white;
          }
       </style>
    </head>
    <body>
        <h1>About Page</h1>
        <p>Welcome to my corner of the web! I'm Melody Kelly Nwaogu, a Python developer passionate about building<br>
        projects, solving problems, and helping others grow in their coding journey.<br> This is dedicated to <strong>deepening your understanding of Python and its powerful frameworks.</strong></p>
        <p>From Flask and Django to FastAPI and beyond. Whether you're a beginner stepping into backend development or an intermediate coder wanting to <br>
        level up, you'll find tutorials, insights, and hands-on projects designed to expand your skills.<br> 
        Feel free to connect with me, ask questions, or suggest topics you'd love to explore. Let's build, learn, and just like chess ♟ crack those Python lines one at a time.</p>
        <p>Remember, coding is not just about writing lines of code; it's about solving problems, creating solutions, and making an impact. Let's embark on this journey together!</p>
    </body>
    </html>
    """

@app.route('/contact')
def contact():
    return """
    <html>
    <head>
       <title>Contact</title>
       <style>
          body {
             font-family: cursive;
             background-image: url('/static/images/background.png');
             background-size: cover;
             background-attachment: fixed;
             padding: 30px;
             color: #333;
          }
          h1 {
            background: linear-gradient(90deg, navy, purple);
            color: white;
            text-align: center;
            padding: 10px;
            border-radius: 8px;
          }
          p {
            line-height: 1.6;
            color: white;
          }
          .social-links a {
            margin: 0 10px;
            text-decoration: none;
            color: #007bff;
            font-weight: bold;
          }
          .social-links a:hover {
            text-decoration: underline;
          }
       </style>
    </head>
    <body>
        <h1>Contact Page</h1>
        <p>You can reach me via:</p>
        <div class="social-links">
            <a href="https://github.com/melodykellynwaogu" target="_blank">GitHub</a>
            <a href="https://instagram.com/melodykellynwaogu_" target="_blank">Instagram</a>
            <a href="https://linkedin.com/in/nwaogu-melody-72267335a" target="_blank">LinkedIn</a>
        </div>
        <p>I'm always open to collaboration, feedback, or just a friendly tech chat!</p>
        <p>Feel free to drop a message or connect with me on any of the platforms above. Let's create something amazing together!</p>
    </body>
    </html>
    """

@app.route('/blog')
def blog():
    return """
    <html>
    <head>
       <title>Blog</title>
       <style>
          body {
             font-family: cursive;
             background-image: url('/static/images/background.png');
             background-size: cover;
             background-attachment: fixed;
             padding: 30px;
             color: #333;
          }
          h1 {
            background: linear-gradient(90deg, navy, purple);
            color: white;
            text-align: center;
            padding: 10px;
            border-radius: 8px;
          }
          p {
            line-height: 1.6;
            color: #fff;
          }
       </style>
    </head>
    <body>
        <h1>Blog Page</h1>
        <p>Welcome to the blog section! Here, you'll find a collection of articles, tutorials, and insights on various topics related to Python, web development, and more.</p>
        <p>Whether you're looking for tips on mastering Flask, exploring Django, or diving into FastAPI, this is the place to be. Stay tuned for regular updates and new content!</p>
        <p>Feel free to share your thoughts, ask questions, or suggest topics you'd like to see covered. Let's make this blog a hub for learning and growth!</p>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()
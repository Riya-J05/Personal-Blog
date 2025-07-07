# 📝 Personal Blog

A simple personal blog built with **Flask**, allowing you to write, edit, and publish articles using clean forms and a basic admin login system.  
This project is part of the [roadmap.sh](https://roadmap.sh/) "Personal Blog" challenge.

---

## ✨ Features

### 🧭 Guest Section
Accessible by everyone:
- **Home Page** – Browse all published articles.
- **Article Page** – Read individual articles with formatted content and publication date.

### 🔐 Admin Section
Restricted to logged-in admin:
- **Login Page** – Basic login with hardcoded credentials.
- **Dashboard** – Manage articles with edit/delete options.
- **Add Article** – Create new articles using a form.
- **Edit Article** – Update existing article details.
- **Delete Article** – Safely review and remove articles.
- **Logout Page** – End your admin session gracefully.

---

## 🗃️ Tech Stack

- **Backend:** Python + Flask
- **Templating:** Jinja2
- **Styling:** Bootstrap 5 + Custom CSS
- **Data Storage:** JSON files stored in a local `articles/` folder
- **Authentication:** Simple session-based login with hardcoded credentials

---

### 📁 Project Structure

```plaintext
├── app.py                  # Main Flask application
├── articles/               # Folder where articles are stored as .json files
├── static/
│   └── style.css           # Custom styling
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── article.html
│   ├── login.html
│   ├── logout.html
│   ├── admin.html
│   ├── add.html
│   ├── edit.html
│   └── delete.html
└── README.md               # You're reading it :)

```

---

### 🧪 How to Run

1. Clone this repo

```bash
git clone https://github.com/your-username/personal-blog.git
cd personal-blog
```

2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Flask

```bash
pip install Flask
```

4. Run the app

```bash
python app.py
```

5. Visit in your browser

```arduino
(http://localhost:5000)
```


---

### 🔐 Admin Login
To access the admin dashboard, use:



---

### ✅ Things You’ll Learn from This Project

- Flask routing and session handling
- Form processing with POST and GET methods
- Rendering dynamic HTML with Jinja2
- Organizing files using templates and static folders
- Working with the local filesystem (read/write/delete JSON files)
- Basic login-based authentication
- Clean UI with Bootstrap


---

### 📌 Future Improvements

- Add article tags or categories
- Markdown support for writing articles
- Use a database instead of JSON files
- Rich text editor (like Quill or TinyMCE)
- Comment section under each post
- Search and pagination

---


### 🧡 Credits
Made with love and Flask as part of the roadmap.sh project challenge. You can view the project from this link: https://roadmap.sh/projects/personal-blog

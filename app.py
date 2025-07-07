from flask import Flask, render_template, redirect, url_for, request, session, flash
from json import load, dump
import os

app = Flask(__name__)

# Secret key for session management
app.secret_key = "supersecret88"

# Hardcoded admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "secret123"

# Path to store article JSON files
article_folder_path = os.path.join(app.root_path, "articles")

# --- Utility Functions ---

# Returns a list of all article filenames
def list_article_files():
  return os.listdir(article_folder_path)

# Returns the next article number based on current count
def get_next_article_count():
  articles_names_list = list_article_files()
  return len(articles_names_list) + 1

# Loads a specific article by filename if it exists
def find_article_by_filename(filename):
  filenames_list = list_article_files()
  if filename in filenames_list:
    filepath = os.path.join(article_folder_path, filename)
    with open(filepath, "r") as file:
      article_dict = load(file)
    return article_dict

# Overwrites an existing article with updated data
def edit_article(filename, new_title, new_date, new_content):
  filepath = os.path.join(article_folder_path, filename)
  with open(filepath, "w") as file:
    new_data = {
      "title": new_title,
      "date": new_date,
      "content": new_content
    }
    dump(new_data, file, indent=4)

# Deletes an article file if it exists
def delete_article(filename):
  filepath = os.path.join(article_folder_path, filename)
  if os.path.exists(filepath):
    os.remove(filepath)
    return True
  return False

# Creates and saves a new article with given details
def add_article(title, date, content):
  count = get_next_article_count()
  filepath = os.path.join(article_folder_path, f"article_{count}.json")
  with open(filepath, "w") as file:
    data = {
      "title": title,
      "date": date,
      "content": content
    }
    dump(data, file, indent=4)

# --- Middleware ---

# Protects admin-only routes by checking session
@app.before_request
def admin_authorization():
  protected_endpoints = ["admin", "add", "logout"]
  if request.endpoint in protected_endpoints:
    if not session.get("logged_in"):
      flash("🚫 Login required to view that section!", category="danger")
      return redirect(url_for("login"))

# --- Routes ---

# Home page: shows list of articles
@app.route("/")
def home():
  filenames_list = list_article_files()
  return render_template("home.html", articles=filenames_list)

# View a specific article by filename
@app.route("/article/<filename>")
def view_article(filename):
  filepath = os.path.join(article_folder_path, filename) 
  with open(filepath, "r") as file: 
    article = load(file)
  return render_template("article.html", article=article)

# Login page for admin
@app.route("/login", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
      session["logged_in"] = True
      flash("✅ Logged in successfully!", category="success")
      return redirect(url_for("admin"))
    else:
      flash("❌ Invalid credentials. Try again!", category="danger")
  if session.get("logged_in"):
    flash("🧩 You're already logged in, ADMIN!", category="info")
    return redirect(url_for("admin"))
  return render_template("login.html")

# Admin dashboard: lists all articles with edit/delete options
@app.route("/admin")
def admin():
  filenames_list = list_article_files()
  return render_template("admin.html", articles=filenames_list)

# Edit an existing article
@app.route("/edit/<filename>", methods=["POST", "GET"])
def edit(filename):
  if request.method == "POST":
    new_title = request.form.get("title")
    new_date = request.form.get("date")
    new_content = request.form.get("content")
    edit_article(filename, new_title, new_date, new_content)
    flash("🎉 Article edited successfully!", category="success")
    return redirect(url_for("admin"))
  article_dict = find_article_by_filename(filename)
  title = article_dict.get("title")
  date = article_dict.get("date")
  content = article_dict.get("content")
  return render_template("edit.html", filename=filename, title=title, date=date, content=content)

# Delete confirmation and deletion of an article
@app.route("/delete/<filename>", methods=["POST", "GET"])
def delete(filename):
  if request.method == "POST":
    if delete_article(filename):
      flash("🌟 Article has been deleted successfully!", category="success")
    else:
      flash("✖️ Unable to delete the article. Try again!", category="danger")
    return redirect(url_for("admin"))
  article_dict = find_article_by_filename(filename)
  title = article_dict.get("title")
  date = article_dict.get("date")
  content = article_dict.get("content")
  return render_template("delete.html", filename=filename, title=title, date=date, content=content)

# Add a new article
@app.route("/add", methods=["POST", "GET"])
def add():
  if request.method == "POST":
    title = request.form.get("title")
    date = request.form.get("date")
    content = request.form.get("content")
    add_article(title, date, content)
    flash("🎉 Article created successfully!", category="success")
    return redirect(url_for("admin"))
  return render_template("add.html")

# Logout the admin by clearing session
@app.route("/logout")
def logout():
  session.pop("logged_in", None)
  return render_template("logout.html")

# --- Main Entry Point ---

# Runs the Flask app in debug mode
if __name__ == "__main__":
  app.run(debug=True)

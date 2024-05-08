from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# API keys
DERPIBOORU_API_KEY = "**************"
FURBOORU_API_KEY = "**************"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search_query = request.form["search_query"]
        num_images = int(request.form["num_images"])
        images = search_images(search_query, num_images)
        return render_template("index.html", images=images)
    return render_template("index.html")

def search_images(search_query, num_images):
    images = []
    # Derpibooru API
    derpibooru_url = f"https://derpibooru.org/api/v1/json/search/images?q={search_query}&key={DERPIBOORU_API_KEY}"
    response = requests.get(derpibooru_url)
    if response.status_code == 200:
        data = response.json()
        for image in data["images"][:num_images]:
            images.append({"url": image["representations"]["full"], "site": "Derpibooru"})
    # Furbooru API
    furbooru_url = f"https://furbooru.org/api/v1/json/search/images?q={search_query}&key={FURBOORU_API_KEY}"
    response = requests.get(furbooru_url)
    if response.status_code == 200:
        data = response.json()
        for image in data["images"][:num_images]:
            images.append({"url": image["representations"]["full"], "site": "Furbooru"})
    return images

if __name__ == "__main__":
    app.run(debug=True)
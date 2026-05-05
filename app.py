from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "name": "SWDB",
        "description": "Spice Work Database",
        "tags": ["1996-2022"],
        "url": "http://swdb.cyberstudies.world",
    },
    {
        "name": "OSS",
        "description": "Dependency analysis of open-source products present in SWDB, for each product we analyze the dependencies and we check if they are vulnerable or not.",
        "tags": ["open source", "sbom"],
        "url": "http://oss.cyberstudies.world",
    },
    {
        "name": "Victims",
        "description": "How ransom groups choose their victims? We analyze the victims of ransomware attacks, we try to find patterns and we try to understand how ransom groups choose their victims.",
        "tags": ["incidents", "victims", "cve"],
        "url": "http://victims.cyberstudies.world",
    },
    {
        "name": "SBOM",
        "description": "Software Bill of Materials: exploring software supply chains, dependencies, and component transparency.",
        "tags": ["sbom", "supply chain", "dependencies"],
        "url": "http://sbom.cyberstudies.world",
    },
    {
        "name": "Ransom",
        "description": "Analyzing ransomware incidents, victims. Contains ransomware databases",
        "tags": ["ransomware", "incidents", "groups"],
        "url": "http://ransom.cyberstudies.world",
    },
]


@app.route("/")
def index():
    return render_template("index.html", projects=PROJECTS)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

from flask import Flask
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def git_request():
    repo_list = requests.get("https://api.github.com/users/scrapinghub/repos")
    repo_list = repo_list.json()
    print(repo_list)
    return '<p> {} </p>'.format(repo_list)


if __name__ == '__main__':
    app.run()

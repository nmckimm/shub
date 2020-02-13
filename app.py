from flask import Flask
import requests

app = Flask(__name__)

access_token = '2bbadeac48f56d418461b1f27391c5c72e48081a'


@app.route('/', methods=['GET'])
def git_request():
    repo_list = requests.get("https://api.github.com/users/scrapinghub/repos?page=1&per_page=200")
    repo_list = repo_list.json()
    print("number of items",len(repo_list))
    for repo_list_item in repo_list:
        print(repo_list_item['html_url'])
        print(repo_list_item['stargazers_count'])
    return '<p> {} </p>'.format(repo_list)


if __name__ == '__main__':
    app.run()

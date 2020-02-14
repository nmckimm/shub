from flask import Flask, render_template
import requests

app = Flask(__name__)
# implement try catch with exception
repo_list = requests.get("https://api.github.com/users/scrapinghub/repos?page=1&per_page=100")
repo_list2 = requests.get("https://api.github.com/users/scrapinghub/repos?page=2&per_page=100")

repo_list = repo_list.json()
repo_list2 = repo_list2.json()
print("number of items list 1:", len(repo_list))
print("number of items list 2:", len(repo_list2))
project_name = []
project_url = []
stargazers_count = []

# for loops to add the project name, url, and star count to individual arrays which can be then sorted
for repo_list_item in repo_list:
    project_name.append(repo_list_item['name'])
    project_url.append(repo_list_item['html_url'])
    stargazers_count.append(repo_list_item['stargazers_count'])

for repo_list_item in repo_list2:
    project_name.append(repo_list_item['name'])
    project_url.append(repo_list_item['html_url'])
    stargazers_count.append(repo_list_item['stargazers_count'])

print("\nNumber of project names: ", len(project_name))
print("Number of  stargazers counts: ", len(stargazers_count))
print("Number of project urls: ", len(project_url))


def bubble_sort(stargazers_count, project_name, project_url):
    # function to sort the three arrays
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i in range(len(stargazers_count)-1):
            if stargazers_count[i] < stargazers_count[i+1]:
                stargazers_count[i], stargazers_count[i+1] = stargazers_count[i+1], stargazers_count[i]
                project_name[i], project_name[i+1] = project_name[i+1], project_name[i]
                project_url[i], project_url[i+1] = project_url[i+1], project_url[i]
                is_swapped = True
    return stargazers_count, project_name, project_url


sorted_arrays = bubble_sort(stargazers_count, project_name, project_url)
# splitting bubble sort output into the original three arrays then slicing the arrays to only contain the first 10
# values in each
stargazers_count, project_name, project_url = sorted_arrays[0][0:10], sorted_arrays[1][0:10], sorted_arrays[2][0:10]
print(stargazers_count, project_name, project_url)


@app.route('/', methods=['GET'])
def home():

    return render_template("index.html", stargazers_count=stargazers_count, project_name=project_name,
                           project_url=project_url)

if __name__ == '__main__':
    app.run()

from django.shortcuts import render
import requests
import pygal
from django.utils.dateparse import parse_datetime

# Two example views. Change or delete as necessary.
def home(request):

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/home.html', context)

def graph(request):
    response = requests.get("https://api.github.com/users/ColeElliotRayo/repos")
    repo_list = response.json()
    
    line_chart = pygal.Bar()
    line_chart.title = 'GitHub Repos by Size'
    for repo_stat in repo_list:
        size = repo_stat["size"]
        repo_name = repo_stat["name"]

        line_chart.add(repo_name,  size)

    context = {
    "github_repos": repo_list,
    "line_chart": line_chart.render().decode("utf8"),
    }

    return render(request, 'pages/graph.html', context)


def chart(request):
    response = requests.get("https://api.github.com/users/ColeElliotRayo/repos")
    repo_list = response.json()

    for repo_stat in repo_list:
        repo_stat["formatted_updated_at"] = parse_datetime(repo_stat["updated_at"]).strftime('%m-%d-%Y')
    
    context = {
        "github_repos": repo_list,
        }

    return render(request, 'pages/chart.html', context)
import requests
import plotly.express as px
# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
# Convert the response object to a dictionary.
response_dict = r.json()
# Process results.
# Explore information about the repositories.
repo_dicts = response_dict['items']
# Examine the first repository.
repo_dict = repo_dicts[0]
# Process repository information.
repo_names, stars = [], []
for repo_dic in repo_dicts:
    repo_names.append(repo_dic['name'])
    stars.append(repo_dic['stargazers_count'])
# Make visualization.
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
yaxis_title_font_size=20)
fig.show()


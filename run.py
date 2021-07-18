import requests
import config


def get_jql_filter(filter_id):
    url = config.url + "/" + str(filter_id)
    response = requests.get(url, headers=config.headers, auth=(config.username, config.password)).json()
    print("Filter name: " + response['name'])
    return response['searchUrl'] + "&maxResults=" + str(config.max_results)


def get_issues(jql_url):
    return requests.get(jql_url, headers=config.headers, auth=(config.username, config.password)).json()


def filter_total(filter_response):
    print("Filter total: " + str(filter_response['total']))


for filterId in config.filter_ids:
    filter_total(get_issues(get_jql_filter(filterId)))

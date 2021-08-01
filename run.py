from jira import JIRA

import config


def connect_to_jira():
    return JIRA(server=config.url, basic_auth=(config.username, config.password))


def get_issues_by_filter(filter_name):
    return jira.search_issues(filter_name)


def print_filter_info(filter_name, filter_issues):
    print("Using filter: " + str(filter_name))
    print("Total issues on filter: " + str(filter_issues.total))


def process(filter_name, filter_query):
    issues = get_issues_by_filter(filter_query)
    print_filter_info(filter_name, issues)


jira = connect_to_jira()

if len(config.filter_ids) != 0:
    print("\nProcessing filters by ids, total: " + str(len(config.filter_ids)))
    for filter_id in config.filter_ids:
        jira_filter = jira.filter(filter_id)
        process(jira_filter, jira_filter.jql)

if len(config.filter_jql_queries) != 0:
    print("\nProcessing custom filters by jql queries, total: " + str(len(config.filter_jql_queries)))
    for jql_name, jql_query in config.filter_jql_queries.items():
        process(jql_name, jql_query)

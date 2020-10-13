import json


def graphql_url() -> str:
    return '/graphql'


def create_graphql_json(query: str, variables: dict) -> dict:
    return {'query': query, 'variables': json.dumps(variables)}


def create_headers(auth_token: str) -> dict:
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Token {auth_token}',
    }

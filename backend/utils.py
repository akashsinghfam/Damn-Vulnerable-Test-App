import config
import requests

def get_slack_user_info(user_id):
    url = f"https://slack.com/api/users.info?user={user_id}&token={config.SLACK_TOKEN}"
    response = requests.get(url)
    return response.json() 
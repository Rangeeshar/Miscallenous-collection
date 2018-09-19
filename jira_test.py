
#Here's how I use the jira module with authentication in a Python script:
from jira.client import JIRA
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
jira = JIRA(basic_auth=('rangeesh','rangeesh96'),options={'server':'https://182.76.223.10:6060/','verify':False},max_retries=0)
issue = jira.issue('UN-9')
print(jira.current_user())

import requests
import json
import sys
import boto3
from ansible.plugins.action import ActionBase


############################## SEND TO TEAMS ##############################
## This module can send message to a teams webhook
###########################################################################

SUCCESS_COLOR = "00CC00"
FAILED_COLOR = "FF0000"

class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):

        web_hook = self._task.args.get("web_hook")
        title = self._task.args.get("title")
        success = self._task.args.get("success")
        environment = self._task.args.get("environment")
        action = self._task.args.get("action")

        if success:
            message_color = SUCCESS_COLOR
            job_status = "Success"
        else:
            job_status = "Failure"
            message_color = FAILED_COLOR

        fullTitle = "[" + title + "] - " + action + " in " + environment + " - " + job_status

        teams_params = {
            "summary": fullTitle,
            "themeColor": message_color,
            "sections": [{
                    "title":  fullTitle,
                    "facts": [{
                        "name": "Environment",
                        "value": environment
                    }, {
                        "name": "Action",
                        "value": action
                    }, {
                        "name": "Status",
                        "value": job_status
                    }]
            }]
        }

        requests.post(web_hook, data=json.dumps(teams_params))
        return {}

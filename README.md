# Send a message to a webhook teams
This action_plugin can be setup on your project if you want to send a message to a teams webhook.

## How to use it ?

Download the action_modules folder to your Ansible project root. After that you can use the plugin like this :

```yaml
    - name: send build result notification to teams when succed
      send_to_teams:
        web_hook: "https://outlook.office.com/webhook/ID"
        success:  True
        title: "Build"
        environment: "{{ your_env }}"
        action: "I tried to build something"
```
## Result

![Build Success](/send_to_teams_success.png)

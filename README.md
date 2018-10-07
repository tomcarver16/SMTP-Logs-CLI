# SMTP-Logs-CLI
A simple CLI that can send emails when called. Created to send weekly log files in a folder.

## Requirements
```
pip install -r requirements.txt
```

## Usage
This script was developed for sending weekly batches of log files if the directory contained log files with data.
Here are all the options that can be used with this script:
```
python smtp_script.py 
        --path <YOUR-FOLDER-PATH-HERE> #/home/ubuntu/folder1
        --smtp <YOUR-SMTP-SERVER-HERE> #smtp.google.com
        --port <YOUR-SMTP-PORT-HERE> #587
        --send-from <FROM-EMAIL> #me@example.com
        --password <YOUR-FROM-PASSWORD-HERE> #password1
        --send-to <TO-EMAIL> #recipent@example.com
        --subject <EMAIL-SUBJECT> #weekly log report
        --body <EMAIL-BODY> #see log files attached
```

##TODO
- [ ] Add the ability to pass html template to body
- [ ] Allow for all parameters to be passed in as json
- [ ] Add parameter for specified file(s) to be sent in the email 
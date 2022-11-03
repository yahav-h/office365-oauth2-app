# Office 365 Suite OAuth2 Application

---
```text
    This repository handles the creation of fresh 
    JWT to users who willing to use Office 365 Suite    
```
--- 
## How To

#### 1. Clone Repo
```shell
 $ git clone https://github.com/yahav-h/Office365SuiteOAuthApplication.git
```

#### 2. Create a Virtual Environment 
```shell
 $ /usr/bin//python3 -m venv venv3
```

#### 3. Dependencies Installation
```shell
 $ ./venv3/bin/python3 -m pip install -r dependencies.txt
```

#### 4. Harvesting Tokens AS Script
```shell
  # Using on PRODUCTION database
  $ ./venv3/bin/python3 ./o365_Auth.py --farm farm-1 --clusters c1,c2,c3
  # Using on DEV database
  $ ./venv3/bin/python3 ./o365_Auth.py --farm farm-1 --clusters c1,c2,c3 --debug 1 
```

#### 5. Starting a Web Server
```shell
 # Starting a web server 
 $ ./venv3/bin/python3 ./o365_Service.py
```
---

## Tool Configuration Files
- you should create a `resources` folder within the main project directory.
- the `resources` folder must contain the below configuration files templates.  
#### Configuration File : `resources/properties.yml`
- local database is created when `database.host` key IS `null` value
- remote database connection is created when `database.host` key IS NOT `null` value
```yaml
# this configuration file should be edited prior to the execution
database:
  host: "<DATABASE_IP>"
  port: "<DATABASE_PORT>"
  user: "<DATABASE_USERNAME>"
  passwd: "<DATABASE_USER_PASSWORD>"
  dbname: "<DATABASE_NAME>"
security:
  password: "<ADMIN_PASSWORD>"
oauth:
  installed:
    client_id: "<O365_CLIENT_ID>"
    client_secret: "<O365_CLIENT_SECRET>"
    scopes: "offline_access Chat.ReadWrite Files.ReadWrite.All Mail.ReadWrite Mail.Send User.Read Sites.Manage.All"
    auth_uri: "https://accounts.google.com/o/oauth2/auth"
    token_uri: "https://login.microsoftonline.com/common/oauth2/v2.0/token"
    base_url: "https://graph.microsoft.com/v1.0/"
    redirect_uris:
      - "http://localhost/"
```

#### Configuration File : `resources/mapping.yml`
```yaml
# this configuration file should include the farms, clusters and their associated users
farm-1: 
  c4:
    # please note that each user should be added as follows <USER@EMAIL.COM:GOOGLE_USER_ID>
    - "userX@subdomain.domain.net:1xcytpi0nngox6"
    - "userY@subdomain.domain.net:3664s552f0evwn"
    - "userZ@subdomain.domain.net:2dj1y382169vsk"
```
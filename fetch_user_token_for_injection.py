import datetime
import time
import base64
import flask
import requests
import helpers
import database
import pickle
from locators import Office365AdminLoginTags
from requests_oauthlib import OAuth2Session


app = flask.Flask(__name__)
email = None
action = None
CLIENT_CONFIG = helpers.getclientconfig().get("oauth")
CLIENT_ID = CLIENT_CONFIG.get("installed").get("client_id")
CLIENT_SECRET = CLIENT_CONFIG.get("installed").get("client_secret")
TOKEN_URI = CLIENT_CONFIG.get("installed").get("token_uri")
AUTH_URI = CLIENT_CONFIG.get("installed").get("auth_uri")
REDIRECT_URI = CLIENT_CONFIG.get("installed").get("redirect_uris").pop()
SCOPES = CLIENT_CONFIG.get("installed").get("scopes")


def user_consent_crawler(auth_uri, email):
    driver = helpers.getwebdriver()
    driver.implicitly_wait(5)
    driver.get(auth_uri)
    if driver.find_element(*Office365AdminLoginTags.EMAIL_FIELD).is_displayed():
        driver.find_element(*Office365AdminLoginTags.EMAIL_FIELD).send_keys(email)
    time.sleep(5)
    if driver.find_element(*Office365AdminLoginTags.NEXT_BUTTON).is_displayed():
        driver.find_element(*Office365AdminLoginTags.NEXT_BUTTON).click()
    time.sleep(5)
    if driver.find_element(*Office365AdminLoginTags.PASSWORD_FIELD).is_displayed():
      driver.find_element(*Office365AdminLoginTags.PASSWORD_FIELD).send_keys("AvananO365_!@#")
    time.sleep(5)
    if driver.find_element(*Office365AdminLoginTags.SIGN_IN_BUTTON).is_displayed():
        driver.find_element(*Office365AdminLoginTags.SIGN_IN_BUTTON).click()
    try:
        time.sleep(5)
        if driver.find_element(*Office365AdminLoginTags.YES_BUTTON).is_displayed():
            driver.find_element(*Office365AdminLoginTags.YES_BUTTON).click()
    except Exception:
        assert "code" in driver.current_url, "current URL is " + driver.current_url
        # catch the current url
        url = driver.current_url
        return url, driver


@app.route('/')
def oauth2callback():
    global email, action
    if not email:
        email = flask.request.args.get("email")
    if 'code' not in flask.request.args:
        flow = OAuth2Session(CLIENT_ID, scope=SCOPES, redirect_uri=REDIRECT_URI)
        flow.redirect_uri = REDIRECT_URI
        auth_uri, state = flow.authorization_url(AUTH_URI, prompt="login")
        user_consent_crawler(auth_uri, email)
        return flask.url_for("oauth2callback")
    else:
        auth_code = flask.request.args.get('code')
        expected_state = flask.request.args.get('state')
        try:
            aad_auth = OAuth2Session(
                CLIENT_ID, state=expected_state, scope=SCOPES, redirect_uri=REDIRECT_URI
            )
            jwt = aad_auth.fetch_token(TOKEN_URI, client_secret=CLIENT_SECRET, code=auth_code)
            data = pickle.dumps(jwt)
            b64_data = base64.b64encode(data).decode("utf-8")
            print({"data": b64_data}, 200)
            return {"data": b64_data}, 200
        except Exception as e:
            print("Error:", str(e))
            print({"data": None}, 400)
            return {"data": None}, 400


if __name__ == '__main__':
    import uuid
    database.init_debug_db()
    app.secret_key = uuid.uuid4().hex
    app.debug = False
    app.run(host="0.0.0.0", port=80)

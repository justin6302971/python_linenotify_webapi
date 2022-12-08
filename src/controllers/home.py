from flask import Blueprint, jsonify, request, current_app
from src.constants.line_notify_endpoints import AUTHORIZE_URL, TOKEN_URL, STATUS_URL
from src.constants.http_status_codes import HTTP_200_OK,HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from os import environ
import validators
import json
import requests
from src.databases.notificationdb import session, UserToken
from datetime import datetime
from flask_jwt_extended import get_jwt_identity, jwt_required

home = Blueprint("home", __name__, url_prefix="/api/v1/home")


@home.post("/oauth")
@jwt_required()
def oauth():
    code = request.form.get('code', '')

    state = request.form.get('state', '')
    is_uuid = validators.uuid(state)
    app_secret_key = current_app.config["APP_SECRET_KEY"]
    is_state_valid = state == app_secret_key

    if is_uuid == False or is_state_valid == False or code == '':
        return jsonify({"isSuccess": False, "Message": "callback request not valid"}), HTTP_400_BAD_REQUEST

    line_notify_client_id = current_app.config["LINE_NOTIFY_CLIENT_ID"]
    line_notify_client_secret = current_app.config["LINE_NOTIFY_CLIENT_SECRET"]
    app_redirect_url = current_app.config["APP_REDIRECT_URL"]

    body = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": app_redirect_url,
        "client_id": line_notify_client_id,
        "client_secret": line_notify_client_secret
    }

    token_resonpse = requests.post(TOKEN_URL, data=body)
    token_resonpse_result = token_resonpse.json()
    access_token = token_resonpse_result['access_token']

    if access_token is None:
        return jsonify({'isSuccess': False, 'Message': 'token is not valid', 'Result': ''}), HTTP_400_BAD_REQUEST

    token_params = f'Bearer {access_token}'
    status_resonpse = requests.get(STATUS_URL, headers={
        'Authorization': token_params})
    status_resonpse_result = status_resonpse.json()
    if status_resonpse_result['status'] != HTTP_200_OK:
        return jsonify({'isSuccess': False, 'Message': 'request fail', 'Result': status_resonpse_result}), HTTP_400_BAD_REQUEST

    target_name = status_resonpse_result['target']

    usertoken = session.query(UserToken).filter(
        UserToken.target_name == target_name,UserToken.status==True).first()

    if usertoken is None:
        # insert new
        new_user_token = UserToken(target_name=target_name, access_token=access_token,
                                   status=True, created_by='system', created_dt=datetime.now())
        session.add(new_user_token)

    else:
        usertoken.access_token = access_token
        usertoken.modified_by = 'system'
        usertoken.modified_dt = datetime.now()

    session.commit()

    # # todo: store user token in some place
    # current_app.config['TOKEN'] = access_token

    return jsonify({"isSuccess": True, "Message": "link line notify successfully"}), HTTP_201_CREATED


@home.get("/")
@jwt_required()
def default():
    # redirect url to line notify connection page
    line_notify_client_id = current_app.config["LINE_NOTIFY_CLIENT_ID"]

    app_redirect_url = current_app.config["APP_REDIRECT_URL"]

    state_code = current_app.config["APP_SECRET_KEY"]

    connection_url = f'{AUTHORIZE_URL}?response_type=code&response_mode=form_post&scope=notify&client_id={line_notify_client_id}&redirect_uri={app_redirect_url}&state={state_code}'

    return jsonify({'isSuccess': True, 'Message': 'click the url below to connect your line', 'Result': connection_url}), HTTP_200_OK

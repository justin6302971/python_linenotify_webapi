from flask import Blueprint, jsonify, request, current_app, json
from src.constants.line_notify_endpoints import MESSAGE_URL, STATUS_URL, REVOKED_URL
from src.constants.http_status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST
import requests
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.databases.notificationdb import session, UserToken


linenotify = Blueprint("linenotify", __name__, url_prefix="/api/v1/linenotify")


@linenotify.get("/tokens/all")
@jwt_required()
def alltokens():
    usertokens = session.query(UserToken).all()

    serialized_list = UserToken.serialize_list(usertokens)

    return jsonify({'isSuccess': True, 'Message': 'target is not valid', 'Result': serialized_list}), HTTP_200_OK


@linenotify.post("/send")
@jwt_required()
def send():
    # find user to send message

    message = request.json.get("message")

    target = request.json.get("target")

    # todo: consider using validator for params validation
    if target is None or target == '':
        return jsonify({'isSuccess': False, 'Message': 'target is not valid', 'Result': ''}), HTTP_400_BAD_REQUEST

    if message is None or message == '':
        return jsonify({'isSuccess': False, 'Message': 'message is not valid', 'Result': ''}), HTTP_400_BAD_REQUEST

    # retrieve token from some place
    usertoken = session.query(UserToken).filter(
        UserToken.target_name == target, UserToken.status == True).first()

    if usertoken is None:
        return jsonify({'isSuccess': False, 'Message': 'target is not valid', 'Result': ''}), HTTP_400_BAD_REQUEST

    token = usertoken.access_token

    if token is None:
        return jsonify({'isSuccess': False, 'Message': 'token is not valid', 'Result': ''}), HTTP_400_BAD_REQUEST

    token_params = f'Bearer {token}'
    # send message

    body = {
        "message": message,
    }

    resonpse = requests.post(MESSAGE_URL, headers={
                             'Authorization': token_params}, data=body)
    resonpse_result = resonpse.json()
    if resonpse_result['status'] != HTTP_200_OK:
        return jsonify({'isSuccess': False, 'Message': 'request fail', 'Result': {'linenotify':resonpse_result}}), HTTP_400_BAD_REQUEST

    return jsonify({'isSuccess': True, 'Message': 'send message successfully', 'Result': ''}), HTTP_200_OK


@linenotify.get("/status")
@jwt_required()
def check_status():

    # todo: pass user target
    target = request.args.get('target', '')
    if target is None or target == '':
        return jsonify({'isSuccess': False, 'Message': 'target is not valid', 'Result': ''}), HTTP_400_BAD_REQUEST
    # retrieve token from some place
    token = session.query(UserToken).filter(
        UserToken.target_name == target, UserToken.status == True).first()

    if token is None:
        return jsonify({'isSuccess': False, 'Message': 'token is not valid', 'Result': ''})

    token_params = f'Bearer {token}'
    resonpse = requests.get(STATUS_URL, headers={
                            'Authorization': token_params})
    resonpse_result = resonpse.json()
    if resonpse_result['status'] != HTTP_200_OK:
        return jsonify({'isSuccess': False, 'Message': 'request fail', 'Result': {'linenotify':resonpse_result}}), HTTP_400_BAD_REQUEST

    return jsonify({'isSuccess': True, 'Message': 'get status successfully', 'Result': f"current target is {resonpse_result['target']}"}), HTTP_200_OK


@linenotify.post("/revoke")
@jwt_required()
def revoke():
    # todo: pass user target
    target = request.json.get("target")

    if target is None:
        return jsonify({'isSuccess': False, 'Message': 'target is not valid', 'Result': ''}), HTTP_400_BAD_REQUEST

    # retrieve token from some place
    token = session.query(UserToken).filter(
        UserToken.access_token == target, UserToken.status == True).first()

    if token is None:
        return jsonify({'isSuccess': False, 'Message': 'token is not valid', 'Result': ''}), HTTP_400_BAD_REQUEST

    token_params = f'Bearer {token}'
    resonpse = requests.post(REVOKED_URL, headers={
        'Authorization': token_params})
    resonpse_result = resonpse.json()
    if resonpse_result['status'] != HTTP_200_OK:
        return jsonify({'isSuccess': False, 'Message': 'request fail', 'Result': resonpse_result}), HTTP_400_BAD_REQUEST

    # todo: update user token status(soft delete)
    token.status = False
    session.commit()

    return jsonify({'isSuccess': True, 'Message': 'revoke successfully', 'Result': resonpse_result['message']}), HTTP_200_OK

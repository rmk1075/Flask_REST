import json

from flask import Blueprint, Response, request, session

from pREST.repository import memrepo as mr
# from pREST.repository import mongorepo as mr
from pREST.domain.request_objects import room_list_request_object as req
from pREST.domain.response_objects import response_objects as res
from pREST.serializers import room_json_serializer as ser
from pREST.domain.use_cases import room_list_use_case as uc

blueprint = Blueprint("room", __name__)

# response_object의 type -> http response type 을 정의
STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500,
}

# repository 에 주입시켜줄 데이터베이스 정보
connection_data = {
    "dbname": "pRESTdb",
    "user": "root",
    "password": "pRESTdb",
    "host": "localhost"
}


@blueprint.route("/rooms", methods=["GET"])
def room():
    for item in request.args.items():
        print(item)

    # session check - session['val']의 값을 1씩 더해서 session 유지되는지 확인
    if 'val' in session.keys():
        print(session['val'])
        session['val'] += 1
    else:
        session['val'] = 0

    qrystr_params = {
        "filters": {},
    }
    for arg, values in request.args.items():
        if arg.startswith("filter_"):
            qrystr_params["filters"][arg.replace("filter_", "")] = values

    # 외부 요청 형태(http, json) -> 유스케이스 request_object로 변환.
    request_object = req.RoomListRequestObject.from_dict(qrystr_params)

    # 사용할 구체적인 Repository를 생성한다.
    # repo = mr.MongoRepo(connection_data)
    room1 = {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "size": 215,
        "price": 39,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    }
    room2 = {
        "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
        "size": 405,
        "price": 66,
        "longitude": 0.18228006,
        "latitude": 51.74640997,
    }
    room3 = {
        "code": "913694c6-435a-4366-ba0d-da5334a611b2",
        "size": 56,
        "price": 60,
        "longitude": 0.27891577,
        "latitude": 51.45994069,
    }

    repo = mr.MemRepo([room1, room2, room3])

    # 유스케이스 인스턴스를 만들어 실행 후 결과인 response_object를 받는다.
    use_case = uc.RoomListUseCase(repo)
    response = use_case.execute(request_object)

    # response_object -> 외부 응답 형태(http, json)로 변환.
    return Response(
        json.dumps(response.value, cls=ser.RoomJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODES[response.type],
    )

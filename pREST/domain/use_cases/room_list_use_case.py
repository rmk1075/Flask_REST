from typing import Union

from pREST.domain.interfaces.repository import Repository
from pREST.domain.request_objects import room_list_request_object as req
from pREST.domain.response_objects import response_objects as res
from pREST.domain.response_objects.response_objects import ResponseFailure, ResponseSuccess


# business login
class RoomListUseCase:
    def __init__(self, repo: Repository):
        self.repo = repo

    # usecase를 실행하는 함수
    # request_object -> response_object
    # 1. request_object를 입력받아 repo라는 저장소를 호출한다.
    # 2. repo는 filters의 조건에 맞는 데이터를 반환한다.
    # 3. 조회한 repo 데이터 (rooms)를 response_object (res)에 넘겨주어서 반환한다.
    # 4. try-catch 예외사항이 적용되어 있다.
    def execute(
        self, request_object: Union[req.ValidRequestObject, req.InvalidRequestObject]
    ) -> Union[ResponseSuccess, ResponseFailure]:
        if not request_object:
            return res.ResponseFailure.build_from_invalid_request_object(request_object)

        try:
            rooms = self.repo.list(filters=request_object.filters)
            return res.ResponseSuccess(rooms)
        except Exception as exc:
            return res.ResponseFailure.build_system_error("{}: {}".format(exc.__class__.__name__, "{}".format(exc)))
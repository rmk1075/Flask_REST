from abc import ABCMeta, abstractmethod
from typing import List

from pREST.domain.entities.room import Room


# Repository, 데이터 저장소 역할을 한다.
# 원하는 데이터를 메소드를 통해서 가져오는 객체로 usecase layer에서는  interface만 정의한다.
class Repository(metaclass=ABCMeta):
    @abstractmethod
    def list(self, filters: dict = None) -> List[Room]:
        pass

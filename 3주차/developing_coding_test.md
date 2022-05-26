#### [참고 원본 - 개발형 코딩 테스트](https://www.youtube.com/watch?v=d8KPN79UAKA&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=10)

### Table of Contents
- [Table of Contents](#table-of-contents)
- [개발형 코딩 테스트](#개발형-코딩-테스트)
- [REST API](#rest-api)
- [JSON](#json)
- [REST API 연습용 서비스](#rest-api-연습용-서비스)
- [리뷰](#리뷰)


### 개발형 코딩 테스트
* 정해진 목적을 수행하는 완성된 프로그램을 개발하는 형태의 코딩 테스트
* 해커톤 형식도 사용
  * 해커톤 : 단기간에 아이디어를 제품화하는 프로젝트, 대체로 1 ~ 2일 진행 후, 발표 및 채점, 수상
* 기존의 알고리즘 코딩 테스트와의 차이

|알고리즘 코딩 테스트| 개발형 코딩 테스트|
|---|---|
|시간 복잡도 고려 | 완성도 높은 하나의 프로그램 개발|
|공간 복잡도 고려 | 다른 모듈을 적절히 조합하는 능력 필요|
|하나의 개별 모듈 개발| - |

* 분야에 따라 요구 사항이 달라짐
  * 모바일 : `iOS`, `Android`
  * 백엔드 : `Java`, `Spring`, `Django`
* 공통적으로 필요한 개념
  * `Server`
    * `Client`에서 받은 요청을 처리해서 응답 전송
    * 웹 브라우저 : 로그인 요청을 받아서, 아이디와 비밀번호 확인 후, 결과를 전달
    * 위와 같은 과정에서 DataBase, 외부 API 등을 포함할 수 있음
  * `Client`
    * `Server`에 필요한 데이터를 요청 후 응답 대기
    * 응답을 받으면, 응답을 화면에 적절히 출력
    * 웹 브라우저 : 서버에서 받은 HTML, CSS 코드를 화면에 출력
    * 게임 APP : 서버에서 받은 경험치, 친구목록 등의 정보를 화면에 출력
  * `HTTP` (HyperText Transfer Protocol)
    * 주로 HTML을 전송하기 위한 규약
    * 모바일 앱 및 게임에서도 특정 형식의 데이터 송수신을 위해 사용
    * 대표적인 HTTP 메서드
      * `GET` : 데이터 조회 요청 (페이지 접속 및 검색)
      * `POST` : 데이터 생성 요청 (회원가입 및 글쓰기)
      * `PUT` : 데이터 수정 요청 (회원 정보 수정)
      * `DELETE` : 데이터 삭제 요청 (회원 정보 삭제)
      * 자동으로 구현되는 것은 아님, 사전에 해당 HTTP 서버에서 구현이 필요
      * 동작을 위해 `python`의 `requests` 모듈을 사용할 수 있음

### REST API
* Representational State Transfer의 약자
* 자원, 행위, 표현의 세 가지로 구성
  * 자원 : `URI`(Uniform Resource Identifier)를 이용, ex) 사용자를 의미
  * 행위 : `HTTP` 메서드를 이용, ex) 회원 등록을 의미
  * 표현 : `Payload`를 이용 ex) 특정 포맷에 맞는 데이터, 아이디 및 비밀번호를 의미
* API (Application Programming Interface) : 실제 다른 프로그램과 상호작용하기 위한 인터페이스

### JSON
* `REST API`를 호출하기 위해 주로 사용하는 형식
* JavaScript Object Notation의 줄임말
* `key`와 `value`의 쌍을 가지는 데이터 객체
* 내부적으로 다른 타입을 포함할 수 있음
```json
{
    "id" : "Jackson",
    "password" : "1234qwer",
    "age" : 30,
    "hobby" : ["Game", "Youtube"]
}
```
* `python`에서는 `json` 모듈을 사용하여 처리할 수 있음
```python
import json

user = {
    "id" : Jackson",
    "password" : "1234qwer",
    "age" : 30,
    "hobby" : ["Game", "Youtube"]
}

# JSON 데이터로 변환하여 출력
json_data = json.dump(user, indent=4)
print(json_data) # json_data 출력

# JSON 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="utf-8") as file:
    json_data = json.dump(user, file, indent=4)
```

### REST API 연습용 서비스
* Mocking : 기능이 있는 것처럼 흉내내어 구현한 것
* [가상 REST API를 제공하는 서비스](https://jsonplaceholder.typicode.com)
```python
import requests

# get 메서드를 통해 데이터 받아오기
target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

# 응답 데이터는 기본적으로 JSON형식이므로, python 객체로 변환
data = response.json()

# 모든 사용자 (user) 정보를 확인하며, 이름 정보만 삽입
name_list = []
for user in data:
    name_list.append(user['name'])

print(name_list)
``` 

### 리뷰
* 생각보다 진짜 REST API는 아무데서나 다 들을 수 있음
* 데이터 저장하는 타입에는 XML, JSON, YAML 등이 존재
* 범용적으로 많이 사용하는 것은 역시 JSON인 것 같음
* 필요한 상황 및 방법에 따라 구현해보는 것이 중요함
* 실무에서 실질적으로 꽤나 많이 필요한 내용으로 생각됨
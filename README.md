# PowerNad
## 과제용 프로젝트임에도 관심가져 주셔서 감사합니다. :)

[![PowerNad](https://img.shields.io/badge/python-3.4%2C%203.5%2C%203.6-blue.svg)]()
[![PowerNad](https://img.shields.io/vso/build/larsbrinkhoff/953a34b9-5966-4923-a48a-c41874cfb5f5/1.svg)]()
[![PowerNad](https://img.shields.io/badge/pypi-0.5.1-orange.svg)](https://pypi.python.org/pypi?:action=display&name=powernad&version=0.3)
[![PowerNad](https://img.shields.io/npm/l/express.svg)](https://github.com/devkingsejong/python-PowerNad#license)

``` 본 문서 또는 라이브러리내에서 언급되는 'Naver' 혹은 '네이버'는 Naver Corp의 상표입니다. ``` <br /> 
``` 'Naver' and '네이버' are trademarks of Naver Corp ``` <br /> 
## What is PowerNad?

PowerNad는 Power for NaverAD의 약자로 [네이버 광고 API](http://naver.github.io/searchad-apidoc/#/guides)를 Python에서 쉽게 사용할 수 있도록 해주는 라이브러리 입니다.

``` 2017. 03. 15 ``` 기준으로 전체 API중 90% 이상의 커버율을 가지고 있습니다. 

## How to Install?

``` pip3 install powernad ``` <br />

or <br />

```git clone https://github.com/devkingsejong/python-PowerNad.git ```

## How to Use?

powernad는 크게 API들이 정의 되어 있는 ```API```와 Request Object들이 정의되어 있는 ```Object```로 나누어져 있습니다.

### 1. Include API

특정 API를 사용하고 싶다면,

```python
from powernad.API.AdGroup import *
from powernad.API.Campaign import *
```
위와 같이 [네이버 광고 API](http://naver.github.io/searchad-apidoc/#/guides)에 정의되어 있는 API명을 import합니다.

### 2. Initialize API

```python
ad_group = AdGroup('API 호출 주소', 'API 키', 'Secret 키', '유저 고유번호')
campaign = Campaign('API 호출 주소', 'API 키', 'Secret 키', '유저 고유번호')
```
```API 호출 주소 ``` : API base url <br />
```API 키``` : api_key <br />
```Secret 키``` : secret_key <br />
```유저 고유번호``` : customer_id <br />

위와 같이 Naver API 관리패널에서 발급받은 정보를 넣어, 초기화 해줍니다.

### 3. Use GET API

(1) 캠페인 아이디를 기반으로 그룹 불러오기

```python
group_list = campaign.get_adgroup_list('cmp-xxxxx')
```

(2) 그룹 아이디를 기반으로 그룹 리스트 불러오기
```python
group_list2 = ad_group.get_adgroup_list_by_ids(그룹고유번호)
```

### 4. Use Post API(Require Request Params)

PowerNad에서는 보다 쉽게 Request 파라미터를 구성할 수 있도록, 미리 정의된 ```Object``` 모음을 제공합니다. <br />

만약 ```그룹 생성 API```를 사용하고 싶다면, 

``` python 
from powernad.API import AdGroup
from powernad.Object.AdGroup.RequestObject.CreateAdgroupObject import CreateAdgroupObject

ad_group = AdGroup('API 호출 주소', 'API 키', 'Secret 키', '유저 고유번호')
cad = CreateAdgroupObject('cmp-a000-00-0003', 'group Name', 'bsn-0001-00-0001', 'bsn-a001-00-0002')
ad_group.create_adgroup(cad)

```
위와 같이 Object를 API파라미터에 넣어주는 것 만으로 간단하게 사용할 수 있습니다. (필수 parameter는 생성자로 정의 가능합니다.)

## License


Copyright (c) <2017> <[devkingsejong](https://github.com/devkingsejong/python-PowerNad)>

이 소프트웨어의 복제본과 관련된 문서화 파일(“소프트웨어”)을 획득하는 사람은 누구라도 소프트웨어를 별다른 제한 없이 무상으로 사용할 수 있는 권한을 부여 받는다.
여기에는 소프트웨어의 복제본을 무제한으로 사용, 복제, 수정, 병합, 공표, 배포, 서브라이선스 설정 및 판매할 수 있는 권리와 이상의 행위를 소프트웨어를 제공받은
다른 수취인들에게 허용할 수 있는 권리가 포함되며, 다음과 같은 조건을 충족시키는 것을 전제로 한다.

```위와 같은 저작권 안내 문구와 본 허용 문구가 소프트웨어의 모든 복제본 및 중요 부분에 포함되어야 한다.```

이 소프트웨어는 상품성, 특정 목적 적합성, 그리고 비침해에 대한 보증을 포함한 어떠한 형태의 보증도 명시적이나 묵시적으로 설정되지 않은 “있는 그대로의” 상태로 제공된다. 소프트웨어를 개발한 프로그래머나 저작권자는 어떠한 경우에도 소프트웨어나 소프트웨어의 사용 등의 행위와 관련하여 일어나는 어떤 요구사항이나 손해 및 기타 책임에 대해 계약상, 불법행위 또는 기타 이유로 인한 책임을 지지 않는다.




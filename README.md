# PowerNad

[![PowerNad](https://img.shields.io/badge/python-3.4%2C%203.5%2C%203.6-blue.svg)]()
[![PowerNad](https://img.shields.io/vso/build/larsbrinkhoff/953a34b9-5966-4923-a48a-c41874cfb5f5/1.svg)]()
[![PowerNad](https://img.shields.io/badge/pypi-v0.01-orange.svg)]()
[![PowerNad](https://img.shields.io/npm/l/express.svg)]()

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
from powernad.API import AdGroup
from powernad.API import Campaign
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

### 3. Use API

#### Use Get API

(1) 캠페인 아이디를 기반으로 그룹 불러오기

```python
group_list = campaign.get_adgroup_list(campaignid = 'cmp-xxxxx')
```

(2)그룹 아이디를 기반으로 그룹 리스트 불러오기
```python
group_list2 = ad_group.get_adgroup_list_by_ids(그룹고유번호)
```

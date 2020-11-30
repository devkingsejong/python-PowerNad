# 캠페인

## 초기화: 

```python
from API.Campaign import Campaign
campain = Campaign(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```


## 캠페인 리스트 불러오기:

```python
campain.get_campaign_list()
```

## 아이디로 캠페인 리스트 불러오기 : 

```python
campain.get_campaign_list_by_ids("cmp-a001-01-000000000171629")
```

## 캠페인 정보 불러오기:

```python
campain.get_campaign("cmp-a001-01-000000000171629")
```

## 캠페인 생성하기: 

```python
from Object.Campain.RequestObject.CampainAddObject import CampainAddObject

campain_add_object = CampaignAddObject(client.CUSTOMER_ID, "WEB_SITE", "난니가정말좋아")
campain.create_campaign(campain_add_object)
```

## 캠페인 업데이트하기: 

```python
from Object.Campain.RequestObject.CampainUpdateObject import CampainUpdateObject

campain_update_object = CampainUpdateObject(True, True, True) # userLock, budget, period만 필드에 들어갑니다.
campain_add_object.update_campaign(campain_update_object, "cmp-a001-01-000000000375491", "userLock") 
```

# 애드그룹

## 초기화:

```python
from API.AdGroup import AdGroup
ad_group = AdGroup(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 제외한 확장 키워드 불러오기:

```python
ad_group.get_restricted_keyword(애드그룹고유번호)
```

## 캠페인 아이디를 기반으로 그룹들 불러오기: 

```python
ad_group.get_adgroup_list(campaignid = None, baseid = None, record_size = None, selector = None)
```

## 그룹 고유 아이디를 기반으로 그룹리스트 불러오기 : 

```python
ad_group.get_adgroup_list_by_ids(그룹고유번호)
```

## 그룹 고유 아이디를 기반으로 그룹 정보 불러오기 : 

```python
ad_group.get_adgroup_by_adgroupid(그룹고유번호)
```

## 제외할 확장 키워드를 추가하기:

```python
from Object.Adgroup.RequestObject.RestrictedKeywordsObject import RestrictedKeywordsObject

restricted_keywords_object = RestrictedKeywordsObject("쁘디성형","에피아테스트2","grp-a001-01-000000002412336")
ad_group.create_restricted_keyword("grp-a001-01-000000002412336", restricted_keywords_object)
```

## 애드그룹 생성하기:

```python
from Object.Adgroup.RequestObject.CreateAdGroupObject import CreateAdGroupObject

create_ad_group_object = CreateAdgroupObject('cmp-a001-01-000000000375491',
                                             'ad_group_name',
                                             'bsn-a001-00-000000000268491',
                                             'bsn-a001-00-000000000268491')
ad_group.create_adgroup(create_ad_group_object)
```

## 애드그룹업데이트하기(필드를 통해):

```python
from Object.Adgroup.RequestObject.UpdateAdgroupObject import UpdateAdgroupObject

update_adgroup_object = UpdateAdgroupObject(50000)
ad_group.update_adgroup('grp-a001-01-000000002412336', {'fields': 'bidAmt'}, update_adgroup_object)
```

## 애드그룹업데이트하기(엔타이어):

```동작 여부 테스트 필요```

## 그룹에서 제외 키워드 삭제하기:

```python
ad_group.delete_group_restricted_keyword('grp-a001-01-000000002412336','rst-a001-00-000000000081865')
```

## 애드그룹 삭제하기 : 

```python
ad_group.delete_adgroup('grp-a001-01-000000002548183')
```

# 애드(소재)

## 초기화:

```python
from API.Ad import Ad

ad = Ad(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 소재고유번호를 통해 리스트 받아오기:

```python
ad_list = ad.get_ad_list_by_ids('nad-a001-01-000000009598016')
print(ad_list[0].nccAdId)
```

## 애드그룹고유번호를 통해 리스트 받아오기:

```python
ad_list = ad.get_ad_list('grp-a001-01-000000002412336')
print(ad_list[0].ad.pc)
```

## 소재고유번호를 통해 소재 정보 받아오기:

```python
target_ad = ad.get_ad('nad-a001-01-000000009598016')
print(target_ad.nccAdgroupId)
```

## 소재등록하기:

```python
from Object.Ad.sub.AdFieldObject import AdFieldObject

filed_obj = AdFieldObject()
filed_obj.description = "이것은 에이피아이 테스트의 일종으로 테스트입니다."
filed_obj.headline = "에이피아이 wowwow"
filed_obj.pc = filed_obj.make_pc_easy('http://www.naver.com')
filed_obj.mobile = filed_obj.make_mobile_easy('http://www.naver.com')

add_obj = CreateAdObject(filed_obj, 'grp-a001-01-000000002412336', 'TEXT_45')

return_obj = ad.create_ad(add_obj)
```

## 소재 수정하기:

```python
from Object.Ad.sub.AdFieldObject import AdFieldObject

filed_obj = AdFieldObject()
filed_obj.description = "이것은 에이피아이 테스트의 일종으로 테스트"
filed_obj.headline = "에이피아이 에드클라우드"
filed_obj.pc = filed_obj.make_pc_easy('http://www.naver.com')
filed_obj.mobile = filed_obj.make_mobile_easy('http://www.naver.com')

update_obj = UpdateAdObject(filed_obj,'nad-a001-01-000000010072369')
update_obj.userLock = 1
ad.update_ad('nad-a001-01-000000010072369', 'userLock', update_obj)
```

## 소재 복사:

```python
ad.copy_ad('nad-a001-01-000000009598016', 'grp-a001-01-000000002548182', '0')
```

## 소재 삭제: 

```python
ad.delete_ad('nad-a001-01-000000010072402')
```

# 확장소재 

## 초기화:

```python
from API.AdExtention import AdExtention

ad_extention = AdExtention(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 캠페인 아이디나 그룹아이디를 기반으로 확장소재 리스트 가져오기:

```python
ad_extention.get_ad_extensions_list('cmp-a001-01-000000000375491')
```

## 확장소재 아이디를 기반으로 확장소재 리스트 가져오기 :

```python
ad_extention.get_ad_extensions_list_by_ids('ext-a001-01-000000000503236')
```

## 확장소재 아이디를 기반으로 확장소재 가져오기:

```python
target_ad_extention = ad_extention.get_ad_extensions('ext-a001-01-000000000503236')
print(target_ad_extention)
```

## 확장 소재를 등록하기: 

```python
from Object.AdExtention.RequestObject.CreateAdExtensionObject import CreateAdExtensionObject

create_ad_extention_object = CreateAdExtensionObject('bsn-a001-00-000000000287001',
                                                     'bsn-a001-00-000000000287001',
                                                     'cmp-a001-01-000000000375491', 'PHONE', False)
ad_extention.creat_ad_extensions(create_ad_extention_object)
```

## 확장소재 업데이트:

```python
from Object.AdExtention.RequestObject.UpdateAdExtensionObject import UpdateAdExtensionObject

update_ad_extention_object = UpdateAdExtensionObject('ext-a001-01-000000000503236', None, False)
ad_extention.update_ad_extensions('ext-a001-01-000000000503236', 'userLock', update_ad_extention_object)
```

## 확장소재 삭제하기:

```python
ad_extention.delete_ad_extensions('ext-a001-01-000000000503236')
```

# 비즈니스채널

## 초기화:

```python
from API.BusinessChannel import BusinessChannel

business_channel = BusinessChannel(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 비즈니스 채널 리스트가져오기:

```python
target_business_channel = business_channel.get_business_channel_list()
print(target_business_channel[0].businessInfo.site)
```

## 채널 타입을 기준으로 채널 리스트 가져오기:

```python
target_business_channel = business_channel.get_business_channel_list_by_type(self, 'PHONE'):
print(target_business_channel[0].businessInfo.site)
```

## 채널 고유번호를 기준으로 채널 리스트 가져오기:

```python
target_business_channel_list = business_channel.get_business_channel_list_by_ids('bsn-a001-00-000000000124029')
print(target_business_channel_list[0].businessInfo.site)
```

## 채널 고유번호로 비즈니스 채널 가져오기:

```python
target_business_channel = business_channel.get_business_channel('bsn-a001-00-000000000124029')
print(target_business_channel.blackStatus)
```

## 비즈니스 채널 만들기:

```python
from Object.BusinessChannel.RequestObject.CreateBusinessChannelObject import CreateBusinessChannelObject

create_business_channel_object = CreateBusinessChannelObject('http://simpangoooo.net', 'apitest2')
business_channel.create_business_channel(create_business_channel_object)
```

## 비즈채널업데이트:

``` 동작 여부 테스트 필요함 ```

## 비즈채널삭제:

```python
business_channel.delete_business_channel('bsn-a001-00-000000000298203')
```

## ids로 비즈채널(클릭초이스) 삭제:

```python
business_channel.delete_business_channel_by_ids('ids,')
```

## request inspect:

``` 지원 예정 ```

# AdKeyword 

## 초기화:

```python
from API.AdKeyword import AdKeyword

ad_keyword = AdKeyword(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 키워드 고유번호를 기반으로 키워드 리스트 가져오기:

```python
ad_keyword.get_adkeyword_list_by_ids(ids)
```

## 라벨 아이디를 기반으로 키워드 리스트 가져오기:

```python
ad_keyword.get_adkeyword_list_by_labelid(labelid)
```

## 그룹 아이디를 기반으로 키워드 리스트 가져오기:

```python
ad_keyword.get_adkeyword_list_by_groupid(group id)
```

## 키워드 정보 가져오기:

```python
target_ad_keyword = ad_keyword.get_adkeyword('nkw-a001-01-000000458957253')
print(target_ad_keyword.bidAmt)
```

## 키워드 생성하기:

```python
from Object.AdKeyword.RequestObject.CreateAdKeywordObject import CreateAdKeywordObject

create_ad_keyword_object = CreateAdKeywordObject("키워드")

ad_keyword.create_adkeyword('grp-a001-01-000000002412336', create_ad_keyword_object)
```

## 키워드 업데이트 하기:

```python
from Object.AdKeyword.RequestObject.UpdateAdKeywordObject import UpdateAdKeywordObject

update_ad_keyword_objecy = UpdateAdKeywordObject('grp-a001-01-000000002412336', 'nkw-a001-01-000000472996331')
update_ad_keyword_objecy.bidAmt = 3450
update_ad_keyword_objecy.useGroupBidAmt = False

ad_keyword.update_adkeyrword('nkw-a001-01-000000472996331', 'bidAmt', update_ad_keyword_objecy)
```

## 키워드 삭제하기:

```python
ad_keyword.delete_adkeyword('nkw-a001-01-000000472996331')
```

## 키워드 한번에 여러개 삭제:

```python
ad_keyword.delete_adkeyword_many(ids_list):
```

## 관리하고 있는 키워드의 리스트 가져오기:

```python
target_ad_keyword = ad_keyword.managed_keyword_list('온라인광고')
print(target_ad_keyword[0].managedKeyword.isAdult)
```

# 라벨

## 초기화:

```python
from API.Label import Label

label = Label(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 라벨 가져오기:

```python
target_label = label.get_label_list()

print(target_label[0].color)
```

## 라벨 업데이트:

```python
from Object.Label.RequestObject.UpdateLabelObject import UpdateLabelObject

update_label_object = UpdateLabelObject('lbl-a001-00-000000000033511')
update_label_object.name = "API TST"

label.update_label(update_label_object)
```

## 라벨 REF(바로가기) 업데이트:

```python
from Object.Label.RequestObject.UpdateLabelRefObject import UpdateLabelRefObject

update_label_ref_object = UpdateLabelRefObject('1109868',
                                               'lbl-a001-00-000000000033513',
                                               'grp-a001-01-000000002601856',
                                               'ADGROUP')
label.update_label_ref(update_label_ref_object)
```

# 타겟

## 초기화:

```python
from API.Target import Target
target = Target(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 타겟리스트 가져오기:

```python
current_target = target.get_target_list('grp-a001-01-000000002412336')
print(current_target[0].nccTargetId)
```

## 타겟리스트 업데이트:

```python
테스트 필요(Target Object 관련 구현)
```

# IpExclusion

## 초기화

```python
from API.IpExclusion import IpExclusion
ip_exclusion = IpExclusion(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 차단된 아이피 리스트 가져오기:

```python
target_ip_exclusion = ip_exclusion.get_ip_exclusion()
print(target_ip_exclusion[0].filterIp)
```

## 차단할 아이피 추가하기:

```python
from Object.IpExclusion.RequestObject.CreateIpExclusionObject import CreateIpExclusionObject

create_ip_exclusion = CreateIpExclusion('1.234.56.7')

ip_exclusion.create_ip_exclusion(create_ip_exclusion)
```

## 차단할 아이피 업데이트:

```python
from Object.IpExclusion.RequestObject.UpdateIpExclusionObject import UpdateIpExclusionObject

update_ip_exclusion = UpdateIpExclusionObject('1.222.34.5', '3487550')
update_ip_exclusion.memo = "change test"

ip_exclusion.update_ip_exclusion(update_ip_exclusion)
```

## 차단할 아이피 삭제하기:

```python
ip_exclusion.delete_ip_exclusion('34.875.50.1')
```

## 차단할 아이피 리스트로 삭제하기:

```python
ip_exclusion.delete_ip_exclusion_many(id list)
```

# 비즈머니

## 초기화

```python
from API.Bizmoney import Bizmoney

biz_money = Bizmoney(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 비즈머니 조회:

```python
current_biz_money = biz_money.get_biz_money()
print(current_biz_money.bizmoney)
```

## 비즈머니 사용실적: 

```python
biz_money.get_biz_money_cost('20170301')
```


# ManagedCustomerLinkList:

## 초기화

```python
from API.ManagedCustomerLink import ManagedCustomerLink

managed_customer_link = ManagedCustomerLink(
                                              client.BASE_URL,
                                              client.API_KEY,
                                              client.SECRET_KEY,
                                              client.CUSTOMER_ID
                                            )
```

## 리스트로 고객리스트 가져오기:

```python
managed_customer_link.get_managed_customer_link_list(타입<선택사항>)
```

# 대용량보고서:

## 초기화

```python
from API.StatReport import StatReport

stat_report = StatReport(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 대용량보고서목록보기:

```python
current_stat_report = stat_report.get_stat_report_list()
print(current_stat_report[0].statDt)
```

## 리스트고유번호로 대용량 보고서 목록보기:

```python
current_stat_report = stat_report.get_stat_report('150381075')
print(current_stat_report.statDt)
```

## 대용량 보고서 생성하기

```python
from Object.StatReport.RequestObject.CreateStatReportObject import CreateStatReportObject

create_stat_report_object = CreateStatReportObject('AD_CONVERSION_DETAIL', '2017-03-10T15:00:00Z')

stat_report.create_stat_report(create_stat_report_object)
```

## 대용량 보고서 삭제하기:

```
stat_report.delete_stat_reports('158389454')
```

## 아이디로 스탯가져오기:

```python
fields = '["impCnt","clkCnt","salesAmt"]'
target_stat_report = stat_report.get_stat_by_id('grp-a001-01-000000002412336',
                                                fields,
                                                '{"since":"2017-02-26","until":"2017-03-04"}',
                                                None, None, None)
print(target_stat_report.data[0].dateEnd)
```

## 아이디 리스트로 가져오기:

```python
fields = '["impCnt","clkCnt","salesAmt"]'
target_stat_report = stat_report.get_stat_by_id('grp-a001-01-000000002412336,grp-a001-01-000000001235166',
                                                fields,
                                                '{"since":"2017-02-26","until":"2017-03-04"}',
                                                None, None, None)
print(target_stat_report.data[0].dateEnd)
```

### 스탯타입으로 가져오기(테스트필):

``` 동작 여부 테스트 필요함 ```

# MasterReport(광고정보일괄다운로드):

## 초기화:

```python
from API.MasterReport import MasterReport
master_report = MasterReport(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 다운로드 목록 불러오기:

```python
current_master_report = master_report.get_master_report_list()
print(current_master_report[0].managerLoginId)
```

## 아이디로 다운로드 정보 가져오기:

```python
current_master_report = master_report.get_master_report_by_id('F9F0D4813CDB89E7F5907EAE79C7A0B2')
print(current_master_report.registTime)
```

## 다운로드  요청 만들기:

```python
from Object.MasterReport.RequestObject.CreateMasterReportObject import CreateMasterReportObject

create_master_report_object = CreateMasterReportObject('Campaign', '2017-03-12T15:00:00Z')
master_report.create_master_report(create_master_report_object)
```

## 전부삭제하기:

```python
master_report.delete_master_report_all()
```

## 특정아이디로 삭제하기:

```python
master_report.delete_master_report_by_id('3BE28582CCC31D199D2C583D191257B5')
```

# 관계있는 키워드 정보들 보기(RelKwdStat):

## 초기화 

```python
from API.RelKwdStat import RelKwdStat
rel_kwd_stat = RelKwdStat(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 관계있는 키워드 정보들 보기(RelKwdStat)


```python
target_rel_kwd_stat = rel_kwd_stat.get_relkwd_stat_list('bsn-a001-00-000000000124029')
print(target_rel_kwd_stat[0].monthlyAveMobileClkCnt)
```

# Estimate

## 초기화

```python
from API.Estimate import Estimate

estimate = Estimate(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 순위로 비딩 평균 가져오기:

```python
from Object.Estimate.RequestObject.GetAvgPositionBidObject import GetAvgPositionBidObject
from Object.Estimate.sub.KeyAndPositionObject import KeyAndPositionObject

key_and_position1 = KeyAndPositionObject('음주운전', 3)
key_and_position2 = KeyAndPositionObject('보험', 3)
get_avg_position_bid_object = GetAvgPositionBidObject('PC', [key_and_position1, key_and_position2])

target_bidding_estimate = estimate.get_avg_position_bid_list('keyword', get_avg_position_bid_object)
print(target_bidding_estimate[0].bid)
```

## 키워드로 평균 비딩 가져오기:

```python
from Object.Estimate.RequestObject.GetMedianBidObject import GetMedianBidObject

get_median_bid_object = GetMedianBidObject('PC', 'DAY', ['화분', '보험'])

target_bid_estimate = estimate.get_median_bid_list('keyword', get_median_bid_object)
print(target_bid_estimate[0].bid)
```

## 노출 최솟값 받아오기:

```python
from Object.Estimate.RequestObject.GetExposureMiniBidObject import GetExposureMiniBidObject
get_exposure_mini_bid_object = GetExposureMiniBidObject('PC', 'DAY', ['화분', '보험'])

target_bid_estimate = estimate.get_exposure_mini_bid_list('keyword', get_exposure_mini_bid_object)
print(target_bid_estimate[0].bid)
```

## 예상실적 받아오기(Median):

```python
from Object.Estimate.RequestObject.GetExposureMiniBidObject import GetExposureMiniBidObject

get_exposure_mini_bid_object = GetExposureMiniBidObject('PC', 'DAY', ['화분', '보험'])

target_bid_estimate = estimate.get_exposure_mini_bid_list('keyword', get_exposure_mini_bid_object)
print(target_bid_estimate[0].cicks)
```

## 예상실적 받아오기(Performance):

```python
from Object.Estimate.RequestObject.GetPerformanceObject import GetPerformanceObject

get_performance_object = GetPerformanceObject('BOTH', False, '보험', [500, 3000, 5000])

target_bid_estimate = estimate.get_performance_list('keyword', get_performance_object)
print(target_bid_estimate[1].clicks)
```

## 예상실적 한번에 많이 받아오기: 
``` 동작 여부 테스트 필요함(NPLA, NPC 제외) ```

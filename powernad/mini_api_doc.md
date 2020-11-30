# 캠페인

## 초기화: 

```
c = Campaign(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```


## 캠페인 리스트 불러오기:

```
c.get_campaign_list()
```

## 아이디로 캠페인 리스트 불러오기 : 

```
c.get_campaign_list_by_ids("cmp-a001-01-000000000171629")
```

## 캠페인 정보 불러오기:

```
c.get_campaign("cmp-a001-01-000000000171629")
```

## 캠페인 생성하기: 

```
ang = CampaignAddObject(client.CUSTOMER_ID, "WEB_SITE", "난니가정말좋아")
c.create_campaign(ang)
```

## 캠페인 업데이트하기: 

```
c.update_campaign(CampaignUpdateObject, "cmp-a001-01-000000000375491", "userLock") 
# userLock, budget, period만 필드에 들어갑니다.
```



# 애드그룹

## 초기화:

```
a = AdGroup(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 제외한 확장 키워드 불러오기:

```
a.get_restricted_keyword(애드그룹고유번호)
```

## 캠페인 아이디를 기반으로 그룹들 불러오기: 

```
a.get_adgroup_list(campaignid = None, baseid = None, record_size = None, selector = None)
```

## 그룹 고유 아이디를 기반으로 그룹리스트 불러오기 : 

```
a.get_adgroup_list_by_ids(그룹고유번호)
```

## 그룹 고유 아이디를 기반으로 그룹 정보 불러오기 : 

```
a.get_adgroup_by_adgroupid(그룹고유번호)
```

## 제외할 확장 키워드를 추가하기:

```
reob = RestrictedKeywordsObject("쁘디성형","에피아테스트2","grp-a001-01-000000002412336")
a.create_restricted_keyword("grp-a001-01-000000002412336", reob)
```


## 애드그룹 생성하기:

```
cad = CreateAdgroupObject('cmp-a001-01-000000000375491', 'ang3', 'bsn-a001-00-000000000268491', 'bsn-a001-00-000000000268491')
a.create_adgroup(cad)
```

## 애드그룹업데이트하기(필드를 통해):

```
inpua = UpdateAdgroupObject(50000)
a.update_adgroup('grp-a001-01-000000002412336',{'fields': 'bidAmt'}, inpua)
```

## 애드그룹업데이트하기(엔타이어):
```동작 여부 테스트 필요```

## 그룹에서 제외 키워드 삭제하기:

```
t = a.delete_group_restricted_keyword('grp-a001-01-000000002412336','rst-a001-00-000000000081865')
```

## 애드그룹 삭제하기 : 

```
a.delete_adgroup('grp-a001-01-000000002548183')
```

# 애드(소재)

## 초기화:

```
ad = Ad(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 소재고유번호를 통해 리스트 받아오기:

```
tt = ad.get_ad_list_by_ids('nad-a001-01-000000009598016')
pprint.pprint(tt[0].nccAdId)
```

## 애드그룹고유번호를 통해 리스트 받아오기:

```
tt = ad.get_ad_list('grp-a001-01-000000002412336')
pprint.pprint(tt[0].ad.pc)
```

## 소재고유번호를 통해 소재정보 받아오기:

```
tt = ad.get_ad('nad-a001-01-000000009598016')
pprint.pprint(tt.nccAdgroupId)
```

## 소재등록하기:

```
filed_obj = AdFieldObject()
filed_obj.description = "이것은 에이피아이 테스트의 일종으로 테스트입니다."
filed_obj.headline = "에이피아이 에드클라우드"
filed_obj.pc = filed_obj.make_pc_easy('http://www.naver.com')
filed_obj.mobile = filed_obj.make_mobile_easy('http://www.naver.com')

add_obj = CreateAdObject(filed_obj, 'grp-a001-01-000000002412336', 'TEXT_45')

return_obj = ad.create_ad(add_obj)
```

## 소재 수정하기:

```
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

```
ad.copy_ad('nad-a001-01-000000009598016', 'grp-a001-01-000000002548182', '0')
```

## 소재 삭제: 

```
ad.delete_ad('nad-a001-01-000000010072402')
```

# 확장소재 

## 초기화:

```
adex = AdExtention(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 캠페인 아이디나 그룹아이디를 기반으로 확장소재 리스트 가져오기:

```
adex = AdExtension(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
ang = adex.get_ad_extensions_list('cmp-a001-01-000000000375491')
```

# 확장소재 아이디를 기반으로 확장소재 리스트 가져오기 :

```
ang2  = adex.get_ad_extensions_list_by_ids('ext-a001-01-000000000503236')

확장소재 아이디를 기반으로 확장소재 가져오기:
wow = adex.get_ad_extensions('ext-a001-01-000000000503236')
pprint.pprint(wow.delFlag)
```

## 확장 소재를 등록하기: 

```
cadex = CreateAdExtensionObject('bsn-a001-00-000000000287001', 'bsn-a001-00-000000000287001', 'cmp-a001-01-000000000375491', 'PHONE', False )
adex.creat_ad_extensions(cadex)
```

## 확장소재 업데이트:

```
upded = UpdateAdExtensionObject('ext-a001-01-000000000503236', None, False)
adex.update_ad_extensions('ext-a001-01-000000000503236', 'userLock', upded)
```

## 확장소재 삭제하기:

```
adex.delete_ad_extensions('ext-a001-01-000000000503236')
```

# 비즈니스채널

## 초기화:

```
bc = BusinessChannel(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 비즈니스 채널 리스트가져오기:

```
test = bc.get_business_channel_list()
print(test[0].businessInfo.site)
```

## 채널 타입을 기준으로 채널 리스트 가져오기:

```
get_business_channel_list_by_type(self, 'PHONE'):
print(test[0].businessInfo.site)
```

## 채널 고유번호를 기준으로 채널 리스트 가져오기:

```
test = bc.get_business_channel_list_by_ids('bsn-a001-00-000000000124029')
print(test[0].businessInfo.site)
```

## 채널 고유번호로 비즈니스 채널 가져오기:

```
test = bc.get_business_channel('bsn-a001-00-000000000124029')
print(test.blackStatus)
```

## 비즈니스 채널 만들기:

```
from Object.BusinessChannel.RequestObject.CreateBusinessChannelObject import CreateBusinessChannelObject

ccc = CreateBusinessChannelObject('http://simpangoooo.net', 'apitest2')
test2 = bc.create_business_channel(ccc)
```

## 비즈채널업데이트:

``` 동작 여부 테스트 필요함 ```

## 비즈채널삭제:

```
bc.delete_business_channel('bsn-a001-00-000000000298203')
```

## ids로 비즈채널(클릭초이스) 삭제:

```
bc.delete_business_channel_by_ids('ids')
```

## request inspect:
``` 지원 예정 ```

# AdKeyword 

## 초기화:

```
adk = AdKeyword(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 키워드 고유번호를 기반으로 키워드 리스트 가져오기:

```
get_adkeyword_list_by_ids(ids)
```

## 라벨 아이디를 기반으로 키워드 리스트 가져오기:

```
get_adkeyword_list_by_labelid(labelid)
```

## 그룹 아이디를 기반으로 키워드 리스트 가져오기:

```
get_adkeyword_list_by_groupid(group id)
```

## 키워드 정보 가져오기:

```
getadk = adk.get_adkeyword('nkw-a001-01-000000458957253')
print(getadk.bidAmt)
```

## 키워드 생성하기:

```
createad = CreateAdKeywordObject("키워드")

adk.create_adkeyword('grp-a001-01-000000002412336', createad)
```

## 키워드 업데이트 하기:

```
upupup = UpdateAdKeywordObject('grp-a001-01-000000002412336', 'nkw-a001-01-000000472996331')
upupup.bidAmt = 3450
upupup.useGroupBidAmt = False

adk.update_adkeyrword('nkw-a001-01-000000472996331', 'bidAmt', upupup)
```

##키워드 삭제하기:

```
adk.delete_adkeyword('nkw-a001-01-000000472996331')
```

## 키워드 한번에 여러개 삭제:

```
adk.delete_adkeyword_many(ids_list):
```

## 관리하고 있는 키워드의 리스트 가져오기:

```
from API.AdKeyword import AdKeyword

adk = AdKeyword(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)

ss = adk.managed_keyword_list('온라인광고')
print(ss[0].managedKeyword.isAdult)

```

# 라벨

## 초기화:

```
lalala = Label(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 라벨 가져오기:

```
test = lalala.get_label_list()

print(test[0].color)
```

## 라벨 업데이트:

```
from Object.Label.RequestObject.UpdateLabelObject import UpdateLabelObject

up = UpdateLabelObject('lbl-a001-00-000000000033511')
up.name = "API TST"

lalala.update_label(up)
```

## 라벨 REF(바로가기) 업데이트:

```
from Object.Label.RequestObject.UpdateLabelRefObject import UpdateLabelRefObject

ref = UpdateLabelRefObject('1109868', 'lbl-a001-00-000000000033513', 'grp-a001-01-000000002601856', 'ADGROUP')
lalala.update_label_ref(ref)
```

# 타겟

## 초기화:

```
from API.Target import Target
tar = Target(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 타겟리스트 가져오기:

```
wow = tar.get_target_list('grp-a001-01-000000002412336')
print(wow[0].nccTargetId)
```

## 타겟리스트 업데이트:

```
tar.update_target(self, targetId, UpdateTargetObject):
```

# IpExclusion

## 초기화

```
from API.IpExclusion import IpExclusion
ip = IpExclusion(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 차단된 아이피 리스트 가져오기:

```
ipex = ip.get_ip_exclusion()
print(ipex[0].filterIp)
```

## 차단할 아이피 추가하기:

```
from Object.IpExclusion.RequestObject.CreateIpExclusionObject import CreateIpExclusionObject

cip = CreateIpExclusion('1.234.56.7')

ip.create_ip_exclusion(cip)
```

## 차단할 아이피 업데이트:

```
from Object.IpExclusion.RequestObject.UpdateIpExclusionObject import UpdateIpExclusionObject

up = UpdateIpExclusionObject('1.222.34.5', '3487550')
up.memo = "change test"

ip.update_ip_exclusion(up)
```

## 차단할 아이피 삭제하기:

```
ip.delete_ip_exclusion('3487550')
```

## 차단할 아이피 리스트로 삭제하기:

```
ip.delete_ip_exclusion_many(id list)
```

# 비즈머니

## 초기화

```
biz = Bizmoney(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 비즈머니 조회:

```
bizm = biz.get_biz_money()
print(bizm.bizmoney)
```

## 비즈머니 사용실적: 

```
biz.get_biz_money_cost('20170301')
```


# ManagedCustomerLinkList:

## 초기화

```
ma = ManagedCustomerLink(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 리스트로 고객리스트 가져오기:

```
ma.get_managed_customer_link_list(타입<선택사항>)
```

# 대용량보고서:

## 초기화

```
stat = StatReport(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)

```

## 대용량보고서목록보기:

```
wow = stat.get_stat_report_list()
print(wow[0].statDt)
```

## 리스트고유번호로 대용량 보고서 목록보기:

```
wow2 = stat.get_stat_report('150381075')
print(wow2.statDt)
```

## 대용량 보고서 생성하기

```
from Object.StatReport.RequestObject.CreateStatReportObject import CreateStatReportObject

ccc = CreateStatReportObject('AD_CONVERSION_DETAIL', '2017-03-10T15:00:00Z')

stat.create_stat_report(ccc)
```

## 대용량 보고서 삭제하기:

```
stat.delete_stat_reports('158389454')
```

## StatReport

### 아이디로 스탯가져오기:

```
fields = '["impCnt","clkCnt","salesAmt"]'
statr = stat.get_stat_by_id('grp-a001-01-000000002412336', fields, '{"since":"2017-02-26","until":"2017-03-04"}', None, None, None)
print(statr.data[0].dateEnd)
```

### 아이디 리스트로 가져오기:

```
fields = '["impCnt","clkCnt","salesAmt"]'
statr = stat.get_stat_by_id('grp-a001-01-000000002412336,grp-a001-01-000000001235166', fields, '{"since":"2017-02-26","until":"2017-03-04"}', None, None, None)
print(statr.data[0].dateEnd)
```

### 스탯타입으로 가져오기(테스트필):

``` 동작 여부 테스트 필요함 ```

# MasterReport(광고정보일괄다운로드):

## 초기화:

```
from API.MasterReport import MasterReport
mreport = MasterReport(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 다운로드 목록 불러오기:

```
m = mreport.get_master_report_list()
print(m[0].managerLoginId)
```

## 아이디로 다운로드 정보 가져오기:

```
m2 = mreport.get_master_report_by_id('F9F0D4813CDB89E7F5907EAE79C7A0B2')
print(m2.registTime)
```

## 다운로드  요청 만들기:

```
from Object.MasterReport.RequestObject.CreateMasterReportObject import CreateMasterReportObject

cm = CreateMasterReportObject('Campaign', '2017-03-12T15:00:00Z')
mreport.create_master_report(cm)
```

## 전부삭제하기:

```
mreport.delete_master_report_all()
```

## 특정아이디로 삭제하기:

```
mreport.delete_master_report_by_id('3BE28582CCC31D199D2C583D191257B5')
```

# 관계있는 키워드 정보들 보기(RelKwdStat):

## 초기화 

```
from API.RelKwdStat import RelKwdStat
rel = RelKwdStat(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 관계있는 키워드 정보들 보기(RelKwdStat)


```
t = rel.get_relkwd_stat_list('bsn-a001-00-000000000124029')
print(t[0].monthlyAveMobileClkCnt)
```

# Estimate

## 초기화

```
from API.Estimate import Estimate

est = Estimate(client.BASE_URL, client.API_KEY, client.SECRET_KEY, client.CUSTOMER_ID)
```

## 순위로 비딩 평균 가져오기:

```
from Object.Estimate.RequestObject.GetAvgPositionBidObject import GetAvgPositionBidObject
from Object.Estimate.sub.KeyAndPositionObject import KeyAndPositionObject

keandp = KeyAndPositionObject('음주운전', 3)
keandp2 = KeyAndPositionObject('보험', 3)
getest = GetAvgPositionBidObject('PC', [keandp, keandp2])

eee = est.get_avg_position_bid_list('keyword', getest)
print(eee[0].bid)
```

## 키워드로 평균 비딩 가져오기:

```
from Object.Estimate.RequestObject.GetMedianBidObject import GetMedianBidObject

medi = GetMedianBidObject('PC', 'DAY', ['화분', '보험'])

e = est.get_median_bid_list('keyword', medi)
print(e[0].bid)
```

## 노출 최솟값 받아오기:

```
from Object.Estimate.RequestObject.GetExposureMiniBidObject import GetExposureMiniBidObject
ex = GetExposureMiniBidObject('PC', 'DAY', ['화분', '보험'])

e = est.get_exposure_mini_bid_list('keyword', ex)
print(e[0].bid)
```

## 예상실적 받아오기:

```
from Object.Estimate.RequestObject.GetExposureMiniBidObject import GetExposureMiniBidObject
ex = GetExposureMiniBidObject('PC', 'DAY', ['화분', '보험'])

from Object.Estimate.RequestObject.GetPerformanceObject import GetPerformanceObject
per = GetPerformanceObject('BOTH', False, '보험', [500, 3000, 5000])

e = est.get_performance_list('keyword', per)
print(e[1].clicks)
```

## 예상실적 한번에 많이 받아오기: 
``` 동작 여부 테스트 필요함(NPLA, NPC 제외) ```

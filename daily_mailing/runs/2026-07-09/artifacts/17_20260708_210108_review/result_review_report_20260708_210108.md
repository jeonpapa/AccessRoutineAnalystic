# MA Daily Monitoring 결과 검토보고서

- 작성 시각: 2026-07-09 11:21 KST
- 대상 run_id: `20260708_210108`
- 생성 시각: 2026-07-08T21:01:08.234427+00:00
- 모니터링 범위: 이전 24시간 / lookback 24h
- Dashboard subscription: 17 / owner: max@msd.com
- 수신자 후보: marketaccess@msd.com

## 1. 종합 판정

**판정: 조건부 보류(quality-gated draft 유지).** 기사 선별과 writer draft 생성은 완료되었지만, 공식 출처 대조 전 live send 또는 최종 게시로 전환하기에는 부족합니다.

핵심 이유:
- Top signal 5건은 모두 MA relevance 4~5 수준으로 주제 적합성은 높습니다.
- 다만 selected 5건 전부 `publisher_verified_required` 및 `official_cross_check_required` 성격을 포함합니다.
- 품질 경고로 `duplicate_implication_boilerplate`가 감지되어, Market Access implication 문구가 기사별로 충분히 분화되지 않았습니다.
- 따라서 현재 산출물은 **검토용 preview/draft**로는 사용 가능하지만, **최종 메일 발송/live dashboard publish 전에는 source verification + editorial de-duplication이 필요**합니다.

## 2. 산출물/품질 지표

| 항목 | 값 |
|---|---|
| 발견 기사 | 378 |
| 최근 기사 | 184 |
| 선별 기사 | 5 |
| review board 기사 | 184 |
| quality status | `quality_gated_draft` |
| sendable | `False` |
| live_send_allowed | `False` |
| warnings | duplicate_implication_boilerplate, official_cross_check_required |

Review board 상태 분포:
- `needs_review`: 175
- `ready_for_writer`: 9

주요 quality flag 분포:
- `publisher_verified_required`: 184
- `unregistered_source_requires_review`: 111
- `official_cross_check_required`: 66
- `keytruda_direct_source_verification_promoted`: 9
- `policy_pricing_tracker`: 7
- `low_value_msd_mention`: 2
- `corporate_report_not_live_ma_signal`: 2

## 3. Top Signal 검토

### 1. 국산 CAR-T 림카토 암질심 통과…퍼제타 보조요법 '재논의'

- 출처: 메디칼타임즈 / https://www.medicaltimes.com/Main/News/NewsView.html?ID=1169668&ref=naverpc
- 발행 시각: 2026-07-08T18:46:00+09:00
- MA relevance: 5/5 · priority: High · score: 11.1
- Review status: `needs_review`
- Matched keywords: 급여 등재, 약평위, 암질심, 약가협상, 급여, 약제급여평가위원회
- Quality flags: publisher_verified_required, official_cross_check_required
- Caveat: Publisher page is identified by registry; official HIRA/MOHW/MFDS cross-check required before send.

### 2. 국산 첫 CAR-T '림카토' 암질심 통과…급여 등재 '청신호'

- 출처: 메디파나뉴스 / https://www.medipana.com/news/articleView.html?idxno=414302
- 발행 시각: 2026-07-08T18:42:00+09:00
- MA relevance: 5/5 · priority: High · score: 11.05
- Review status: `needs_review`
- Matched keywords: 급여 등재, 암질심, 약가협상, 급여, 약제급여평가위원회
- Quality flags: publisher_verified_required, official_cross_check_required
- Caveat: Publisher page is identified by registry; official HIRA/MOHW/MFDS cross-check required before send.

### 3. 림카토 암질심 재도전 성공...퍼제타주 급여확대 재논의

- 출처: 데일리팜 / https://new.dailypharm.com/user/news/340272?REFERER=NP
- 발행 시각: 2026-07-08T18:36:00+09:00
- MA relevance: 5/5 · priority: High · score: 8.75
- Review status: `needs_review`
- Matched keywords: 급여 등재, 암질심, 급여
- Quality flags: publisher_verified_required, official_cross_check_required
- Caveat: Publisher page is identified by registry; official HIRA/MOHW/MFDS cross-check required before send.

### 4. 림카토주 다시 암질심으로…환우회 "급여기준 신속히 마련"

- 출처: 청년의사 / http://www.docdocdoc.co.kr/news/articleView.html?idxno=3040769
- 발행 시각: 2026-07-08T11:26:00+09:00
- MA relevance: 5/5 · priority: High · score: 8.45
- Review status: `needs_review`
- Matched keywords: 암질심, 급여, 심평원
- Quality flags: publisher_verified_required, official_cross_check_required
- Caveat: Publisher page is identified by registry; official HIRA/MOHW/MFDS cross-check required before send.

### 5. 로슈, 유방암 치료제 개발 오츠카 자회사와 제휴

- 출처: 약업신문 / https://www.yakup.com/news/index.html?mode=view&cat=16&nid=329523
- 발행 시각: 2026-07-08T06:02:00+09:00
- MA relevance: 4/5 · priority: High · score: 8.25
- Review status: `ready_for_writer`
- Matched keywords: 키트루다
- Quality flags: keytruda_direct_source_verification_promoted, publisher_verified_required, official_cross_check_required
- Caveat: Publisher page is identified by registry; official HIRA/MOHW/MFDS cross-check required before send.

## 4. Dashboard/Mail 운영 판단

### Dashboard
- run artifact, HTML draft, markdown draft, review board는 이미 daily-monitoring run 폴더에 생성되어 있습니다.
- admin operational board DB에는 run/article 이력이 적재되어 dashboard에서 누적 이력으로 조회 가능한 상태입니다.
- 본 검토보고서는 같은 run 폴더에 별도 산출물로 저장하고 run JSON/review board JSON에 `result_review_report_*_path` 메타데이터를 추가했습니다.

### Mail
- 메일 본문 후보는 HTML draft 기준으로 준비되어 있습니다.
- 현재 Gmail OAuth token은 draft 생성에 필요한 `gmail.compose`/`gmail.modify` scope가 없어 Gmail Draft 업로드는 차단됩니다.
- live send는 quality gate 및 explicit approval 전에는 실행하지 않는 것이 맞습니다.

## 5. 후속 액션

1. HIRA/MOHW/MFDS 또는 해당 위원회 공식 발표/자료와 림카토·퍼제타 급여기준 사실관계를 교차 확인합니다.
2. 림카토 관련 중복 기사 4건은 하나의 핵심 신호로 통합하고, 퍼제타/MSD 영향 문단을 별도 보강합니다.
3. 로슈/Otsuka 제휴 건은 키트루다 직접 영향이 약하므로 “watchlist” 또는 competitive context로 격하 여부를 결정합니다.
4. Gmail Draft 운영을 위해 `gmail.compose` scope 재인증 후 draft 생성만 수행하고, live send는 별도 승인 gate를 둡니다.

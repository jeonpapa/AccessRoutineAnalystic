# PR-NEW-AMJ-004 — 저노출 oncology product/regimen source registry

| 항목 | 값 |
|---|---|
| status | CANDIDATE |
| committee | AMJILSIM |
| current_weight | 0.55 |
| last_updated | 2026-09-04 |
| seed_case | 2026-08-19 7차 암질심 브렌랩주·보라니고정·브루킨사 FN |

## 룰 가설

암질심 안건 중 일부는 환자단체·국회·전문매체 high-noise 신호 없이도 공식 결과표에 등장한다. 특히 국내 도입 신약, 희귀 고형암/혈액암 target therapy, 기존 급여기준 확대, 같은 품목 내 병용요법별 split decision은 D-2 매체 중심 예측으로 누락될 수 있다.

## 탐색 대상

- 다발골수종 ADC 및 BCMA/혈액암 target therapy: 브렌랩, 벨란타맙, belantamab, BCMA, 다발골수종 병용요법.
- 다발골수종 T-cell engager/BCMA-GPRC5D-FcRH5 axis: 텍베일리, 테클리스타맙, teclistamab, 3차 이상 재발/불응성 다발골수종.
- late-line solid tumor targeted therapy: 프루자클라, 프루퀸티닙, fruquintinib, 전이성 결장직장암 후속치료, 항-VEGF/항-EGFR 이후.
- 저등급 glioma/분자표적 치료: 보라니고, 보라시데닙, vorasidenib, IDH1, IDH2, 성상세포종, 희돌기교종.
- CLL/SLL·BTK inhibitor: 브루킨사, 자누브루티닙, zanubrutinib, CLL, SLL, 1차 단독요법.
- 희귀 암종 regimen 확대: 침샘도관암, salivary duct carcinoma, HER2, Docetaxel, Trastuzumab.
- 표현: 결정신청, 급여기준 확대, 급여기준 신설, 병용요법, 단독요법, 허가 후 급여, 국내 도입.

## 적용 방식

1. D-30~D-7에 MFDS 허가/국내 도입 기사, 회사 보도자료, 학회 guideline·허가사항 변경, 전문매체 약제 소개를 product registry로 수집한다.
2. D-7~D-2에는 public pressure가 큰 품목과 별도로, registry 품목을 `LOW/MEDIUM watch`로 유지한다.
3. 사전 상정 신호가 없으면 `predicted_on_agenda=YES`로 올리지 않되, D+1 FN 분석 때 product/regimen registry coverage 여부를 점검한다.
4. 같은 품목 내 복수 regimen 또는 line이 존재하면 baseline 후보를 product 하나로 압축하지 말고 regimen row로 분리한다.

## 검증 사례

| 회의 | 누락 품목/regimen | 실제 결과 | 학습 |
|---|---|---|---|
| 2026-08-19 7차 암질심 | 브렌랩주 보르테조밉+덱사메타손 | 급여기준 설정 | 다발골수종 ADC 및 병용 파트너별 registry 필요 |
| 2026-08-19 7차 암질심 | 브렌랩주 포말리도마이드+덱사메타손 | 급여기준 미설정 | 같은 품목 내 split decision 가능성 |
| 2026-08-19 7차 암질심 | 보라니고정 | 급여기준 설정 | 희귀 glioma/IDH 변이 product registry 필요 |
| 2026-08-19 7차 암질심 | 브루킨사캡슐 CLL/SLL 1차 | 급여기준 설정 | 혈액암 기존품목 급여기준 확대 registry 필요 |
| 2026-09-03 9차 약평위 | 텍베일리주 | 급여의 적정성이 있음 | 혈액암 late-line T-cell engager product registry 필요 |
| 2026-09-03 9차 약평위 | 프루자클라캡슐 | 급여의 적정성이 있음 | 전이성 결장직장암 후속치료 targeted therapy registry 필요 |

## 2026-09-04 보정

- 9차 약평위에서 텍베일리와 프루자클라가 D-2 product-level 후보에서 누락됐다.
- current_weight 0.50 → 0.55. 다발골수종 T-cell engager와 late-line CRC targeted therapy를 D-30~D-7 registry bucket에 추가한다.
- 약평위 결정신청 품목에도 이 룰을 보조 적용하되, 공식 안건 비공개 특성상 사전 YES 승격은 product-level 신청/경평소위/회사 보도 확인 후에만 허용한다.

## 적용 주의

- 이 룰은 product coverage를 넓히기 위한 후보 룰이다. registry에 들어왔다는 이유만으로 agenda YES를 주지 않는다.
- 공식 안건 비공개 특성상 false positive를 줄이려면 confidence는 MEDIUM 이하에서 시작한다.
- Leadership PDF에는 이 룰명이나 FN/FP 언어를 넣지 않는다. D+1 audit에서만 학습한다.

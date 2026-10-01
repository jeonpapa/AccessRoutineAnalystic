# PR-NEW-AMJ-010 — 저노출 혈액암 1차·세포치료 registry

| 항목 | 값 |
|---|---|
| status | CANDIDATE |
| committee | AMJILSIM |
| current_weight | 0.55 |
| last_updated | 2026-10-01 |
| seed_case | 2026-09-30 8차 암질심: 반플리타·민쥬비·카빅티 |

## 룰 가설

암질심은 회의 직전 공개 신호가 약한 혈액암 품목·급여기준 확대·세포치료 안건도 포함할 수 있다. AML/CML 1차 치료, 림프종 적응증 split, CAR-T/BCMA 치료는 일반적인 media-pressure 신호와 별도로 registry에서 추적해야 한다.

## 적용 방식

1. D-30~D-7에 국내 허가, 회사 신청·보도, 전문학회·가이드라인, 기존 급여범위와 치료라인을 product × indication × line × regimen row로 수집한다.
2. D-7~D-2에는 `LOW/MEDIUM` watch로 유지하며, body-verified 회의 일정·회사 신청·공식 자료 중 하나가 추가되기 전에는 agenda YES로 승격하지 않는다.
3. D+1에는 실제 결과표를 신규/확대, 설정/미설정, 적응증 split으로 분해해 registry coverage를 보정한다.

## Seed cases

| 회의 | 품목/단위 | 실제 결과 | 학습 |
|---|---|---|---|
| 2026-09-30 8차 암질심 | 반플리타 AML 신규 1차 | 급여기준 설정 | 저노출 AML 1차 registry |
| 2026-09-30 8차 암질심 | 민쥬비 소포성 림프종 | 급여기준 설정 | 혈액암 regimen row |
| 2026-09-30 8차 암질심 | 민쥬비 DLBCL | 급여기준 미설정 | 동일 제품 적응증 split |
| 2026-09-30 8차 암질심 | 카빅티 다발골수종 | 급여기준 미설정 | CAR-T/BCMA registry |

## 적용 주의

- registry 등재만으로 agenda YES를 주지 않는다.
- 적응증·병용·치료라인을 제품 하나로 압축하지 않는다.
- leadership PDF에는 이 룰명, FN/FP, confidence 또는 weight를 넣지 않는다.

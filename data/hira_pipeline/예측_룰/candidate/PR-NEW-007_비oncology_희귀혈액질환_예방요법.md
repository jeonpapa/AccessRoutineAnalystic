---
rule_id: PR-NEW-007
name: "비oncology 희귀·혈액질환 장기 예방요법 결정신청 → 약평위 단일 안건 가능성"
category: 안건_예측
established_at: 2026-08-07
last_calibrated: 2026-08-07
evidence_count: 1
weight: 0.58
tp_count: 0
fn_count: 1
fp_count: 0
condition: |
  혈우병, 중증근무력증, 신경·희귀·소아질환 등 비oncology 희귀질환에서 장기 예방요법 또는 maintenance therapy 성격의
  신약이 결정신청 단계에 있고, MFDS 허가·회사 보도자료·환자단체 급여요구·전문지 경평소위/급여신청 보도 중 하나 이상으로
  product-level 후보명이 확인되는 경우 약평위 단일 안건으로 상정될 수 있다.
prediction: "비oncology 희귀질환 장기 예방요법 신약은 항암 전환 신호가 없어도 해당 차수 약평위 결정신청 안건 가능"
status: CANDIDATE
승격_조건: "product-level D-30~D-7 후보 식별 후 TP 2건 또는 하임파지 유사 사례 2건 추가 시 ACTIVE 검토"
관련_룰: "PR-NEW-006 — 비oncology 결정신청 scope 확장"
---

# PR-NEW-007 — 비oncology 희귀·혈액질환 예방요법 결정신청 룰

## 창출 배경

2026-08-06 제8차 약평위는 공식 결과표에 **하임파지프리필드펜주 150mg/mL(마스타시맙, 한국화이자제약)** 1품목만 공개했다. D-2 baseline은 사이람자·엘라히어·버제니오 등 암질심→약평위 transition 후보를 HIGH로 두었고, 비oncology·희귀 결정신청은 category watch로만 남겼다. 결과적으로 하임파지라는 product-level 후보를 사전에 식별하지 못한 FN이 발생했다.

## 패턴 정의

비oncology 희귀질환 신약은 암질심을 거치지 않으며, 항암제 대비 전문지 coverage가 약하거나 특정 학회·환자단체·회사 보도자료에 흩어져 있을 수 있다. 특히 혈우병 예방요법처럼 장기 투여·출혈 예방·소아 포함·기존 치료 대비 투여부담 감소를 가치로 제시하는 제품은 단일 품목 약평위 안건으로 공개될 수 있다.

## 사전 탐색 키워드

```text
D-30~D-7 검색 bucket:
- 혈우병 신약 급여 / 혈우병 예방요법 급여 / 마스타시맙 급여 / 하임파지 약평위
- 희귀질환 신약 급여 적정성 / 소아 희귀질환 약평위 / 예방요법 결정신청
- 중증근무력증 신약 급여 / 신경희귀질환 급여 / 장기 예방요법 약가
- 회사명 + 제품명 + 급여신청 / 경평소위 / 평가금액 / 약평위
```

## Scoring guard

| 신호 | score 처리 |
|---|---|
| product명 + 회사 + 급여신청/경평소위 보도 확인 | MEDIUM 이상 |
| product명 없이 질환군·환자단체 요구만 존재 | WATCH 유지 |
| MFDS 허가만 있고 급여신청 신호 없음 | WATCH, 차기 차수 자동 YES 금지 |
| HIRA 공식 결과표에 사전 미식별 product 등장 | FN으로 기록하고 source registry 보강 |

## 2026-08-07 보정

- 하임파지 FN으로 rule 생성. 단, 이번은 사후 생성이므로 tp_count는 0, fn_count는 1로 시작한다.
- PR-NEW-006은 경평소위 보도 기반 비oncology 룰이고, PR-NEW-007은 희귀·혈액질환 예방요법 product registry 보강 룰로 분리한다.
- 다음 약평위 D-30~D-7 routine에서 항암 후보 HIGH보다 비oncology product-level source discovery를 병렬 수행한다.

# HIRA 보고서 자가 개선 룰 — Senior Market Access Leadership Quality

> **목적**: 약평위·암질심 D-2 사전 보고서, D+1 결과 리뷰, 월간 트렌드 보고서가 매 회차마다 전문 시니어 Market Access 리드 관점으로 개선되도록 강제하는 품질 룰이다.  
> **적용 범위**: Hermes, Claude, Codex 등 모든 보고서 작성 에이전트.  
> **운영 원칙**: `예측_룰/`은 상정·결과 예측 정확도를 학습하고, 본 문서는 리더십 보고서의 톤·구조·가독성·해석 품질을 학습한다.

## 1. 기본 레퍼런스 우선순위

보고서 작성 전 반드시 아래 순서로 레퍼런스를 확인한다.

1. **HIRA 공식 보도자료 / 세부 고시 / 공식 일정** — 회의명, 차수, 품목, 성분, 회사, 효능·효과, 심의결과 문구의 단독 권위.
2. **`agents/ingest/committee_results.json`** — dashboard·manifest와 연결되는 curated reimbursement source.
3. **`data/hira_pipeline/예측_룰/`** — 상정 후보, 신호강도, 과거 TP/FP/FN, 후보 룰·활성 룰.
4. **최근 accepted report markdown/PDF** — 특히 아래 skeleton과 톤을 기본 형식으로 삼는다.
   - `data/hira_pipeline/보고서/D+1_결과_리뷰/2026-07-03_yakpyungwi-7_d_plus_1.md`
   - `data/hira_pipeline/보고서/D+1_결과_리뷰/2026-07-09_amjilsim-6_d_plus_1.md`
   - `data/hira_pipeline/보고서/D-2_사전_예측/2026-06-30_yakpyungwi-7_d_minus_2.md`
   - `data/hira_pipeline/보고서/D-2_사전_예측/2026-07-06_amjilsim-6_d_minus_2.md`
5. **전문지·매체 기사** — 공식 결과가 말하지 않는 사유·시장 반응·회사 동향의 보조 근거. 단, 공식 사실을 대체하지 않는다.

## 2. 리더십 보고서 고정 skeleton

### D+1 결과 리뷰

```text
# [YYYY년 제N차 약평위/암질심] D+1 결과 리뷰
## Leadership Brief | YYYY.MM.DD

메타데이터 표: 회의 / 회의일 / 보고 대상 / 공식 확인 / 핵심 결과

## 1. Executive Snapshot
- 한 줄 결론
- 3대 leadership implication 표

## 2. 공식 심의 결과: compact result table
- 공식 품목·성분·회사·대상/효능효과·심의결과 표

## 3. 시장·정책 시사점
## 4. MSD 영향: direct issue 여부 + read-through
## 5. Next watchlist
## 6. Leadership actions
## 7. 출처 및 해석 범위
```

### D-2 사전 예측

```text
# [YYYY년 제N차 약평위/암질심] D-2 사전 예측 보고서
## Leadership Brief | YYYY.MM.DD [위원회] 사전 점검

메타데이터 표: 회의 / 회의 예정일 / 보고 대상 / 공식 확인 / 핵심 질문

## 1. Executive Snapshot
- 한 줄 결론
- 핵심 메시지 / Leadership Implication 표

## 2. 직전 차수 기준선
## 3. Leadership Watchlist: High / Medium / Low 후보
## 4. MSD 관점의 주요 영향
## 5. 결과 발표 후 확인사항
## 6. Source & Caveat
```

암질심과 약평위는 위원회 성격만 반영하고 **section skeleton은 동일 수준으로 유지**한다. 암질심 보고서를 긴 예측/audit 서술로 변형하거나 약평위보다 허술한 요약으로 축소하지 않는다.

## 3. 톤·문체 룰

- **시니어 Market Access 리드 관점**: 단순 사실 나열이 아니라 “그래서 leadership이 무엇을 봐야 하는가”를 먼저 말한다.
- **공식 용어**: `급여 적정성 있음`, `평가금액 이하 수용 시 적정`, `급여기준 설정`, `급여기준 미설정`, `재심의/재논의`를 사용한다. `통과/미통과`는 내부 shorthand 또는 인용이 아니면 leadership prose에서 피한다.
- **한 문단 한 메시지**: 각 문단 첫 문장은 핵심 판단, 뒤 문장은 근거·의미·후속 확인으로 구성한다.
- **MSD relevance 분리**: 직접 품목 영향과 간접 read-through를 분리한다. 직접 영향이 없으면 “없다”고 명확히 쓰되, 항암 sequencing, biomarker segmentation, BIA, 가격수용 gate, RSA/재정관리 측면의 read-through를 제시한다.
- **불확실성 표현**: “모름/실패”가 아니라 “공개 신호 부재”, “공식 고시 확인 필요”, “약가협상·건정심 이후 확정”처럼 비즈니스 리스크와 다음 확인 포인트로 표현한다.

## 4. 가독성·테이블 룰

- Executive Snapshot은 항상 보고서 앞쪽에 두고, 한 줄 결론은 2문장 이하로 제한한다.
- 긴 약물 설명은 표로 압축하고, 본문은 implication 중심으로 쓴다.
- 표는 5개 컬럼 이하를 기본으로 하며, 셀 안 문장은 1~2개로 제한한다.
- 보고서마다 최소 3개 이상의 리더십 액션 또는 후속 확인사항을 포함한다.
- PDF 렌더링 시 Noto Sans KR Regular/SemiBold/Bold를 우선 사용하고, 제목·섹션·표 헤더의 굵기 계층이 눈에 보여야 한다.

## 5. 보고서와 audit 분리 룰

Leadership PDF/markdown에는 아래 항목을 넣지 않는다. 필요 시 별도 operational note 또는 `예측_룰/audit_log.md`에만 둔다.

- `brdBltNo`, crawler mechanics, raw URL hash, manifest path, cron/job ID
- TP/FP/FN, rule weight, precision/recall/F1, candidate promotion/retirement
- repo path, Python module name, render script, dashboard import mechanics
- `프리뷰`, `예측 보정`, `hit/miss/surprise` 등 내부 캘리브레이션 언어

예외: Joseph에게 운영상 보고해야 하는 경우 Slack operational note에서만 간략히 알리고, leadership PDF에는 넣지 않는다.

## 6. 자가 평가 gate — 8점 미만이면 재작성

보고서 작성 후 아래 10개 항목을 각 1~10점으로 자체 평가한다. 하나라도 8점 미만이면 해당 부분을 재작성한 뒤 PDF/manifest를 재생성한다.

| 평가 항목 | 8점 기준 |
|---|---|
| 공식 사실 정확성 | HIRA 공식 문구·차수·품목·회사·효능효과가 오류 없이 반영됨 |
| Executive clarity | 첫 30초 안에 핵심 결론·의사결정 포인트가 보임 |
| Senior MA insight | payer/reimbursement/가격·재정·환자군·협상 함의가 구체적임 |
| MSD relevance | 직접 영향과 read-through가 분리되고 실무적으로 유용함 |
| 구조/템플릿 준수 | accepted report skeleton과 section parity 유지 |
| 테이블 가독성 | 핵심 정보가 compact table로 정리되고 셀 과밀도가 낮음 |
| 용어 품질 | 공식 용어 사용, `통과/미통과` 남용 없음 |
| Audit 분리 | crawler/hash/rule/cron 등 내부 메타가 leadership report에 없음 |
| Source & Caveat | 공식 출처와 해석 범위·미확정 사항이 명확함 |
| PDF 시각 품질 | Noto Sans KR, 굵기 hierarchy, page density, footer가 양호함 |

## 7. 회차별 개선 기록 방식

- 품질 이슈가 발생하면 본 문서에 직접 장황하게 누적하지 말고, `data/hira_pipeline/보고서/quality_audit/` 아래에 회차별 `YYYY-MM-DD_[committee]_[d2|dplus]_quality_audit.md`를 생성한다.
- audit에는 `문제`, `참조한 accepted report`, `수정 원칙`, `재발방지 룰`, `최종 점수`만 남긴다.
- 재발방지 룰이 범용화되면 본 문서의 해당 section에 짧게 반영한다.

## 8. 금지되는 낮은 품질 패턴

- 공식 결과표를 길게 복붙하고 leadership implication이 없는 보고서.
- 후보 예측 근거만 길고 MSD/업무 영향이 빈약한 보고서.
- 암질심을 약평위보다 덜 중요한 보고서처럼 짧고 느슨하게 쓰는 방식.
- 내부 예측룰·크롤러·manifest 설명이 리더십 문서 본문에 섞이는 방식.
- “가능성이 있다”만 반복하고 가격수용, BIA, RSA, biomarker, line of therapy, 고시 확인 등 실무 후속 포인트가 없는 문장.

## 9. 운영 체크리스트

보고서 발행 전 최소 확인:

1. 최신 HIRA 공식 보도자료 또는 회의 일정 확인.
2. `committee_results.json`와 보고서 내용의 품목·결과 불일치 여부 확인.
3. `예측_룰/audit_log.md` 및 active/candidate 룰에서 후보·신호 변화 확인.
4. 최근 accepted report skeleton과 section parity 비교.
5. 자가 평가 10개 항목 모두 8점 이상.
6. PDF 텍스트 추출로 필수 키워드·금지어 확인.
7. manifest/hash 재생성 및 artifact path/size 확인.

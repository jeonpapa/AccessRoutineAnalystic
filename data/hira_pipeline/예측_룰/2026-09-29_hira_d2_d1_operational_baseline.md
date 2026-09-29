# 2026-09-29 HIRA D-2/D-1 prediction operational baseline

- 실행 기준: 2026-09-29 15:30 KST.
- 활성 대상: 8차 암질심(2026-09-30, D-1 보완 발행) 및 10차 약평위(2026-10-01, D-2 발행).
- 공식 HIRA 확인:
  - 최신 list helper 성공: page 1 brdBltNo 11924~11915는 추석·지역본부 일반 보도자료.
  - 현재 페이지 `find`는 약평위·암질심 심의결과 0건.
  - 최신 relevant official baseline: 11898(2026-09-03 제9차 약평위), 11882(2026-08-19 제7차 암질심). 두 detail body에서 회차·품목·공식 결과 문구 확인.
  - 직접 pageIndex=1~7 raw pagination은 timeout 반복. 해당 timeout은 신규 없음의 증거로 사용하지 않고, 성공한 list/detail 결과와 저장된 공식 baseline을 authoritative same-run evidence로 유지.
- 사전 후보 baseline:
  - 8차 암질심: 셈블릭스는 복수 전문매체의 9/30 상정 예정 신호로 High 관찰. 임델트라는 반복 미상정·public-pressure 한계로 Medium Watch. 키트루다는 적응증 미확정 신호로 Medium Watch. 퍼제타·티루캡은 보완자료/재신청 확인 전 Watch.
  - 10차 약평위: 사이람자·엘라히어·버제니오는 9차까지 반복 미상정되어 High 승격 금지, Watch 유지. 비항암 희귀·자가면역 및 late-line oncology와 기존 급여범위 확대를 병렬 탐색.
- D+1 baseline fields: actual_on_agenda, official result wording, indication/line/biomarker split, company, price-conditional vs unconditional result, and subsequent reimbursement action.
- 산출물: `2026-09-29_amjilsim-8_d_minus_1.md/.pdf`, `2026-09-29_yakpyungwi-10_d_minus_2.md/.pdf`.
- 리더십 문서 제외: internal rule IDs, confidence, TP/FP/FN, precision/recall/F1, brdBltNo, repository/manifest/hash/cron mechanics.

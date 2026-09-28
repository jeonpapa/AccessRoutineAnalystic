# 2026-09-28 제8차 암질심 D-2 operational baseline

- 실행 기준: 2026-09-28 15:31 KST, 회의일 2026-09-30, D-2 활성.
- 캘린더: 8차 암질심 2026-09-30; 10차 약평위 2026-10-01. 이번 발행 대상은 8차 암질심.
- 공식 HIRA 확인:
  - 최신 list helper 성공: HIRA 게시판 page 1 최신 brdBltNo 11924~11915는 추석·지역본부 일반 보도자료. `find`의 암질심 심의결과 검색은 0건.
  - 공식 최신 relevant baseline detail: brdBltNo=11882, 2026년 제7차 중증(암)질환심의위원회 심의결과 공개. Detail URL: https://www.hira.or.kr/bbsDummy.do?pgmid=HIRAA020041000100&brdScnBltNo=4&brdBltNo=11882&pageIndex=1&pageIndex2=1
  - detail body에서 보라니고·브루킨사 및 설정/미설정 문구 확인. 브렌렙은 split-line extraction으로 keyword count 0이지만 본문 archive/공식 상세 snippet에 병용요법별 설정·미설정이 명시됨.
  - raw direct pagination page 1~7은 HIRA 응답 timeout이 반복되어 helper 성공 list/detail evidence를 authoritative same-run official baseline으로 유지. Timeout은 신규 없음의 증거로 취급하지 않음.
- 사전 신호:
  - 셈블릭스(애시미닙) CML 1차요법: dailypharm 342797 및 monews 414127, 2026-09-30 8차 암질심 상정 예정 신호. ASC4FIRST MMR 48주 67.7%, 144주 77.1% vs 비교군 53.4%가 audit에 기록됨.
  - 임델트라(탈라타맙): 5~7차 반복 미상정 baseline. public pressure 단독으로 상정 HIGH 승격하지 않고 WATCH 유지.
- private prediction baseline:
  - 셈블릭스: predicted_on_agenda=YES, confidence=HIGH, evidence=복수 body-verified media schedule signal + existing 3차 급여/1차 확대 context. D+1은 실제 상정 및 급여기준 문구, 1차 대상군/전환조건/재정관리 확인.
  - 임델트라: predicted_on_agenda=WATCH, confidence=LOW-MEDIUM, rule context=public-pressure limitation / repeated non-agenda FP. 회사 재신청·보완자료·구체 차수 신호 없이는 승격 금지.
  - 비공개 신규·확대 안건: predicted_on_agenda=UNKNOWN, confidence=LOW; D+1 전체 결과표에서 전수 확인.
- 산출물: `data/hira_pipeline/보고서/D-2_사전_예측/2026-09-28_amjilsim-8_d_minus_2.md` 및 PDF.
- 리더십 PDF 제외 항목: rule_id, confidence, precision/recall/F1, hit/miss/surprise, brdBltNo, repo/manifest/hash/cron mechanics.

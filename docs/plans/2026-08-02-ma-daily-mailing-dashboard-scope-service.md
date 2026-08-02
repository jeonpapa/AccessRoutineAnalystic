# MA Daily Mailing Dashboard Scope Service Implementation Plan

> **For Hermes:** continue from the existing dashboard-scope bus and 06:00 KST cron job; do not rebuild the service from scratch.

**Goal:** MA AI Dashboard에서 관심 영역·키워드·미디어·수신자를 선택하면 Hermes가 매일 06:00 KST에 이전 24시간 주요 뉴스와 Market Access insight를 Gmail draft/live-send gate로 생성합니다.

**Architecture:** Dashboard subscription CRUD writes deterministic `daily_mailing/scopes/*.json` snapshots and `scopes_index.json`. Hermes cron job `MA Daily Mailing — dashboard scope bus 06:00 KST` runs `/opt/data/scripts/ma_daily_mailing_runner.py`, mirrors scope JSON into `/opt/data/daily-monitoring`, generates draft/review artifacts, creates Gmail drafts when OAuth scope allows, and writes audited run bundles under `daily_mailing/runs/<date>/`.

**Current service state:**
- Cron job: `735dc85cdb73`, schedule `0 21 * * *` = 06:00 KST, `script=ma_daily_mailing_runner.py`, `no_agent=true`.
- Active scopes: `14`–`19` under `daily_mailing/scopes/`.
- Writer/reviewer pipeline exists in `/opt/data/daily-monitoring/agents/daily_mailing/`.
- Forwarded monitoring emails can be consumed through `forwarded_input_paths`; BioSpectator is currently calibration/style reference only, not live source promotion.

---

## Task 1: Make dashboard CRUD export scheduler-facing scope JSON

**Objective:** Each subscription create/update/delete must keep `daily_mailing/scopes/*.json` and `scopes_index.json` in sync.

**Files:**
- Modify: `api/server.py`

**Implementation:**
- Add `_MAIL_SCOPE_DIR` and helper functions:
  - `_mail_scope_index_payload()`
  - `_write_mail_scope_index()`
  - `_mail_scope_from_item()`
  - `_write_mail_scope_from_item()`
  - `_delete_mail_scope()`
- Preserve advanced operator fields in existing JSON: `companies`, `brands`, `aliases`, `disease_areas`, `policy_topics`, `custom_sources`, `forwarded_input_paths`, `personas`, `lookback_hours`, `delivery_mode`, and `test_request`.
- On create/update, return `{item, scope}`.
- On delete, remove the corresponding scope file and rewrite the index.

**Verification:**
```bash
python3 -m py_compile api/server.py
```

---

## Task 2: Add explicit Scope JSON control in dashboard UI

**Objective:** Saved subscription cards should let an operator manually sync/export the exact Hermes scope JSON.

**Files:**
- Modify: `data/dashboard_v2/src/api/mailSubscriptions.ts`
- Modify: `data/dashboard_v2/src/pages/daily-mailing/page.tsx`

**Implementation:**
- Add `DashboardMailScope` and `MailScopeResponse` types.
- Add `exportMailSubscriptionScope(id)` API helper calling `GET /api/mail-subscriptions/<id>/scope`.
- Add a `Scope JSON` button on saved subscription cards.
- Change new subscription defaults to 06:00 and Joseph’s approved recipient email.

**Verification:**
```bash
cd data/dashboard_v2
npm run build
```

Known environment pitfall: if Vite/Rolldown optional native bindings are missing, run `npm install --no-audit --no-fund` locally and rebuild, but do not commit incidental `node_modules`, `out/`, or lockfile churn unless intentionally updating dependencies.

---

## Task 3: Forwarded email intake operating rule

**Objective:** Use forwarded monitoring emails as private source-intake seeds without leaking raw email text or copying newsletter wording.

**Implementation contract:**
- Archive forwarded emails as private JSON files, not public repo text.
- Add file paths to scope JSON `forwarded_input_paths`.
- `daily-monitoring` loads them through `load_forwarded_input_items(...)` and promotes only after publisher-body extraction.
- BioSpectator/newsletters stay as calibration/style references unless Joseph explicitly changes the policy.

**Quality gate:** recipient-facing email must not expose internal review flags, private paths, raw forwarded content, or generic MA boilerplate.

---

## Task 4: Delivery mode rollout

**Objective:** Keep service fail-closed until quality and approval gates are stable.

**Default:** `gmail_draft`.

**Live send:** only via separately approved live-send job/scope override, with verified recipients, current artifact, Gmail message id/thread id, and local delivery record.

---

## Task 5: Ongoing quality loop

**Objective:** Raise drafts from “draft_only_insufficient_quality” to sendable executive briefing quality.

**Focus areas from latest runs:**
- Increase `MA Top Signals` count.
- Register/verify recurring publisher sources.
- Reduce generic implication phrasing.
- Preserve Joseph style: conclusion first, mechanism explained, watchpoint converted into decision-useful signal.

# status — 로봇 밸류체인 (my-course)

| 단계 | 상태 | 날짜 | 메모 |
|---|---|---|---|
| 주제 · brief | 완료 | 2026-10-31 | 로봇 밸류체인 · 대상 자동차 부품사 재직자 · 결과물 교재 3장 + 강의 덱 + 강의 스킬 → `forge/brief.md` |
| 교재 목차 | 완료 · 승인 | 2026-10-31 | 3장 → `forge/outline.md` |
| 자료 조사 | 완료 · 승인 | 2026-10-31 | 출처 1장 7 · 2장 4(확인) · 3장 8, 숫자 20개(확인 16 · 조건부 4 — 2026-10-31 재집계로 정정, 처음 보고는 15·5로 잘못 셈) → `forge/sources.md`, `forge/facts.csv` |
| 교재 본문 | **완료 · 확정** | 2026-10-31 | `textbook/ch1~3.md` + 그림 2장(`textbook/fig/ch1_valuechain.svg`, `ch2_bom_chart.svg`). 숫자·출처 자동 대조 통과 |
| 교재 검수 · 파일 | **완료 · 승인** | 2026-10-31 | 검수 수정 10곳(2025E 표기, 단정 문장 7, 소제목 수치 1, facts F14 기준연도). `Robot_Value_Chain_Textbook.docx`·`.pdf`(A4 18쪽) — Word COM 변환(`forge/build/`) |
| 강의 덱 | **완료 · 승인** | 2026-10-31 | `Robot_Value_Chain_Deck.pptx`·`.pdf` 22장. report-navy-deck field 모드, 글꼴 Noto Sans KR(Noto Sans CJK KR 미설치). 빌드 `forge/deck/build.js`, 렌더·PDF는 PowerPoint COM(LibreOffice 미사용 → Keynote 후처리 불필요). QA: facts에 없는 숫자 0 · 16pt 미만은 표지 고정 크기 2건뿐 · qa_callout_overlap 통과 · 22장 육안 확인 |
| 강의 스킬 · 커리큘럼 | 완료 · 승인 ① | 2026-10-31 | `learn-robot-valuechain` 블록 6개·120분 → `forge/curriculum.md` |
| 강의 스킬 · 수업·퀴즈 | 완료 | 2026-10-31 | SKILL.md + 블록 6개 + 퀴즈 10문항 + 과제. lint 오류 0 · 경고 0 → `forge/qa/skill_lint.txt` |
| 강의 스킬 · 학습자 자료 | 완료 | 2026-10-31 | `GUIDE.md`, `README.md` |
| 강의 스킬 · 배포 | **완료 · 승인 ③ public** | 2026-10-31 | https://github.com/supdrm54-eng/learn-robot-valuechain · https://supdrm54-eng.github.io/learn-robot-valuechain/ (built, HTTP 200) · 커밋 486e278 · 51파일 7.8MB · 공개 점검 0/0 · noreply 작성자 · zip `../learn-robot-valuechain.zip` |
| 강의 스킬 · 배우기·공유 | 다음 | | 직접 수강, 동료 공유 |
| 강의 스킬 · 실습 MVP | 완료 · 승인 ② | 2026-10-31 | `assets/answers/build_answers.py` → 산출물 6종·대시보드·expected.json(16값). verify 16/16 · 본문 16/16. 대시보드: 콘솔 오류 0, 375px 가로 스크롤 없음, [S#] 17개. 검산 중 고침: B5 퀴즈 8년 계산 117.5%, 미확보 목록 오탐(S3) |

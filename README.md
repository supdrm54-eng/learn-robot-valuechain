# 로봇 밸류체인 — learn-robot-valuechain

자동차 부품사 재직자를 위한 로봇 밸류체인 강의 패키지다. **교재 3장 · 강의 덱 22장 · 2시간 자율학습 강의 스킬**이 한 저장소에 있다. 수업은 Claude Code 스킬 `/learn-robot-valuechain`이 진행한다(Skills as Curriculum). supdrm54-eng가 course-forge로 KMA 자동차특화 AI 융합 전문가 과정 로봇 특강을 바탕으로 만들었다.

> 이 강의가 답할 질문 — 휴머노이드 원가의 절반이 액추에이터에 몰린 로봇 밸류체인에서, 우리 자동차 부품사는 어떤 기존 역량을 옮겨 어느 부품부터 들어갈 수 있는가?

- **실습 결과 대시보드(정답 예시)**: https://supdrm54-eng.github.io/learn-robot-valuechain/
- 처음이면 [GUIDE.md](GUIDE.md)부터. 기본 환경은 Claude 데스크톱 앱(Code 탭). VS Code는 GUIDE 부록 B

## 설치 — 한 줄

```
npx skills add supdrm54-eng/learn-robot-valuechain --agent claude-code --global --yes 를 실행해 줘
```

새 세션에서 `/learn-robot-valuechain`을 입력하면 수업이 시작된다. Node.js가 없으면 GUIDE.md 2단계대로 설치한다.

## 들어 있는 것

| 결과물 | 파일 |
|---|---|
| 교재 3장 | [Robot_Value_Chain_Textbook.pdf](Robot_Value_Chain_Textbook.pdf) · [.docx](Robot_Value_Chain_Textbook.docx) · 원고 [textbook/](textbook/) |
| 강의 덱 22장 | [docs/Robot_Value_Chain_Deck.pdf](docs/Robot_Value_Chain_Deck.pdf) · [.pptx](docs/Robot_Value_Chain_Deck.pptx) |
| 강의 스킬 | [.claude/skills/learn-robot-valuechain/](.claude/skills/learn-robot-valuechain/) |
| 검증 자료 | [forge/facts.csv](forge/facts.csv)(공개 숫자 20개: 확인 16 · 조건부 4) · [forge/sources.md](forge/sources.md) |

## 블록

| Block | 주제 | 끝나면 생기는 것 |
|---|---|---|
| 0 | 준비 | `~/robot-vc-lab` 작업 폴더와 자료 3종 |
| 1 | 로봇을 해부한다 | 시장 카드 3장, 우리 제품 지도(내부) |
| 2 | 돈은 어디에 있나 | BOM·출하 계산표, 대시보드 차트 |
| 3 | 숫자를 믿기 전에 | 확인/조건부 집계와 인용 문구 |
| 4 | 어디로 들어가나 | 현대모비스 판단표, 우리 회사 판단표(내부) |
| 5 | 공개와 공유 | 대시보드 공개 주소, 공유 메시지 |

## 수업 방식

| 구분 | 내용 |
|---|---|
| 목표 — AI Native | 계산·표·차트는 Claude가, "이 숫자를 믿어도 되나 · 우리는 어디서 시작하나" 판단은 내가 |
| 방법 — Skills as Curriculum | 스킬이 블록마다 설명 → 실습 → STOP → 확인·퀴즈를 진행한다 |
| 형식 — 자율학습 | 2시간, 퀴즈 10문항, 정답 수치 16개로 스스로 점검 |

## 원본 강의와 데이터 출처

| 자료 | 출처 | 구분 |
|---|---|---|
| 원본 강의 | [keerhee/kma-auto-genai-3-1](https://github.com/keerhee/kma-auto-genai-3-1) `Robot_Special/` — 로봇과 스마트팩토리 특강 덱 | 개념·비교표·원가 범위 |
| 시장 숫자 | IFR World Robotics 2025 (2025-09-25), IFR Robot Density (2024-01-10) | 국제기구 공개 보도자료 |
| 원가·출하 전망 | Bank of America Institute, *Physical AI Part 2* (2026-03-12) | 금융기관 공개 PDF — 'E'는 추정 |
| 부품사·완성차 사례 | The Korea Herald, 머니투데이, Axios, 데일리안, 뉴시스, 이투데이, CEO스코어데일리 (2026-01~05) | 언론 보도 |

숫자별 출처·교차확인·미확보 기록은 [forge/sources.md](forge/sources.md)와 [forge/facts.csv](forge/facts.csv)에 있다. 모든 숫자는 원문 그대로이며 단위·기준연도를 붙였다. 회사 내부 자료는 이 저장소에 없다.

## 개정 이력

| 날짜 | 바뀐 점 |
|---|---|
| 2026-10-31 | 첫 판 — 교재 3장, 덱 22장, 강의 스킬(블록 6개·퀴즈 10문항·정답 수치 16개 검증) |
| 2026-10-31 | 덱을 `docs/`로 옮김 · 표지 글자 16pt 이상으로 · 슬라이드 출처 줄에서 기관명 제거([S6] 번호로 연결) |

## 만든 방법

- `/course-forge`로 만들었다. 제작 기록(brief·목차·자료 조사·커리큘럼·검수)은 [forge/](forge/)에 있다.
- 덱은 report-navy-deck 스킬(field 모드), 교재 docx·PDF와 덱 렌더는 Microsoft Word·PowerPoint로 변환했다.

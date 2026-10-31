# Block 0: 준비 — 작업 폴더·자료·환경

> **Phase A 시작 시 그대로 출력한다:**
> ```
> 📖 공식 문서: https://code.claude.com/docs/en/overview · https://docs.python.org/3/library/csv.html
> ```

## EXPLAIN

### 1. 오늘 쓰는 자료

| 자료 | 무엇인가 |
|---|---|
| `facts.csv` | 교재에 쓴 공개 숫자 20개. 숫자마다 단위·기준연도·출처 번호·교차확인 결과·상태(확인/조건부)가 붙어 있다 |
| `sources.md` | 출처 목록. 번호(S1, S5 …)·기관·발행일·주소·신뢰도 |
| `Robot_Value_Chain_Textbook.pdf` | 교재 3장. 막히면 해당 장을 펼쳐 본다 |
| `my_*.md` | 오늘 만들 **회사 내부용** 파일. 공개 저장소에 올리지 않는다 |

### 2. 왜 새로 검색하지 않고 facts.csv만 쓰는가

| 기준 | 매번 웹에서 새로 찾기 | 검증된 facts.csv 쓰기 |
|---|---|---|
| 결과 | 사람마다, 날마다 다른 숫자 | 누구나 같은 숫자 — 정답과 맞춰 볼 수 있다 |
| 신뢰 | 출처 확인을 매번 다시 해야 한다 | 이미 교차 확인한 숫자와 그 기록 |
| 오늘의 초점 | 숫자 모으기 | 숫자를 **해석하고 판단하기** |

### 3. 케이스 — 숫자 하나가 바꾼 보고서

교재를 만드는 과정에서 "2025년 휴머노이드 출하 20,000대"를 처음엔 실적으로 적었다. 원문 차트를 다시 보니 2025년 옆에 'E'(추정)가 붙어 있었다. 숫자는 같아도 '실적'과 '추정'은 보고서의 무게가 다르다. 오늘 수업 내내 이 'E'를 놓치지 않는 연습을 한다.

## EXECUTE

아래 프롬프트를 붙여 넣으라고 안내한다. Phase A 출력 직전에 `{SKILL_DIR}`을 이 SKILL.md가 있는 실제 폴더 경로로 바꿔 보여 준다.

```
로봇 밸류체인 수업 작업 폴더를 준비해 줘.

1. 내 홈 폴더 아래에 robot-vc-lab 폴더를 만들고, 그 안에 data, output 폴더를 만들어 줘.
2. {SKILL_DIR}/assets/lab/ 안의 파일 3개(facts.csv, sources.md, Robot_Value_Chain_Textbook.pdf)를 robot-vc-lab/data/ 로 복사해 줘. 원본은 수정하지 마.
3. facts.csv 의 행 수와 열 이름을 보여 줘. 한글이 깨지면 UTF-8로 다시 읽어 줘.
4. robot-vc-lab/.gitignore 를 만들어 my_*.md 와 env_check.txt 가 나중에 공개 저장소에 올라가지 않게 해 줘.
5. Python 3(python, python3, py 순서로)과 Git, GitHub CLI(gh)가 있는지 확인해 줘. 없으면 설치 방법을 알려 주고, 설치는 내 허락을 받은 뒤에 해.
6. 결과를 robot-vc-lab/env_check.txt 에 날짜와 함께 적어 줘. 비밀번호나 토큰을 묻지 마.
```

끝나면 수강생이 직접 할 일을 안내한다.

1. 데스크톱 앱 왼쪽 위 **새 세션**을 누른다.
2. **Local**을 고르고 폴더 선택에서 홈 폴더의 `robot-vc-lab`을 고른다.
3. 새 세션 입력칸에 `/learn-robot-valuechain`을 입력하고 "Block 0 완료"라고 말한다.

### 확인할 것 (Phase B)

- `~/robot-vc-lab/data/`에 자료가 3개 있다.
- `facts.csv`가 20행(머리줄 제외)이다.
- `.gitignore`에 `my_*.md`와 `env_check.txt`가 있다.
- `env_check.txt`에 Python·Git·gh 상태가 적혀 있다.

막히면 원인을 Claude Code에게 찾게 하는 후속 프롬프트를 준다. 정답은 "정답 보기" 요청이 있을 때만 연다.

```
robot-vc-lab 준비가 어디서 막혔는지 env_check.txt와 폴더 상태를 보고 원인을 찾아 줘. 고치기 전에 무엇을 바꿀지 먼저 말해 줘.
```

## QUIZ

Block 0은 퀴즈가 없다. 확인이 끝나면 AskUserQuestion으로 Block 1로 넘어갈지 묻는다.

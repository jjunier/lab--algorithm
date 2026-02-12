# 📘 PS(Problem Solving) & Coding Test Prep

>   코딩 테스트를 위한 자료구조 및 알고리즘 기반의 문제 풀이 스터디 레포지토리입니다.



## 📅 진행 방식

- 전반적인 자료 구조 및 알고리즘 개념 숙지 및 코드 구현
    - `시간 복잡도`와 `공간 복잡도` 이해
    - `자료 구조` : 리스트와 선형 배열, 연결 리스트, 스택, 큐(환형 큐, 우선순위 큐), 트리(이진 트리, 이진 탐색 트리), 힙, 해시
    - `알고리즘` : 정렬과 탐색, 재귀, BFS, DFS, 그리디, 동적 계획법
- 매일 1~2문제 풀이
    - 문제 당 최대 제한 시간은 1시간
- 주제별 집중 학습 (예: 스택/큐/정렬/트리 등)
- 백준, 프로그래머스, leetcode 등 중심 풀이



## 📁 디렉토리 구조

```bash
📁 ps-algorithm-study
├── 01_Theory          # 알고리즘 & 자료구조 이론 정리
├── 02_PS              # 문제 풀이 (백준, 프로그래머스 등)
│   ├── BOJ/           # 백준
│   ├── Programmers/   # 프로그래머스
│   └── LeetCode/      # 리트코드
├── 03_SQL             # SQL 문제 풀이
│   ├── Programmers/   # 프로그래머스 (SQL 문제)
└── _image             # 이미지 저장용
```



## ✅ 커밋 메시지 규칙 (Emoji + Conventional Commits + 학습 태그)

### :laughing: Emoji

| 이모지                 | 설명          | 상황                               | 의미             |
| ---------------------- | ------------- | ---------------------------------- | ---------------- |
| ✅ `:white_check_mark:` | 손쉽게 해결   | 제한 시간 1시간 이내에 무난하게 풂 | 실력 내에서 해결 |
| 🔍 `:mag:`              | 약간 어려웠음 | 인터넷 개념 검색 등을 참조함       | 탐색하며 학습    |
| 🧠 `:brain:`            | 답을 참고함   | 제한 시간 내 해결 실패, 답안 참고  | 공부 목적의 풀이 |



### :bookmark: Conventional Commits

| 타입       | 설명                              |
| ---------- | --------------------------------- |
| `feat`     | 새로운 기능 / 문제 풀이 추가      |
| `fix`      | 문제 해결 또는 코드 수정          |
| `refactor` | 코드 구조 개선 (성능 향상 포함)   |
| `docs`     | 문서 수정 (``README.md`, 주석 등) |
| `test`     | 테스트 코드 작성                  |
| `chore`    | 설정 파일 변경, 기타 자잘한 작업  |



### :speech_balloon: 커밋 메시지 예시

```bash
✅ feat: Add BOJ 10818 solution [Array]
🔍 feat: Solve BOJ 1966 with Queue [Simulation]
🧠 feat: Study BOJ 1005 (ACM Craft) [DP + Topological Sort]
```
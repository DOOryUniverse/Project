# 기업 신용평가 모델링_ 팀 FiTing

## 최종 목표 모델

- 기업 신용평가 모델  **creating** 개발
    
    💡creating : credit + rating
    

ESG중 Social: 기부금?! 재무요소지만 특이하게 현 시대 트렌드를 반영해 기부금을 반영

## FiTing 소개

- 팀 명칭
    
    Finance+raTing의 합성어
    
- 팀 소개

[안녕하세요 FiTing 입니다. ](https://www.notion.so/FiTing-f1a399bdbbed4751a6c2fca30aaf35d6)

|  | 주 분야  | 주 역할 |
| --- | --- | --- |
| 김태환 | 통계/경제 | 팀장 + 도메인지식 |
| 강승연 | 통계 | 코드작성 + 시각화  |
| 김민정 | 일본어/경제 | 일지 작성 + 도메인지식 |
| 이정환 | 산업경영공학 | 코드작성 |
| 이지현 | 문헌정보 | 노션 정리 |

[[회의록] 신용평가 모델](https://www.notion.so/af766136f8c94f1796cf757b809ee03d)

## 자료조사 정리

[이지현 ](https://www.notion.so/8313e9d86bf847d6a3e94a660682725a)

[이정환](https://www.notion.so/04d72aae486a425495d3db24038bbe87)

[강승연](https://www.notion.so/1de8246d870347caad3f371d46307574)

[김민정](https://www.notion.so/a41a2e50ed4c48c0999829173f67c2c4)

[김태환](https://www.notion.so/99c327ca3b35459ba25174b06dd43157)

[발표 일정](https://www.notion.so/2b9efaf4461e43fe934ddcfef0a767a1)

# 프로젝트 계획

![Untitled](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Untitled.png)

[기업 대출 신용평가 모델 기획안  ](https://www.notion.so/9324013c487e4e8ea62719f585b77dee)

[데이터 수집](https://www.notion.so/31132a808b194db99ce6a5b6f9539a0e)

[데이터 처리 · 저장](https://www.notion.so/a440a8d10edc413a884a78ee34ce0b1e)

[데이터 분석](https://www.notion.so/1481aeb20ec14bb1ac7d71d8a0999acf)

[결과 시각화 ](https://www.notion.so/3471051dd5d043c1aabcfdc246cc9e38)

[의사결정 개발 (비즈니스 모델 개발 반영) ](https://www.notion.so/68464ec55f554156a1832ccfb6ca4885)


 ![Untitled](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Untitled%201.png)
    

재무제표는 116개의 기업을 선택하였고, 각 재무비율의 산업평균을 기준으로 평균 이하인 기업을 부실기업으로, 평균 이상인 기업을 건전기업으로 분류하여 각각 58개씩 할당하였다. 

선택된 재무변수는 현금비율, 순운전자본비율, EBITDA/이자비용비율, 자기자본비율, 매출액세전순이익율, 총자본영업이익율, 매출액영업이익율, 기업세전순이익률로 재무의 건전성과 기업의 수익성이 기업부실에 영향을 끼친다는 것을 알 수 있었다

또한 경영마인드의 혁신 즉, 실시간으로 이루어지는 재무분석과 경영관리시스템 구축이 필요함을 시사해 준다. 향후 연구방향과 과제는 비재무적 변수를 찾아내는 통계적 방법의 연구와 데이터마이닝 기법인 규칙유도기법(rule induction)과 인공신경망(artificial neural networks) 분석을 이용한 기업부실예측은 향후 연구과제로 남긴다.

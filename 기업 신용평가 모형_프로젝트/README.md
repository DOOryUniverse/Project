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

## Open DART를 이용한 코스닥 재무제표 수집

[KRX.ipynb](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/KRX.ipynb)

[Open DART를 이용한 전체 재무제표 수집.ipynb](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Open_DART%EB%A5%BC_%EC%9D%B4%EC%9A%A9%ED%95%9C_%EC%A0%84%EC%B2%B4_%EC%9E%AC%EB%AC%B4%EC%A0%9C%ED%91%9C_%EC%88%98%EC%A7%91.ipynb)

[코스닥주요재무지표.csv](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/%EC%BD%94%EC%8A%A4%EB%8B%A5%EC%A3%BC%EC%9A%94%EC%9E%AC%EB%AC%B4%EC%A7%80%ED%91%9C.csv)

[https://github.com/DOOryUniverse/UBION_Project](https://github.com/DOOryUniverse/UBION_Project)

- 그래프 그리기 참고 링크 
[https://blog.naver.com/PostView.nhn?blogId=freed0om&logNo=221957415249&categoryNo=67&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postList](https://blog.naver.com/PostView.nhn?blogId=freed0om&logNo=221957415249&categoryNo=67&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postList)
    
    ![Untitled](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Untitled%201.png)
    

### 기타 즐겨찾기

- 모델별 자동 피쳐 선정
    - [https://velog.io/@emseoyk/핸즈온-ML-with-Kaggle-1-2-Feature-Selection](https://velog.io/@emseoyk/%ED%95%B8%EC%A6%88%EC%98%A8-ML-with-Kaggle-1-2-Feature-Selection)

[(4) DART 기업 재무 공시자료 가져오기.ipynb](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/(4)_DART_%EA%B8%B0%EC%97%85_%EC%9E%AC%EB%AC%B4_%EA%B3%B5%EC%8B%9C%EC%9E%90%EB%A3%8C_%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0.ipynb)

[코스닥주요재무지표10.csv](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/%EC%BD%94%EC%8A%A4%EB%8B%A5%EC%A3%BC%EC%9A%94%EC%9E%AC%EB%AC%B4%EC%A7%80%ED%91%9C10.csv)

[재무비율.xlsx](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/%EC%9E%AC%EB%AC%B4%EB%B9%84%EC%9C%A8.xlsx)

[(X)(2001)중소기업의 신용조사서 분석을 통한 부실기업 예측모형 연구.pdf](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/(X)(2001)%EC%A4%91%EC%86%8C%EA%B8%B0%EC%97%85%EC%9D%98_%EC%8B%A0%EC%9A%A9%EC%A1%B0%EC%82%AC%EC%84%9C_%EB%B6%84%EC%84%9D%EC%9D%84_%ED%86%B5%ED%95%9C_%EB%B6%80%EC%8B%A4%EA%B8%B0%EC%97%85_%EC%98%88%EC%B8%A1%EB%AA%A8%ED%98%95_%EC%97%B0%EA%B5%AC.pdf)

![Untitled](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Untitled%202.png)

![Untitled](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Untitled%203.png)

![Untitled](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Untitled%204.png)

![Untitled](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Untitled%205.png)

![Untitled](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Untitled%206.png)

![Untitled](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Untitled%207.png)

[(다시 봐야할듯)기업부실 예측의 성과개선을 위한 기하평균 정확도 기반의 앙상블 학습.pdf](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/(%EB%8B%A4%EC%8B%9C_%EB%B4%90%EC%95%BC%ED%95%A0%EB%93%AF)%EA%B8%B0%EC%97%85%EB%B6%80%EC%8B%A4_%EC%98%88%EC%B8%A1%EC%9D%98_%EC%84%B1%EA%B3%BC%EA%B0%9C%EC%84%A0%EC%9D%84_%EC%9C%84%ED%95%9C_%EA%B8%B0%ED%95%98%ED%8F%89%EA%B7%A0_%EC%A0%95%ED%99%95%EB%8F%84_%EA%B8%B0%EB%B0%98%EC%9D%98_%EC%95%99%EC%83%81%EB%B8%94_%ED%95%99%EC%8A%B5.pdf)

![Untitled](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Untitled%208.png)

![———————원조————————](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Untitled%209.png)

———————원조————————

k1 k2 모형 

![Untitled](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Untitled%2010.png)

![Untitled](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Untitled%2011.png)

![Untitled](%E1%84%80%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B8%20%E1%84%89%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%A6%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC_%20%E1%84%90%E1%85%B5%E1%86%B7%20FiTing%20cd876f0d5cb84ddd8031d9ff194955a8/Untitled%2012.png)

재무제표는 116개의 기업을 선택하였고, 각 재무비율의 산업평균을 기준으로 평균 이하인 기업을 부실기업으로, 평균 이상인 기업을 건전기업으로 분류하여 각각 58개씩 할당하였다. 

선택된 재무변수는 현금비율, 순운전자본비율, EBITDA/이자비용비율, 자기자본비율, 매출액세전순이익율, 총자본영업이익율, 매출액영업이익율, 기업세전순이익률로 재무의 건전성과 기업의 수익성이 기업부실에 영향을 끼친다는 것을 알 수 있었다

또한 경영마인드의 혁신 즉, 실시간으로 이루어지는 재무분석과 경영관리시스템 구축이 필요함을 시사해 준다. 향후 연구방향과 과제는 비재무적 변수를 찾아내는 통계적 방법의 연구와 데이터마이닝 기법인 규칙유도기법(rule induction)과 인공신경망(artificial neural networks) 분석을 이용한 기업부실예측은 향후 연구과제로 남긴다.

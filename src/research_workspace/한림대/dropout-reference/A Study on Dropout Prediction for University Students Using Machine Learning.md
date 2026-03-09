# A Study on Dropout Prediction for University Students Using Machine Learning

## 📋 기본 정보

- **저자**: Choong Hee Cho, Yang Woo Yu, Hyeon Gyu Kim
- **출판 연도**: 2023
- **저널**: Applied Sciences, Vol. 13, 12004 (MDPI)
- **DOI**: https://doi.org/10.3390/app132112004
- **데이터**: 삼육대학교 재학생 20,050명, 168,000건 학사 레코드 (2010~2022)
- **주제 분류**: 중도탈락 예측 / 머신러닝 / 클래스 불균형 처리

---

## 🎯 Abstract

### 목적
- 중소규모 4년제 대학(삼육대) 재학생의 중도탈락을 머신러닝으로 예측하는 모델 구현
- 클래스 불균형(중도탈락률 약 5%) 문제 해결을 위한 오버샘플링 기법의 효과 분석

### 핵심 발견
- 6개 ML 알고리즘 비교 실험에서 **LightGBM이 F1-score 0.840으로 최고 성능** 달성
- 오버샘플링(SMOTE, ADASYN, Borderline-SMOTE) 적용 시 RF 모델 제외 전 모델 성능 **오히려 하락**
- 중도탈락-비탈락 데이터 간 **클래스 오버랩이 심각**하여 오버샘플링된 합성 샘플이 노이즈로 작용함

### 함의
- 클래스 불균형 데이터에서 오버샘플링이 항상 유효하지 않음을 실증
- 기존 선행 연구 대비 F1-score 기준 최고 성능 갱신

---

## 📊 상세 분류

### 배경 및 필요성

- 한국 4년제 대학 중도탈락률: **약 5%** (2018년 기준)
- 사이버 대학: 18.9%, MOOC: 80~95%
- 탈락률이 극단적으로 낮거나 높을 경우 클래스 불균형 문제 → Accuracy만으로 평가 불가
- 불균형 반영 지표로 **F1-score** 채택 필요성 제기

---

### 사용 변수 전체 목록 [CORE]

> 원천 DB는 7개 테이블로 구성되며, 병합 시 최대 150개 속성 생성. 이 중 Dropout과의 상관계수 ≥ 0.01인 **11개 속성**을 최종 학습 변수로 선택함.

#### 원천 테이블별 변수

| 테이블 | 원천 속성 | 요약 속성명 | 설명 |
|---|---|---|---|
| Grade | Grade (avg) | **Grade** | 지수평활법(α=0.8) 적용 가중 평균 학점 (0~4.5) |
| Grade | NumF | **NumF** | 마지막 등록 학기의 F학점 과목 수 |
| AcademicStatus | Status | **NumSem** | 총 등록 학기 수 (입학·재학·편입 상태 횟수) |
| AcademicStatus | Status | **NumAbs** | 졸업/중퇴 직전 연속 휴학 학기 수 |
| AcademicStatus | Status | **Dropout** | 최종 상태: 중도탈락(1) / 비중도탈락(0) ← **레이블** |
| Scholarship | Scholarship | **Scholar** | 마지막 등록 학기 장학금 수령액 |
| Counsel | NumCouns | **NumCouns** | 마지막 등록 학기 상담 횟수 |
| ExtraCourse | NumExtra | **NumExtra** | 마지막 등록 학기 비교과 프로그램 참여 횟수 |
| ExtraCourse | NumVolun | *(NumExtra에 통합)* | 봉사활동 참여 횟수 |
| BookLoan | NumBook | **NumBook** | 마지막 등록 학기 도서 대출 수 |
| StudentInfo | Dept | **Dept** | 학과(부) 번호 |
| StudentInfo | AdmType | **AdmType** | 입학 유형: 신입학(0) / 편입(1) |
| StudentInfo | Region | **Region** | 출신 고등학교 지역 코드 |

> **최종 학습 피처**: Grade, NumF, NumSem, NumAbs, Scholar, NumCouns, NumBook, Dept, AdmType, Region (10개)
> **레이블**: Dropout (1개)

---

### 핵심 변수 (Dropout과의 상관도 순위) [CORE]

| 순위 | 변수 | Dropout 상관계수 | 방향 |
|---|---|---|---|
| 1 | **Grade** | -0.47 | 학점 낮을수록 탈락 위험↑ |
| 2 | **NumSem** | -0.44 | 등록 학기 적을수록 탈락 위험↑ |
| 3 | **NumF** | +0.27 | F학점 많을수록 탈락 위험↑ |
| 4 | **Scholar** | -0.25 | 장학금 없을수록 탈락 위험↑ |
| 5 | **NumAbs** | +0.24 | 연속 휴학 길수록 탈락 위험↑ |
| 6 | NumCouns | +0.01 | (미미한 양의 상관) |
| 7 | NumBook | +0.03 | |
| 8 | Dept | +0.03 | |
| 9 | AdmType | +0.08 | 편입생의 탈락률 소폭 높음 |
| 10 | Region | +0.08 | |

> Grade ↔ NumSem 간 상관계수 0.32, Grade ↔ NumF 간 상관계수 -0.52 (다중공선성 주의)

---

### 사용 모델 [CORE]

#### 비교 알고리즘 6종

| 모델 | 라이브러리 | 주요 하이퍼파라미터 |
|---|---|---|
| Logistic Regression (LR) | Scikit-learn | C=100 |
| Decision Tree (DT) | Scikit-learn | max_depth=10, random_state=0 |
| Random Forest (RF) | Scikit-learn | n_estimators=100, random_state=0 |
| SVM | Scikit-learn | C=100 |
| DNN | Keras 2.0 | Dense(128, relu) → Dense(32, relu) → Dense(1, sigmoid), optimizer=adam, loss=binary_crossentropy, epochs=50 |
| **LightGBM** | lightgbm | n_estimators=100, random_state=0 |

#### 오버샘플링 기법 3종

- **SMOTE** (K-NN 기반 합성 샘플 생성)
- **ADASYN** (적응형 합성 샘플링)
- **Borderline-SMOTE** (경계 샘플 중심 증강)

#### 전처리

- 결합 테이블 → CSV → Python DataFrame
- 입력값 정규화: `StandardScaler` (0~1 범위)
- 학습/테스트 분리: `train_test_split(test_size=0.2)`
- Grade 평균화: 지수평활법 `y = αy_t + α(1-α)y_{t-1} + ...` (α=0.8)

---

### 핵심 성능 지표 [CORE]

#### 오버샘플링 미적용 (기본 성능)

| 알고리즘 | Accuracy | Precision | Recall | **F1-Score** |
|---|---|---|---|---|
| LR | 0.927 | 0.815 | 0.637 | 0.715 |
| DT | 0.947 | 0.856 | 0.755 | 0.802 |
| RF | 0.953 | 0.883 | 0.777 | 0.827 |
| SVM | 0.942 | 0.825 | 0.753 | 0.787 |
| DNN | 0.947 | 0.843 | 0.776 | 0.808 |
| **LightGBM** | **0.955** | **0.867** | **0.814** | **0.840** |
| 평균 | 0.945 | 0.848 | 0.752 | 0.796 |

> **최고 성능: LightGBM** — F1-score 0.840, Accuracy 0.955
> LightGBM은 실행 시간도 1.1초로 RF(2.9초), SVM(6.1초), DNN(27.6초) 대비 우월

#### SMOTE 적용 후 성능 변화

| 알고리즘 | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| LR | 0.868 | 0.523 | 0.883 | 0.657 |
| DT | 0.929 | 0.706 | 0.868 | 0.778 |
| **RF** | **0.949** | **0.797** | **0.866** | **0.830** ↑ |
| SVM | 0.921 | 0.668 | 0.890 | 0.763 |
| DNN | 0.928 | 0.691 | 0.904 | 0.784 |
| LightGBM | — | — | — | — (패키지 충돌 오류) |
| 평균 | 0.919 | 0.677 | 0.882 | 0.762 ↓ |

> SMOTE 적용 시 평균 F1-score: 0.796 → 0.762 **(하락)**
> Precision 대폭 하락 (0.848 → 0.677), Recall만 상승 (0.752 → 0.882)

#### ADASYN / Borderline-SMOTE 성능 비교

| 오버샘플링 기법 | 평균 F1-Score |
|---|---|
| 미적용 | **0.796** |
| SMOTE | 0.762 |
| Borderline-SMOTE | 0.742 |
| ADASYN | 0.735 (최저) |

---

### 선행 연구 대비 성능 비교

| 지표 | 선행 연구 알고리즘 | 선행 연구 점수 | 제안 모델 (LightGBM) |
|---|---|---|---|
| F1-score | CatBoost+XGBoost | 0.808 | **0.840** |
| Precision | Ridge Regression | 0.739 | **0.867** |
| F1-score | RF | 0.810 | **0.840** |
| F1-score | SVM | 0.804 | **0.840** |
| Accuracy | DNN | 0.768 | **0.955** |

---

### 결론 및 한계

- LightGBM이 정확도·F1-score·실행 시간 모든 면에서 최적 모델임이 실험으로 증명됨
- 오버샘플링 기법이 데이터 오버랩 상황에서 오히려 노이즈 증가로 성능 저하를 유발함
- **한계**: 단일 대학 데이터 사용, 학기별 예측 모델 미구현
- **향후 연구**: 클래스 경계 기반 노이즈 저감 오버샘플링 기법 연구, 학기별 중도탈락 예측 모델 개발

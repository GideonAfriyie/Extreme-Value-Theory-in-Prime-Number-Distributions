# Uncovering Prime Number Patterns
### A Data-Driven Analysis of Gaps, Growth, and Conjectures

## Author Statement
This project was inspired by an **Abstract Mathematics course**, where I explored deep questions about prime numbers, such as **Mersenne primes** and their unpredictability. I became curious: _Is there a pattern in prime numbers?_ _Can I find a formula?_ While no simple formula emerged, this journey gave me valuable insights into **prime gaps**, **logarithmic trends**, and classical **conjectures** — all through hands-on computation and statistical analysis.

---

## 🎯 Goals
- Analyze the **first 1,000 prime numbers**
- Explore **prime gaps** and their statistical trends
- Visualize **logarithmic growth** of primes
- Investigate **Cramér’s Conjecture** and **Twin Prime Conjecture**
- Work with **Mersenne primes** and other unique subsets
- Use **Python and Excel** for a hybrid data approach

---

## 📈 Key Insights

### 📊 Prime Gaps
- Gaps vary from **1 to 34**, most frequent: **2, 4, 6**
- **Mean** gap ≈ 17.05, **Median** = 17, **Mode** = 16
- **Standard Deviation**
- Gaps increase irregularly, consistent with theoretical expectations

### 🔍 Cramér’s Conjecture
- Predicts gaps grow roughly as **log(p)²**
- Confirmed: all actual gaps lie **below this bound** for first 1,000 primes

### 🧪 Twin Primes
- Counted all pairs with a gap of **2**
- Found strong clustering early, gradual drop with increasing primes
- Supports idea that **twin primes become rarer**, but still occur

### 📉 Logarithmic Trends
- `log(pₙ)` grows steadily with prime index
- Visualizations reinforce the **Prime Number Theorem**

### ⚡ Mersenne Primes
- Briefly explored primes of form `2^p - 1`
- These primes are **rare** but **important** in cryptography and theory

---

## 💻 Technologies Used
- **Python:** Jupyter Notebook, NumPy, matplotlib, `csv`
- **Excel:** Gap calculation, frequency analysis, statistical summary
- **GitHub:** Version control and documentation

---

## 📂 Files in Repository
## Files
- `first_1000_primes.csv`: List of generated primes
- `First 1,000 prime numbers.py`: Prime generation script
- `Cramers Conjecture Comparison.ipynb`: Python notebook with visualiztions
- `Twin Prime Conjecture.ipynb`: Python notebook with visualizations
- `Logarithmic Prime Spacing.ipynb`: Python notebook with visualizations
- `prime_gap_analysis.xlsx`: Excel stats and charts
- `README.md`: This file

---

## 🎓 Educational Outcome
This project strengthened my understanding of:

- Number theory, which I havent taken as a course yet (especially gaps and growth rates)
- Mathematical conjectures and open questions
- Data visualization and exploratory analysis
- Scientific programming and reproducible workflows

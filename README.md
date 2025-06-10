🔢 **Uncovering Prime Number Patterns**

A Statistical and Computational Study of Gaps, Growth, and Conjectures

**Author**: Gideon Afriyie


🧠 **Author Statement**

This project emerged from an abstract mathematics course that introduced me to the mysterious nature of prime numbers — from Mersenne primes to the unpredictability of their distribution. I became curious: Is there a pattern in prime numbers? Can I find a formula? Inspired by these ideas, I launched an independent investigation into the patterns and behaviors of prime gaps using Python, Excel, and classical number theory. Although a formula for predicting primes remains out of reach, this research helped me uncover compelling patterns and connections — and pushed me to apply real-world computational techniques to an age-old mathematical mystery.

🎯 **Project Objectives**

🔍 Analyze the first 1,000 prime numbers

📏 Investigate prime gaps and their statistical behavior

📈 Visualize logarithmic growth and prime distribution

🧩 Test alignment with Cramér’s Conjecture

♊ Identify Twin Primes and assess their distribution

✴ Explore connections to Mersenne primes

🛠 Use Python + Excel in a hybrid data-science workflow

📊 **Key Insights & Results**

**📐 Prime Gaps**
Gaps ranged from 1 to 34

Most frequent gaps: 2, 4, 6

Statistical Summary:

Mean ≈ 17.05

Median = 17

Mode = 6

Standard deviation: Moderate irregularity

Gaps grow irregularly but remain bounded — consistent with theoretical expectations

🔎 **Cramér’s Conjecture**
Predicts that prime gaps grow approximately as 
log
⁡
(
𝑝
)
2
log(p) 
2
 

Plotted conjectured bound vs. actual gaps

Result: All observed gaps fell well below the predicted upper bound — offering empirical support for the conjecture (within this sample)

♊ **Twin Primes**
Identified all twin prime pairs (gap = 2)

Found frequent clustering among lower primes

Occurrence diminished gradually but did not vanish

Observation aligns with the Twin Prime Conjecture (infinitely many twin primes)

📉 **Logarithmic Trends**
Plotted log(𝑝_𝑛) against prime index

Curve gradually flattens — consistent with the Prime Number Theorem

Further plots of gap size vs. log(p) reveal nonlinear dispersion patterns

⚡ **Mersenne Primes (Brief Note)**
Considered primes of the form 2^n - 1

Not directly analyzed, but recognized for their rarity, structure, and relevance in cryptography

💻 **Technologies Used**
Tool	                   Role
Python	                 Prime generation, statistical computation, plotting (NumPy, matplotlib, csv)
Jupyter Notebook	       Interactive exploration and documentation
Excel	                   Frequency tables, descriptive statistics, additional visualizations
GitHub	                Version control, project publication, collaboration-ready structure

📁 **Repository Contents**
File	                              Description
first_1000_primes.csv	                 List of generated primes
First 1,000 prime numbers.py	         Python script for prime generation
Cramers_Conjecture_Comparison.ipynb	   Visual analysis of Cramér's Conjecture
Twin_Prime_Conjecture.ipynb	           Notebook examining twin primes
Logarithmic_Prime_Spacing.ipynb	        Visual exploration of prime growth via logarithms
prime_gap_analysis.xlsx	                Excel file with full statistical breakdown and charts
README.md	                              Project overview (this file)

🎓 **Educational Takeaways**
Through this self-directed project, I significantly expanded my skills in:

🔢 Number theory fundamentals — especially gaps, growth, and conjectural models

🧠 Mathematical exploration without formal coursework

🛠 Computational thinking — bridging math theory and real data analysis

📊 Data visualization and pattern recognition

📁 Reproducible workflows and open research practices

📌 Future Directions
Scale to 10,000+ primes for deeper statistical rigor

Explore higher-order conjectures (e.g. Riemann Hypothesis, Hardy-Littlewood k-tuple conjecture)

Develop interactive visual tools for public engagement

Submit project as an undergraduate research article or poster

Thanks for visiting! Feel free to fork, contribute, or reach out with insights or suggestions.

“The primes are the atoms of arithmetic — yet we are still decoding their structure.” – Anonymous

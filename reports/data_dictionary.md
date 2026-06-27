# Mutual Fund Analytics Data Dictionary

## dim_fund

| Column            | Data Type | Description                     | Source                   |
| ----------------- | --------- | ------------------------------- | ------------------------ |
| amfi_code         | INTEGER   | Unique AMFI scheme identifier   | 01_fund_master_clean.csv |
| scheme_name       | TEXT      | Name of mutual fund scheme      | 01_fund_master_clean.csv |
| fund_house        | TEXT      | Mutual fund company             | 01_fund_master_clean.csv |
| category          | TEXT      | Fund category (Equity/Debt)     | 01_fund_master_clean.csv |
| expense_ratio_pct | REAL      | Annual expense ratio percentage | 01_fund_master_clean.csv |

## fact_nav

| Column    | Data Type | Description     | Source                   |
| --------- | --------- | --------------- | ------------------------ |
| amfi_code | INTEGER   | Fund identifier | 02_nav_history_clean.csv |
| nav_date  | DATE      | NAV date        | 02_nav_history_clean.csv |
| nav       | REAL      | Net Asset Value | 02_nav_history_clean.csv |

## fact_transactions

| Column           | Data Type | Description                | Source                             |
| ---------------- | --------- | -------------------------- | ---------------------------------- |
| investor_id      | TEXT      | Unique investor identifier | 08_investor_transactions_clean.csv |
| transaction_date | DATE      | Transaction date           | 08_investor_transactions_clean.csv |
| transaction_type | TEXT      | SIP / Lumpsum / Redemption | 08_investor_transactions_clean.csv |
| amount_inr       | REAL      | Transaction amount in INR  | 08_investor_transactions_clean.csv |
| state            | TEXT      | Investor state             | 08_investor_transactions_clean.csv |
| kyc_status       | TEXT      | KYC verification status    | 08_investor_transactions_clean.csv |

## fact_performance

| Column             | Data Type | Business Definition                                 | Source                          |
| ------------------ | --------- | --------------------------------------------------- | ------------------------------- |
| amfi_code          | INTEGER   | Unique AMFI code identifying the mutual fund scheme | 07_scheme_performance_clean.csv |
| return_1yr_pct     | REAL      | Fund return over the last 1 year (%)                | 07_scheme_performance_clean.csv |
| return_3yr_pct     | REAL      | Fund return over the last 3 years (%)               | 07_scheme_performance_clean.csv |
| return_5yr_pct     | REAL      | Fund return over the last 5 years (%)               | 07_scheme_performance_clean.csv |
| benchmark_3yr_pct  | REAL      | 3-year benchmark return (%)                         | 07_scheme_performance_clean.csv |
| alpha              | REAL      | Excess return generated over the benchmark          | 07_scheme_performance_clean.csv |
| beta               | REAL      | Measure of fund volatility compared to the market   | 07_scheme_performance_clean.csv |
| sharpe_ratio       | REAL      | Risk-adjusted return using total risk               | 07_scheme_performance_clean.csv |
| sortino_ratio      | REAL      | Risk-adjusted return considering downside risk      | 07_scheme_performance_clean.csv |
| std_dev_ann_pct    | REAL      | Annualized standard deviation of fund returns (%)   | 07_scheme_performance_clean.csv |
| max_drawdown_pct   | REAL      | Maximum decline from peak value (%)                 | 07_scheme_performance_clean.csv |
| aum_crore          | REAL      | Assets Under Management (₹ Crore)                   | 07_scheme_performance_clean.csv |
| expense_ratio_pct  | REAL      | Annual expense ratio charged by the fund (%)        | 07_scheme_performance_clean.csv |
| morningstar_rating | INTEGER   | Morningstar fund rating                             | 07_scheme_performance_clean.csv |
| risk_grade         | TEXT      | Risk level assigned to the fund                     | 07_scheme_performance_clean.csv |

---

## fact_aum

| Column         | Data Type | Business Definition                         | Source                         |
| -------------- | --------- | ------------------------------------------- | ------------------------------ |
| date           | DATE      | Date of AUM record                          | 03_aum_by_fund_house_clean.csv |
| fund_house     | TEXT      | Mutual fund company name                    | 03_aum_by_fund_house_clean.csv |
| aum_lakh_crore | REAL      | Total Assets Under Management in lakh crore | 03_aum_by_fund_house_clean.csv |
| aum_crore      | REAL      | Total Assets Under Management in crore      | 03_aum_by_fund_house_clean.csv |
| num_schemes    | INTEGER   | Number of schemes managed by the fund house | 03_aum_by_fund_house_clean.csv |

---

## dim_date

| Column     | Data Type | Business Definition                        | Source    |
| ---------- | --------- | ------------------------------------------ | --------- |
| date_key   | INTEGER   | Unique identifier for each date (YYYYMMDD) | Generated |
| full_date  | DATE      | Complete calendar date                     | Generated |
| year       | INTEGER   | Calendar year                              | Generated |
| quarter    | INTEGER   | Quarter of the year (1–4)                  | Generated |
| month      | INTEGER   | Month number (1–12)                        | Generated |
| month_name | TEXT      | Name of the month (January–December)       | Generated |

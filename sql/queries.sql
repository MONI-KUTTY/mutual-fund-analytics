-- 1. Top 5 Funds by AUM

SELECT scheme_name, aum_crore
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV Per Month

SELECT
strftime('%Y-%m', nav_date) AS month,
ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 3. SIP Year-over-Year Growth

SELECT *
FROM fact_transactions
WHERE transaction_type = 'SIP';


-- 4. Transactions by State

SELECT
state,
COUNT(*) AS total_transactions,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;


-- 5. Funds with Expense Ratio < 1%

SELECT
scheme_name,
expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- 6. Top 5 Funds by 3-Year Return

SELECT
scheme_name,
return_3yr_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY return_3yr_pct DESC
LIMIT 5;


-- 7. Average Return by Category

SELECT
category,
ROUND(AVG(return_3yr_pct),2) AS avg_return
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
GROUP BY category;


-- 8. Total AUM by Fund House

SELECT
fund_house,
SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC;


-- 9. Transaction Count by Payment Mode

SELECT
payment_mode,
COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY payment_mode
ORDER BY transaction_count DESC;


-- 10. Risk Category Distribution

SELECT
risk_category,
COUNT(*) AS total_funds
FROM dim_fund
GROUP BY risk_category;
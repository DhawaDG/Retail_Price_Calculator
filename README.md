# 🇦🇺 Australian E-Commerce Retail Price Calculator

A clean, light-weight, and production-ready Streamlit web application engineered specifically for e-commerce operators selling into the Australian market (with optimized shipping buffers for regions like Tasmania).

---

## 🧠 Why This Calculator Exists

When running an e-commerce storefront (like Shopify), calculating a sustainably profitable retail price can be frustratingly complex. Store owners frequently encounter these major bottlenecks:

1. **The Cost of 3rd Party Apps:** Relying on premium Shopify apps or pricing SaaS tools introduces unwanted monthly subscription overheads, chipping away at early-stage margins.
2. **Inaccurate "Blind Match" Math:** Many generic tools or manual spreadsheets use a static "2x or 3x markup formula" that fails to account for invisible financial leaks like platform transactional micro-fees, localized taxes, or scalable marketing budgets.
3. **Display vs Net Disconnect:** Australian consumer law mandates tax-inclusive pricing. Calculating margins based on tax-exclusive models leads to heavily degraded net profits.

This application solves these hurdles by providing a completely **free, isolated, and exact** localized calculation matrix that strips away guesswork and safeguards your target net margins.

---

## 📐 The Core Mathematical Formula

To protect your bottom line, this calculator uses an algebraic margin-protection formula. Instead of adding percentages to the cost (which skews real margins), it derives the required top-line retail price by dividing your total absolute costs by the remaining percentage of revenue.

```text
Retail Price = (Total Landed Cost + Fixed Overhead Buffer) / (1 - (GST% + Processing Fee% + Marketing% + Target Profit Margin%))
```

### Variable Breakdown:
* **Total Landed Cost:** Product Cost (COGS) + Shipping Fee to Destination (e.g., Tasmania)
* **Fixed Overhead Buffer:** Flattened per-item cost buffer covering software subscriptions (Shopify baseline), applications, and customer service time buffers.
* **The Denominator Breakdown (1 - Σ%):** Dynamically ensures every dollar flowing into your payment gateway has its localized tax (10% GST), transaction fee (e.g., 2.5% Shopify Payments), and customer acquisition marketing budget (e.g., 20% CAC) subtracted *before* allocating your true net profit.

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.10+
* **Framework:** Streamlit
* **Hosting Compatibility:** Free tier on Streamlit Community Cloud or self-hosted via Docker/VPS.

---

## 🚀 Local Installation & Virtual Environment Setup

To run this application locally on your machine without interfering with your system-wide Python dependencies (avoiding `PEP 668` environment errors):

### 1. Move Into the Project Directory
```bash
cd "~/Desktop/VScode_Project/Retail Price Calculator"
```

### 2. Establish a Virtual Environment Core
On Ubuntu/Debian Linux systems, ensure your venv package is active:

```bash
sudo apt update && sudo apt install python3-venv -y
python3 -m venv .venv
```

### 3. Activate the Environment Context
```bash
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Launch the Web Application
```bash
streamlit run app.py


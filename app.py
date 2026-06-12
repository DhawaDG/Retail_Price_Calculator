import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Aussie E-commerce Pricing Calculator",
    page_icon="🇦🇺",
    layout="centered"
)

st.title("🇦🇺 Australian Retail Price Calculator")
st.markdown("Calculate competitive retail prices that account for GST, Shopify fees, marketing, and healthy margins.")
st.divider()

# Create two columns for layout
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📦 Product & Shipping Costs")
    product_cost = st.number_input("Product Cost ($)", min_value=0.0, value=15.00, step=0.50, format="%.2f")
    shipping_cost = st.number_input("Shipping to Tasmania ($)", min_value=0.0, value=5.00, step=0.50, format="%.2f")
    
    landed_cost = product_cost + shipping_cost
    st.info(f"**Total Landed Cost:** ${landed_cost:.2f}")

    st.subheader("⚙️ Overhead & Fees")
    gst_pct = st.slider("Australian GST %", min_value=0, max_value=25, value=10) / 100
    processing_pct = st.slider("Payment Processing Fee %", min_value=0.0, max_value=10.0, value=2.5, step=0.1) / 100
    marketing_pct = st.slider("Marketing / Ad Spend %", min_value=0, max_value=50, value=20) / 100
    profit_pct = st.slider("Target Net Profit Margin %", min_value=5, max_value=70, value=30) / 100
    
    fixed_buffer = st.number_input("Fixed buffer per item ($) (Shopify/Admin)", min_value=0.0, value=1.00, step=0.10)

with col2:
    st.subheader("🎯 Recommended Pricing")
    
    # Formula Math
    total_variable_pct = gst_pct + processing_pct + marketing_pct + profit_pct
    
    if total_variable_pct >= 1.0:
        st.error("❌ Total percentages equal or exceed 100%. Please lower your target profit or marketing sliders.")
    else:
        # Calculate Retail Price
        retail_price = (landed_cost + fixed_buffer) / (1 - total_variable_pct)
        multiplier = retail_price / landed_cost if landed_cost > 0 else 0
        
        # Display main metric
        st.metric(label="Suggested Retail Price (AUD)", value=f"${retail_price:.2f}", delta=f"{multiplier:.1f}x Landed Cost")
        
        st.divider()
        st.write("📋 **Price Breakdown:**")
        
        # Cost Breakdown Data
        breakdown = {
            "Landed Cost": landed_cost,
            "GST Component": retail_price * gst_pct,
            "Processing Fees": retail_price * processing_pct,
            "Marketing Budget": retail_price * marketing_pct,
            "Fixed Buffer": fixed_buffer,
            "Net Profit": retail_price * profit_pct
        }
        
        for item, amount in breakdown.items():
            if item == "Net Profit":
                st.write(f"🟢 **{item}:** ${amount:.2f}")
            else:
                st.write(f"• {item}: ${amount:.2f}")
                
        st.caption("Note: GST is calculated as tax-inclusive, matching standard Australian retail display laws.")
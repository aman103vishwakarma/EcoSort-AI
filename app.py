import streamlit as st

st.set_page_config(page_title="EcoSort AI", page_icon="♻️")

st.title("♻️ EcoSort AI - Intelligent Waste Segregation")
st.subheader("Target SDG: 12 - Responsible Consumption & Production")

st.write("""
Welcome to the prototype for **EcoSort AI**. 
Upload an image of your household waste, and our multi-agent system will identify the material and give you localized disposal instructions.
""")

uploaded_file = st.file_uploader("Upload an image of the item (e.g., Plastic bottle, Pizza box)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Item", use_column_width=True)
    
    if st.button("Analyze with EcoSort Agent"):
        with st.spinner("Vision Agent analyzing..."):
            st.success("Item Identified: **PET Plastic Bottle**")
        
        with st.spinner("Researcher Agent checking local municipal rules..."):
            st.info("Local Rule Found: Plastic bottles must be emptied and crushed.")
            
        st.success("✅ **Action:** Place in the **Blue Recycling Bin**.")
        st.balloons()

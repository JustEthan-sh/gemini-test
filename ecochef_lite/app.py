import streamlit as st
import vision
import db
import chef # Import chef module

# Initialize the database
db.init_db()

st.set_page_config(page_title="EcoChef Lite", page_icon="🥦")

st.title("🥦 EcoChef Lite")
st.subheader("The Terminal-Grade Kitchen OS.")

st.write("Welcome to EcoChef Lite! Your AI-powered assistant to minimize food waste.")

# Create tabs for different modules
tab1, tab2, tab3 = st.tabs(["Snap & Audit", "Virtual Pantry", "Chef's Logic"])

with tab1:
    vision.ingest_module()

with tab2:
    st.header("🛒 Virtual Pantry")

    st.subheader("Add New Item")
    with st.form("add_item_form", clear_on_submit=True):
        item_name = st.text_input("Item Name")
        col1, col2 = st.columns(2)
        with col1:
            quantity = st.text_input("Quantity (e.g., 1, 500g)")
        with col2:
            days_until_expiry = st.number_input("Days until Expiry (optional)", min_value=0, value=7)
        category = st.text_input("Category (e.g., Fruit, Vegetable, Dairy)")
        
        submitted = st.form_submit_button("Add Item")
        if submitted:
            if item_name:
                db.add_item(item_name, quantity, days_until_expiry, category)
                st.success(f"Added {item_name} to your pantry!")
            else:
                st.error("Item Name cannot be empty.")

    st.subheader("Your Current Inventory")
    inventory_items = db.get_all_items() # Get current inventory for chef module
    if inventory_items:
        for item in inventory_items:
            item_id, name, qty, expiry, cat = item
            col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1, 1])
            with col1:
                st.write(name)
            with col2:
                st.write(qty)
            with col3:
                st.write(f"{expiry} days")
            with col4:
                st.write(cat)
            with col6:
                if st.button("Delete", key=f"delete_{item_id}"):
                    db.delete_item(item_id)
                    st.experimental_rerun()
    else:
        st.info("Your pantry is empty. Add some items!")

with tab3:
    chef.chef_module(inventory_items) # Call chef_module here with inventory

# Sidebar for navigation or quick actions
st.sidebar.title("Navigation")
st.sidebar.write("More features coming soon!")

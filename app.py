
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Online Shopping Prediction",
    page_icon="🛒",
    layout="wide"
)

@st.cache_resource
def load_model():
    data = joblib.load("purchase_prediction_model.pkl")
    return data["model"], data["columns"]

model, model_columns = load_model()

st.title("🛒 Online Shopping Purchase Prediction")
st.write("Predict whether a website visitor is likely to make a purchase.")
st.divider()

st.subheader("Visitor Information")

col1, col2 = st.columns(2)

with col1:
    st.write("**Browsing Activity**")

    administrative = st.number_input("Administrative Pages", min_value=0, value=0)
    administrative_duration = st.number_input("Administrative Duration", min_value=0.0, value=0.0)

    informational = st.number_input("Informational Pages", min_value=0, value=0)
    informational_duration = st.number_input("Informational Duration", min_value=0.0, value=0.0)

    product_related = st.number_input("Product Related Pages", min_value=0, value=1)
    product_duration = st.number_input("Product Related Duration", min_value=0.0, value=0.0)

with col2:
    st.write("**Visitor Details**")

    bounce_rates = st.number_input("Bounce Rates", min_value=0.0, max_value=1.0, value=0.0)
    exit_rates = st.number_input("Exit Rates", min_value=0.0, max_value=1.0, value=0.0)

    page_values = st.number_input("Page Values", min_value=0.0, value=0.0)
    special_day = st.number_input("Special Day", min_value=0.0, max_value=1.0, value=0.0)

    month = st.selectbox(
        "Month",
        ["Feb", "Mar", "May", "June", "Jul", "Aug",
         "Sep", "Oct", "Nov", "Dec"]
    )

    visitor_type = st.selectbox(
        "Visitor Type",
        ["Returning_Visitor", "New_Visitor", "Other"]
    )

    weekend = st.selectbox("Weekend", [False, True])

col3, col4, col5 = st.columns(3)

with col3:
    operating_systems = st.number_input("Operating Systems", min_value=1, value=1)

with col4:
    browser = st.number_input("Browser", min_value=1, value=1)

with col5:
    region = st.number_input("Region", min_value=1, value=1)

traffic_type = st.number_input("Traffic Type", min_value=1, value=1)

st.divider()

if st.button("Predict Purchase", use_container_width=True):

    input_data = pd.DataFrame([{
        "Administrative": administrative,
        "Administrative_Duration": administrative_duration,
        "Informational": informational,
        "Informational_Duration": informational_duration,
        "ProductRelated": product_related,
        "ProductRelated_Duration": product_duration,
        "BounceRates": bounce_rates,
        "ExitRates": exit_rates,
        "PageValues": page_values,
        "SpecialDay": special_day,
        "Month": month,
        "OperatingSystems": operating_systems,
        "Browser": browser,
        "Region": region,
        "TrafficType": traffic_type,
        "VisitorType": visitor_type,
        "Weekend": weekend
    }])

    input_data = pd.get_dummies(
        input_data,
        columns=["Month", "VisitorType"],
        drop_first=True,
        dtype=int
    )

    input_data = input_data.reindex(
        columns=model_columns,
        fill_value=0
    )

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    st.metric("Purchase Probability", f"{probability:.1%}")

    if prediction:
        st.success("The visitor is likely to make a purchase!")
    else:
        st.warning("The visitor is unlikely to make a purchase.")

    st.progress(float(probability))

st.divider()
st.caption("Machine Learning Project | Online Shopping Purchase Prediction")

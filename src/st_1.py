import streamlit as st

from modules.simple_ml_models import HousePriceModel


if __name__ == "__main__":
    house_price_model = HousePriceModel()

    st.title("HousePriceModel")


    with st.form("my_form"):
        n_floors = st.number_input("n_floors", min_value=0, max_value=10, value=1)
        area = st.slider("area", min_value=1, max_value=300, value=50)
        heating = st.radio("heating", ("A", "B", "C"), index=0)

        submitted = st.form_submit_button("Submit")
        if submitted:
            result_price = house_price_model(n_floors=n_floors, area=area, heating=heating)
            st.write(f"Price: {result_price}")
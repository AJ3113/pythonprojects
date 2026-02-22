import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
def generate_house_data(n_samples=100):
  np.random.seed(50)
  size=np.random.normal(1400,50,n_samples)
  price=size*50+np.random.normal(0,50,n_samples)
  return pd.DataFrame({'size':size,'price':price})
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
def train_model():
  df=generate_house_data(n_samples=100)
  X=df[['size']]
  Y=df[['price']]
  X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
  model=LinearRegression()
  model.fit(X_train,Y_train)
  predictions=model.predict(X_test)
  mse=mean_squared_error(Y_test,predictions)
  return model,mse
def main():
    st.title("Simple Linear Regression House Price Prediction App")
    st.write("Enter your house size to estimate its price.")

    model, mse = train_model()
    st.write(f"Model Mean Squared Error: {mse:.2f}")

    size = st.number_input('House size (sq ft)', min_value=500, max_value=2000, value=1500)

    if st.button('Predict price'):
        predicted_price = model.predict([[size]])[0][0]

        st.success(f'Estimated price: ${predicted_price:,.2f}')

        df = generate_house_data()

        fig = px.scatter(df, x='size', y='price', title="Size vs House Price")
        fig.add_scatter(
            x=[size],
            y=[predicted_price],  
            mode='markers',
            marker=dict(color='red', size=15),
            name='Prediction'
        )

        st.plotly_chart(fig)
if __name__=="__main__":
    main()
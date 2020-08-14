# Logo Classifier
Summer 2017 project: Logo Classifier

_**NOTE - THE PROJECT IN NO LONGER MAINTAINED. IT WAS NOT UPDATED SINCE 2017. IT MAY CONTAIN SECURITY VULNERABILITIES!**_

# What it does?
The project has a custom build image classifier (built in Keras) that classifies five kind of logos of food outlets: BurgerKing, KFC, PizzaHut, Dominos and Starbucks.
The user uploads the logo of one of these food outlets. The underlying Convolution Neural Network predicts the food outlet through the logo and then redirects the user to a specified urls where the coupons of that food outlet are available.

# How to use

**Note**: Project runs in Python3. All the setup steps below must be done with Python3 only.

- Install a python3 virtual environment and activate it. [optional]
- Download the dependencies
  > pip install -r requirements.txt
- Download the weights **model.h5** from [here](https://drive.google.com/file/d/1oCFuAd36ppiIJ6bxRJGXgkMO6uBfnV5K/view)
- Place the weights in the root directory of the project
- Run the server
  > python manage.py runserver
- Go to browser and open : http://localhost:8000/
- Upload the logo of one of the above mentioned five food outlets.

# Additional Information
View the complete project report in PDF format from [here](https://drive.google.com/file/d/1esL9W0pyMbwk1nG_uxvXHC2IN2Cbho03/view)

# hdb-resale-price-e2e-web-flask

This is the deployment repository for HDB Resale Price Prediction

## Flask Web Application
To visit the website, please go to https://hdb-resale-price-e2e-web-flask.onrender.com/ 

*(Note: This website is run on render.com a free website. If there is no activities on the web server, the server will sleep and it will take a minute or 2 to wake it up.)*

For overall project plan, please visit https://github.com/mlnotes2718/hdb-resale-price-end-to-end-ml-project-docs 

## Technical Details
- This flask application was deployed on render.com under free plan
- We use a static web page (`index.html`) to allow users to enter teh details of HDB Flats.
- The web page will call the prediction function in the flask app to make prediction based on the user input.
- Currently, we manually download the joblib file from the machine learning repository. We will consider a coordinated updated whenever there is an updated version. 

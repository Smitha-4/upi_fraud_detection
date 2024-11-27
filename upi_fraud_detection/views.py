from django.shortcuts import render
import pickle
import math
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')



def predict_fraud_risk(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        age = request.POST.get('age')
        trans_amount = request.POST.get('trans_amount')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        model_path = './best_DecisionTreeClassifier().pkl'
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        data = { 'trans_hour':math.randint(1,24),'trans_day':math.randint(1,31),'trans_month':math.randint(1,2),'trans_year':math.randint(2021,2024),
                'category':math.randint(1,5),'upi_number':phone_number,'age':age,'trans_amount':trans_amount,'state':state,'zip': zip_code,}
        print(data)
        fraud_risk = model.predict([data])[0]  # Assuming the model returns a single prediction
        if fraud_risk == 0:
            prediction_message = 'Low risk of fraud.'
            print(prediction_message)
        elif fraud_risk == 1:
            prediction_message = 'High risk of fraud. We strongly recommend verifying the identity.'
            print(prediction_message)
        else:
            prediction_message = 'Fraud risk prediction unavailable.'
            print(prediction_message)

        return render(request, 'index.html', {'prediction': prediction_message})

    
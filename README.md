# 🚀 Spend Sense – Smart Payment Recommendation for Travelers  

Spend Sense is an **AI-powered financial assistant** that helps users decide whether to **use Digital or Cash payments while traveling**.  
It leverages a **custom Decision Engine (ML + Data Analysis)**, powered by **FastAPI** and deployed on **Azure**, making integration effortless with **a single API call**.  

- **change branch to deployement_Azure to get deployed version**
---

## 🌟 Features  

✅ **AI-Powered Payment Recommendations** – Data-driven insights for smarter financial decisions.  
✅ **FastAPI-Powered ML Model** – Ensures quick and reliable predictions.  
✅ **Simple API Integration** – Requires just one API request.  
✅ **Azure Deployment** – Secure, scalable, and cloud-hosted.  

---

## 🔧 How It Works  

Spend Sense analyzes **network conditions, service providers, and location-based financial trends** to suggest the most suitable payment method.  

### 🖥️ API Documentation  

#### 🔹 **Endpoint**  
```http
https://spendsensedev.azurewebsites.net/predict
{
    "Content-Type": "application/json"
}
```
```JSON BODY
{
    "service_provider": "AIRTEL",
    "network_type": "3G",
    "start_loc": "Delhi",
    "end_loc": "Delhi"
}
```
## Deployement
- Hosted on: Microsoft Azure
- Backend Framework: FastAPI
- Machine Learning: Custom Decision Engine (ML + Data Analysis)
- API Structure: Single POST request for seamless integration

Architect & Lead Developer: Nitish Mathur

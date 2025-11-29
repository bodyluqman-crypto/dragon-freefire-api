from flask import Flask, request, Response
import requests
import json
from datetime import datetime

app = Flask(__name__)

# المفاتيح النشطة
API_KEYS = {
    "dragon123": {"status": "active", "created": "2025-11-29", "expires": "2025-12-29"},
    "dragon456": {"status": "active", "created": "2025-11-29", "expires": "2025-12-29"}
}

@app.route('/')
def home():
    return {"message": "DRAGON API", "developer": "DRAGON"}

@app.route('/bancheck')
def bancheck():
    key = request.args.get('key', '')
    uid = request.args.get('uid', '')
    
    if key not in API_KEYS:
        return {"error": "مفتاح غير صحيح"}
    
    # هنا كود فحص البان الحقيقي
    return {
        "status": "NOT BANNED", 
        "uid": uid, 
        "developer": "DRAGON",
        "message": "تم الفحص بنجاح"
    }

if __name__ == '__main__':
    app.run()

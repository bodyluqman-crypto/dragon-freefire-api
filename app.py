from flask import Flask, jsonify, request

app = Flask(__name__)

API_KEYS = {
    "dragon123": "active",
    "dragon456": "active"
}

@app.route('/')
def home():
    return jsonify({
        "message": "🚀 DRAGON Free Fire API", 
        "developer": "DRAGON",
        "status": "working"
    })

@app.route('/bancheck')
def bancheck():
    api_key = request.args.get('key', '')
    player_id = request.args.get('uid', '')
    
    if api_key not in API_KEYS:
        return jsonify({"error": "Invalid API key"})
    
    if not player_id:
        return jsonify({"error": "Player ID required"})
    
    return jsonify({
        "status": "NOT BANNED",
        "player_id": player_id,
        "developer": "DRAGON",
        "message": "Success"
    })

if __name__ == '__main__':
    app.run()

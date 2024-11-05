from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
anomalies = []

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/log_anomaly', methods=['POST'])
def log_anomaly():
    new_log = request.get_json()  
    
    if new_log:
        new_log['new'] = True
        anomalies.append(new_log)  
        print("Anomaly added:", new_log)  
        return jsonify({'status': 'Anomaly logged'}), 200
    else:
        print("No data received")  
        return jsonify({'status': 'No data received'}), 400
'''
@app.route('/anomalies')
def show_anomalies():
    # Clear the 'new' flag after anomalies are fetched
    for anomaly in anomalies:
        anomaly['new'] = False
    return jsonify(anomalies)
'''
@app.route('/anomalies')
def show_anomalies():
    '''
    anomalies = [
    {
        "user_id": "user1",
        "timestamp": "2024-11-03T10:15:30",
        "action_type": "data_transfer",
        "resource": "server2",
        "action_details": "unusually large data transfer",
        "new": True
    }
]'''

    print(anomalies)  
    return jsonify(anomalies)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from agent import call_agent


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-agent-response', methods=['POST'])
def get_agent_response():
    user_prompt = request.form['user-prompt']
    response = call_agent(user_prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
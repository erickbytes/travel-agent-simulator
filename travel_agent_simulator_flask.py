from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <form action="/run" method="post">
            <button type="submit">Run Script</button>
        </form>
    ''')

@app.route('/run', methods=['POST'])
def run_script():
    result = subprocess.run(['python', 'travel_agent_simulator_basic.py'], capture_output=True, text=True)
    return f"<pre>{result.stdout}</pre>"

if __name__ == '__main__':
    app.run(debug=True)

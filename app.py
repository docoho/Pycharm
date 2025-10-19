from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome. Use /job?jobname=xxx'
@app.route('/job', methods=['GET'])
def job_handler():
    jobname = request.args.get('jobname')

    if jobname == 'normal':
        return '0'
    elif jobname == 'error':
        return '1'
    elif jobname == 'timeout':
        time.sleep(3600)  # 等待1小时
        return '0'
    else:
        return 'Invalid jobname', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# This code uses the 'psutil' library to monitor system resources such as CPU and memory utilization.
# The 'Flask' library is imported to create a web application.
import psutil
from flask import Flask, render_template

# The 'app' object is created as a Flask application.
app = Flask(__name__)

# The '@app.route("/")' decorator defines the root URL endpoint for the web application.
@app.route("/")

# The 'index()' function is executed when the root URL is accessed.
def index():
    cpu_percent = psutil.cpu_percent()  # Get the CPU utilization percentage
    memory_percent = psutil.virtual_memory().percent  # Get the memory utilization percentage
    Message = None  # Initialize the message variable

    # Check if CPU or memory utilization is above 80%
    if cpu_percent > 80 or memory_percent > 80:
        Message = "High CPU or memory utilization detected. Please scale up."

    # Render the HTML template and pass the CPU and memory utilization values, and the message
    return render_template("index.html", cpu_percent=cpu_percent, memory_percent=memory_percent, message=Message)

# The 'app.run()' function is called to run the Flask application with debugging enabled on the host '0.0.0.0'.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

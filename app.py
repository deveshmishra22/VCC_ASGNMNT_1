from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    page = request.args.get("page")

    # Assignment Details 
    assignment_section = ""
    if page == "assignment":
        assignment_section = """
        <hr>
        <h2>Assignment Details</h2>

        <p><b>Student Name:</b> Devesh</p>
        <p><b>Title:</b> Microservice Deployment Using VMs</p>

        <h3>Architecture</h3>
        <ul>
            <li>Host OS: Windows</li>
            <li>Virtualization Tool: VirtualBox</li>
            <li>VM1_MicroserviceHost: Ubuntu Server + Python3 + venv</li>
            <li>                      NAT: 10.0.2.15/24 </li>
            <li>                      Local: 192.168.100.10/24 Port:5000 </li>
            <li>VM2_CLIENT: UI based Ubuntu Server with Browser + Curl +Lynx </li>
            <li>                      NAT: 10.0.2.15/24 </li>
            <li>                      local : 192.168.100.11/24 </li> 
            
        </ul>

        <h3>Submission Links</h3>
        <ul>
            <li>
                <a href="https://github.com/deveshmishra22/VCC_ASGNMNT_1" target="_blank">
                    GitHub Repos Link
                </a>
            </li>
            <li>
                <a href="https://drive.google.com/drive/folders/1G3WBMpvM29YFNkKrF4bc8cdj-JgyKGdB?usp=sharing" target="_blank">
                    Video with Voice-over Link
                </a>
            </li>
        </ul>
        """

    return f"""
    <html>
        <head>
            <title>Microservice Client Page</title>
        </head>
        <body>
            <h1>Microservice Deployment</h1>

            <p>
                This page is accessed from <b>Client VM2 </b> and served by the
                <b>VM1 Microservice Host</b> over an internal network.
            </p>

            <h3>Navigation</h3>
            <ul>
                <li>
                    <a href="/health">Health Status</a>
                </li>
                <li>
                    <a href="/?page=assignment">Assignment Details</a>
                </li>
            </ul>

            {assignment_section}
        </body>
    </html>
    """

# -------------------------------------------------
# HEALTH API (JSON)
# -------------------------------------------------
@app.route('/health')
def health():
    return jsonify(
        status="UP",
        service="Asgnmnt Server Health"
    )

# -------------------------------------------------
# APPLICATION ENTRY POINT
# -------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

import os
import requests
from datetime import datetime
from flask import Flask, render_template_string, request

# ==========================================
#   Discord Token Manager -- Made by Haribo
# ==========================================

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Discord Token Manager -- Made by Haribo --</title>
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 1100px;
            margin: 0 auto;
            background-color: #1e1e1e;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.6);
        }
        h2 {
            text-align: center;
            color: #5865F2;
            margin-bottom: 5px;
        }
        .signature {
            text-align: center;
            color: #00ffcc;
            font-size: 13px;
            font-style: italic;
            margin-bottom: 25px;
        }
        .input-box {
            background-color: #2d2d2d;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        input[type="text"] {
            width: calc(100% - 120px);
            background-color: #181818;
            color: #00ffcc;
            border: 1px solid #444;
            border-radius: 6px;
            padding: 10px;
            font-family: monospace;
            font-size: 13px;
        }
        button {
            padding: 10px 20px;
            background-color: #5865F2;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 14px;
            font-weight: bold;
            cursor: pointer;
            margin-left: 10px;
        }
        button:hover { background-color: #4752C4; }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: #181818;
            border-radius: 8px;
            overflow: hidden;
        }
        th, td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #333;
            font-size: 13px;
        }
        th { background-color: #252525; color: #00ffcc; }
        tr:hover { background-color: #222222; }
        .btn-action {
            padding: 5px 10px;
            font-size: 12px;
            margin-right: 5px;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
        }
        .btn-login { background-color: #2fa84f; color: white; }
    </style>
</head>
<body>
    <div class="container">
        <h2>⚡ Discord Token Manager</h2>
        <div class="signature">-- Made by Haribo --</div>
        
        <!-- Kesinlikle patlamayan düz form submit -->
        <form action="/" method="POST" class="input-box">
            <input type="text" name="token" placeholder="Enter token here (e.g. MTM3NjYyOD...)" required>
            <button type="submit">Check Token</button>
        </form>

        <h3 style="color: #a0a0a0; margin-top: 30px;">Scanned Accounts</h3>
        <table id="tokenTable">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Username</th>
                    <th>Nitro</th>
                    <th>Creation Date</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {% if results %}
                    {% for item in results %}
                    <tr>
                        <td>{{ loop.index }}</td>
                        <td>{{ item.username }}</td>
                        <td>{{ item.nitro }}</td>
                        <td>{{ item.created_at }}</td>
                        <td>
                            <a class="btn-action btn-login" href="https://discord.com/login" target="_blank" onclick="navigator.clipboard.writeText('{{ item.token }}')">Copy Token & Login</a>
                        </td>
                    </tr>
                    {% endfor %}
                {% else %}
                    <tr><td colspan="5" style="text-align: center; color: #777;">No tokens checked yet. Enter one above.</td></tr>
                {% endif %}
            </tbody>
        </table>
    </div>
</body>
</html>
"""

# Geçici hafızada taranan hesapları tutalım
checked_accounts = []

@app.route("/", methods=["GET", "POST"])
def index():
    global checked_accounts
    if request.method == "POST":
        token = request.form.get("token", "").strip().strip('"').strip("'")
        if token:
            headers = {
                "Authorization": token,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
            try:
                print(f"[*] Checking token via Form POST: {token[:15]}...")
                r = requests.get("https://discord.com/api/v9/users/@me", headers=headers, timeout=5)
                
                if r.status_code == 200:
                    user_data = r.json()
                    sub_r = requests.get("https://discord.com/api/v9/users/@me/billing/subscriptions", headers=headers, timeout=5)
                    has_nitro = False
                    if sub_r.status_code == 200 and len(sub_r.json()) > 0:
                        has_nitro = True
                        
                    user_id = int(user_data.get("id", 0))
                    timestamp = ((user_id >> 22) + 1420070400000) / 1000
                    creation_date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                    
                    # Listeye ekle (aynı token varsa ekleme)
                    if not any(acc['token'] == token for acc in checked_accounts):
                        checked_accounts.append({
                            "token": token,
                            "username": f"{user_data.get('username')}#{user_data.get('discriminator', '0')}",
                            "email": user_data.get("email"),
                            "phone": user_data.get("phone"),
                            "nitro": "Active 🚀" if has_nitro else "None ❌",
                            "created_at": creation_date
                        })
                    print("[SUCCESS] Token added to list!")
                else:
                    print(f"[-] Invalid token! Status: {r.status_code}")
            except Exception as e:
                print(f"[-] Error: {e}")

    return render_template_string(HTML_TEMPLATE, results=checked_accounts)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
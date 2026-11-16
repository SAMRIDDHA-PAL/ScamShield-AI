async function checkScam() {
    const text = document.getElementById('callText').value;
    const resultDiv = document.getElementById('result');
    
    if (!text.trim()) {
        alert("Paste the text!");
        return;
    }

    resultDiv.style.display = 'block';
    document.getElementById('resultTitle').innerText = "Analyzing... Please Wait...";
    document.getElementById('riskText').innerText = "";
    document.getElementById('reasonsList').innerHTML = "";
    document.getElementById('actionText').innerText = "";

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();
        console.log(data);

        document.getElementById('resultTitle').innerText = data.result || "No Result";
        document.getElementById('resultTitle').style.color = data.result.includes("SCAM") ? "red" : "green";
        
        document.getElementById('scoreFill').style.width = data.risk_score + "%";
        document.getElementById('scoreFill').style.background = data.risk_score > 60 ? "red" : "green";
        document.getElementById('riskText').innerText = "Risk Score: " + data.risk_score + "/100";
        
        document.getElementById('reasonsList').innerHTML = data.reasons.map(r => `<li>${r}</li>`).join('');
        document.getElementById('actionText').innerText = data.action;

    } catch (error) {
        console.log(error);
        document.getElementById('resultTitle').innerText = "Error! Backend connect hochhe na. Terminal check koro.";
    }
}

function fillDemo1() {
    document.getElementById('callText').value = "Hello sir, I am calling from SBI Bank. Your account will be blocked in 2 hours. Please share your OTP 482913 to verify.";
}

function fillDemo2() {
    document.getElementById('callText').value = "Hi, this is your delivery boy. Your parcel has arrived, please come downstairs.";
}

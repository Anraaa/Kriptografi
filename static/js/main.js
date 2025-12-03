const API = "http://localhost:5000";

async function encrypt() {
    const file = document.getElementById("enc_file").files[0];
    const key = document.getElementById("enc_key").value;

    let form = new FormData();
    form.append("file", file);
    form.append("key", key);

    let resp = await fetch(`${API}/encrypt`, {
        method: "POST",
        body: form
    });

    let blob = await resp.blob();
    download(blob, "encrypted.bf");
}

async function decrypt() {
    const file = document.getElementById("dec_file").files[0];
    const key = document.getElementById("dec_key").value;

    let form = new FormData();
    form.append("file", file);
    form.append("key", key);

    let resp = await fetch(`${API}/decrypt`, {
        method: "POST",
        body: form
    });

    let blob = await resp.blob();
    download(blob, "decrypted_output");
}

function download(blob, filename) {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    a.click();
    window.URL.revokeObjectURL(url);
}

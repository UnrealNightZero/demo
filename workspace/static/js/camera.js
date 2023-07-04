function OpenCanera(){
    navigator.mediaDevices.getUserMedia({video: true})
            .then(stream => {
                const video = document.getElementById("video");
                video.srcObject = stream;
            })
            .catch(error => {
                console.log("Error accessing camera:", error);
            })
}

function take_picture(){
    const video = document.getElementById("video");
	const canvas = document.getElementById("canvas");
    canvas.width = video.videoWidth;
	canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    const img = canvas.toDataURL('image/jpeg');

    fetch('/processImage',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            userId: 1,
            imageData: img
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Image processed:", data);
        const result = document.getElementById("result");
        result.src = data.imageData;
        result.style.display = "block";
    })
    .catch(error => {
        console.error("Error processing image:", error);
    });
}

document.querySelector("#showVideo").addEventListener("click", OpenCanera);

document.querySelector("#take_picture").addEventListener("click", take_picture);
  // 1. Click Photo
    function clickPhoto() {
      navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
        videoEl.srcObject = stream;
        setTimeout(() => {
          canvasEl.width = videoEl.videoWidth;
          canvasEl.height = videoEl.videoHeight;
          canvasEl.getContext('2d').drawImage(videoEl, 0, 0);
          const photo = canvasEl.toDataURL('image/png');
          photoDownload.href = photo;
          photoDownload.download = "photo.png";
          photoDownload.style.display = "inline";
          stream.getTracks().forEach(track => track.stop());
          alert("📸 Photo clicked!");
        }, 3000);
      }).catch(err => alert("Camera not accessible"));
    }
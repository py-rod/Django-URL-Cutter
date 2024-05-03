function downloadQRimage() {
    const pathImg = document.getElementById('download_qr_image')

    let canvas = document.createElement('canvas')
    let context = canvas.getContext('2d')


    canvas.width = pathImg.clientWidth * 5
    canvas.height = pathImg.clientHeight * 5


    context.drawImage(pathImg, 0, 0, canvas.width, canvas.height)

    canvas.toBlob(function (blob) {
        saveAs(blob, 'qr_image.png')
    })
}

document.getElementById('download_qr_link').addEventListener('click', function (event) {
    event.preventDefault()

    downloadQRimage();
})

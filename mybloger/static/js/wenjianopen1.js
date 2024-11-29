const canvas = document.getElementById('drawCanvas');
const ctx = canvas.getContext('2d');
const openButton = document.querySelector('.open-button');
const changButton = document.querySelector('.chang-button');
const ellipseButton = document.querySelector('.ellipse-button');
const lineButton = document.querySelector('.line-button');
const polygonButton = document.querySelector('.polygon-button');
const saveButton = document.querySelector('.save-button');
const saveAsButton = document.querySelector('.save-as-button');
const fileInput = document.getElementById('fileInput');


openButton.addEventListener('click', () => {
    fileInput.click();
});



// fileInput.addEventListener('change', function (event) {
//     const files = event.target.files;
//     if (files.length > 0) {
//         const file = files[0];
//         const reader = new FileReader();
//         reader.onload = function (e) {
//             const img = new Image();
//             img.onload = function () {
//                 // 获取图片的宽高
//                 const imgWidth = img.width;
//                 const imgHeight = img.height;

//                 // 获取画布容器的宽高（这里假设与CSS中设置的相同）
//                 const canvasContainerWidth = 800;
//                 const canvasContainerHeight = 600;

//                 // 计算缩放比例
//                 let scaleWidth = canvasContainerWidth / imgWidth;
//                 let scaleHeight = canvasContainerHeight / imgHeight;
//                 let scale = Math.min(scaleWidth, scaleHeight); // 取较小的比例以保证图片不被裁剪

//                 // 计算画布的实际尺寸（保持宽高比）
//                 const canvasWidth = imgWidth * scale;
//                 const canvasHeight = imgHeight * scale;

//                 // 设置画布的宽高（这将影响绘制区域的大小）
//                 canvas.width = canvasWidth * 1.5;
//                 canvas.height = canvasHeight * 1.5;

//                 // 获取画布的上下文
//                 const ctx = canvas.getContext('2d');

//                 // 清除画布上的旧内容（如果有的话）
//                 ctx.clearRect(0, 0, canvasWidth * 1.5, canvasHeight);

//                 // 计算图片在画布上的绘制位置，以确保居中
//                 const x = (canvasContainerWidth - canvasWidth) / 2;
//                 const y = (canvasContainerHeight - canvasHeight) / 2;

//                 // 绘制图片到画布上（此时图片已经等比例缩放并居中）
//                 ctx.drawImage(img, x, y, canvasWidth * 1.5, canvasHeight * 1.5);
//             };
//             img.src = e.target.result;
//         };
//         reader.readAsDataURL(file);
//     }
// });


// fileInput.addEventListener('change', function(event) {
//     const files = event.target.files;
//     if (files.length > 0) {
//         const file = files[0];
//         const reader = new FileReader();
//         reader.onload = function(e) {
//             const img = new Image();
//             img.onload = function() {
//                 canvas.width = img.width;
//                 canvas.height = img.height;
//                 ctx.drawImage(img, 0, 0, img.width, img.height);
//             };
//             img.src = e.target.result;
//         }
//         reader.readAsDataURL(file);
//     }
// });

let isDrawing = false;
let startX, startY;
let img = new Image();

fileInput.addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(event) {
            img.onload = function() {
                canvas.width = img.width;
                canvas.height = img.height;
                ctx.drawImage(img, 0, 0);
            };
            img.src = event.target.result;
        };
        reader.readAsDataURL(file);
    }
});


changButton.addEventListener('click', () => {
    isDrawing = true;
    
    savecurrent();
});
 


canvas.addEventListener('mousedown', function(e) {
    if (isDrawing) {
        const rect = canvas.getBoundingClientRect();
        startX = e.clientX - rect.left/2;
        startY = e.clientY - rect.top/2;
    }
});
 
canvas.addEventListener('mousemove', function(e) {
    if (isDrawing) {
        const rect = canvas.getBoundingClientRect();
        const currentX = e.clientX - rect.left/2;
        const currentY = e.clientY - rect.top/2;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height); // 重新绘制图片
        ctx.strokeStyle = 'red'; // 设置线条颜色为红色
        ctx.setLineDash([5, 5]); // 设置虚线样式，5个单位的实线和5个单位的空白
        ctx.lineWidth = 2; // 设置线条宽度
        ctx.strokeRect(startX, startY, currentX - startX, currentY - startY); // 绘制虚线框
    }
});

canvas.addEventListener('mouseup', function() {
    saveCurrentState();
    if (!isDrawing) return;
    isDrawing = false;
});

function saveCurrentState() {
    const dataURL = canvas.toDataURL('image/png');
    img.src = dataURL;
}


// 直线绘制	 
// let isDrawing = false;
// let startX, startY;

// changButton.addEventListener('click', () => {
//     isDrawing = true;
// });

// canvas.addEventListener('mousedown', function (e) {
//     if (!isDrawing) return;
//     startX = e.offsetX;
//     startY = e.offsetY;
//     ctx.beginPath();
//     ctx.moveTo(startX, startY);
// });

// canvas.addEventListener('mousemove', function (e) {
//     if (!isDrawing) return;
//     const x = e.offsetX;
//     const y = e.offsetY;
//     ctx.lineTo(x, y);
//     ctx.strokeStyle = 'red';
//     ctx.lineWidth = 2;
//     ctx.stroke();
// });

// canvas.addEventListener('mouseup', function () {
//     if (!isDrawing) return;
//     isDrawing = false;
//     ctx.closePath();
// });





saveButton.addEventListener('click', function () {
    const dataURL = canvas.toDataURL('image/png');
    const link = document.createElement('a');
    link.href = dataURL;
    link.download = 'annotated-image.png';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
});

saveAsButton.addEventListener('click', function () {
    // 获取用户输入的文件名
    const filename = prompt("请输入文件名：", "annotated-image.png");
    if (filename) {
        // 如果用户输入了文件名，使用该文件名保存图片
        const dataURL = canvas.toDataURL('image/png');
        const link = document.createElement('a');
        link.href = dataURL;
        // 确保文件名有正确的扩展名
        const safeFilename = filename.replace(/[^a-zA-Z0-9.]/g, '_') + '.png';
        link.download = safeFilename;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
});
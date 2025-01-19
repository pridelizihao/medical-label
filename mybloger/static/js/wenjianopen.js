  // 打开按钮点击事件
  const openButton = document.querySelector('.open-button');
  openButton.addEventListener('click', () => {
    const fileInput = document.getElementById('fileInput');
    fileInput.click(); // 触发文件选择
  });
  
  //文件选择输入框的change事件
  const fileInput = document.getElementById('fileInput');
  const imagesContainer = document.getElementById('images-container');
  fileInput.addEventListener('change', function (event) {
    const files = event.target.files;
    imagesContainer.innerHTML = ''; // 清空之前的图片
    for (let i = 0; i < files.length; i++) {
      const file = files[i];
      if (file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = function (e) {
          const imgElement = document.createElement('img');
          imgElement.src = e.target.result;
          imgElement.style.maxWidth = '100%';
          imgElement.style.maxHeight = '100%';
          imagesContainer.appendChild(imgElement);
        };
        reader.readAsDataURL(file);
      }
    }
  });
  
      
  
  
      // 保存带有标注的图片的函数
      function saveAnnotatedImage() {
        // 获取 canvas 元素和绘图上下文
        const canvas = document.getElementById('drawCanvas');
        const ctx = canvas.getContext('2d');
  
        // 确保 canvas 大小与图片匹配
        const img = imagesContainer.querySelector('img');
        if (img) {
          canvas.width = img.offsetWidth;
          canvas.height = img.offsetHeight;
          // 将图片绘制到 canvas 上
          ctx.drawImage(img, 0, 0, img.offsetWidth, img.offsetHeight);
        }
  
        // 遍历所有的矩形标注并绘制到 canvas 上
        const rectangles = document.querySelectorAll('.rectangle-overlay');
        rectangles.forEach(rect => {
          ctx.strokeStyle = window.getComputedStyle(rect).borderColor;
          ctx.lineWidth = parseInt(window.getComputedStyle(rect).borderWidth);
          ctx.strokeRect(rect.offsetLeft, rect.offsetTop, rect.offsetWidth, rect.offsetHeight);
        });
  
        // 将 canvas 转换为 PNG 图片的数据 URL
        const dataURL = canvas.toDataURL('image/png');
        // 创建一个下载链接
        const link = document.createElement('a');
        // 设置链接的 href 为数据 URL
        link.href = dataURL;
        // 设置下载的文件名
        link.download = 'annotated-image.png';
        // 模拟点击链接以触发下载
        link.click();
      }
  
      // 获取保存按钮元素，并为其添加点击事件监听器
      const saveButton = document.querySelector('.save-button');
      saveButton.addEventListener('click', saveAnnotatedImage);
      保存带有标注的图片的函数
    // function saveAnnotatedImage() {
    //   // 获取 canvas 元素
    //   const canvas = document.getElementById('drawCanvas');
  
    //   // 将 canvas 转换为 PNG 图片的数据 URL
    //   const dataURL = canvas.toDataURL('image/png');
  
    //   // 创建一个下载链接
    //   const link = document.createElement('a');
    //   // 设置链接的 href 为数据 URL
    //   link.href = dataURL;
    //   // 设置下载的文件名
    //   link.download = 'annotated-image.png';
    //   // 将链接添加到文档中
    //   document.body.appendChild(link);
    //   // 模拟点击链接以触发下载
    //   link.click();
    //   // 从文档中移除链接
    //   document.body.removeChild(link);
    // }
  
    // // 获取保存按钮元素，并为其添加点击事件监听器
    // const saveButton = document.querySelector('.save-button');
    // saveButton.addEventListener('click', saveAnnotatedImage);
  
      
  
      //另存为
      function saveAsImages() {
        const images = document.querySelectorAll('#images-container img');
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
  
        let totalWidth = 0;
        let maxHeight = 0;
  
        // 计算总宽度和最大高度
        images.forEach((img, index) => {
          const imgWidth = img.width;
          const imgHeight = img.height;
          maxHeight = Math.max(maxHeight, imgHeight);
          if (index === 0) {
            totalWidth += imgWidth;
          } else {
            totalWidth += imgWidth + 10; // 假设每张图片之间有10px的间隔
          }
        });
  
        canvas.width = totalWidth;
        canvas.height = maxHeight;
  
        // 将图片绘制到canvas上
        let currentX = 0;
        images.forEach((img, index) => {
          const imgWidth = img.width;
          const imgHeight = img.height;
          ctx.drawImage(img, currentX, 0, imgWidth, imgHeight);
          if (index === 0) {
            currentX += imgWidth;
          } else {
            currentX += imgWidth + 10; // 假设每张图片之间有10px的间隔
          }
        });
  
        // 将canvas转换为Blob对象
        canvas.toBlob((blob) => {
          // 使用FileSaver.js保存图片
          const filename = prompt("请输入文件名：", "image.png"); // 允许用户输入文件名
          if (filename) {
            saveAs(blob, filename);
          }
        }, 'image/png');
      }
  
      // 点击另存为按钮显示另存为的选项
      const saveAsButton = document.querySelector('.save-as-button');
      saveAsButton.addEventListener('click', saveAsImages);
  
    //   let isDrawingRectangle = false;
    //   let startXRectangle, startYRectangle;
  
    //   const rectButton = document.querySelector('.chang-button');
    //   rectButton.addEventListener('click', () => {
    //     document.body.style.cursor = 'crosshair';
    //     isDrawingRectangle = true;
    //   });
  
    //   canvas.addEventListener('mousedown', handleMouseDownRectangle);
    //   canvas.addEventListener('mousemove', handleMouseMoveRectangle);
    //   canvas.addEventListener('mouseup', handleMouseUpRectangle);
  
    //   function handleMouseDownRectangle(e) {
    //       if (isDrawingRectangle) {
    //           startXRectangle = e.offsetX;
    //           startYRectangle = e.offsetY;
    //           ctx.beginPath();
    //           ctx.moveTo(startXRectangle, startYRectangle);
    //       }
    //   }
  
      // function handleMouseMoveRectangle(e) {
      //     if (!isDrawingRectangle) return;
  
      //     // 清空画布
      //     ctx.clearRect(0, 0, canvas.width, canvas.height);
  
      //     // 绘制背景图片
      //     const img = document.getElementById('sourceImage');
      //     ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
  
      //     // 绘制矩形
      //     const x = e.offsetX;
      //     const y = e.offsetY;
      //     ctx.strokeStyle = 'red'; // 矩形边框颜色
      //     ctx.lineWidth = 2; // 矩形边框宽度
      //     ctx.strokeRect(startXRectangle, startYRectangle, x - startXRectangle, y - startYRectangle);
      // }
  
      // function handleMouseUpRectangle() {
      //     if (!isDrawingRectangle) return;
      //     isDrawingRectangle = false;
      //      ctx.closePath();
      // }
  
      // // 确保 canvas 大小与图片匹配
      // const img = document.getElementById('sourceImage');
      // if (img) {
      //     canvas.width = img.offsetWidth;
      //     canvas.height = img.offsetHeight;
      // }


    isDrawingRectangle = false;
    //矩形按钮点击事件
    const rectButton = document.querySelector('.chang-button');
      rectButton.addEventListener('click', () => {
        document.body.style.cursor = 'crosshair';
        isDrawingRectangle = true;
      });
  
      imagesContainer.addEventListener('mousedown', handleMouseDownRectangle);
  
      function handleMouseDownRectangle(e) {
        if (e.target.tagName === 'IMG' && isDrawingRectangle) {
          startXRectangle = e.offsetX;
          startYRectangle = e.offsetY;
          rectOverlayRectangle = document.createElement('div');
          rectOverlayRectangle.className = 'rectangle-overlay';
          imagesContainer.appendChild(rectOverlayRectangle);
          currentImage = e.target;
          if (currentImage) {
            currentImage.style.pointerEvents = 'none';
          }
          imagesContainer.addEventListener('mousemove', handleMouseMoveRectangle);
          imagesContainer.addEventListener('mouseup', handleMouseUpRectangle);
        }
      }
  
      function handleMouseMoveRectangle(e) {
        if (!isDrawingRectangle) return;
        const x = Math.min(startXRectangle, e.offsetX);
        const y = Math.min(startYRectangle, e.offsetY);
        const width = Math.abs(startXRectangle - e.offsetX);
        const height = Math.abs(startYRectangle - e.offsetY);
        rectOverlayRectangle.style.left = `${x}px`;
        rectOverlayRectangle.style.top = `${y}px`;
        rectOverlayRectangle.style.width = `${width}px`;
        rectOverlayRectangle.style.height = `${height}px`;
      }
  
      function handleMouseUpRectangle() {
        if (!isDrawingRectangle) return;
        isDrawingRectangle = false;
        imagesContainer.removeEventListener('mousemove', handleMouseMoveRectangle);
        imagesContainer.removeEventListener('mouseup', handleMouseUpRectangle);
        if (currentImage) {
          currentImage.style.pointerEvents = 'auto';
        }
      }
  
      // 获取 canvas 元素和绘图上下文
      const canvas = document.getElementById('drawCanvas');
      const ctx = canvas.getContext('2d');
  
      let isDrawingEllipse = false;
      let startXEllipse, startYEllipse;
      // 确保 canvas 大小与图片匹配
      const img = imagesContainer.querySelector('img');
      if (img) {
        canvas.width = img.offsetWidth;
        canvas.height = img.offsetHeight;
      }
  
  
      // //矩形按钮点击事件
      // const rectButton = document.querySelector('.chang-button');
      // rectButton.addEventListener('click', () => {
      //   document.body.style.cursor = 'crosshair';
      //   isDrawingRectangle = true;
      // });
  
      // imagesContainer.addEventListener('mousedown', handleMouseDownRectangle);
  
      // function handleMouseDownRectangle(e) {
      //   if (e.target.tagName === 'IMG' && isDrawingRectangle) {
      //     startXRectangle = e.offsetX;
      //     startYRectangle = e.offsetY;
      //     rectOverlayRectangle = document.createElement('div');
      //     rectOverlayRectangle.className = 'rectangle-overlay';
      //     imagesContainer.appendChild(rectOverlayRectangle);
      //     currentImage = e.target;
      //     if (currentImage) {
      //       currentImage.style.pointerEvents = 'none';
      //     }
      //     imagesContainer.addEventListener('mousemove', handleMouseMoveRectangle);
      //     imagesContainer.addEventListener('mouseup', handleMouseUpRectangle);
      //   }
      // }
  
      // function handleMouseMoveRectangle(e) {
      //   if (!isDrawingRectangle) return;
      //   const x = Math.min(startXRectangle, e.offsetX);
      //   const y = Math.min(startYRectangle, e.offsetY);
      //   const width = Math.abs(startXRectangle - e.offsetX);
      //   const height = Math.abs(startYRectangle - e.offsetY);
      //   rectOverlayRectangle.style.left = `${x}px`;
      //   rectOverlayRectangle.style.top = `${y}px`;
      //   rectOverlayRectangle.style.width = `${width}px`;
      //   rectOverlayRectangle.style.height = `${height}px`;
      // }
  
      // function handleMouseUpRectangle() {
      //   if (!isDrawingRectangle) return;
      //   isDrawingRectangle = false;
      //   imagesContainer.removeEventListener('mousemove', handleMouseMoveRectangle);
      //   imagesContainer.removeEventListener('mouseup', handleMouseUpRectangle);
      //   if (currentImage) {
      //     currentImage.style.pointerEvents = 'auto';
      //   }
      // }
  
      // // 获取 canvas 元素和绘图上下文
      // const canvas = document.getElementById('drawCanvas');
      // const ctx = canvas.getContext('2d');
  
      // let isDrawingEllipse = false;
      // let startXEllipse, startYEllipse;
      // // 确保 canvas 大小与图片匹配
      // const img = imagesContainer.querySelector('img');
      // if (img) {
      //   canvas.width = img.offsetWidth;
      //   canvas.height = img.offsetHeight;
      // }
  
      
      // // 点击椭圆按钮鼠标样式为椭圆
      // const ellipseButton = document.querySelector('.ellipse-button');
      // ellipseButton.addEventListener('click', () => {
      //   document.body.style.cursor = 'crosshair';
      //   isDrawingEllipse = true;
      // });
  
      // imagesContainer.addEventListener('mousedown', handleMouseDownEllipse);
  
      // function handleMouseDownEllipse(e) {
      //   if (e.target.tagName === 'IMG' && isDrawingEllipse) {
      //     startXEllipse = e.offsetX;
      //     startYEllipse = e.offsetY;
      //     ellipseOverlayEllipse = document.createElement('div');
      //     ellipseOverlayEllipse.className = 'ellipse-overlay';
      //     imagesContainer.appendChild(ellipseOverlayEllipse);
      //     currentImage = e.target;
      //     if (currentImage) {
      //       currentImage.style.pointerEvents = 'none';
      //     }
      //     imagesContainer.addEventListener('mousemove', handleMouseMoveEllipse);
      //     imagesContainer.addEventListener('mouseup', handleMouseUpEllipse);
      //   }
      // }
  
      // function handleMouseMoveEllipse(e) {
      //   if (!isDrawingEllipse) return;
      //   const x = Math.min(startXEllipse, e.offsetX);
      //   const y = Math.min(startYEllipse, e.offsetY);
      //   const width = Math.abs(startXEllipse - e.offsetX);
      //   const height = Math.abs(startYEllipse - e.offsetY);
      //   ellipseOverlayEllipse.style.left = `${x}px`;
      //   ellipseOverlayEllipse.style.top = `${y}px`;
      //   ellipseOverlayEllipse.style.width = `${width}px`;
      //   ellipseOverlayEllipse.style.height = `${height}px`;
      // }
  
      // function handleMouseUpEllipse() {
      //   if (!isDrawingEllipse) return;
      //   isDrawingEllipse = false;
      //   imagesContainer.removeEventListener('mousemove', handleMouseMoveEllipse);
      //   imagesContainer.removeEventListener('mouseup', handleMouseUpEllipse);
      //   if (currentImage) {
      //     currentImage.style.pointerEvents = 'auto';
      //   }
      // }
  
      // // 点击直线按钮鼠标样式为直线
      // const lineButton = document.querySelector('.line-button');
      // lineButton.addEventListener('click', () => {
      //   document.body.style.cursor = 'crosshair';
      //   isDrawingLine = true;
      // });
  
      // imagesContainer.addEventListener('mousedown', handleMouseDownLine);
  
      // function handleMouseDownLine(e) {
      //   if (e.target.tagName === 'IMG' && isDrawingLine) {
      //     startXLine = e.offsetX;
      //     startYLine = e.offsetY;
      //     lineOverlayLine = document.createElement('div');
      //     lineOverlayLine.className = 'line-overlay';
      //     imagesContainer.appendChild(lineOverlayLine);
      //     currentImage = e.target;
      //     if (currentImage) {
      //       currentImage.style.pointerEvents = 'none';
      //     }
      //     imagesContainer.addEventListener('mousemove', handleMouseMoveLine);
      //     imagesContainer.addEventListener('mouseup', handleMouseUpLine);
      //   }
      // }
  
      // function handleMouseMoveLine(e) {
      //   if (!isDrawingLine) return;
      //   const x = Math.min(startXLine, e.offsetX);
      //   const y = Math.min(startYLine, e.offsetY);
      //   const width = Math.abs(startXLine - e.offsetX);
      //   const height = Math.abs(startYLine - e.offsetY);
      //   lineOverlayLine.style.left = `${x}px`;
      //   lineOverlayLine.style.top = `${y}px`;
      //   lineOverlayLine.style.width = `${width}px`;
      //   lineOverlayLine.style.height = `${height}px`;
      // }
  
      // function handleMouseUpLine() {
      //   if (!isDrawingLine) return;
      //   isDrawingLine = false;
      //   imagesContainer.removeEventListener('mousemove', handleMouseMoveLine);
      //   imagesContainer.removeEventListener('mouseup', handleMouseUpLine);
      //   if (currentImage) {
      //     currentImage.style.pointerEvents = 'auto';
      //   }
      // }
  
      // // 点击矩形按钮鼠标样式为矩形
      // const rectangleButton = document.querySelector('.rectangle-button');
      // rectangleButton.addEventListener('click', () => {
      //   document.body.style.cursor = 'crosshair';
      //   isDrawingRectangle = true;
      // });
  
      // imagesContainer.addEventListener('mousedown', handleMouseDownRectangle);
  
      // function handleMouseDownRectangle(e) {
      //   if (e.target.tagName === 'IMG' && isDrawingRectangle) {
      //     startXRectangle = e.offsetX;
      //     startYRectangle = e.offsetY;
      //     rectangleOverlayRectangle = document.createElement('div');
      //     rectangleOverlayRectangle.className = 'rectangle-overlay';
      //     imagesContainer.appendChild(rectangleOverlayRectangle);
      //     currentImage = e.target;
      //     if (currentImage) {
      //       currentImage.style.pointerEvents = 'none';
      //     }
      //     imagesContainer.addEventListener('mousemove', handleMouseMoveRectangle);
      //     imagesContainer.addEventListener('mouseup', handleMouseUpRectangle);
      //   }
      // }
  
      // function handleMouseMoveRectangle(e) {
      //   if (!isDrawingRectangle) return;
      //   const x = Math.min(startXRectangle, e.offsetX);
      //   const y = Math.min(startYRectangle, e.offsetY);
      //   const width = Math.abs(startXRectangle - e.offsetX);
      //   const height = Math.abs(startYRectangle - e.offsetY);
      //   rectangleOverlayRectangle.style.left = `${x}px`;
      //   rectangleOverlayRectangle.style.top = `${y}px`;
      //   rectangleOverlayRectangle.style.width = `${width}px`;
      //   rectangleOverlayRectangle.style.height = `${height}px`;
      // }
  
      // function handleMouseUpRectangle() {
      //   if (!isDrawingRectangle) return;
      //   isDrawingRectangle = false;
      //   imagesContainer.removeEventListener('mousemove', handleMouseMoveRectangle);
      //   imagesContainer.removeEventListener('mouseup', handleMouseUpRectangle);
      //   if (currentImage) {
      //     currentImage.style.pointerEvents = 'auto';
      //   }
      // }
  
      // // 点击圆形按钮鼠标样式为圆形
      // const circleButton = document.querySelector('.circle-button');
      // circleButton.addEventListener('click', () => {
      //   document.body.style.cursor = 'crosshair';
      //   isDrawingCircle = true;
      // });
  
      // imagesContainer.addEventListener('mousedown', handleMouseDownCircle);
  
      // function handleMouseDownCircle(e) {
      //   if (e.target.tagName === 'IMG' && isDrawingCircle) {
      //     startXCircle = e.offsetX;
      //     startYCircle = e.offsetY;
      //     circleOverlayCircle = document.createElement('div');
      //     circleOverlayCircle.className = 'circle-overlay';
      //     imagesContainer.appendChild(circleOverlayCircle);
      //     currentImage = e.target;
      //     if (currentImage) {
      //       currentImage.style.pointerEvents = 'none';
      //     }
      //     imagesContainer.addEventListener('mousemove', handleMouseMoveCircle);
      //     imagesContainer.addEventListener('mouseup', handleMouseUpCircle);
      //   }
      // }
  
      // function handleMouseMoveCircle(e) {
      //   if (!isDrawingCircle) return;
      //   const x = Math.min(startXCircle, e.offsetX);
      //   const y = Math.min(startYCircle, e.offsetY);
      //   const width = Math.abs(startXCircle - e.offsetX);
      //   const height = Math.abs(startYCircle - e.offsetY);
      //   circleOverlayCircle.style.left = `${x}px`;
      //   circleOverlayCircle.style.top = `${y}px`;
      //   circleOverlayCircle.style.width = `${width}px`;
      //   circleOverlayCircle.style.height = `${height}px`;
      // }
  
      // function handleMouseUpCircle() {
      //   if (!isDrawingCircle) return;
      //   isDrawingCircle = false;
      //   imagesContainer.removeEventListener('mousemove', handleMouseMoveCircle);
      //   imagesContainer.removeEventListener('mouseup', handleMouseUpCircle);
      //   if (currentImage) {
      //     currentImage.style.pointerEvents = 'auto';
      //   }
      // }
  
      // // 点击多边形按钮鼠标样式为多边形
      // const polygonButton = document.querySelector('.polygon-button');
      // polygonButton.addEventListener('click', () => {
      //   document.body.style.cursor = 'crosshair';
      //   isDrawingPolygon = true;
      // });
  
      // imagesContainer.addEventListener('mousedown', handleMouseDownPolygon);
  
      // function handleMouseDownPolygon(e) {
      //   if (e.target.tagName === 'IMG' && isDrawingPolygon) {
      //     startXPolygon = e.offsetX;
      //     startYPolygon = e.offsetY;
      //     polygonOverlayPolygon = document.createElement('div');
      //     polygonOverlayPolygon.className = 'polygon-overlay';
      //     imagesContainer.appendChild(polygonOverlayPolygon);
      //     currentImage = e.target;
      //     if (currentImage) {
      //       currentImage.style.pointerEvents = 'none';
      //     }
      //     imagesContainer.addEventListener('mousemove', handleMouseMovePolygon);
      //     imagesContainer.addEventListener('mouseup', handleMouseUpPolygon);
      //   }
      // }
  
      // function handleMouseMovePolygon(e) {
      //   if (!isDrawingPolygon) return;
      //   const x = Math.min(startXPolygon, e.offsetX);
      //   const y = Math.min(startYPolygon, e.offsetY);
      //   const width = Math.abs(startXPolygon - e.offsetX);
      //   const height = Math.abs(startYPolygon - e.offsetY);
      //   polygonOverlayPolygon.style.left = `${x}px`;
      //   polygonOverlayPolygon.style.top = `${y}px`;
      //   polygonOverlayPolygon.style.width = `${width}px`;
      //   polygonOverlayPolygon.style.height = `${height}px`;
      // }
  
      // function handleMouseUpPolygon() {
      //   if (!isDrawingPolygon) return;
      //   isDrawingPolygon = false;
      //   imagesContainer.removeEventListener('mousemove', handleMouseMovePolygon);
      //   imagesContainer.removeEventListener('mouseup', handleMouseUpPolygon);
      //   if (currentImage) {
      //     currentImage.style.pointerEvents = 'auto';
      //   }
      // }
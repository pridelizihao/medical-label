
    // 根据设备宽度计算html标签的font-size值
    function resetHtmlFontsize() {
    document.documentElement.style.fontSizes = screen.width / 10 + 'px'
    }
    resetHtmlFontsize()
    window.onresize = resetHtmlFontsize;
    // 文件按钮点击后显示新建打开保存另存为的选项
    const fileButton = document.querySelector('.file-button');
    const fileOptions = document.createElement('div');
    fileOptions.classList.add('file-options');
    fileOptions.innerHTML = `
        <button>新建</button>
        <br>
        <button class="open-button">打开</button>
        <br>
        <button class="save-button">保存</button>
        <br>
        <button class="save-as-button">另存为</button>
        <br>
      `;
    fileOptions.style.display = 'none';
    fileOptions.style.display = 'none'; // 确保这个样式被设置
    fileOptions.style.position = 'absolute'; // 设置为绝对定位
    fileOptions.style.left = '0px'; // 设置左边距
    fileOptions.style.top = '80px'; // 设置上边距

    // 将选项容器添加到 body 中
    document.body.appendChild(fileOptions);

    // 点击文件按钮显示或隐藏选项
    fileButton.addEventListener('click', () => {
        if (fileOptions.style.display === 'none') {
            fileOptions.style.display = 'block';
        } else {
            fileOptions.style.display = 'none';
        }
    });

    
  


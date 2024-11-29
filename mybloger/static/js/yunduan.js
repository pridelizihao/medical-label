// 云端按钮点击后显示的按钮
const transferButton = document.querySelector('.transfer-button');
const transferOptions = document.createElement('div');
transferOptions.classList.add('transfer-options');
transferOptions.innerHTML = `
  <button>接收文件</button>
  <br>
  <button>上传文件</button>
  <br>
  <button>传输文件给</button>
`;

transferOptions.style.display = 'none';
transferOptions.style.display = 'none'; // 确保这个样式被设置
transferOptions.style.position = 'absolute'; // 设置为绝对定位
transferOptions.style.left = '240px'; // 设置左边距
transferOptions.style.top = '80px'; // 设置上边距

// 将选项容器添加到 body 中
document.body.appendChild(transferOptions);

// 点击自动标注按钮按钮显示或隐藏选项
transferButton.addEventListener('click', () => {
  if (transferOptions.style.display === 'none') {
    transferOptions.style.display = 'block';
  } else {
    transferOptions.style.display = 'none';
  }
});
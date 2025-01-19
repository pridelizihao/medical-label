// 自动标注按钮点击后显示标注病变部位，标注健康部位的按钮
const autoButton = document.querySelector('.auto-button');
const autoOptions = document.createElement('div');
autoOptions.classList.add('auto-options');
autoOptions.innerHTML = `
  <button ">标注健康部位</button>
  <br>
  <button ">标注病变部位</button>
  <br>
  `;
;
autoOptions.style.display = 'none';
autoOptions.style.display = 'none'; // 确保这个样式被设置
autoOptions.style.position = 'absolute'; // 设置为绝对定位
autoOptions.style.left = '100px'; // 设置左边距
autoOptions.style.top = '80px'; // 设置上边距

// 将选项容器添加到 body 中
document.body.appendChild(autoOptions);

// 点击自动标注按钮按钮显示或隐藏选项
autoButton.addEventListener('click', () => {
  if (autoOptions.style.display === 'none') {
    autoOptions.style.display = 'block';
  } else {
    autoOptions.style.display = 'none';
  }
});
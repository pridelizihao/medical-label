// 点击图形按钮鼠标样式为十字准线
const ovalButtons = document.querySelectorAll('.oval-button');
ovalButtons.forEach(button => {
  button.addEventListener('click', () => {
    document.body.style.cursor = 'crosshair';
  });
});
// 点击刷子按钮改变鼠标样式为刷子
const brushButton = document.querySelector('.brush-button');
brushButton.addEventListener('click', () => {
  document.body.style.cursor = 'url(brush.png), auto';
});

// 点击鼠标按钮恢复鼠标默认样式
const mouseButton = document.querySelector('.mouse-button');
mouseButton.addEventListener('click', () => {
  document.body.style.cursor = 'default';
});
// 点击tag按钮鼠标样式为标签图形
const tagButton = document.querySelector('.tag-button');
tagButton.addEventListener('click', () => {
  document.body.style.cursor = 'url(标签图片.png), auto';
});
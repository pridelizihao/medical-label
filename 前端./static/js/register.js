document.addEventListener('DOMContentLoaded', function() {
    function bindCaptcha() {
        document.querySelector("#get_check_number").addEventListener("click", function(event) {
            let email = document.querySelector("input[name='email']").value;
            if (!email) {
                alert("请输入邮箱");
                return false;
            }
            event.target.removeEventListener("click", bindCaptcha);

            // ajax request to send email to server
            email = document.querySelector("input[name='email']").value;

            fetch("/author/captcha?email=" + email, {
                method: "GET"
            })
           .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json(); // 或者 response.text() 如果你期望的是文本响应
            })
            .then(result => {
                console.log(result);
            })
           .catch(error => {
                console.log(error);
            });


            let countdown = 6;
            let timer = setInterval(function() {
                if (countdown <= 0) {
                    document.querySelector("#get_check_number").textContent = "获取验证码";
                    clearInterval(timer);
                    bindCaptcha();
                } else {
                    countdown--;
                    document.querySelector("#get_check_number").textContent = countdown + "秒后重发";
                }
            }, 1000);
        });
    }

    bindCaptcha();
});
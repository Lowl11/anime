class Logger {

    HandleException(jqueryXHR, exception, url, data = null) {
        let msg = '';
        if (jqueryXHR.status === 0) {
            // TODO нужно вывести сообщение (попап) юзеру о том что проблема с коннектом
            // msg = 'Not connect.\n Verify Network.';
        } else if (jqueryXHR.status == 404) {
            msg = 'Запрашиваемая страница не найдена. Код - 404';
        } else if (jqueryXHR.status == 500) {
            msg = 'Ошибка на стороне сервера. Код - 500';
        } else if (exception === 'parsererror') {
            msg = 'Ошибка чтения запрашиваемого JSON';
        } else if (exception === 'timeout') {
            msg = 'Время истекло (Timeout error)';
        } else if (exception === 'abort') {
            msg = 'Ajax запрос был прерван';
        } else {
            msg = 'Неизвестная ошибка: \n' + jqueryXHR.responseText;
        }
        this.Write(msg, url, data);
    }
    
    Write(message, url, data = null) {
        if (data == null)
            data = 0;
        else
            data = JSON.stringify(data);
        
        let sendData = {
            'message': message,
            'data': data,
            'url': url
        };

        if (ProjectSettings.Environemnt == Environments.DEBUG)
            this.DebugWrite(sendData.message);

        $.ajaxSetup({
            beforeSend: (xhr, settings) => {
                xhr.setRequestHeader("X-CSRFToken", this.GetCSRFToken());
            }
        });
        $.ajax({
            type: "POST",
            url: "/cms/log/",
            data: sendData,
            cache: false,
            success: function(data) {},
            error: function() {}
        });
    }

    DebugWrite(message) {
        console.log("Message:", message);
    }

    GetCSRFToken() {
        let name = 'csrftoken';
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

}

var logger = new Logger();

window.onerror = function(errorMessage, url, lineNumber) {
    logger.Write(errorMessage + ' на линии ' + lineNumber, url);
}
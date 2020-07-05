let RequestTypes = {
    "POST": "POST",
    "GET": "GET",
    "PUT": "PUT",
    "DELETE": "DELETE"
};

class Utils {

    static AjaxRequest(url, data, onSuccess, onError = null, requestType = RequestTypes.POST) {
        $.ajaxSetup({
            beforeSend: (xhr, settings) => {
                xhr.setRequestHeader("X-CSRFToken", Utils.GetCSRFToken());
            }
        });
        $.ajax({
            type: requestType,
            url: url,
            data: data,
            cache: false,
            success: (successData) => {
                onSuccess(successData);
            },
            error: (jqXHR, exception) => {
                logger.HandleException(jqXHR, exception, url, data);
                if (onError != null)
                    onError();
            }
        });
    }

    static GetCSRFToken() {
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
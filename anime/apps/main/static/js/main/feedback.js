$(() => {

    let feedback = new Feedback();

});

class Feedback {

    TextArea = $('.feedback-form');
    Submit = $('.feedback-send');
    SuccessBlock = $('.success-block');
    ErrorBlock = $('.error-block');

    constructor() {
        this.BindActions();
    }

    BindActions() {
        this.Submit.off('click.FeedBackSend');
        this.Submit.on('click.FeedBackSend', () => {
            this.SendForm();
        });
    }

    SendForm() {
        let data = this.collectData();
        let url = '/cms/feedback_send/';

        
        $.ajaxSetup({
            beforeSend: (xhr, settings) => {
                xhr.setRequestHeader("X-CSRFToken", this.GetCSRFToken());
            }
        });
        $.ajax({
            type: "POST",
            url: url,
            data: data,
            cache: false,
            success: (data) => {
                this.HideElements();
                if (data == "1")
                    this.SuccessBlock.show();
                else
                    this.ErrorBlock.show();
            },
            error: (jqXHR, exception) => {
                logger.HandleException(jqXHR, exception, url, data);
            }
        });
    }

    HideElements() {
        this.TextArea.hide();
        this.Submit.hide();
    }

    collectData() {
        let text = this.TextArea.val();
        let data = {
            'text': text
        };
        return data;
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

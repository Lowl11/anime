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
        let onSuccess = (successData) => {
            this.HideElements();
            if (successData == "1")
                this.SuccessBlock.show();
            else
                this.ErrorBlock.show();
        };

        Utils.AjaxRequest(url, data, onSuccess);
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

}

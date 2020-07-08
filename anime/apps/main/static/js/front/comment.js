class CommentManager {

    CommentSendButton = $('.send-comment-button');
    CommentTextArea = $('.send-comment-textarea');
    Data = {};
    Url = "";
    MinLength = 5;

    constructor(data, url, minLength = null) {
        this.Data = data;
        this.Url = url;
        if (minLength != null)
            this.MinLength = minLength;
        this.BindActions();
    }

    BindActions() {
        this.CommentSendButton.off('click.SendComment');
        this.CommentSendButton.on('click.SendComment', () => {
            let text = this.CommentTextArea.val();
            if (text.length > this.MinLength) {
                this.Data['text'] = text;

                let onSuccess = (successData) => {
                    if (successData == "1")
                        window.location.reload();
                };

                Utils.AjaxRequest(this.Url, this.Data, onSuccess);
            }
        });
    }

}
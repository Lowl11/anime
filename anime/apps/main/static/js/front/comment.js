class CommentManager {

    CommentSendButton = $('.send-comment-button');
    CommentTextArea = $('.send-comment-textarea');
    DeleteCommentButton = $('.delete-comment');

    Data = {};
    CreateUrl = "";
    DeleteUrl = "";
    MinLength = 5;

    constructor(data, createUrl, deleteUrl, minLength = null) {
        this.Data = data;
        this.CreateUrl = createUrl;
        this.DeleteUrl = deleteUrl;
        if (minLength != null)
            this.MinLength = minLength;
        this.BindActions();
    }

    BindActions() {
        // Отправка комментария
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

        // Удаление комментария
        this.DeleteCommentButton.off('click.DeleteComment');
        this.DeleteCommentButton.on('click.DeleteComment', (e) => {
            let ask = confirm("Вы точно хотите удалить данный комментарий?");
            if (ask) {
                let id = $(e.currentTarget).data('id');
                let data = { 'id': id };
                let onSuccess = (successData) => {
                    if (successData == "1") {
                        this.DeleteVisualComment(id);
                    }
                };
                Utils.AjaxRequest(this.DeleteUrl, data, onSuccess);
            }
        });
    }

    DeleteVisualComment(id) {
        let commentElement = $('#comment' + id);
        commentElement.remove();
    }

}
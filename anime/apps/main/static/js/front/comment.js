class CommentManager {

    CommentSendButton = $('.send-comment-button');
    CommentTextArea = $('.send-comment-textarea');
    DeleteCommentButton = $('.delete-comment');
    CommentsBlock = $('.comments-block');

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
        this.DeleteCommentButton = $('.delete-comment');

        // Отправка комментария
        this.CommentSendButton.off('click.SendComment');
        this.CommentSendButton.on('click.SendComment', () => {
            let text = this.CommentTextArea.val();
            if (text.length > this.MinLength) {
                this.Data['text'] = text;

                let onSuccess = (successData) => {
                    if (successData != "1") {
                        this.CreateVisualComment(successData);
                        setTimeout(() => { this.BindActions(); }, 0);
                    }
                };

                Utils.AjaxRequest(this.CreateUrl, this.Data, onSuccess);
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

    CreateVisualComment(commentData) {
        let commentsBlockHtml = this.CommentsBlock.html();
        let html = '<div class="comment" id="comment"' + commentData.id + '">';
        html += '<div class="author-image"><img src="' + commentData.author.image_url + '" alt=""></div>';
        html += '<div class="comment-info">';
        html += '<div class="author">' + commentData.author.username + '</div>';
        html += '<div class="text">' + commentData.text + '</div>';
        html += '<div class="publish-date">' + commentData.publish_date + '</div>';
        html += '</div>';
        if (commentData.author.role == 3) {
            html += '<div class="comment-management">';
            html += '<img src="/static/img/icons/delete.png" alt="Удалить комментарий" class="delete-comment" data-id="' + commentData.id + '">';
            html += '</div>';
        }
        html += '</div>';
        this.CommentsBlock.html(html + commentsBlockHtml);
    }

    DeleteVisualComment(id) {
        let commentElement = $('#comment' + id);
        commentElement.remove();
    }

}
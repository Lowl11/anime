function FileManager () {

    this.animation = new FMAnimations();
    this.createFolderUrl = '/cms/fm/create_folder/';

    this.Constructor = function() {
        this.BindActions();
    }

    this.BindActions = function() {
        // elements
        let createFolder = $('#create-folder');

        // binds
        createFolder.off('click.CreateFolder');
        createFolder.on('click.CreateFolder', () => {
            let modalTitle = 'Создать папку';
            let onApply = (errorObject) => {
                let folderName = $('#modal-input-input').val();
                if (folderName.length == 0) {
                    errorObject.text('Поле для заполнения пустое!');
                } else { // валидация пройдена :D
                    errorObject.text('');
                    let onSuccess = (data) => {
                        console.log(data);
                        this.animation.CloseModalInput();
                        this.UpdateFileManager();
                    };
                    this.SendAjax(this.createFolderUrl, { 'name': folderName }, onSuccess, 'GET');
                }
            }
            this.animation.OpenModalInput(modalTitle, onApply);
        });
    }

    this.UpdateFileManager = function() {
        // 
    }

    this.SendAjax = function(url, data, onSuccess, requestType = 'POST') {
        $.ajax({
            type: requestType,
            url: url,
            data: data,
            cached: false,
            success: onSuccess,
            error: function() {
                console.error('Ошибка запроса Ajax');
            }
        });
    }

    this.Constructor();

}

function FMAnimations() {

    this.Constructor = function() {}

    this.OpenModalInput = function(title, onApply) {
        let modalInput = $('.modal-input'); // модалка

        // верх модалки (header)
        let headerObject = modalInput.find('.header');
        let titleObject = headerObject.find('.title');
        
        // нижняя часть (footer)
        let footerObject = modalInput.find('.footer');
        let applyObject = footerObject.find('.apply-modal');
        let closeObject = footerObject.find('.close-modal');
        let errorObject = footerObject.find('.error-msg');

        // затемненный фон
        let backgroundCover = $('.background-cover');
        backgroundCover.show();

        titleObject.text(title); // ставим название модалки

        // действие на подтверждение модалки
        applyObject.off('click.ApplyModalInput');
        applyObject.on('click.ApplyModalInput', () => {
            onApply(errorObject);
        });

        // действие на закрытие модалки
        closeObject.off('click.CloseModalInput');
        closeObject.on('click.CloseModalInput', () => this.CloseModalInput());

        modalInput.show();
    }

    this.CloseModalInput = function() {
        let modalInput = $('.modal-input'); // модалка
        let backgroundCover = $('.background-cover');

        $('#modal-input-input').val(''); // очищение поля

        modalInput.hide();
        backgroundCover.hide();
    }
    
    this.Constructor();

}
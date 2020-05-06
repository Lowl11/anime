function FileManager () {

    this.animation = new FMAnimations();
    this.createFolderUrl = '/cms/fm/create_folder/';
    this.parentId = 0;
    this.folderName = 'Кореная папка';
    this.objects = [];

    this.Constructor = function() {
        $('#folder-name').text(this.folderName);
        this.OpenFolder();
    }

    this.BindActions = function() {
        // elements
        let createFolder = $('#create-folder');
        let folders = $('.object.folder');
        let backFolder = $('#back-folder');
        let renameFolder = $('#rename-folder');

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
                        this.animation.CloseModalInput();
                        this.UpdateFileManager();
                    };
                    this.SendAjax(this.createFolderUrl, { 'name': folderName, 'parent_id': parentId }, onSuccess, 'GET');
                }
            }
            this.animation.OpenModalInput(modalTitle, onApply);
        });

        folders.off('click.OpenFolder');
        folders.on('click.OpenFolder', (e) => {
            this.parentId = $(e.currentTarget).data('id');
            this.folderName = $(e.currentTarget).data('name');
            $('#folder-name').text(this.folderName);

            this.OpenFolder();
        });

        backFolder.off('click.BackFolder');
        backFolder.on('click.BackFolder', (e) => {
            let id = $(e.currentTarget).data('id');
            $('#folder-name').text($(e.currentTarget).data('name'));
            this.parentId = id;
            this.OpenFolder();
        });

        renameFolder.off('click.RenameFolder');
        renameFolder.on('click.RenameFolder', () => {
            console.log('asd');
        });
    }

    this.OpenFolder = function() {
        let updateUrl = '/cms/fm/objects/';
        let onSuccess = (data) => {
            this.objects = JSON.parse(data);
            this.UpdateFileManager();
            this.BindActions();
        };
        this.SendAjax(updateUrl, { 'parent_id': this.parentId }, onSuccess, 'GET');
    }

    this.UpdateFileManager = function() {
        let fileObjects = $('.file-objects');
        let html = '';
        $.each(this.objects, (index, value) => {
            html += '<div class="object-wrapper">';
            html += '<div class="object ' + value.type + '" data-id="' + value.id + '" data-name="' + value.name + '">'
            html += '<div class="glyphicon glyphicon-' + value.type + '-open"></div>';
            html += value.name;
            html += '</div></div>';
        });
        fileObjects.html(html);
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
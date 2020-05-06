class FileManager {

    GUI = new FileManagerGUI();
    Data = new FileManagerData(this.GUI);

    RootFolder = true;
    CurrentFolderName = 'Коренная папка';
    FileObjects = [];

    constructor() { 
        this.GUI.SetCurrentFolder(this.CurrentFolderName, 0);
        this.FileObjects = this.Data.GetObjects();
    }

}

class FileManagerGUI {

    Data = new FileManagerData(this);

    // Кнопки
    BackFolder = $('#back-folder');
    CreateFolder = $('#create-folder');
    RenameFolder = $('#rename-folder');
    DeleteFolder = $('#delete-folder');
    UploadFile = $('#upload-file');

    // модалки
    ModalInput = $('.modal-input');
    ModalInputTitle = this.ModalInput.find('.header').find('.title');
    ModalInputField = this.ModalInput.find('.content').find('input');

    ModalSure = $('.modal-sure');
    ModalSureTitle = this.ModalSure.find('.header').find('.title');
    
    // "принять" и "закрыть" кнопки модалки
    ModalApply = $('.apply-modal');
    ModalCancel = $('.close-modal');

    // Объект текста ошибки
    ErrorObject = $('.error-msg');

    // Название нынешней папки
    CurrentFolder = $('#folder-name');

    // div в котором лежат все объекты (файлы, папки)
    Objects = $('.file-objects');

    constructor() {
        this.BindActions();
    }

    BindActions() {
        // закрытие модалки
        this.ModalCancel.off('click.ModalCancel');
        this.ModalCancel.on('click.ModalCancel', () => this.HideModal());

        // кнопка назад
        this.BackFolder.off('click.BackFolder');
        this.BackFolder.on('click.BackFolder', () => {
            let breadCrump = this.GetBreadCrump();
            let parentId = parseInt(breadCrump[breadCrump.length - 2]);
            breadCrump.pop();
            this.SetBreadCrump(breadCrump);

            if (parentId < 0)
                parentId = 0;
            this.Data.GetObjects(parentId);
        });

        // создать папку
        this.CreateFolder.off('click.CreateFolder');
        this.CreateFolder.on('click.CreateFolder', () => {
            let onApply = () => {
                let folderName = this.ModalInputField.val();
                if (folderName.length > 0) {
                    let currentFolderId = this.CurrentFolder.data('id');
                    let onSuccess = () => {
                        this.HideModal();
                        this.Data.GetObjects(currentFolderId);
                    };
                    this.Data.CreateFolder(currentFolderId, folderName, onSuccess);
                } else {
                    this.ErrorObject.text('Название папки не может быть пустым');
                }
            };
            this.ShowModal('input', 'Создать папку', onApply);
        });

        this.RenameFolder.off('click.RenameFolder');
        this.RenameFolder.on('click.RenameFolder', () => {
            let onApply = () => {
                let folderName = this.ModalInputField.val();
                if (folderName.length > 0) {
                    let currentFolderId = this.CurrentFolder.data('id');
                    let onSuccess = () => {
                        this.HideModal();
                        this.SetCurrentFolder(folderName, currentFolderId);
                        this.Data.GetObjects(currentFolderId);
                    };
                    this.Data.RenameFolder(currentFolderId, folderName, onSuccess);
                } else {
                    this.ErrorObject.text('Название папки не может быть пустым');
                }
            };
            this.ShowModal('input', 'Переименовать папку', onApply, this.CurrentFolder.text());
        });

        this.DeleteFolder.off('click.DeleteFolder');
        this.DeleteFolder.on('click.DeleteFolder', () => {
            let onApply = () => {
                let breadCrump = this.GetBreadCrump();
                let parentId = breadCrump[breadCrump.length - 2];
                let onSuccess = () => {
                    this.HideModal();
                    this.Data.GetObjects(parentId);
                };
                let currentFolderId = this.CurrentFolder.data('id');
                this.Data.DeleteFolder(currentFolderId, onSuccess);
            };
            this.ShowModal('sure', 'Удалить папку?', onApply);
        });
    }

    DrawObjects(objects) {
        let html = '';
        $.each(objects, (index, value) => {
            html += '<div class="object-wrapper">';
            html += '<div class="object ' + value.type + '" data-id="' + value.id + '" data-name="' + value.name + '">'
            html += '<div class="glyphicon glyphicon-' + value.type + '-open"></div>';
            html += value.name;
            html += '</div></div>';
        });
        this.Objects.html(html);

        let generated = $('.object');
        generated.off('click.OpenFolder');
        generated.on('click.OpenFolder', (e) => {
            let folder = $(e.currentTarget);
            let folderId = folder.data('id');
            let folderName = folder.data('name');

            this.SetCurrentFolder(folderName, folderId);
            let breadCrump = this.GetBreadCrump();
            breadCrump.push(folderId);
            this.SetBreadCrump(breadCrump);

            this.Data.GetObjects(folderId);
        });
    }

    SetCurrentFolder(folderName, folderId) {
        this.CurrentFolder.text(folderName);
        this.CurrentFolder.data('id', folderId);
    }

    ShowModal(type, title, onClick, value = '') {
        let modalObject, titleObject;
        switch (type) {
            case 'input':
                modalObject = this.ModalInput;
                titleObject = this.ModalInputTitle;
                this.ModalInputField.val(value);
                break;
            case 'sure':
                modalObject = this.ModalSure;
                titleObject = this.ModalSureTitle;
                break;
            default:
                modalObject = null;
                titleObject = null;
        }
        modalObject.show();
        titleObject.text(title);
        this.ModalApply.off('click.ModalApply');
        this.ModalApply.on('click.ModalApply', () => onClick(this.ErrorObject));
        this.ToggleBlur();
    }

    HideModal() {
        this.ModalInput.hide();
        this.ModalSure.hide();
        this.ToggleBlur();
    }

    ToggleBlur() {
        let blurObject = $('.background-cover');
        if (blurObject.data('toggled') == 0) {
            blurObject.show();
            blurObject.data('toggled', '1');
        }
        else {
            blurObject.hide();
            blurObject.data('toggled', '0');
        }
    }

    GetBreadCrump() {
        let breadCrumpObject = $('.bread-crump');
        let breadCrump = breadCrumpObject.text().split(' ');
        return breadCrump;
    }

    SetBreadCrump(breadCrump) {
        let text = '';
        for (let i = 0; i < breadCrump.length; i++) {
            text += breadCrump[i] + ' ';
        }
        $('.bread-crump').text(text.trim());
    }

}

class FileManagerData {

    GUI = null;
    BaseUrl = '/cms/fm/';
    CreateFolderUrl = this.BaseUrl + 'create_folder/';
    RenameFolderUrl = this.BaseUrl + 'rename_folder/';
    DeleteFolderUrl = this.BaseUrl + 'delete_folder/';
    GetObjectsUrl = this.BaseUrl + 'objects/';

    constructor(gui) {
        this.GUI = gui;
    }

    GetObjects(parentId) {
        let data = {
            'parent_id': parentId
        }
        let onSuccess = (data) => {
            let objects = JSON.parse(data);
            this.GUI.DrawObjects(objects);
        }
        this.SendAjax(this.GetObjectsUrl, data, onSuccess);
    }

    CreateFolder(parentId, folderName, onSuccess) {
        let data = {
            'name': folderName,
            'parent_id': parentId
        };
        this.SendAjax(this.CreateFolderUrl, data, onSuccess);
    }

    RenameFolder(folderId, folderName, onSuccess) {
        let data = {
            'name': folderName,
            'folder_id': folderId
        };
        this.SendAjax(this.RenameFolderUrl, data, onSuccess);
    }

    DeleteFolder(folderId, onSuccess) {
        let data = {
            'folder_id': folderId
        };
        this.SendAjax(this.DeleteFolderUrl, data, onSuccess);
    }

    SendAjax(url, data, onSuccess) {
        $.ajax({
            type: 'GET',
            url: url,
            data: data,
            cache: false,
            success: onSuccess,
            error: function() {
                console.error('Ошибка отправки Ajax запроса');
            }
        });
    }

}
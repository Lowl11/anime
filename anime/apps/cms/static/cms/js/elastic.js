function ElasticManager() {

    this.indices = [];
    this.delete_index_buttons = [];

    this.constructor = function() {
        this.handle_elements();
    }

    this.handle_elements = function() {
        this.handle_indices();
        this.handle_delete_buttons();
        this.bind_actions();
    }

    this.bind_actions() = function() {
        // привязка действий к jquery элементам
    }

    this.handle_delete_buttons = function() {
        let delete_buttons = $('.delete-btn');
        this.handle_delete_index_buttons(delete_buttons);
        console.log(this.delete_index_buttons);
    }

    this.handle_delete_index_buttons = function(delete_buttons) {
        $.each(delete_buttons, (index, value) => {
            value = $(value);
            let delete_type = value.data('type');
            if (delete_type == 'index')
                this.delete_index_buttons.push(value);
        });
    }

    this.handle_indices = function() {
        let trIndex = $('.index');
        $.each(trIndex, (index, value) => {
            let tds = trIndex.find('td');
            let indexObj = new Index();
            index.id = index;
            $.each(tds, (index, value) => {
                value = $(value);
                let name = value.data('name');
                switch (name) {
                    case 'status':
                        indexObj.status = value.text();
                        break;
                    case 'name':
                        indexObj.name = value.text();
                        break;
                    case 'hash_code':
                        indexObj.hash_code = value.text();
                        break;
                    case 'docs_count':
                        indexObj.docs_count = parseInt(value.text());
                        break;
                    case 'delete_count':
                        indexObj.delete_count = parseInt(value.text());
                        break;
                    case 'size':
                        indexObj.size = value.text();
                        break;
                }
            });
            this.indices.push(indexObj);
        });
    }

    this.constructor();

}

function Index() {

    this.id = 0;
    this.status = '';
    this.name = '';
    this.hash_code = '';
    this.docs_count = 0;
    this.delete_count = 0;
    this.size = '';

}
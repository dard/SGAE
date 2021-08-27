$(function () {
     $('#data').DataTable({
         responsive: true,
         autoWidth: false,
         destroy: true,
         deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },


        columns: [
            {"data": "id"},
            {"data": "dni"},
            {"data": "nombre"},
            {"data": "apellido"},
			{"data": "fecha_nacimiento"},
            {"data": "sexo"},
            {"data": "email"},
            {"data": "direccion"},
            {"data": "telefono"},
            {"data": "comorvilidades"},
            {"data": "observaciones"},
			{"data": "opciones"},
        ],
        columnDefs: [
            // {
            //         targets: [-3],
            //         class: 'text-center',
            //         orderable: false,
            //         render: function (data, type, row) {
            //             return <class="form-check" input type="checkbox" class="form-check-input">;
            //         }
            //     },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/alumnoedit/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/alumnodelete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        // initComplete: function (settings, json) {
        //     alert('Tabla cargada');
        // }
    });
});

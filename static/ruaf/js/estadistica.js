var date_range = null;
var date_now = new moment().format('YYYY-MM-DD');



function generar_reporte(){

    var parameters={
        'action':"search_report",
        'start_date': date_now,
        'end_date': date_now,
    }
    

    if (date_range !== null) {
        parameters['start_date'] = date_range.startDate.format('YYYY-MM-DD');
        parameters['end_date'] = date_range.endDate.format('YYYY-MM-DD');

    }

    window.location = "/ruaf/genestadistica/nv/"+parameters['start_date']+'/'+parameters['end_date'];
    
}   

$(function () {
  
    $('input[name="date_range"]').daterangepicker({


         locale : {
             format: 'YYYY-MM-DD',
             applyLabel: '<i class="fas fa-chart-pie"></i> Aplicar',
             cancelLabel: '<i class="fas fa-times"></i> Cancelar',
         },
         cancelButtonClasses:'btn-danger',
         

    }).on('apply.daterangepicker', function (ev, picker) {

        date_range = picker;        
        generar_reporte();
        
    }).on('cancel.daterangepicker', function (ev, picker) {
        $(this).data('daterangepicker').setStartDate(date_now);
        $(this).data('daterangepicker').setEndDate(date_now);
        date_range = picker;
        generar_reporte();
    });

   
});